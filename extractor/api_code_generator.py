from api_json_extractor import Extractor
import json
import os
import re
import requests
import subprocess
from dotenv import load_dotenv

def is_url(path):
    return path.startswith("http://") or path.startswith("https://")

def markdown_file_parser(file_path):
    """Parser for markdown files - reads and returns the raw markdown text"""
    with open(file_path, 'r', encoding='utf-8') as file:
        markdown_content = file.read()
    return markdown_content

def copy_file_to_doc_md(source_file_path, file_type):
    """Copy a file to doc.md in the same directory"""
    try:
        # Get the directory of the source file
        source_dir = os.path.dirname(source_file_path)
        doc_md_path = os.path.join(source_dir, "doc.md")
        
        # Check if doc.md already exists
        if os.path.exists(doc_md_path):
            print(f"  doc.md already exists for {os.path.basename(source_file_path)}")
            return doc_md_path
        
        # Copy the file content to doc.md
        with open(source_file_path, 'r', encoding='utf-8') as source_file:
            content = source_file.read()
        
        with open(doc_md_path, 'w', encoding='utf-8') as doc_file:
            doc_file.write(content)
        
        print(f"  ✓ Copied {file_type} to doc.md for {os.path.basename(source_file_path)}")
        return doc_md_path
        
    except Exception as e:
        print(f"  ✗ Error copying {file_type} to doc.md: {e}")
        return None

def convert_html_to_markdown(html_file_path):
    """Convert HTML file to markdown using the html_to_markdown_converter"""
    try:
        # Get the directory of the HTML file
        html_dir = os.path.dirname(html_file_path)
        doc_md_path = os.path.join(html_dir, "doc.md")
        
        # Check if doc.md already exists
        if os.path.exists(doc_md_path):
            print(f"  doc.md already exists for {os.path.basename(html_file_path)}")
            return doc_md_path
        
        # Find the converter script - check if we're already in extractor/ or need to go into it
        current_dir = os.getcwd()
        if os.path.basename(current_dir) == "extractor":
            converter_script = "html_to_markdown_converter.py"
        else:
            converter_script = os.path.join("extractor", "html_to_markdown_converter.py")
        
        # Make sure the converter script exists
        if not os.path.exists(converter_script):
            print(f"  ✗ Converter script not found: {converter_script}")
            return None
        
        # Run the HTML to markdown converter
        result = subprocess.run([
            "python", converter_script, html_file_path
        ], capture_output=True, text=True, check=True)
        
        if result.returncode == 0 and os.path.exists(doc_md_path):
            print(f"  ✓ Converted HTML to doc.md for {os.path.basename(html_file_path)}")
            return doc_md_path
        else:
            print(f"  ✗ Failed to convert HTML to markdown for {os.path.basename(html_file_path)}")
            print(f"  ✗ Converter output: {result.stdout}")
            print(f"  ✗ Converter error: {result.stderr}")
            return None
            
    except subprocess.CalledProcessError as e:
        print(f"  ✗ Converter script failed with exit code {e.returncode}")
        print(f"  ✗ Stdout: {e.stdout}")
        print(f"  ✗ Stderr: {e.stderr}")
        return None
    except Exception as e:
        print(f"  ✗ Error converting HTML to markdown: {e}")
        return None

def detect_function_call(value):
    """
    Detect if a value contains a function call pattern like 'function_name()'
    Returns the function name if detected, None otherwise
    """
    if isinstance(value, str):
        # Pattern to match function calls like 'get_auth_token()' 
        pattern = r'^([a-zA-Z_][a-zA-Z0-9_]*)\(\)$'
        match = re.match(pattern, value)
        if match:
            return match.group(1)
    return None

def load_auth_function(function_name):
    """
    Load an auth function from utils/auth_functions/ directory
    Returns the function code as a string, or None if not found
    """
    auth_functions_dir = "utils/auth_functions"
    function_file = f"{function_name}.py"
    function_path = os.path.join(auth_functions_dir, function_file)
    
    if os.path.exists(function_path):
        with open(function_path, 'r', encoding='utf-8') as f:
            return f.read()
    return None

