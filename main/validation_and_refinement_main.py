import os
import json
import subprocess
import sys
import ast
from pathlib import Path
import re
from markdown import markdown


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.validation_and_refinement.kb_builder import (
    build_parameter_dict,
    build_description_dicts,
    build_response_dict
)
from utils.validation_and_refinement.kb_searcher import (
    initialize_model,
    encode_keys,
)
from utils.validation_and_refinement.gpt_eval import (
    initialize_gpt_evaluator,
    gpt_evaluate,
)
from utils.validation_and_refinement.fix_code import (
    initialize_claude,
    fix_code,
)
from utils.validation_and_refinement.kb_searcher import search_kb


def main():
    # Define the path to the API docs
    apidocs_dir = os.path.join("extractor", "apidocs")

    print("Building knowledge bases...")
    # Build the parameter dictionary
    parameter_dict = build_parameter_dict(apidocs_dir)

    # Build the description dictionaries
    description_to_param_dict, param_to_description_dict = build_description_dicts(apidocs_dir)

    print("Initializing embedding model...")
    # Initialize the embedding model
    embedding_model = initialize_model()
    
    # Encode the keys
    param_keys, param_keys_emb = encode_keys(embedding_model, parameter_dict)
    description_keys, description_keys_emb = encode_keys(embedding_model, description_to_param_dict)

    # Initialize the GPT evaluator
    print("Initializing GPT evaluator...")
    gpt, gpt_prompt = initialize_gpt_evaluator()

    # Initialize the Claude code fixer
    print("Initializing Claude API client...")
    claude = initialize_claude()

    # Document the success and error counts
    tool_success = 0
    tool_code_error = 0
    tool_server_error = 0
    tool_hard_error = 0

    # Validation starts
    need_refinement = []
    successful_tools = []
    # successful_tools_dir = "webarena_tools_toRyan/gitlab"
    print("Validating tools...")
    for tool_folder in os.listdir(apidocs_dir):
        # if tool_folder != "":
        #     continue

        # get the python tool scripts
        files = os.listdir(os.path.join(apidocs_dir, tool_folder))
        tools = [x for x in files if x.endswith(".py")]
        # get the api json file
        api_txt = [x for x in files if x.endswith(".txt")]
        api_json = json.load(open(os.path.join(apidocs_dir, tool_folder, api_txt[0])))
        
        for tool in tools:

            print(f"Validating tool: {tool}")

            tool_path = os.path.join(apidocs_dir, tool_folder, tool)
            code = open(tool_path, "r").read()
            function_name = extract_function_names(code)

            api_description = api_json
            for endpoint in api_json["endpoints"]:
                api_name = endpoint["name"].lower()
                api_name = re.sub(r'\W', '_', api_name)
                if function_name == api_name:
                    api_description = endpoint["description"]
                    print(f"API description: {api_description}")
                    break
            
            try:
                result = subprocess.run(
                    ["python", tool_path], capture_output=True, text=True, check=True
                )
                if result.stdout:
                    output = result.stdout
                    gpt_answer = gpt_evaluate(
                        gpt,
                        gpt_prompt,
                        api_description=api_description,
                        api_response=output,
                        code=code,
                    )
                    if gpt_answer == "code_error":
                        tool_code_error += 1
                        need_refinement.append(tool_path)
                        print(f"Tool {tool_path} returned a code error.")
                    elif gpt_answer == "server_error":
                        tool_server_error += 1
                        print(f"Tool {tool_path} returned a server error.")
                    elif gpt_answer == "information":
                        tool_success += 1
                        output_json = json.loads(output)
                        successful_tools.append(tool_path)
                        # save in file
                        with open(tool_path[:-3] + '_response.json', "w") as f:
                            json.dump(output_json, f)
                        print(f"Tool {tool_path} executed successfully.")
                        # copy the successful tools to a new folder
                        # with open(successful_tools_dir + '/' + tool, "w") as f:
                        #     f.write(code)
                        
                    else:
                        print(f"Tool {tool_path} gpt answer: {gpt_answer}")
            except subprocess.CalledProcessError as e:
                tool_hard_error += 1
                need_refinement.append(tool_path)
                print(f"Tool {tool_path} cannot be executed.")
            
            print("---------------------------\n")

    print(
        f"Tool success: {tool_success}, Tool code error: {tool_code_error}, Tool server error: {tool_server_error}, Tool hard error: {tool_hard_error}"
    )
    print("####################################\n")


    with open("main/need_refinement.txt", "w") as f:
        for tool in need_refinement:
            f.write(tool + "\n")

    # build the response dictionary
    print("Building response dictionary...")
    response_dict = build_response_dict(apidocs_dir)
    # build the response keys
    response_keys, response_keys_emb = encode_keys(embedding_model, response_dict)
    
    # Refine the tools
    refine_success = 0
    refine_fail = 0
    print("Refining tools...")
    for tool_folder in os.listdir(apidocs_dir):
        # get the python tool scripts
        files = os.listdir(os.path.join(apidocs_dir, tool_folder))
        tools = [x for x in files if x.endswith(".py")]
        # get the api json file
        api_txt = [x for x in files if x.endswith(".txt")]
        api_json = json.load(open(os.path.join(apidocs_dir, tool_folder, api_txt[0]))) 
        md_text = open(os.path.join(apidocs_dir, tool_folder, api_txt[0][:-3] + "md"), encoding="utf-8").read()
        
        for tool in tools:
            tool_path = os.path.join(apidocs_dir, tool_folder, tool)
            if tool_path not in need_refinement:
                continue
            code = open(tool_path, "r").read()
            function_name = extract_function_names(code)
            
            api_description = None
            for endpoint in api_json["endpoints"]:
                api_name = endpoint["name"].lower()
                api_name = re.sub(r'\W', '_', api_name)
                if function_name == api_name:
                    api_description = endpoint["description"]
                    print(f"API description: {api_description}")
                    break
    
            try:
                result = subprocess.run(
                    ["python", tool_path], capture_output=True, text=True, check=True
                )
                if result.stdout:
                    output = result.stdout
                    error_message = result.stdout.strip() if len(result.stdout) < 500 else result.stdout[:500]

                    # Get the required parameters from the code
                    params = get_required_param_name(tool_path)
                    param_examples = {}
                    for param in params:
                        # Search the knowledge base for the most relevant keys to the query.
                        example = search_kb(param, param_keys, param_keys_emb, parameter_dict, response_keys, response_keys_emb, response_dict, description_keys, description_to_param_dict, description_keys_emb, embedding_model)
                        param_examples[param] = example
                    
                    print(param_examples)

                    # Fix the code using Claude
                    # new_code = fix_code(claude, code, error_message, api_description, param_examples)
                    new_code = fix_code(claude, code, error_message, md_text, param_examples)
                    # time.sleep(10)
                    with open(tool_path, "w") as f:
                        f.write(new_code)
                    print(f"Refined: {tool}")
            except subprocess.CalledProcessError as e:
                error_message = e.stderr.strip() if len(e.stderr) < 500 else e.stderr[:500]

                # Get the required parameters from the code
                params = get_required_param_name(tool_path)
                param_examples = {}
                for param in params:
                    # Search the knowledge base for the most relevant keys to the query.
                    example = search_kb(param, param_keys, param_keys_emb, parameter_dict, response_keys, response_keys_emb, response_dict, description_keys, description_to_param_dict, description_keys_emb, embedding_model)
                    param_examples[param] = example
                
                print(param_examples)

                # Fix the code using Claude
                # new_code = fix_code(claude, code, error_message, api_description, param_examples)
                new_code = fix_code(claude, code, error_message, md_text, param_examples)
                # time.sleep(10)
                with open(tool_path, "w") as f:
                    f.write(new_code)
                print(f"Refined: {tool}")
            finally:
                try:
                    result = subprocess.run(
                        ["python", tool_path], capture_output=True, text=True, check=True
                    )
                    if result.stdout:
                        output = result.stdout if len(result.stdout) < 500 else result.stdout[:500]
                        gpt_answer = gpt_evaluate(
                            gpt,
                            gpt_prompt,
                            api_description=api_description,
                            api_response=output,
                            code=code,
                        )
                    if gpt_answer == "information":
                        refine_success += 1
                        successful_tools.append(tool_path)
                        print(f"Refined tool {tool_path} executed successfully.")
                        # copy the successful tools to a new folder
                        # with open(successful_tools_dir + '/' + tool, "w") as f:
                        #     f.write(code)
                    elif gpt_answer == "code_error":
                        refine_fail += 1
                        print(f"Refined tool {tool_path} returned a code error.")
                except subprocess.CalledProcessError as e:
                    refine_fail += 1
                    print(f"Refined tool {tool_path} cannot be executed.")
                finally:
                    print("---------------------------\n")

    print(f"Refine success: {refine_success}, Refine fail: {refine_fail}, NumToolsNeedRefinement: {len(need_refinement)}")

    # copy the successful tools to a new folder
    successful_tools_dir = "webarena_tools_toRyan"
    for tool in successful_tools:
        tool_name = os.path.basename(tool)
        new_tool_path = os.path.join(successful_tools_dir, tool_name)
        with open(new_tool_path, "w") as f:
            f.write(open(tool, "r").read())

