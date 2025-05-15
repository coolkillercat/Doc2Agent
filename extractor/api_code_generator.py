from api_json_extractor import Extractor
import json
import os
import re
import requests
from dotenv import load_dotenv

def is_url(path):
    return path.startswith("http://") or path.startswith("https://")

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
        self.save_to_registry(api_form)
        for endpoint in api_form['endpoints']:    
            method = endpoint['method']
            api_name = endpoint['name']
            # Replace all non-alphanumeric characters with underscore
            api_name = re.sub(r'\W', '_', api_name)
            # Convert to lowercase
            api_name = api_name.lower()
            if method == "GET":
                if isinstance(endpoint['url'], list):
                    endpoint_url = endpoint['url'][0]
                else:
                    endpoint_url = endpoint['url']
                # Replace < and > with { and } in url   
                endpoint_url = endpoint_url.replace("<", "{").replace(">", "}")
                url = '"' + endpoint_url + '"'
                required_param = endpoint['required_parameters']
                querystring = "{"
                param_list = ""
                param_example = []
                for param in required_param:
                    param_name = re.sub(r'\W', '_', param['name'])
                    is_string_type = param["type"] == "string"
                    param_list += param_name
                    if param["default"]: # if default, assigne default value to param
                        if is_string_type:
                            param_list += f"='{param['default']}'"
                        else:
                            param_list += f"={param['default']}"
                    param_list += ", "
                    querystring += f"'{param_name}': {param_name}, "
                    example_value = f"'{param['example']}'" if is_string_type else f"{param['example']}"
                    param_example.append(example_value)
                querystring += "}"
                param_list = param_list[:-2]
                with open('./template/GET_template.txt', 'r') as template_file:
                    code_template = template_file.read()
                param_examples_seperated = ", ".join(param_example)
                generated_code += code_template.format(param_list=param_list, url=url, querystring=querystring, api_name=api_name, param_examples_seperated=param_examples_seperated) + "\n"
                # generated_code += f"{api_name}({', '.join(param_example)})\n\n"
            elif method == "POST":
                if isinstance(endpoint['url'], list):
                    endpoint_url = endpoint['url'][0]
                else:
                    endpoint_url = endpoint['url']
                endpoint_url = endpoint_url.replace("<", "{").replace(">", "}")
                url = '"' + endpoint_url + '"'
                required_param = endpoint['required_parameters']
                payload = "{"
                param_list = ""
                param_example = []
                for param in required_param:
                    param_name = re.sub(r'\W', '_', param['name'])
                    is_string_type = param["type"] == "string"

                    param_list += param_name
                    if param["default"]: # if default, assigne default value to param
                        if is_string_type:
                            param_list += f"='{param['default']}'"
                        else:
                            param_list += f"={param['default']}"
                    param_list += ", "
                    payload += f"'{param_name}': {param_name}, "
                    example_value = f"'{param['example']}'" if is_string_type else f"{param['example']}"
                    param_example.append(example_value)
                payload += "}"
                param_list = param_list[:-2]
                
                with open('./template/POST_template.txt', 'r') as template_file:
                    code_template = template_file.read()
                param_examples_seperated = ", ".join(param_example)
                generated_code += code_template.format(param_list=param_list, url=url, payload=payload, api_name=api_name, param_examples_seperated=param_examples_seperated) + "\n"
                # generated_code += f"{api_name}({', '.join(param_example)})\n\n"

        return generated_code

    def generate_from_api_json_and_save(self, api_form, output_folder_path, config=None):
        if isinstance(api_form, str):
            api_form = json.loads(api_form)
        for endpoint in api_form['endpoints']:     
            generated_code = ""
            method = endpoint['method']
            api_name = endpoint['name']
            # Replace all non-alphanumeric characters with underscore
            api_name = re.sub(r'\W', '_', api_name)
            # Convert to lowercase
            api_name = api_name.lower()
            if method == "GET":
                if isinstance(endpoint['url'], list):
                    endpoint_url = endpoint['url'][0]
                else:
                    endpoint_url = endpoint['url']
                # Replace < and > with { and } in url   
                endpoint_url = endpoint_url.replace("<", "{").replace(">", "}")
                endpoint_url = endpoint_url.replace(" ", "_")
                if config and "base_url" in config:
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
                generated_code += code_template.format(param_list=param_list, url=url, querystring=querystring, api_name=api_name, validate_req_param=validate_req_param, param_examples_seperated=param_examples_seperated) + "\n"
                # generated_code += f"if __name__ == '__main__':\n\tprint({api_name}({', '.join(param_example)}))\n\n"
            elif method == "POST":
                if isinstance(endpoint['url'], list):
                    endpoint_url = endpoint['url'][0]
                else:
                    endpoint_url = endpoint['url']
                endpoint_url = endpoint_url.replace("<", "{").replace(">", "}")
                endpoint_url = endpoint_url.replace(" ", "_")
                if config and "base_url" in config:
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
                generated_code += code_template.format(param_list=param_list, url=url, payload=payload, api_name=api_name, validate_req_param=validate_req_param, param_examples_seperated=param_examples_seperated) + "\n"
                # generated_code += f"if __name__ == '__main__':\n\tprint({api_name}({', '.join(param_example)}))\n\n"
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
            api_html = [f for f in os.listdir(api_path) if f.endswith('.html')][0]
            target_path = os.path.join(api_path, api_folder + ".txt")
            config_path = os.path.join(api_path, ".config")
            config = None
            if os.path.exists(config_path) and not overwrite:
                with open(config_path, 'r') as config_file:
                    config = json.load(config_file)
            if os.path.exists(target_path):
                with open(target_path, 'r', encoding='utf-8') as api_file:
                    api_form = api_file.read()
            else:
                html_file = os.path.join(api_path, api_html)
                api_form = extractor.extract_api_json(html_file)

            with open(os.path.join(api_path, api_folder + ".txt"), 'w', encoding='utf-8') as api_file:
                api_file.write(api_form)
            generator.generate_from_api_json_and_save(api_form, api_path, config)