class Generator():
    def __init__(self):
        pass

    def convert_openapi_to_toolformat(self, openapi_dict):
        endpoints = []
        for path, methods in openapi_dict.get("paths", {}).items():
            for method, details in methods.items():
                ep = {
                    "name": details.get("summary", f"{method.upper()} {path}"),
                    "description": details.get("description", ""),
                    "method": method.upper(),
                    "url": path,
                    "headers": [],
                    "required_parameters": [],
                    "optional_parameters": []
                }
                for p in details.get("parameters", []):
                    param = {
                        "name": p.get("name"),
                        "type": p.get("schema", {}).get("type", "string"),
                        "description": p.get("description"),
                        "default": p.get("schema", {}).get("default"),
                        "example": p.get("example", "example")
                    }
                    if p.get("required", False):
                        ep["required_parameters"].append(param)
                    else:
                        ep["optional_parameters"].append(param)
                endpoints.append(ep)
        return {
            "title": openapi_dict.get("info", {}).get("title", "Generated API"),
            "endpoints": endpoints
        }

    def save_to_registry(self, api_form, registry_path="tool_registry.json"):
        if isinstance(api_form, str):
            api_form = json.loads(api_form)
        new_tools = []
        for ep in api_form["endpoints"]:
            tool_entry = {
                "tool_name": ep["name"].replace(" ", "_").lower(),
                "method": ep["method"],
                "url": ep["url"][0] if isinstance(ep["url"], list) else ep["url"],
                "description": ep.get("description", ""),
                "required_parameters": [p["name"] for p in ep.get("required_parameters", [])],
                "example": ep["name"].replace(" ", "_"),
            }
            new_tools.append(tool_entry)

        os.makedirs(os.path.dirname(registry_path), exist_ok=True)
        if os.path.exists(registry_path):
            with open(registry_path, "r") as f:
                registry = json.load(f)
        else:
            registry = []
        registry.extend(new_tools)
        with open(registry_path, "w") as f:
            json.dump(registry, f, indent=2)

    def generate_from_api_json_and_save(self, api_form, output_folder_path, config=None):
        if isinstance(api_form, str):
            api_form = json.loads(api_form)
        # self.save_to_registry(api_form)
        for endpoint in api_form['endpoints']:     
            generated_code = ""
            method = endpoint['method']
            api_name = endpoint['name']
            # Replace all non-alphanumeric characters with underscore
            api_name = re.sub(r'\W', '_', api_name)
            # Convert to lowercase
            api_name = api_name.lower()
            
            # Process headers from config and collect auth functions
            headers = "{}"
            auth_functions_code = ""
            if config and "headers" in config:
                headers = "{"
                for key, value in config["headers"].items():
                    function_name = detect_function_call(value)
                    if function_name:
                        # Load auth function code
                        auth_code = load_auth_function(function_name)
                        if auth_code:
                            auth_functions_code += auth_code + "\n"
                            # Replace function call with actual function call in headers
                            headers += f"'{key}': {function_name}(), "
                        else:
                            print(f"Warning: Auth function '{function_name}' not found in utils/auth_functions/")
                            headers += f"'{key}': '{value}', "
                    else:
                        headers += f"'{key}': '{value}', "
                headers += "}"
            
            if method == "GET":
                if isinstance(endpoint['url'], list):
                    endpoint_url = endpoint['url'][0]
                else:
                    endpoint_url = endpoint['url']
                # Replace < and > with { and } in url   
                endpoint_url = endpoint_url.replace("<", "{").replace(">", "}")
                endpoint_url = endpoint_url.replace(" ", "_")
                
                # Handle base_url from config - always use config base_url if available
                if config and "base_url" in config:
                    # If endpoint_url is a full URL, extract just the path
                    if endpoint_url.startswith("http://") or endpoint_url.startswith("https://"):
                        from urllib.parse import urlparse
                        parsed_url = urlparse(endpoint_url)
                        endpoint_url = parsed_url.path + (parsed_url.query and f"?{parsed_url.query}" or "")
                    url = '"' + config["base_url"] + endpoint_url + '"'
                else:
                    url = '"' + endpoint_url + '"'
                    
                required_param = endpoint['required_parameters']
                optional_param = endpoint['optional_parameters']
                optional_param = [] if optional_param is None else optional_param
                querystring = "{"
                param_list = ""
                param_example = []
                validate_req_param = ""
                reconstruct_querystring = True
                for param in required_param:
                    param_name = re.sub(r'\W', '_', param['name'])
                    is_string_type = param["type"] == "string"
                    # some urls use ":" as identifier for parameters, replace :param or param: with {param}
                    for m in re.finditer(r':(\w+)|(\w+):', url):
                        if m.group(1) == param_name:
                            url = url[:m.start()] + '{' + m.group(1) + '}' + url[m.end():]
                    # quote the params in url
                    for m in re.finditer(r'\{(\w+)\}', url):
                        if m.group(1) == param_name:
                            if config and "url_in_param" in config and config["url_in_param"]:
                                url = url[:m.start()] + f"{{quote({m.group(1)})}}" + url[m.end():]
                            else:
                                url = url[:m.start()] + f"{{quote({m.group(1)}, safe='')}}" + url[m.end():]
                    if param_name =='payload':
                        # if we have payload in parameter, we don't need to reconstruct the querystring
                        reconstruct_querystring = False
                    # if param["default"]:
                    #     if is_string_type:
                    #         querystring += f"'{param_name}': '{param['default']}', "
                    #     else:
                    #         querystring += f"'{param_name}': {param['default']}, "
                    # else:
                    #     querystring += f"'{param_name}': {param_name}, "
                    # param_list += param_name + ", "
                    validate_req_param += f"assert {param_name} is not None, 'Missing required parameter: {param_name}'\n    "
                    param_list += param_name
                    if param["default"]: # if default, assigne default value to param
                        if is_string_type:
                            param_list += f"='{param['default']}'"
                        else:
                            param_list += f"={param['default']}"
                    else:
                        param_list += f"=None"
                    param_list += ", "
                    querystring += f"'{param_name}': {param_name}, "
                    example_value = f"{param_name}='''{param['example']}'''" if is_string_type else f"{param_name}={param['example']}"
                    param_example.append(example_value)
                for param in optional_param:
                    param_name = re.sub(r'\W', '_', param['name'])
                    is_string_type = param["type"] == "string"
                    if param_name =='payload':
                        # if we have payload in parameter, we don't need to reconstruct the querystring
                        reconstruct_querystring = False
                    # if param["default"]:
                    #     if is_string_type:
                    #         querystring += f"'{param_name}': '{param['default']}', "
                    #     else:
                    #         querystring += f"'{param_name}': {param['default']}, "
                    # else:
                    #     querystring += f"'{param_name}': {param_name}, "
                    # param_list += param_name + ", "
                    param_list += param_name
                    if param["default"]: # if default, assigne default value to param
                        if is_string_type:
                            param_list += f"='{param['default']}'"
                        else:
                            param_list += f"={param['default']}"
                    else:
                        param_list += f"=None"
                    param_list += ", "
                    querystring += f"'{param_name}': {param_name}, "
                    example_value = f"{param_name}='''{param['example']}'''" if is_string_type else f"{param_name}={param['example']}"
                    param_example.append(example_value)                    
                querystring += "}"
                if not reconstruct_querystring:
                    querystring = "payload"
                param_list = param_list[:-2]
                with open('./template/GET_template.txt', 'r') as template_file:
                    code_template = template_file.read()
                param_examples_seperated = ", ".join(param_example)
                generated_code += code_template.format(param_list=param_list, url=url, querystring=querystring, api_name=api_name, validate_req_param=validate_req_param, param_examples_seperated=param_examples_seperated, headers=headers, auth_functions_code=auth_functions_code) + "\n"
                # generated_code += f"if __name__ == '__main__':\n\tprint({api_name}({', '.join(param_example)}))\n\n"
            elif method == "POST":
                if isinstance(endpoint['url'], list):
                    endpoint_url = endpoint['url'][0]
                else:
                    endpoint_url = endpoint['url']
                endpoint_url = endpoint_url.replace("<", "{").replace(">", "}")
                endpoint_url = endpoint_url.replace(" ", "_")
                
                # Handle base_url from config - always use config base_url if available
                if config and "base_url" in config:
                    # If endpoint_url is a full URL, extract just the path
                    if endpoint_url.startswith("http://") or endpoint_url.startswith("https://"):
                        from urllib.parse import urlparse
                        parsed_url = urlparse(endpoint_url)
                        endpoint_url = parsed_url.path + (parsed_url.query and f"?{parsed_url.query}" or "")
                    url = '"' + config["base_url"] + endpoint_url + '"'
                else:
                    url = '"' + endpoint_url + '"'
                    
                required_param = endpoint['required_parameters']
                optional_param = endpoint['optional_parameters']
                optional_param = [] if optional_param is None else optional_param
                payload = "{"
                param_list = ""
                validate_req_param = ""
                param_example = []
                reconstruct_payload = True
                for param in required_param:
                    param_name = re.sub(r'\W', '_', param['name'])
                    is_string_type = param["type"] == "string"
                    if param_name =='payload':
                        # if we have payload in parameter, we don't need to reconstruct the payload
                        reconstruct_payload = False
                    # if param["default"]:
                    #     if is_string_type:
                    #         payload += f"'{param_name}': '{param['default']}', "
                    #     else:
                    #         payload += f"'{param_name}': {param['default']}, "
                    # else:
                    #     payload += f"'{param_name}': {param_name}, "
                    # param_list += param_name + ", "
                    validate_req_param += f"assert {param_name} is not None, 'Missing required parameter: {param_name}'\n    "
                    param_list += param_name
                    if param["default"]: # if default, assigne default value to param
                        if is_string_type:
                            param_list += f"='{param['default']}'"
                        else:
                            param_list += f"={param['default']}"
                    else:
                        param_list += f"=None"
                    param_list += ", "
                    payload += f"'{param_name}': {param_name}, "
                    example_value = f"{param_name}='''{param['example']}'''" if is_string_type else f"{param_name}={param['example']}"
                    param_example.append(example_value)
                for param in optional_param:
                    param_name = re.sub(r'\W', '_', param['name'])
                    is_string_type = param["type"] == "string"
                    if param_name =='payload':
                        # if we have payload in parameter, we don't need to reconstruct the payload
                        reconstruct_payload = False
                    # if param["default"]:
                    #     if is_string_type:
                    #         payload += f"'{param_name}': '{param['default']}', "
                    #     else:
                    #         payload += f"'{param_name}': {param['default']}, "
                    # else:
                    #     payload += f"'{param_name}': {param_name}, "
                    # param_list += param_name + ", "
                    param_list += param_name
                    if param["default"]:
                        if is_string_type:
                            param_list += f"='{param['default']}'"
                        else:
                            param_list += f"={param['default']}"
                    else:
                        param_list += f"=None"
                    param_list += ", "
                    payload += f"'{param_name}': {param_name}, "
                    example_value = f"{param_name}='''{param['example']}'''" if is_string_type else f"{param_name}={param['example']}"
                    param_example.append(example_value)
                payload += "}"
                if not reconstruct_payload:
                        payload = "payload"
                param_list = param_list[:-2]
                
                with open('./template/POST_template.txt', 'r') as template_file:
                    code_template = template_file.read()
                param_examples_seperated = ", ".join(param_example)
                generated_code += code_template.format(param_list=param_list, url=url, payload=payload, api_name=api_name, validate_req_param=validate_req_param, param_examples_seperated=param_examples_seperated, headers=headers, auth_functions_code=auth_functions_code) + "\n"
                # generated_code += f"if __name__ == '__main__':\n\tprint({api_name}({', '.join(param_example)}))\n\n"
            elif method == "PUT":
                if isinstance(endpoint['url'], list):
                    endpoint_url = endpoint['url'][0]
                else:
                    endpoint_url = endpoint['url']
                endpoint_url = endpoint_url.replace("<", "{").replace(">", "}")
                endpoint_url = endpoint_url.replace(" ", "_")
                
                # Handle base_url from config - always use config base_url if available
                if config and "base_url" in config:
                    # If endpoint_url is a full URL, extract just the path
                    if endpoint_url.startswith("http://") or endpoint_url.startswith("https://"):
                        from urllib.parse import urlparse
                        parsed_url = urlparse(endpoint_url)
                        endpoint_url = parsed_url.path + (parsed_url.query and f"?{parsed_url.query}" or "")
                    url = '"' + config["base_url"] + endpoint_url + '"'
                else:
                    url = '"' + endpoint_url + '"'
                    
                required_param = endpoint['required_parameters']
                optional_param = endpoint['optional_parameters']
                optional_param = [] if optional_param is None else optional_param
                payload = "{"
                param_list = ""
                validate_req_param = ""
                param_example = []
                reconstruct_payload = True
                for param in required_param:
                    param_name = re.sub(r'\W', '_', param['name'])
                    is_string_type = param["type"] == "string"
                    if param_name =='payload':
                        # if we have payload in parameter, we don't need to reconstruct the payload
                        reconstruct_payload = False
                    validate_req_param += f"assert {param_name} is not None, 'Missing required parameter: {param_name}'\n    "
                    param_list += param_name
                    if param["default"]: # if default, assigne default value to param
                        if is_string_type:
                            param_list += f"='{param['default']}'"
                        else:
                            param_list += f"={param['default']}"
                    else:
                        param_list += f"=None"
                    param_list += ", "
                    payload += f"'{param_name}': {param_name}, "
                    example_value = f"{param_name}='''{param['example']}'''" if is_string_type else f"{param_name}={param['example']}"
                    param_example.append(example_value)
                for param in optional_param:
                    param_name = re.sub(r'\W', '_', param['name'])
                    is_string_type = param["type"] == "string"
                    if param_name =='payload':
                        # if we have payload in parameter, we don't need to reconstruct the payload
                        reconstruct_payload = False
                    param_list += param_name
                    if param["default"]:
                        if is_string_type:
                            param_list += f"='{param['default']}'"
                        else:
                            param_list += f"={param['default']}"
                    else:
                        param_list += f"=None"
                    param_list += ", "
                    payload += f"'{param_name}': {param_name}, "
                    example_value = f"{param_name}='''{param['example']}'''" if is_string_type else f"{param_name}={param['example']}"
                    param_example.append(example_value)
                payload += "}"
                if not reconstruct_payload:
                        payload = "payload"
                param_list = param_list[:-2]
                
                with open('./template/PUT_template.txt', 'r') as template_file:
                    code_template = template_file.read()
                param_examples_seperated = ", ".join(param_example)
                generated_code += code_template.format(param_list=param_list, url=url, payload=payload, api_name=api_name, validate_req_param=validate_req_param, param_examples_seperated=param_examples_seperated, headers=headers, auth_functions_code=auth_functions_code) + "\n"
            elif method == "DELETE":
                if isinstance(endpoint['url'], list):
                    endpoint_url = endpoint['url'][0]
                else:
                    endpoint_url = endpoint['url']
                # Replace < and > with { and } in url   
                endpoint_url = endpoint_url.replace("<", "{").replace(">", "}")
                endpoint_url = endpoint_url.replace(" ", "_")
                
                # Handle base_url from config - always use config base_url if available
                if config and "base_url" in config:
                    # If endpoint_url is a full URL, extract just the path
                    if endpoint_url.startswith("http://") or endpoint_url.startswith("https://"):
                        from urllib.parse import urlparse
                        parsed_url = urlparse(endpoint_url)
                        endpoint_url = parsed_url.path + (parsed_url.query and f"?{parsed_url.query}" or "")
                    url = '"' + config["base_url"] + endpoint_url + '"'
                else:
                    url = '"' + endpoint_url + '"'
                    
                required_param = endpoint['required_parameters']
                optional_param = endpoint['optional_parameters']
                optional_param = [] if optional_param is None else optional_param
                querystring = "{"
                param_list = ""
                param_example = []
                validate_req_param = ""
                reconstruct_querystring = True
                for param in required_param:
                    param_name = re.sub(r'\W', '_', param['name'])
                    is_string_type = param["type"] == "string"
                    # some urls use ":" as identifier for parameters, replace :param or param: with {param}
                    for m in re.finditer(r':(\w+)|(\w+):', url):
                        if m.group(1) == param_name:
                            url = url[:m.start()] + '{' + m.group(1) + '}' + url[m.end():]
                    # quote the params in url
                    for m in re.finditer(r'\{(\w+)\}', url):
                        if m.group(1) == param_name:
                            if config and "url_in_param" in config and config["url_in_param"]:
                                url = url[:m.start()] + f"{{quote({m.group(1)})}}" + url[m.end():]
                            else:
                                url = url[:m.start()] + f"{{quote({m.group(1)}, safe='')}}" + url[m.end():]
                    if param_name =='payload':
                        # if we have payload in parameter, we don't need to reconstruct the querystring
                        reconstruct_querystring = False
                    validate_req_param += f"assert {param_name} is not None, 'Missing required parameter: {param_name}'\n    "
                    param_list += param_name
                    if param["default"]: # if default, assigne default value to param
                        if is_string_type:
                            param_list += f"='{param['default']}'"
                        else:
                            param_list += f"={param['default']}"
                    else:
                        param_list += f"=None"
                    param_list += ", "
                    querystring += f"'{param_name}': {param_name}, "
                    example_value = f"{param_name}='''{param['example']}'''" if is_string_type else f"{param_name}={param['example']}"
                    param_example.append(example_value)
                for param in optional_param:
                    param_name = re.sub(r'\W', '_', param['name'])
                    is_string_type = param["type"] == "string"
                    if param_name =='payload':
                        # if we have payload in parameter, we don't need to reconstruct the querystring
                        reconstruct_querystring = False
                    param_list += param_name
                    if param["default"]: # if default, assigne default value to param
                        if is_string_type:
                            param_list += f"='{param['default']}'"
                        else:
                            param_list += f"={param['default']}"
                    else:
                        param_list += f"=None"
                    param_list += ", "
                    querystring += f"'{param_name}': {param_name}, "
                    example_value = f"{param_name}='''{param['example']}'''" if is_string_type else f"{param_name}={param['example']}"
                    param_example.append(example_value)                    
                querystring += "}"
                if not reconstruct_querystring:
                    querystring = "payload"
                param_list = param_list[:-2]
                with open('./template/DELETE_template.txt', 'r') as template_file:
                    code_template = template_file.read()
                param_examples_seperated = ", ".join(param_example)
                generated_code += code_template.format(param_list=param_list, url=url, querystring=querystring, api_name=api_name, validate_req_param=validate_req_param, param_examples_seperated=param_examples_seperated, headers=headers, auth_functions_code=auth_functions_code) + "\n"
            with open(os.path.join(output_folder_path, api_name + "_" + method + ".py"), 'w', encoding='utf-8') as output_file: #some apis have get/post with same name
                output_file.write(generated_code)