def get_required_param_name(path: str | Path):
    source = Path(path).read_text(encoding="utf-8")
    try:
        tree = ast.parse(source, filename=str(path))
    except Exception as e:
        return []

    src_lines = source.splitlines()
    out = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Assert):
            line_text = src_lines[node.lineno - 1]
            out.append((node.lineno, line_text))

    params = []
    for _, text in out:
        param = text.strip().split(" ")[1].strip()
        params.append(param)
    
    return params

def extract_function_names(code_str):
    """
    Extracts function names from a given Python code string.
    
    Args:
        code_str (str): A string containing Python code
        
    Returns:
        list: A list of function names found in the code
    """
    function_names = []
    
    class FunctionVisitor(ast.NodeVisitor):
        def visit_FunctionDef(self, node):
            function_names.append(node.name)
            self.generic_visit(node)  # Continue visiting child nodes
            
    try:
        tree = ast.parse(code_str)
        visitor = FunctionVisitor()
        visitor.visit(tree)
    except SyntaxError as e:
        print(f"Syntax error in code: {e}")
        return []
    
    if not function_names:
        print("No function names found in the code.")
        return []
    
    # return function_names[1]
    return function_names[0]

def find_api_in_md(md, api_endpoint):
    chunk = md.split(api_endpoint)
    if len(chunk) < 2:
        return md
    




if __name__ == "__main__":
    main()
