import os
import json
import subprocess
import sys
import ast
from pathlib import Path
import re
from typing import List, Set, Optional

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
    from dotenv import load_dotenv
    load_dotenv()
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
    print("Validating tools...")
    # Set up logging
    import logging
    logging.basicConfig(
        filename='validation.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logger = logging.getLogger(__name__)
    
    # Load existing metadata if available
    metadata_table = {'tools': []}
    if os.path.exists('tool_validation_metadata.json'):
        try:
            with open('tool_validation_metadata.json', 'r') as f:
                metadata_table = json.load(f)
            logger.info(f"Loaded existing metadata with {len(metadata_table['tools'])} tools")
            print(f"Loaded existing metadata with {len(metadata_table['tools'])} tools")
            
            # Count existing stats
            for tool in metadata_table['tools']:
                if tool['status'] == 'information':
                    tool_success += 1
                elif tool['status'] == 'code_error':
                    tool_code_error += 1
                    need_refinement.append(tool['path'])
                elif tool['status'] == 'server_error':
                    tool_server_error += 1
                elif tool['status'] == 'hard_error':
                    tool_hard_error += 1
                    need_refinement.append(tool['path'])
        except Exception as e:
            logger.error(f"Error loading metadata: {str(e)}")
            print(f"Error loading metadata: {str(e)}")
    
    SAVE_INTERVAL = 10  # Save every 10 tools processed
    
    # Keep track of validated tools to avoid duplicates
    validated_tools = {tool['path'] for tool in metadata_table['tools']}
    
    for tool_folder in os.listdir(apidocs_dir):
        # get the python tool scripts
        files = os.listdir(os.path.join(apidocs_dir, tool_folder))
        tools = [x for x in files if x.endswith(".py")]
        # get the api json file
        api_txt = [x for x in files if x.endswith(".txt")]
        api_json = json.load(open(os.path.join(apidocs_dir, tool_folder, api_txt[0])))
        
        for tool in tools:
            tool_path = os.path.join(apidocs_dir, tool_folder, tool)
            
            # Skip if already validated
            if tool_path in validated_tools:
                logger.info(f"Skipping already validated tool: {tool}")
                print(f"Skipping already validated tool: {tool}")
                continue

            logger.info(f"Validating tool: {tool}")
            print(f"Validating tool: {tool}")

            code = open(tool_path, "r").read()
            function_name = extract_function_names(code)

            api_description = api_json
            for endpoint in api_json["endpoints"]:
                api_name = endpoint["name"].lower()
                api_name = re.sub(r'\W', '_', api_name)
                if function_name == api_name:
                    api_description = endpoint["description"]
                    logger.info(f"API description: {api_description}")
                    print(f"API description: {api_description}")
                    break

            tool_metadata = {
                'path': tool_path,
                'function_name': function_name,
                'api_description': api_description,
                'status': None,
                'error_type': None
            }

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
                    tool_metadata['status'] = gpt_answer
                    
                    if gpt_answer == "code_error":
                        tool_code_error += 1
                        need_refinement.append(tool_path)
                        tool_metadata['error_type'] = 'code_error'
                        logger.error(f"Tool {tool_path} returned a code error.")
                        print(f"Tool {tool_path} returned a code error.")
                    elif gpt_answer == "server_error":
                        tool_server_error += 1
                        tool_metadata['error_type'] = 'server_error'
                        logger.error(f"Tool {tool_path} returned a server error.")
                        print(f"Tool {tool_path} returned a server error.")
                    elif gpt_answer == "information":
                        tool_success += 1
                        output_json = json.loads(output)
                        # save in file
                        with open(tool_path[:-3] + '_response.json', "w") as f:
                            json.dump(output_json, f)
                        logger.info(f"Tool {tool_path} executed successfully.")
                        print(f"Tool {tool_path} executed successfully.")
                    else:
                        logger.warning(f"Tool {tool_path} gpt answer: {gpt_answer}")
                        print(f"Tool {tool_path} gpt answer: {gpt_answer}")
            except subprocess.CalledProcessError as e:
                tool_hard_error += 1
                need_refinement.append(tool_path)
                tool_metadata['status'] = 'hard_error'
                tool_metadata['error_type'] = str(e)
                logger.error(f"Tool {tool_path} cannot be executed. Error: {str(e)}")
                print(f"Tool {tool_path} cannot be executed.")
            
            # Add tool metadata to table
            metadata_table['tools'].append(tool_metadata)
            
            # Save metadata table periodically
            if len(metadata_table['tools']) % SAVE_INTERVAL == 0:
                with open('tool_validation_metadata.json', 'w') as f:
                    json.dump(metadata_table, f, indent=2)
                logger.info(f"Saved metadata table with {len(metadata_table['tools'])} tools")
            
            logger.info("---------------------------")
            print("---------------------------\n")

    # Save final metadata table
    with open('tool_validation_metadata.json', 'w') as f:
        json.dump(metadata_table, f, indent=2)
    
    summary = f"Tool success: {tool_success}, Tool code error: {tool_code_error}, Tool server error: {tool_server_error}, Tool hard error: {tool_hard_error}"
    logger.info(summary)
    print(summary)

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
    import time
    # Load existing refinement metadata if available
    refinement_metadata = {'tools': []}
    if os.path.exists('tool_refinement_metadata.json'):
        try:
            with open('tool_refinement_metadata.json', 'r') as f:
                refinement_metadata = json.load(f)
            logger.info(f"Loaded existing refinement metadata with {len(refinement_metadata['tools'])} tools")
            print(f"Loaded existing refinement metadata with {len(refinement_metadata['tools'])} tools")
            
            # Count existing refinement stats
            for tool in refinement_metadata['tools']:
                if tool['status'] == 'success':
                    refine_success += 1
                elif tool['status'] == 'fail':
                    refine_fail += 1
        except Exception as e:
            logger.error(f"Error loading refinement metadata: {str(e)}")
            print(f"Error loading refinement metadata: {str(e)}")
    
    # Keep track of refined tools to avoid duplicates
    refined_tools = {tool['path'] for tool in refinement_metadata['tools']}
    
    for tool_folder in os.listdir(apidocs_dir):
        # get the python tool scripts
        files = os.listdir(os.path.join(apidocs_dir, tool_folder))
        tools = [x for x in files if x.endswith(".py")]
        # get the api json file
        api_txt = [x for x in files if x.endswith(".txt")]
        api_json = json.load(open(os.path.join(apidocs_dir, tool_folder, api_txt[0])))
        
        for tool in tools:
            tool_path = os.path.join(apidocs_dir, tool_folder, tool)
            if tool_path not in need_refinement:
                continue
                
            # Skip if already refined
            if tool_path in refined_tools:
                logger.info(f"Skipping already refined tool: {tool}")
                print(f"Skipping already refined tool: {tool}")
                continue
                
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
    
            tool_refinement_metadata = {
                'path': tool_path,
                'function_name': function_name,
                'api_description': api_description,
                'status': None,
                'error_type': None
            }
    
            try:
                result = subprocess.run(
                    ["python", tool_path], capture_output=True, text=True, check=True
                )
                if result.stdout:
                    output = result.stdout
                    error_message = result.stdout.strip()

                    # Get the required parameters from the code
                    params = get_required_param_name(tool_path)
                    param_examples = {}
                    for param in params:
                        # Search the knowledge base for the most relevant keys to the query.
                        example = search_kb(param, param_keys, param_keys_emb, parameter_dict, response_keys, response_keys_emb, response_dict, description_keys, description_to_param_dict, description_keys_emb, embedding_model)
                        param_examples[param] = example
                    
                    print(param_examples)

                    # Fix the code using Claude
                    for _ in range(3):
                        try:
                            new_code = fix_code(claude, code, error_message, api_description, param_examples)
                            break
                        except:
                            time.sleep(60) # prevent overflow
                            new_code = ''
                    if not new_code: # failed 3 times
                        print("skip")
                        continue
                    with open(tool_path, "w") as f:
                        f.write(new_code)
                    print(f"Refined: {tool}")
            except subprocess.CalledProcessError as e:
                error_message = e.stderr.strip()

                # Get the required parameters from the code
                try:
                    params = get_required_param_name(tool_path)
                except:
                    continue
                param_examples = {}
                for param in params:
                    # Search the knowledge base for the most relevant keys to the query.
                    example = search_kb(param, param_keys, param_keys_emb, parameter_dict, response_keys, response_keys_emb, response_dict, description_keys, description_to_param_dict, description_keys_emb, embedding_model)
                    param_examples[param] = example
                
                print(param_examples)

                # Fix the code using Claude
                import time
                for _ in range(3):
                    try:
                        new_code = fix_code(claude, code, error_message, api_description, param_examples)
                        break
                    except:
                        new_code = ''
                        time.sleep(60)
                        continue
                with open(tool_path, "w", encoding='UTF-8') as f:
                    f.write(new_code)
                print(f"Refined: {tool}")
            finally:
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
                    if not gpt_answer:
                        continue
                    if gpt_answer == "information":
                        refine_success += 1
                        tool_refinement_metadata['status'] = 'success'
                        print(f"Refined tool {tool_path} executed successfully.")
                    elif gpt_answer == "code_error":
                        refine_fail += 1
                        tool_refinement_metadata['status'] = 'fail'
                        tool_refinement_metadata['error_type'] = 'code_error'
                        print(f"Refined tool {tool_path} returned a code error.")
                except subprocess.CalledProcessError as e:
                    refine_fail += 1
                    tool_refinement_metadata['status'] = 'fail'
                    tool_refinement_metadata['error_type'] = str(e)
                    print(f"Refined tool {tool_path} cannot be executed.")
                finally:
                    # Add tool refinement metadata to table
                    refinement_metadata['tools'].append(tool_refinement_metadata)
                    
                    # Save refinement metadata periodically
                    if len(refinement_metadata['tools']) % SAVE_INTERVAL == 0:
                        with open('tool_refinement_metadata.json', 'w') as f:
                            json.dump(refinement_metadata, f, indent=2)
                        logger.info(f"Saved refinement metadata table with {len(refinement_metadata['tools'])} tools")
                    
                    print("---------------------------\n")

    # Save final refinement metadata table
    with open('tool_refinement_metadata.json', 'w') as f:
        json.dump(refinement_metadata, f, indent=2)

    print(f"Refine success: {refine_success}, Refine fail: {refine_fail}, NumToolsNeedRefinement: {len(need_refinement)}")


    # # Validation starts again
    # print("Validating tools again...")
    # tool_success = 0
    # tool_code_error = 0
    # tool_server_error = 0
    # tool_hard_error = 0

    # # run the tools
    # for tool_folder in os.listdir(apidocs_dir):
    #     # get the python tool scripts
    #     files = os.listdir(os.path.join(apidocs_dir, tool_folder))
    #     tools = [x for x in files if x.endswith(".py")]
    #     # get the api json file
    #     api_txt = [x for x in files if x.endswith(".txt")]
    #     api_json = json.load(open(os.path.join(apidocs_dir, tool_folder, api_txt[0])))
        
    #     for tool in tools:
    #         tool_path = os.path.join(apidocs_dir, tool_folder, tool)
    #         code = open(tool_path, "r").read()
    #         try:
    #             result = subprocess.run(
    #                 ["python", tool_path], capture_output=True, text=True, check=True
    #             )
    #             if result.stdout:
    #                 output = result.stdout
    #                 gpt_answer = gpt_evaluate(
    #                     gpt,
    #                     gpt_prompt,
    #                     api_description=api_json,
    #                     api_response=output,
    #                     code=code,
    #                 )
    #                 if gpt_answer == "code_error":
    #                     tool_code_error += 1
    #                     print(f"Tool {tool_path} returned a code error.")
    #                 elif gpt_answer == "server_error":
    #                     tool_server_error += 1
    #                     print(f"Tool {tool_path} returned a server error.")
    #                 elif gpt_answer == "information":
    #                     tool_success += 1
    #                     print(f"Tool {tool_path} executed successfully.")
    #                 else:
    #                     print(f"Tool {tool_path} gpt answer: {gpt_answer}")
    #         # except subprocess.CalledProcessError as e:
    #         except Exception as e:
    #             tool_hard_error += 1
    #             print(f"Tool {tool_path} cannot be executed.")
    
    # print(
    #     f"Tool success: {tool_success}, Tool code error: {tool_code_error}, Tool server error: {tool_server_error}, Tool hard error: {tool_hard_error}"
    # )
    


def get_required_param_name(path: str | Path):
    source = Path(path).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(path))

    src_lines = source.splitlines()
    out = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Assert):
            line_text = src_lines[node.lineno - 1]
            out.append((node.lineno, line_text))

    params = []
    for lineno, text in out:
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
    
    if function_names:
        return function_names[0]
    return []

if __name__ == "__main__":
    main()