# Use this if API json forms are not available
# if __name__ == "__main__":
#     extractor = Extractor()
#     agent = Generator()
#     files_path = "../free_api_docs"
#     count = 0

#     files = os.listdir(files_path)
#     # sort the files based on the number in the file name
#     files.sort(key=lambda x: int(''.join(filter(str.isdigit, x))))

#     for file in files:

#         if file.endswith(".html"):
#             print("----------------------" + file + "----------------------")
#             html_file = os.path.join(files_path, file)

#             try:
#                 api_form = extractor.extract_api_json(html_file)
#                 generated_output = agent.generate_from_api_json(api_form)
#             except Exception as e:
#                 with open("../log/" + file + ".txt", "w") as f:
#                     f.write(str(e))
#                 continue    

#             output_file_name = file + ".py"
#             with open("../output/" + output_file_name , 'w') as output_file:
#                 output_file.write(generated_output)

#             output_api_form = file + ".txt"
#             with open("../output/" + output_api_form , 'w') as output_file:
#                 output_file.write(api_form)


# Use this if API json forms are available
if __name__ == "__main__":
    import sys
    import argparse

    parser = argparse.ArgumentParser(
        prog='ToolFactoryExtractor',
        description='Extract JSON information from API Documentations',
    )
    parser.add_argument(
        "filepath",
        type=str,
        help="Path to the file that needs to be processed."
    )
    parser.add_argument(
        "-o", "--overwrite",
        action="store_true",
        help="Specify this flag to overwrite the file if it already exists."
    )
    args = parser.parse_args()

    load_dotenv()
    extractor = Extractor()
    generator = Generator()

    folder_path = args.filepath
    overwrite = args.overwrite
    if is_url(folder_path):
        print(f"Downloading OpenAPI spec from: {folder_path}")
        response = requests.get(folder_path)
        if response.status_code != 200:
            raise ValueError(f"Failed to download URL: {folder_path}")
        os.makedirs("temp", exist_ok=True)
        folder_path = "temp/openapi.json"
        with open(folder_path, "w") as f:
            f.write(response.text)

    if folder_path.endswith(".json"):
        with open(folder_path, 'r', encoding='utf-8') as api_file:
            openapi_data = json.load(api_file)
        api_form = generator.convert_openapi_to_toolformat(openapi_data)
        generator.generate_from_api_json_and_save(api_form, "output")
    else:
        api_folders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]
        for api_folder in api_folders:
            api_path = os.path.join(folder_path, api_folder)
            
            # Look for documentation files in order of preference
            api_html = [f for f in os.listdir(api_path) if f.endswith('.html')]
            api_markdown = [f for f in os.listdir(api_path) if f.endswith('.md')]
            api_json = [f for f in os.listdir(api_path) if f.endswith('.json')]
            api_txt = [f for f in os.listdir(api_path) if f.endswith('.txt') and not f.startswith(api_folder)]  # Exclude the output .txt file
            
            # Determine which file to use and appropriate parser
            api_file_path = None
            file_parser = None
            file_type = None
            
            # Priority: check for existing doc.md first, then process other formats
            doc_md_path = os.path.join(api_path, "doc.md")
            
            if os.path.exists(doc_md_path):
                api_file_path = doc_md_path
                file_parser = markdown_file_parser
                file_type = "existing doc.md"
                print(f"Processing existing doc.md for API: {api_folder}")
            elif api_html:
                # Convert HTML to markdown first
                html_file_path = os.path.join(api_path, api_html[0])
                print(f"Found HTML file: {api_html[0]} for API: {api_folder}")
                converted_md_path = convert_html_to_markdown(html_file_path)
                if converted_md_path:
                    api_file_path = converted_md_path
                    file_parser = markdown_file_parser
                    file_type = "converted from HTML"
                    print(f"Processing converted doc.md for API: {api_folder}")
                else:
                    print(f"Failed to convert HTML, skipping API: {api_folder}")
                    continue
            elif api_markdown:
                # Copy markdown to doc.md
                markdown_file_path = os.path.join(api_path, api_markdown[0])
                print(f"Found Markdown file: {api_markdown[0]} for API: {api_folder}")
                copied_md_path = copy_file_to_doc_md(markdown_file_path, "Markdown")
                if copied_md_path:
                    api_file_path = copied_md_path
                    file_parser = markdown_file_parser
                    file_type = "copied from Markdown"
                    print(f"Processing copied doc.md for API: {api_folder}")
                else:
                    print(f"Failed to copy Markdown, skipping API: {api_folder}")
                    continue
            elif api_json:
                # Copy JSON to doc.md
                json_file_path = os.path.join(api_path, api_json[0])
                print(f"Found JSON file: {api_json[0]} for API: {api_folder}")
                copied_md_path = copy_file_to_doc_md(json_file_path, "JSON")
                if copied_md_path:
                    api_file_path = copied_md_path
                    file_parser = markdown_file_parser
                    file_type = "copied from JSON"
                    print(f"Processing copied doc.md for API: {api_folder}")
                else:
                    print(f"Failed to copy JSON, skipping API: {api_folder}")
                    continue
            elif api_txt:
                # Copy TXT to doc.md
                txt_file_path = os.path.join(api_path, api_txt[0])
                print(f"Found TXT file: {api_txt[0]} for API: {api_folder}")
                copied_md_path = copy_file_to_doc_md(txt_file_path, "TXT")
                if copied_md_path:
                    api_file_path = copied_md_path
                    file_parser = markdown_file_parser
                    file_type = "copied from TXT"
                    print(f"Processing copied doc.md for API: {api_folder}")
                else:
                    print(f"Failed to copy TXT, skipping API: {api_folder}")
                    continue
            else:
                print(f"No supported documentation files found for API: {api_folder}")
                print(f"  Looked for: HTML, MD, JSON, TXT files")
                continue
                
            target_path = os.path.join(api_path, api_folder + ".txt")
            config_path = os.path.join(api_path, ".config")
            config = None
            if os.path.exists(config_path):
                with open(config_path, 'r') as config_file:
                    config = config_file.read()
                    config = json.loads(config)
            if overwrite or not os.path.exists(target_path):
                print(f"  Extracting API JSON from {file_type}...")
                api_form = extractor.extract_api_json(api_file_path, file_parser)
            else:
                with open(target_path, 'r', encoding='utf-8') as api_file: # load in utf-8
                    api_form = api_file.read()
            
            with open(os.path.join(api_path, api_folder + ".txt"), 'w', encoding='utf-8') as api_file:
                api_file.write(api_form)
            generator.generate_from_api_json_and_save(api_form, api_path, config)