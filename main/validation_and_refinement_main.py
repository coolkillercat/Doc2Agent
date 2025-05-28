import os
import json
import subprocess
import sys
import ast
from pathlib import Path
import re
from markdown import markdown

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


def setup_logging():
    """Set up logging configuration"""
    import logging
    logging.basicConfig(
        filename='validation.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger(__name__)


def initialize_knowledge_bases(apidocs_dir):
    """Initialize knowledge bases and embedding models"""
    print("Building knowledge bases...")
    parameter_dict = build_parameter_dict(apidocs_dir)
    description_to_param_dict, param_to_description_dict = build_description_dicts(apidocs_dir)
    
    print("Initializing embedding model...")
    embedding_model = initialize_model()
    
    param_keys, param_keys_emb = encode_keys(embedding_model, parameter_dict)
    description_keys, description_keys_emb = encode_keys(embedding_model, description_to_param_dict)
    
    return {
        'parameter_dict': parameter_dict,
        'description_to_param_dict': description_to_param_dict,
        'param_to_description_dict': param_to_description_dict,
        'embedding_model': embedding_model,
        'param_keys': param_keys,
        'param_keys_emb': param_keys_emb,
        'description_keys': description_keys,
        'description_keys_emb': description_keys_emb
    }


def initialize_ai_models():
    """Initialize GPT evaluator and Claude fixer"""
    print("Initializing GPT evaluator...")
    gpt, gpt_prompt = initialize_gpt_evaluator()
    
    print("Initializing Claude API client...")
    claude = initialize_claude()
    
    return gpt, gpt_prompt, claude


def load_api_data(apidocs_dir, tool_folder):
    """Load API data for a specific tool folder"""
    files = os.listdir(os.path.join(apidocs_dir, tool_folder))
    tools = [x for x in files if x.endswith(".py")]
    api_txt = [x for x in files if x.endswith(".txt")]
    api_json = json.load(open(os.path.join(apidocs_dir, tool_folder, api_txt[0])))
    return tools, api_json


def get_api_description(api_json, function_name):
    """Get API description for a specific function"""
    for endpoint in api_json["endpoints"]:
        api_name = endpoint["name"].lower()
        api_name = re.sub(r'\W', '_', api_name)
        if function_name == api_name:
            return endpoint["description"]
    return api_json


def validation(apidocs_dir="extractor/apidocs/", use_existing_metadata=True):
    """Validate all tools in the API docs directory
    
    Args:
        apidocs_dir (str): Path to the API docs directory
        use_existing_metadata (bool): If True, load and continue from existing metadata.
                                    If False, start fresh and overwrite existing metadata.
    """
    logger = setup_logging()
    
    # Initialize knowledge bases and models
    kb_data = initialize_knowledge_bases(apidocs_dir)
    gpt, gpt_prompt, claude = initialize_ai_models()
    
    # Document the success and error counts
    tool_success = 0
    tool_code_error = 0
    tool_server_error = 0
    tool_hard_error = 0
    
    need_refinement = []
    successful_tools = []
    
    # Load existing metadata if available and requested
    metadata_table = {'tools': []}
    if use_existing_metadata and os.path.exists('tool_validation_metadata.json'):
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
    elif not use_existing_metadata:
        logger.info("Starting fresh validation - existing metadata will be overwritten")
        print("Starting fresh validation - existing metadata will be overwritten")
    
    SAVE_INTERVAL = 10
    validated_tools = {tool['path'] for tool in metadata_table['tools']} if use_existing_metadata else set()
    
    print("Validating tools...")
    for tool_folder in os.listdir(apidocs_dir):
        tools, api_json = load_api_data(apidocs_dir, tool_folder)
        
        for tool in tools:
            tool_path = os.path.join(apidocs_dir, tool_folder, tool)
            
            # Skip if already validated and using existing metadata
            if use_existing_metadata and tool_path in validated_tools:
                logger.info(f"Skipping already validated tool: {tool}")
                print(f"Skipping already validated tool: {tool}")
                continue

            logger.info(f"Validating tool: {tool}")
            print(f"Validating tool: {tool}")

            code = open(tool_path, "r").read()
            function_name = extract_function_names(code)
            api_description = get_api_description(api_json, function_name)
            
            logger.info(f"API description: {api_description}")
            print(f"API description: {api_description}")

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
                        successful_tools.append(tool_path)
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
    
    return {
        'tool_success': tool_success,
        'tool_code_error': tool_code_error,
        'tool_server_error': tool_server_error,
        'tool_hard_error': tool_hard_error,
        'need_refinement': need_refinement,
        'successful_tools': successful_tools
    }


def refinement(apidocs_dir="extractor/apidocs/", need_refinement=None, use_existing_metadata=True):
    """Refine tools that need improvement
    
    Args:
        apidocs_dir (str): Path to the API docs directory
        need_refinement (list): List of tool paths that need refinement. If None, loads from file.
        use_existing_metadata (bool): If True, load and continue from existing metadata.
                                    If False, start fresh and overwrite existing metadata.
    """
    logger = setup_logging()
    
    # Initialize knowledge bases and models
    kb_data = initialize_knowledge_bases(apidocs_dir)
    gpt, gpt_prompt, claude = initialize_ai_models()
    
    # Build response dictionary for refinement
    print("Building response dictionary...")
    response_dict = build_response_dict(apidocs_dir)
    response_keys, response_keys_emb = encode_keys(kb_data['embedding_model'], response_dict)
    
    # Load need_refinement list if not provided
    if need_refinement is None:
        need_refinement = []
        if os.path.exists("main/need_refinement.txt"):
            with open("main/need_refinement.txt", "r") as f:
                need_refinement = [line.strip() for line in f.readlines()]
    
    refine_success = 0
    refine_fail = 0
    successful_tools = []
    
    print("Refining tools...")
    import time
    
    # Load existing refinement metadata if available and requested
    refinement_metadata = {'tools': []}
    if use_existing_metadata and os.path.exists('tool_refinement_metadata.json'):
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
    elif not use_existing_metadata:
        logger.info("Starting fresh refinement - existing metadata will be overwritten")
        print("Starting fresh refinement - existing metadata will be overwritten")
    
    SAVE_INTERVAL = 10
    refined_tools = {tool['path'] for tool in refinement_metadata['tools']} if use_existing_metadata else set()
    
    for tool_folder in os.listdir(apidocs_dir):
        tools, api_json = load_api_data(apidocs_dir, tool_folder)
        
        for tool in tools:
            tool_path = os.path.join(apidocs_dir, tool_folder, tool)
            if tool_path not in need_refinement:
                continue
                
            # Skip if already refined and using existing metadata
            if use_existing_metadata and tool_path in refined_tools:
                logger.info(f"Skipping already refined tool: {tool}")
                print(f"Skipping already refined tool: {tool}")
                continue
                
            code = open(tool_path, "r").read()
            function_name = extract_function_names(code)
            api_description = get_api_description(api_json, function_name)
            print(f"API description: {api_description}")
    
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
                    error_message = result.stdout.strip() if len(result.stdout) < 500 else result.stdout[:500]

                    # Get the required parameters from the code
                    params = get_required_param_name(tool_path)
                    param_examples = {}
                    for param in params:
                        example = search_kb(param, kb_data['param_keys'], kb_data['param_keys_emb'], 
                                          kb_data['parameter_dict'], response_keys, response_keys_emb, 
                                          response_dict, kb_data['description_keys'], 
                                          kb_data['description_to_param_dict'], kb_data['description_keys_emb'], 
                                          kb_data['embedding_model'])
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
                error_message = e.stderr.strip() if len(e.stderr) < 500 else e.stderr[:500]

                # Get the required parameters from the code
                try:
                    params = get_required_param_name(tool_path)
                except:
                    continue
                param_examples = {}
                for param in params:
                    example = search_kb(param, kb_data['param_keys'], kb_data['param_keys_emb'], 
                                      kb_data['parameter_dict'], response_keys, response_keys_emb, 
                                      response_dict, kb_data['description_keys'], 
                                      kb_data['description_to_param_dict'], kb_data['description_keys_emb'], 
                                      kb_data['embedding_model'])
                    param_examples[param] = example
                
                print(param_examples)

                # Fix the code using Claude
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
                        output = result.stdout if len(result.stdout) < 500 else result.stdout[:500]
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
                        successful_tools.append(tool_path)
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
    
    return {
        'refine_success': refine_success,
        'refine_fail': refine_fail,
        'successful_tools': successful_tools
    }


def copy_successful_tools(successful_tools, output_dir="webarena_tools_toRyan"):
    """Copy successful tools to output directory"""
    os.makedirs(output_dir, exist_ok=True)
    for tool in successful_tools:
        tool_name = os.path.basename(tool)
        new_tool_path = os.path.join(output_dir, tool_name)
        with open(new_tool_path, "w") as f:
            f.write(open(tool, "r").read())


def main(use_existing_metadata=True):
    """Main function to run validation and refinement pipeline
    
    Args:
        use_existing_metadata (bool): If True, load and continue from existing metadata.
                                    If False, start fresh and overwrite existing metadata.
    """
    from dotenv import load_dotenv
    load_dotenv()
    
    # Define the path to the API docs
    apidocs_dir = os.path.join("extractor", "apidocs")
    
    # Run validation
    validation_results = validation(apidocs_dir, use_existing_metadata=use_existing_metadata)
    
    # Run refinement
    refinement_results = refinement(apidocs_dir, validation_results['need_refinement'], use_existing_metadata=use_existing_metadata)
    
    # Copy all successful tools to output directory
    all_successful_tools = list(set(validation_results['successful_tools'] + refinement_results['successful_tools']))
    copy_successful_tools(all_successful_tools)


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
