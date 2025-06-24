import os
import json
import subprocess
import sys
import ast
from pathlib import Path
import re
from markdown import markdown
<<<<<<< HEAD
from collections import defaultdict
from sentence_transformers import SentenceTransformer
import anthropic
=======
>>>>>>> 963c487f600a8a356913b965684eb5a41275604c

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
    evaluate_doc_completeness,
)
from utils.validation_and_refinement.fix_code import (
    initialize_claude,
    fix_code,
)
from utils.validation_and_refinement.kb_searcher import search_kb


<<<<<<< HEAD
def load_api_config(tool_folder):
    """Load configuration from .config file in API folder
    
    Args:
        tool_folder: Path to the API tool folder
        
    Returns:
        dict: Configuration dictionary, or None if not found
    """
    config_path = os.path.join(tool_folder, ".config")
    if os.path.exists(config_path):
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
                return config
        except Exception as e:
            print(f"Error loading config from {config_path}: {str(e)}")
    return None


def setup_logging():
    """Set up logging configuration"""
    import logging
    logging.basicConfig(
        filename='validation.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger(__name__)


=======
def setup_logging():
    """Set up logging configuration"""
    import logging
    logging.basicConfig(
        filename='validation.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger(__name__)


>>>>>>> 963c487f600a8a356913b965684eb5a41275604c
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


<<<<<<< HEAD
def create_api_json_from_code(apidocs_dir, tool_folder, tools):
    """Create API JSON structure from Python code docstrings when JSON file is missing
    
    Args:
        apidocs_dir: Directory containing API docs
        tool_folder: The specific tool folder
        tools: List of Python tool files
        
    Returns:
        dict: Mock API JSON structure with endpoints extracted from code
    """
    endpoints = []
    
    for tool in tools:
        tool_path = os.path.join(apidocs_dir, tool_folder, tool)
        try:
            with open(tool_path, 'r', encoding='utf-8') as f:
                code = f.read()
            
            # Extract function name and docstring
            function_name = extract_function_names(code)
            if function_name:
                # Parse the AST to get the docstring
                try:
                    tree = ast.parse(code)
                    for node in ast.walk(tree):
                        if isinstance(node, ast.FunctionDef) and node.name == function_name:
                            docstring = ast.get_docstring(node)
                            if docstring:
                                # Create endpoint entry
                                api_name = function_name.lower()
                                api_name = re.sub(r'\W', '_', api_name)
                                
                                endpoints.append({
                                    "name": api_name,
                                    "description": docstring.strip(),
                                    "method": "GET",  # Default method
                                    "url": f"/{api_name}",  # Mock URL
                                    "parameters": []  # Could be extracted from docstring if needed
                                })
                            break
                except Exception as e:
                    print(f"Error parsing {tool}: {e}")
                    # Fallback: use filename as description
                    api_name = function_name.lower() if function_name else tool[:-3]
                    api_name = re.sub(r'\W', '_', api_name)
                    endpoints.append({
                        "name": api_name,
                        "description": f"API function from {tool}",
                        "method": "GET",
                        "url": f"/{api_name}",
                        "parameters": []
                    })
        except Exception as e:
            print(f"Error reading {tool}: {e}")
    
    return {
        "endpoints": endpoints,
        "base_url": "",
        "description": f"API documentation generated from code in {tool_folder}"
    }


=======
>>>>>>> 963c487f600a8a356913b965684eb5a41275604c
def load_api_data(apidocs_dir, tool_folder):
    """Load API data for a specific tool folder"""
    files = os.listdir(os.path.join(apidocs_dir, tool_folder))
    tools = [x for x in files if x.endswith(".py")]
    api_txt = [x for x in files if x.endswith(".txt")]
<<<<<<< HEAD
    
    # Handle case where API JSON file doesn't exist
    if api_txt:
        api_json = json.load(open(os.path.join(apidocs_dir, tool_folder, api_txt[0]), encoding='utf-8'))
    else:
        # Create a mock API JSON structure from the Python files
        api_json = create_api_json_from_code(apidocs_dir, tool_folder, tools)
    
    return tools, api_json


def get_short_description_from_api_json(api_json, function_name):
    """Extract short description from API JSON for a specific function
    
    Args:
        api_json: The API documentation dictionary
        function_name: The name of the function to get documentation for
        
    Returns:
        str: The short API description from JSON, or empty string if not found
    """
    if not api_json or "endpoints" not in api_json:
        return ""
    
=======
    api_json = json.load(open(os.path.join(apidocs_dir, tool_folder, api_txt[0])))
    return tools, api_json


def get_api_description(api_json, function_name):
    """Get API description for a specific function"""
>>>>>>> 963c487f600a8a356913b965684eb5a41275604c
    for endpoint in api_json["endpoints"]:
        api_name = endpoint["name"].lower()
        api_name = re.sub(r'\W', '_', api_name)
        if function_name == api_name:
<<<<<<< HEAD
            return endpoint.get("description", "")
    return ""


def get_first_sentence_from_docstring(code):
    """Extract the first sentence from the docstring in the code
    
    Args:
        code: The Python code as a string
        
    Returns:
        str: The first sentence of the docstring, or empty string if not found
    """
    try:
        tree = ast.parse(code)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if ast.get_docstring(node):
                    docstring = ast.get_docstring(node)
                    # Extract the first sentence (split by period, exclamation, or question mark)
                    import re
                    sentences = re.split(r'[.!?]+', docstring.strip())
                    if sentences and sentences[0].strip():
                        return sentences[0].strip()
    except:
        pass
    return ""


def get_api_description(api_json, function_name, tool_folder, code=None):
    """Get API description for a specific function
    
    Args:
        api_json: The API documentation dictionary
        function_name: The name of the function to get documentation for
        tool_folder: The folder containing the API documentation
        code: Optional Python code string to extract docstring from
        
    Returns:
        tuple: (short_description, detailed_description)
               short_description: for GPT evaluator (from API JSON or first sentence of docstring)
               detailed_description: for code fixer (current implementation)
    """
    # Get the detailed description (current implementation)
    detailed_description = ""
    
    # First try to get the description from locator.json
    locator_path = os.path.join(tool_folder, "locator.json")
    
    if os.path.exists(locator_path):
        try:
            with open(locator_path, 'r', encoding='utf-8') as f:
                locator_data = json.load(f)
                if function_name in locator_data:
                    if isinstance(locator_data[function_name], dict):
                        # If it's a cached evaluation result, return the doc
                        detailed_description = locator_data[function_name]['doc']
                    else:
                        # If it's the old format, evaluate completeness
                        gpt, _ = initialize_gpt_evaluator()
                        is_complete, _ = evaluate_doc_completeness(gpt, locator_data[function_name], function_name, locator_path)
                        if is_complete:
                            detailed_description = locator_data[function_name]
        except Exception as e:
            print(f"Error reading locator.json: {str(e)}")
    
    # If locator.json doesn't exist or documentation is incomplete, try doc.md
    if not detailed_description:
        doc_path = os.path.join(tool_folder, "doc.md")
        if os.path.exists(doc_path):
            try:
                with open(doc_path, 'r', encoding='utf-8') as f:
                    doc_content = f.read()
                    detailed_description = doc_content
            except Exception as e:
                print(f"Error reading doc.md: {str(e)}")
    
    # If both locator.json and doc.md are not available or incomplete, use the current description from api_json
    if not detailed_description and api_json and "endpoints" in api_json:
        for endpoint in api_json["endpoints"]:
            api_name = endpoint["name"].lower()
            api_name = re.sub(r'\W', '_', api_name)
            if function_name == api_name:
                detailed_description = endpoint.get("description", "")
                break
    
    # If still no detailed description, use the entire api_json (if available)
    if not detailed_description:
        if api_json:
            detailed_description = api_json
        else:
            detailed_description = f"No API documentation available for {function_name}"
    
    # Get short description for GPT evaluator
    # First try to get from API JSON
    short_description = get_short_description_from_api_json(api_json, function_name)
    
    # If not found in API JSON and code is provided, try to get first sentence from docstring
    if not short_description and code:
        short_description = get_first_sentence_from_docstring(code)
    
    # If still no short description, use the detailed description
    if not short_description:
        short_description = detailed_description
    
    return short_description, detailed_description
=======
            return endpoint["description"]
    return api_json
>>>>>>> 963c487f600a8a356913b965684eb5a41275604c


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
    tool_request_error = 0
    tool_hard_error = 0
    
    need_refinement = []
    successful_tools = []
<<<<<<< HEAD
    request_error_tools = []
    
    # Use shared metadata file with refinement
    metadata_table = {'tools': [], 'validation_summary': {}, 'refinement_rounds': {}}
    metadata_file = 'tool_validation_refinement_metadata.json'
    
    if use_existing_metadata and os.path.exists(metadata_file):
        try:
            with open(metadata_file, 'r', encoding='utf-8') as f:
                metadata_table = json.load(f)
            logger.info(f"Loaded existing shared metadata with {len(metadata_table['tools'])} tools")
            print(f"Loaded existing shared metadata with {len(metadata_table['tools'])} tools")
            
            # Count existing stats from validation entries only
            for tool in metadata_table['tools']:
                if tool.get('phase') == 'validation':
                    if tool['status'] == 'information':
                        tool_success += 1
                        successful_tools.append(tool['path'])
                    elif tool['status'] == 'code_error':
                        tool_code_error += 1
                        need_refinement.append(tool['path'])
                    elif tool['status'] == 'server_error':
                        tool_server_error += 1
                    elif tool['status'] == 'request_error':
                        tool_request_error += 1
                        request_error_tools.append(tool['path'])
                        need_refinement.append(tool['path'])  # Add request errors to refinement list
                    elif tool['status'] == 'hard_error':
                        tool_hard_error += 1
                        need_refinement.append(tool['path'])
=======
    
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
>>>>>>> 963c487f600a8a356913b965684eb5a41275604c
        except Exception as e:
            logger.error(f"Error loading metadata: {str(e)}")
            print(f"Error loading metadata: {str(e)}")
    elif not use_existing_metadata:
        logger.info("Starting fresh validation - existing metadata will be overwritten")
        print("Starting fresh validation - existing metadata will be overwritten")
    
    SAVE_INTERVAL = 10
<<<<<<< HEAD
    validated_tools = {tool['path'] for tool in metadata_table['tools'] if tool.get('phase') == 'validation'} if use_existing_metadata else set()
=======
    validated_tools = {tool['path'] for tool in metadata_table['tools']} if use_existing_metadata else set()
>>>>>>> 963c487f600a8a356913b965684eb5a41275604c
    
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

<<<<<<< HEAD
            code = open(tool_path, "r", encoding='utf-8').read()
            function_name = extract_function_names(code)
            short_description, detailed_description = get_api_description(api_json, function_name, os.path.join(apidocs_dir, tool_folder), code)
            
            # logger.info(f"API description (detailed): {detailed_description}")
            # print(f"API description (detailed): {detailed_description}")
            # print(f"API description (short for GPT): {short_description}")
=======
            code = open(tool_path, "r").read()
            function_name = extract_function_names(code)
            api_description = get_api_description(api_json, function_name)
            
            logger.info(f"API description: {api_description}")
            print(f"API description: {api_description}")
>>>>>>> 963c487f600a8a356913b965684eb5a41275604c

            tool_metadata = {
                'path': tool_path,
                'function_name': function_name,
<<<<<<< HEAD
                'api_description': detailed_description,
                'phase': 'validation',
                'status': None,
                'error_type': None,
                'response': None,
                'exception': None,
                'gpt_evaluation': None,
                'timestamp': None
=======
                'api_description': api_description,
                'status': None,
                'error_type': None
>>>>>>> 963c487f600a8a356913b965684eb5a41275604c
            }

            try:
                result = subprocess.run(
                    ["python", tool_path], capture_output=True, text=True, check=True
                )
                output = result.stdout if result.stdout else ""
                tool_metadata['response'] = output
                tool_metadata['timestamp'] = json.dumps({"execution_time": "validation"}, default=str)
                
                if output:
                    gpt_answer = gpt_evaluate(
                        gpt,
                        gpt_prompt,
                        api_description=short_description,
                        api_response=output,
                        code=code,
                    )
                    tool_metadata['status'] = gpt_answer
<<<<<<< HEAD
                    tool_metadata['gpt_evaluation'] = gpt_answer
=======
>>>>>>> 963c487f600a8a356913b965684eb5a41275604c
                    
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
                    elif gpt_answer == "request_error":
                        tool_request_error += 1
                        request_error_tools.append(tool_path)
                        need_refinement.append(tool_path)  # Add request errors to refinement list
                        tool_metadata['error_type'] = 'request_error'
                        logger.error(f"Tool {tool_path} returned a request error.")
                        print(f"Tool {tool_path} returned a request error.")
                    elif gpt_answer == "information":
                        tool_success += 1
                        output_json = json.loads(output)
                        successful_tools.append(tool_path)
<<<<<<< HEAD
                        
                        # Extract JSON key hierarchy for documentation
                        try:
                            # Extract the actual data to analyze (json first, then text as fallback)
                            data_to_analyze = output_json.get("json")
                            if data_to_analyze is None:
                                # Try to parse the text field as JSON
                                text_content = output_json.get("text", "")
                                if text_content:
                                    try:
                                        data_to_analyze = json.loads(text_content)
                                    except:
                                        data_to_analyze = output_json  # Use the whole output as fallback
                                else:
                                    data_to_analyze = output_json
                            
                            key_hierarchy = extract_json_key_hierarchy(data_to_analyze)
                            
                            
                            # Get API description for context
                            api_description = get_api_description(api_json, function_name, os.path.join(apidocs_dir, tool_folder), code)
                            
                            # Call Claude 3.7 to explain the expected information
                            returns_description = call_claude_for_doc_explanation(
                                key_hierarchy, function_name, api_description, code
                            )
                            
                            # Update function documentation with Returns section
                            update_function_docstring_with_returns(tool_path, returns_description)
                            
                            print(f"Updated documentation for {function_name} with response explanation.")
                            logger.info(f"Updated documentation for {function_name} in {tool_path}")
                            
                        except Exception as e:
                            print(f"Error updating documentation for {tool_path}: {str(e)}")
                            logger.warning(f"Error updating documentation for {tool_path}: {str(e)}")
                        
                        # save in file with proper format for kb_builder
                        response_data = {
                            "status_code": 200,
                            "text": output,
                            "json": output_json,
                            "content": output
                        }
                        with open(tool_path[:-3] + '_response.json', "w", encoding='utf-8') as f:
                            json.dump(response_data, f)
=======
                        # save in file
                        with open(tool_path[:-3] + '_response.json', "w") as f:
                            json.dump(output_json, f)
>>>>>>> 963c487f600a8a356913b965684eb5a41275604c
                        logger.info(f"Tool {tool_path} executed successfully.")
                        print(f"Tool {tool_path} executed successfully.")
                    else:
                        logger.warning(f"Tool {tool_path} gpt answer: {gpt_answer}")
                        print(f"Tool {tool_path} gpt answer: {gpt_answer}")
            except subprocess.CalledProcessError as e:
                tool_hard_error += 1
                need_refinement.append(tool_path)
                tool_metadata['status'] = 'hard_error'
<<<<<<< HEAD
                tool_metadata['error_type'] = 'execution_error'
                tool_metadata['exception'] = str(e)
                tool_metadata['response'] = e.stderr if e.stderr else ""
                tool_metadata['timestamp'] = json.dumps({"execution_time": "validation"}, default=str)
=======
                tool_metadata['error_type'] = str(e)
>>>>>>> 963c487f600a8a356913b965684eb5a41275604c
                logger.error(f"Tool {tool_path} cannot be executed. Error: {str(e)}")
                print(f"Tool {tool_path} cannot be executed.")
            
            # Add tool metadata to table
            metadata_table['tools'].append(tool_metadata)
            
            # Save metadata table periodically
            if len(metadata_table['tools']) % SAVE_INTERVAL == 0:
<<<<<<< HEAD
                with open(metadata_file, 'w', encoding='utf-8') as f:
=======
                with open('tool_validation_metadata.json', 'w') as f:
>>>>>>> 963c487f600a8a356913b965684eb5a41275604c
                    json.dump(metadata_table, f, indent=2)
                logger.info(f"Saved metadata table with {len(metadata_table['tools'])} tools")
            
            logger.info("---------------------------")
            print("---------------------------\n")

<<<<<<< HEAD
    # Update validation summary in metadata
    metadata_table['validation_summary'] = {
        'tool_success': tool_success,
        'tool_code_error': tool_code_error,
        'tool_server_error': tool_server_error,
        'tool_request_error': tool_request_error,
        'tool_hard_error': tool_hard_error,
        'need_refinement': need_refinement,
        'successful_tools': successful_tools,
        'request_error_tools': request_error_tools
    }
=======
    # Save final metadata table
    with open('tool_validation_metadata.json', 'w') as f:
        json.dump(metadata_table, f, indent=2)
    
    summary = f"Tool success: {tool_success}, Tool code error: {tool_code_error}, Tool server error: {tool_server_error}, Tool hard error: {tool_hard_error}"
    logger.info(summary)
    print(summary)
>>>>>>> 963c487f600a8a356913b965684eb5a41275604c

    # Save final metadata table
    with open(metadata_file, 'w', encoding='utf-8') as f:
        json.dump(metadata_table, f, indent=2)
    
    summary = f"Tool success: {tool_success}, Tool code error: {tool_code_error}, Tool server error: {tool_server_error}, Tool request error: {tool_request_error}, Tool hard error: {tool_hard_error}"
    logger.info(summary)
    print(summary)

    with open("main/need_refinement.txt", "w", encoding='utf-8') as f:
        for tool in need_refinement:
            f.write(tool + "\n")
    
    return {
        'tool_success': tool_success,
        'tool_code_error': tool_code_error,
        'tool_server_error': tool_server_error,
<<<<<<< HEAD
        'tool_request_error': tool_request_error,
        'tool_hard_error': tool_hard_error,
        'need_refinement': need_refinement,
        'successful_tools': successful_tools,
        'request_error_tools': request_error_tools
    }


def refinement(apidocs_dir="extractor/apidocs/", need_refinement=None, use_existing_metadata=True, force_refine=False, round_num=1, use_response_only=False):
=======
        'tool_hard_error': tool_hard_error,
        'need_refinement': need_refinement,
        'successful_tools': successful_tools
    }


def refinement(apidocs_dir="extractor/apidocs/", need_refinement=None, use_existing_metadata=True):
>>>>>>> 963c487f600a8a356913b965684eb5a41275604c
    """Refine tools that need improvement
    
    Args:
        apidocs_dir (str): Path to the API docs directory
        need_refinement (list): List of tool paths that need refinement. If None, loads from file.
<<<<<<< HEAD
        use_existing_metadata (bool): If True, load and continue from existing metadata. Only applies to round 1.
                                    If False, start fresh and overwrite existing metadata.
        force_refine (bool): If True, refine all tools regardless of validation status. Only applies to round 1.
        round_num (int): The current round number of refinement.
        use_response_only (bool): If True, only use response_dict for parameter inference.
    """
    logger = setup_logging()
    
    print(f"Starting refinement round {round_num}")
    logger.info(f"Starting refinement round {round_num}")
    
    if use_response_only:
        print("Using response-only mode for parameter inference")
        logger.info("Using response-only mode for parameter inference")
    
=======
        use_existing_metadata (bool): If True, load and continue from existing metadata.
                                    If False, start fresh and overwrite existing metadata.
    """
    logger = setup_logging()
    
>>>>>>> 963c487f600a8a356913b965684eb5a41275604c
    # Initialize knowledge bases and models
    kb_data = initialize_knowledge_bases(apidocs_dir)
    gpt, gpt_prompt, claude = initialize_ai_models()
    
    # Build response dictionary for refinement
    print("Building response dictionary...")
    response_dict = build_response_dict(apidocs_dir)
    response_keys, response_keys_emb = encode_keys(kb_data['embedding_model'], response_dict)
    
<<<<<<< HEAD
    # Load need_refinement list if not provided (only for round 1)
    if need_refinement is None and not force_refine and round_num == 1:
        need_refinement = []
        if os.path.exists("main/need_refinement.txt"):
            with open("main/need_refinement.txt", "r", encoding='utf-8') as f:
                need_refinement = [line.strip() for line in f.readlines()]
    elif need_refinement is None:
        need_refinement = []
    
    refine_success = 0
    refine_fail = 0
    refine_request_error = 0
    successful_tools = []
    request_error_tools = []
    still_need_refinement = []
=======
    # Load need_refinement list if not provided
    if need_refinement is None:
        need_refinement = []
        if os.path.exists("main/need_refinement.txt"):
            with open("main/need_refinement.txt", "r") as f:
                need_refinement = [line.strip() for line in f.readlines()]
    
    refine_success = 0
    refine_fail = 0
    successful_tools = []
>>>>>>> 963c487f600a8a356913b965684eb5a41275604c
    
    print("Refining tools...")
    import time
    
<<<<<<< HEAD
    # Use shared metadata file with validation
    metadata_file = 'tool_validation_refinement_metadata.json'
    metadata_table = {'tools': [], 'validation_summary': {}, 'refinement_rounds': {}}
    
    # For round 1, respect use_existing_metadata parameter
    if round_num == 1:
        if use_existing_metadata and os.path.exists(metadata_file):
            try:
                with open(metadata_file, 'r', encoding='utf-8') as f:
                    metadata_table = json.load(f)
                logger.info(f"Loaded existing shared metadata with {len(metadata_table['tools'])} tools")
                print(f"Loaded existing shared metadata with {len(metadata_table['tools'])} tools")
                
                # Count existing refinement stats for this round
                for tool in metadata_table['tools']:
                    if tool.get('phase') == 'refinement' and tool.get('round') == round_num:
                        if tool['status'] == 'success':
                            refine_success += 1
                            successful_tools.append(tool['path'])
                        elif tool['status'] == 'request_error':
                            refine_request_error += 1
                            request_error_tools.append(tool['path'])
                        elif tool['status'] == 'fail':
                            refine_fail += 1
                            still_need_refinement.append(tool['path'])
            except Exception as e:
                logger.error(f"Error loading refinement metadata: {str(e)}")
                print(f"Error loading refinement metadata: {str(e)}")
        elif not use_existing_metadata:
            logger.info(f"Starting fresh refinement - existing metadata will be overwritten")
            print(f"Starting fresh refinement - existing metadata will be overwritten")
    else:
        # For round 2+, always load existing metadata
        if os.path.exists(metadata_file):
            try:
                with open(metadata_file, 'r', encoding='utf-8') as f:
                    metadata_table = json.load(f)
                logger.info(f"Loaded existing shared metadata for round {round_num} with {len(metadata_table['tools'])} tools")
                print(f"Loaded existing shared metadata for round {round_num} with {len(metadata_table['tools'])} tools")
            except Exception as e:
                logger.error(f"Error loading refinement metadata: {str(e)}")
                print(f"Error loading refinement metadata: {str(e)}")
    
    # Note: Request error tools are no longer skipped in subsequent rounds
    
    # Initialize round metadata if not exists
    if 'refinement_rounds' not in metadata_table:
        metadata_table['refinement_rounds'] = {}
    if str(round_num) not in metadata_table['refinement_rounds']:
        metadata_table['refinement_rounds'][str(round_num)] = {
            'tools_processed': 0,
            'success': 0,
            'request_error': 0,
            'fail': 0
        }
    
    SAVE_INTERVAL = 10
    
    # For round 1, check which tools have been refined; for round 2+, process all tools in need_refinement
    if round_num == 1 and use_existing_metadata:
        refined_tools = {tool['path'] for tool in metadata_table['tools'] if tool.get('phase') == 'refinement' and tool.get('round') == round_num}
    else:
        refined_tools = set()

    for tool_folder in os.listdir(apidocs_dir):
        tools, api_json = load_api_data(apidocs_dir, tool_folder)
        
        # Load config for this tool folder
        tool_folder_path = os.path.join(apidocs_dir, tool_folder)
        config = load_api_config(tool_folder_path)
=======
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
>>>>>>> 963c487f600a8a356913b965684eb5a41275604c
        
        for tool in tools:
            tool_path = os.path.join(apidocs_dir, tool_folder, tool)
            if not force_refine and tool_path not in need_refinement:
                continue
<<<<<<< HEAD
=======
                
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
>>>>>>> 963c487f600a8a356913b965684eb5a41275604c
                
            
            # Get the latest error response and code from metadata instead of running the tool
            latest_tool_data = None
            error_message = None
            code = None
            
            # Find the most recent entry for this tool
            for tool_data in reversed(metadata_table['tools']):
                if tool_data['path'] == tool_path:
                    latest_tool_data = tool_data
                    break
            
            if latest_tool_data:
                # Use cached error response and code
                if latest_tool_data.get('response'):
                    error_message = latest_tool_data['response']
                elif latest_tool_data.get('exception'):
                    error_message = latest_tool_data['exception']
                
                if latest_tool_data.get('updated_code'):
                    code = latest_tool_data['updated_code']
                    print(f"Using updated code from round {latest_tool_data.get('round', 'unknown')} for {tool}")
                else:
                    code = open(tool_path, "r", encoding='utf-8').read()
                    print(f"Using original code from file for {tool}")
                
                print(f"Using cached error message: {error_message[:200]}..." if len(error_message) > 200 else f"Using cached error message: {error_message}")
            else:
                # No previous data, read from file
                code = open(tool_path, "r", encoding='utf-8').read()
                error_message = "No previous error message found"
                print(f"No previous data found for {tool}, using original code")
                
            function_name = extract_function_names(code)
            short_description, detailed_description = get_api_description(api_json, function_name, os.path.join(apidocs_dir, tool_folder), code)
            # print(f"API description (detailed): {detailed_description}")
            # print(f"API description (short for GPT): {short_description}")
            # if config:
                # print(f"Using config: {config}")
    
            tool_refinement_metadata = {
                'path': tool_path,
                'function_name': function_name,
                'api_description': detailed_description,
                'phase': 'refinement',
                'round': round_num,
                'status': None,
                'error_type': None,
                'response': None,
                'exception': None,
                'gpt_evaluation': None,
                'updated_code': None,
                'timestamp': None
            }
    
            # Get the required parameters from the code
            try:
                params = get_required_param_name(tool_path)
                print(f"Query parameters: {params}")
            except:
                print("Could not extract parameters, skipping tool")
                continue
                
            param_examples = {}
            for param in params:
                examples_list = search_kb(param, kb_data['param_keys'], kb_data['param_keys_emb'], 
                                        kb_data['parameter_dict'], response_keys, response_keys_emb, 
                                        response_dict, kb_data['description_keys'], 
                                        kb_data['description_to_param_dict'], kb_data['description_keys_emb'], 
                                        kb_data['embedding_model'], use_response_only=use_response_only)
                # Store the list of candidates (up to 3)
                param_name = param.split("][")[-1][:-1]
                param_examples[param_name] = examples_list
            
            print(param_examples)

<<<<<<< HEAD
            # Fix the code using Claude with cached error message
            new_code = None
            for attempt in range(3):
=======
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
>>>>>>> 963c487f600a8a356913b965684eb5a41275604c
                try:
                    new_code = fix_code(claude, code, error_message, detailed_description, param_examples, config)
                    break
                except Exception as e:
                    print(f"Claude fix attempt {attempt + 1} failed: {e}")
                    time.sleep(60)  # prevent overflow
                    
            if not new_code:
                print(f"Failed to fix code for {tool} after 3 attempts, skipping")
                continue
            
            # Save the updated code to metadata and file
            tool_refinement_metadata['updated_code'] = new_code
            tool_refinement_metadata['timestamp'] = json.dumps({"execution_time": f"refinement_round_{round_num}"}, default=str)
            
            with open(tool_path, "w", encoding='utf-8') as f:
                f.write(new_code)
            print(f"Refined: {tool}")
            
            # Test the refined tool and save response
            try:
                # Set environment variable for Python to use UTF-8
                env = os.environ.copy()
                env["PYTHONIOENCODING"] = "utf-8"
                
                result = subprocess.run(
                    ["python", tool_path], 
                    capture_output=True, 
                    text=True, 
                    check=True,
                    encoding='utf-8',
                    env=env
                )
                output = result.stdout if result.stdout else ""
                tool_refinement_metadata['response'] = output
                
                if output:
                    gpt_answer = gpt_evaluate(
                        gpt,
                        gpt_prompt,
                        api_description=short_description,
                        api_response=output,
                        code=new_code,
                    )
<<<<<<< HEAD
                    tool_refinement_metadata['gpt_evaluation'] = gpt_answer
                    tool_refinement_metadata['status'] = gpt_answer
                    
                    if gpt_answer == "information":
                        refine_success += 1
                        successful_tools.append(tool_path)
                        
                        # Extract JSON key hierarchy for documentation
                        try:
                            output_json = json.loads(output)
                            
                            # Extract the actual data to analyze (json first, then text as fallback)
                            data_to_analyze = output_json.get("json")
                            if data_to_analyze is None:
                                # Try to parse the text field as JSON
                                text_content = output_json.get("text", "")
                                if text_content:
                                    try:
                                        data_to_analyze = json.loads(text_content)
                                    except:
                                        data_to_analyze = output_json  # Use the whole output as fallback
                                else:
                                    data_to_analyze = output_json
                            
                            key_hierarchy = extract_json_key_hierarchy(data_to_analyze)
                            
                            # Get function name from the tool path
                            function_name = extract_function_names(new_code)
                            
                            # Get API description for context  
                            api_description = get_api_description(api_json, function_name, os.path.join(apidocs_dir, tool_folder), new_code)
                            
                            # Call Claude 3.7 to explain the expected information
                            returns_description = call_claude_for_doc_explanation(
                                key_hierarchy, function_name, api_description, new_code
                            )
                            
                            # Update function documentation with Returns section
                            update_function_docstring_with_returns(tool_path, returns_description)
                            
                            print(f"Updated documentation for {function_name} with response explanation.")
                            logger.info(f"Updated documentation for {function_name} in {tool_path}")
                            
                            # save refined response in file with proper format for kb_builder
                            response_data = {
                                "status_code": 200,
                                "text": output,
                                "json": output_json,
                                "content": output
                            }
                            with open(tool_path[:-3] + '_response.json', "w", encoding='utf-8') as f:
                                json.dump(response_data, f)
                            
                        except Exception as e:
                            print(f"Error updating documentation for {tool_path}: {str(e)}")
                            logger.warning(f"Error updating documentation for {tool_path}: {str(e)}")
                        
=======
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
>>>>>>> 963c487f600a8a356913b965684eb5a41275604c
                        print(f"Refined tool {tool_path} executed successfully.")
                    elif gpt_answer == "request_error":
                        refine_request_error += 1
                        tool_refinement_metadata['error_type'] = 'request_error'
                        request_error_tools.append(tool_path)
                        print(f"Refined tool {tool_path} returned a request error.")
                    elif gpt_answer == "code_error":
                        refine_fail += 1
<<<<<<< HEAD
                        still_need_refinement.append(tool_path)
                        tool_refinement_metadata['status'] = 'fail'
                        tool_refinement_metadata['error_type'] = 'code_error'
                        print(f"Refined tool {tool_path} returned a code error.")
                    else:
                        # Handle other GPT responses
                        refine_fail += 1
                        still_need_refinement.append(tool_path)
                        tool_refinement_metadata['status'] = 'fail'
                        tool_refinement_metadata['error_type'] = 'other_error'
                        print(f"Refined tool {tool_path} returned: {gpt_answer}")
                        
            except subprocess.CalledProcessError as e:
                refine_fail += 1
                still_need_refinement.append(tool_path)
                tool_refinement_metadata['status'] = 'fail'
                tool_refinement_metadata['error_type'] = 'execution_error'
                tool_refinement_metadata['exception'] = str(e)
                tool_refinement_metadata['response'] = e.stderr if e.stderr else ""
                print(f"Refined tool {tool_path} cannot be executed.")
            
            # Update round statistics
            metadata_table['refinement_rounds'][str(round_num)]['tools_processed'] += 1
            if tool_refinement_metadata['status'] == 'success' or tool_refinement_metadata['status'] == 'information':
                metadata_table['refinement_rounds'][str(round_num)]['success'] += 1
            elif tool_refinement_metadata['status'] == 'request_error':
                metadata_table['refinement_rounds'][str(round_num)]['request_error'] += 1
            elif tool_refinement_metadata['status'] == 'fail':
                metadata_table['refinement_rounds'][str(round_num)]['fail'] += 1
            
            # Add tool refinement metadata to table
            metadata_table['tools'].append(tool_refinement_metadata)
            
            # Save refinement metadata periodically
            if len(metadata_table['tools']) % SAVE_INTERVAL == 0:
                with open(metadata_file, 'w', encoding='utf-8') as f:
                    json.dump(metadata_table, f, indent=2)
                logger.info(f"Saved metadata table with {len(metadata_table['tools'])} tools")
            
            print("---------------------------\n")

    # Save final refinement metadata table
    with open(metadata_file, 'w', encoding='utf-8') as f:
        json.dump(metadata_table, f, indent=2)

    print(f"Round {round_num} - Refine success: {refine_success}, Refine request error: {refine_request_error}, Refine fail: {refine_fail}, NumToolsNeedRefinement: {len(need_refinement)}")
    
    return {
        'refine_success': refine_success,
        'refine_request_error': refine_request_error,
        'refine_fail': refine_fail,
        'successful_tools': successful_tools,
        'request_error_tools': request_error_tools,
        'still_need_refinement': still_need_refinement
    }


def save_response_dict(apidocs_dir, output_file="response_dict.json"):
    """Save the response dictionary as a JSON file for downstream tasks
    
    Args:
        apidocs_dir: Directory containing API docs
        output_file: Name of the output JSON file
    """
    print("Building and saving response dictionary...")
    response_dict = build_response_dict(apidocs_dir)
    
    # Convert defaultdict to regular dict and handle sets for JSON serialization
    response_dict_serializable = {}
    for key, value_set in response_dict.items():
        # Convert set to list for JSON serialization
        response_dict_serializable[key] = list(value_set)
    
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(response_dict_serializable, f, indent=2, ensure_ascii=False)
        print(f"Response dictionary saved to {output_file} with {len(response_dict_serializable)} response paths")
    except Exception as e:
        print(f"Error saving response dictionary: {e}")


def infer_parameter_from_response_only(query, apidocs_dir="extractor/apidocs/", max_candidates=3):
    """Standalone function to infer parameter values using only the response_dict
    
    Args:
        query: Parameter name or description to search for
        apidocs_dir: Directory containing API docs
        max_candidates: Maximum number of candidate results to return
        
    Returns:
        List of inferred parameter values (up to max_candidates) or None if not found
    """
    print(f"Inferring parameter values for '{query}' using response data only...")
    
    # Build response dictionary
    response_dict = build_response_dict(apidocs_dir)
    
    # Initialize embedding model and encode response keys
    embedding_model = initialize_model()
    response_keys, response_keys_emb = encode_keys(embedding_model, response_dict)
    
    # Perform search using response_only mode
    results = search_kb(
        query, 
        [], [], {},  # Empty parameter data
        response_keys, response_keys_emb, response_dict,
        [], {}, [],  # Empty description data
        embedding_model,
        use_response_only=True,
        max_candidates=max_candidates
    )
    
    if results:
        print(f"Found {len(results)} parameter inference candidates: {results}")
    else:
        print(f"No parameter inference results found for '{query}'")
    
    return results


def copy_successful_tools(validation_results, refinement_results, output_dir="webarena_tools_toRyan", tool_types=None, apidocs_dir="extractor/apidocs"):
    """Copy tools of specified types to output directory
    
    Args:
        validation_results: Results from validation function
        refinement_results: Results from refinement function
        output_dir: Directory to copy tools to
        tool_types: List of tool types to copy (e.g., ['success', 'request_error']). 
                   If None, defaults to ['success']
        apidocs_dir: Path to the API docs directory to find existing tools
    """
    if tool_types is None:
        tool_types = ['success']
    
    os.makedirs(output_dir, exist_ok=True)
    
    # First, get a list of all existing tools in the apidocs directory
    existing_tools = set()
    if os.path.exists(apidocs_dir):
        for tool_folder in os.listdir(apidocs_dir):
            tool_folder_path = os.path.join(apidocs_dir, tool_folder)
            if os.path.isdir(tool_folder_path):
                files = os.listdir(tool_folder_path)
                tools = [x for x in files if x.endswith(".py")]
                for tool in tools:
                    tool_path = os.path.join(apidocs_dir, tool_folder, tool)
                    existing_tools.add(tool_path)
    
    print(f"Found {len(existing_tools)} existing tools in {apidocs_dir}")
    
    all_tools = []
    
    # Collect tools based on specified types
    if 'success' in tool_types:
        all_tools.extend(validation_results.get('successful_tools', []))
        all_tools.extend(refinement_results.get('successful_tools', []))
    
    if 'request_error' in tool_types:
        all_tools.extend(validation_results.get('request_error_tools', []))
        all_tools.extend(refinement_results.get('request_error_tools', []))
    
    # Remove duplicates while preserving order
    unique_tools = []
    seen = set()
    for tool in all_tools:
        if tool not in seen:
            unique_tools.append(tool)
            seen.add(tool)
    
    # Filter to only include tools that actually exist
    existing_unique_tools = []
    missing_tools = []
    for tool in unique_tools:
        if tool in existing_tools:
            existing_unique_tools.append(tool)
        else:
            missing_tools.append(tool)
    
    if missing_tools:
        print(f"Warning: {len(missing_tools)} tools from metadata no longer exist:")
        for missing_tool in missing_tools[:5]:  # Show first 5 missing tools
            print(f"  - {missing_tool}")
        if len(missing_tools) > 5:
            print(f"  ... and {len(missing_tools) - 5} more")
    
    print(f"Copying {len(existing_unique_tools)} tools of types {tool_types} to {output_dir}")
    
    copied_count = 0
    for tool in existing_unique_tools:
        try:
            tool_name = os.path.basename(tool)
            new_tool_path = os.path.join(output_dir, tool_name)
            with open(new_tool_path, "w", encoding='utf-8') as f:
                with open(tool, "r", encoding='utf-8') as source_f:
                    f.write(source_f.read())
            copied_count += 1
        except Exception as e:
            print(f"Error copying {tool}: {e}")
    
    print(f"Successfully copied {copied_count} tools to {output_dir}")


def main(use_existing_metadata=True, force_refine=True, tool_types=['success'], max_refinement_rounds=1, use_response_only=True, build_response_dict_through_metadata=True):
    """Main function to run validation and refinement pipeline
    
    Args:
        use_existing_metadata (bool): If True, load and continue from existing metadata. Only applies to round 1.
                                    If False, start fresh and overwrite existing metadata.
        force_refine (bool): If True, refine all tools regardless of validation status. Only applies to round 1.
        tool_types (list): List of tool types to copy to output directory. 
                          Options: ['success', 'request_error']. Defaults to ['success'].
        max_refinement_rounds (int): Maximum number of refinement rounds to perform. Defaults to 1.
        use_response_only (bool): If True, only use response_dict for parameter inference during refinement.
        build_response_dict_through_metadata (bool): If True, build the response_dict through the metadata.
=======
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
>>>>>>> 963c487f600a8a356913b965684eb5a41275604c
    """
    from dotenv import load_dotenv
    load_dotenv()
    
    # Define the path to the API docs
    apidocs_dir = os.path.join("extractor", "apidocs")
<<<<<<< HEAD

=======
>>>>>>> 963c487f600a8a356913b965684eb5a41275604c
    
    # Run validation
    validation_results = validation(apidocs_dir, use_existing_metadata=use_existing_metadata)
    
<<<<<<< HEAD
    # Collect all refinement results across rounds
    all_refinement_results = {
        'successful_tools': [],
        'request_error_tools': [],
        'still_need_refinement': [],
        'rounds': {}
    }
    
    # Determine initial tools that need refinement
    if force_refine:
        # Get all tools if force_refine is True
        need_refinement = []
        for tool_folder in os.listdir(apidocs_dir):
            tools, _ = load_api_data(apidocs_dir, tool_folder)
            for tool in tools:
                tool_path = os.path.join(apidocs_dir, tool_folder, tool)
                need_refinement.append(tool_path)
    else:
        need_refinement = validation_results['need_refinement']
    
    print(f"\nStarting refinement process with maximum {max_refinement_rounds} rounds")
    print(f"Initial tools needing refinement: {len(need_refinement)}")
    
    # Run multiple rounds of refinement
    for round_num in range(1, max_refinement_rounds + 1):
        if not need_refinement:
            print(f"No more tools need refinement. Stopping after {round_num - 1} rounds.")
            break
            
        print(f"\n{'='*50}")
        print(f"REFINEMENT ROUND {round_num}")
        print(f"{'='*50}")
        print(f"Tools to refine in this round: {len(need_refinement)}")
        
        # For round 1, use the original parameters; for round 2+, always continue from existing metadata
        round_use_existing_metadata = use_existing_metadata if round_num == 1 else True
        round_force_refine = force_refine if round_num == 1 else False
        
        # Run refinement for this round
        refinement_results = refinement(
            apidocs_dir, 
            need_refinement, 
            use_existing_metadata=round_use_existing_metadata,
            force_refine=round_force_refine,
            round_num=round_num,
            use_response_only=use_response_only
        )
        
        # Store round results
        all_refinement_results['rounds'][round_num] = {
            'refine_success': refinement_results['refine_success'],
            'refine_request_error': refinement_results['refine_request_error'],
            'refine_fail': refinement_results['refine_fail'],
            'successful_tools': refinement_results['successful_tools'],
            'request_error_tools': refinement_results['request_error_tools'],
            'still_need_refinement': refinement_results['still_need_refinement']
        }
        
        # Accumulate successful and request error tools across all rounds
        all_refinement_results['successful_tools'].extend(refinement_results['successful_tools'])
        all_refinement_results['request_error_tools'].extend(refinement_results['request_error_tools'])
        
        # Update need_refinement for next round (only tools that still failed)
        need_refinement = refinement_results['still_need_refinement']
        all_refinement_results['still_need_refinement'] = need_refinement
        
        print(f"\nRound {round_num} Summary:")
        print(f"  Success: {refinement_results['refine_success']}")
        print(f"  Request Error: {refinement_results['refine_request_error']}")
        print(f"  Still Need Refinement: {len(refinement_results['still_need_refinement'])}")
        
        # If no tools need further refinement, stop early
        if not need_refinement:
            print(f"All tools resolved! Completed in {round_num} rounds.")
            break
    
    # Remove duplicates from accumulated results
    all_refinement_results['successful_tools'] = list(set(all_refinement_results['successful_tools']))
    all_refinement_results['request_error_tools'] = list(set(all_refinement_results['request_error_tools']))
    
    print(f"\n{'='*50}")
    print("FINAL SUMMARY")
    print(f"{'='*50}")
    print(f"Validation - Success: {validation_results['tool_success']}, "
          f"Code Error: {validation_results['tool_code_error']}, "
          f"Server Error: {validation_results['tool_server_error']}, "
          f"Request Error: {validation_results['tool_request_error']}, "
          f"Hard Error: {validation_results['tool_hard_error']}")
    
    print(f"Refinement - Total Rounds: {len(all_refinement_results['rounds'])}")
    print(f"  Total Successful: {len(all_refinement_results['successful_tools'])}")
    print(f"  Total Request Errors: {len(all_refinement_results['request_error_tools'])}")
    print(f"  Still Need Refinement: {len(all_refinement_results['still_need_refinement'])}")
    
    # Copy tools of specified types to output directory
    copy_successful_tools(validation_results, all_refinement_results, 
                         output_dir="webarena_tools_toRyan", tool_types=tool_types, 
                         apidocs_dir=apidocs_dir)
    
    # Save response dictionary as JSON file if requested
    if build_response_dict_through_metadata:
        save_response_dict(apidocs_dir, "response_dict.json")
=======
    # Run refinement
    refinement_results = refinement(apidocs_dir, validation_results['need_refinement'], use_existing_metadata=use_existing_metadata)
    
    # Copy all successful tools to output directory
    all_successful_tools = list(set(validation_results['successful_tools'] + refinement_results['successful_tools']))
    copy_successful_tools(all_successful_tools)
>>>>>>> 963c487f600a8a356913b965684eb5a41275604c


def get_required_param_name(path: str | Path):
    source = Path(path).read_text(encoding="utf-8")
    try:
        tree = ast.parse(source, filename=str(path))
    except Exception as e:
        return []

    # Extract function name from the code
    function_name = extract_function_names(source)
    if not function_name:
        function_name = "unknown"

    params = []
<<<<<<< HEAD
    
    # Find the main function definition and extract its parameters
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == function_name:
            # Extract parameters from function signature
            for arg in node.args.args:
                # Skip 'self' parameter if present
                if arg.arg != 'self':
                    # Format as [functionname][parametername]
                    formatted_param = f"[{function_name}][{arg.arg}]"
                    params.append(formatted_param)
            break
    
    # If no parameters found from function signature, try to find assert statements as fallback
    if not params:
        src_lines = source.splitlines()
        for node in ast.walk(tree):
            if isinstance(node, ast.Assert):
                line_text = src_lines[node.lineno - 1]
                # Extract parameter name from assert statement
                try:
                    param = line_text.strip().split(" ")[1].strip()
                    formatted_param = f"[{function_name}][{param}]"
                    params.append(formatted_param)
                except:
                    pass
=======
    for _, text in out:
        param = text.strip().split(" ")[1].strip()
        params.append(param)
>>>>>>> 963c487f600a8a356913b965684eb5a41275604c
    
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
<<<<<<< HEAD
    # print("extracted function names: ", function_names)
    return function_names[-1]

def find_api_in_md(md, api_endpoint):
    chunk = md.split(api_endpoint)
    if len(chunk) < 2:
        return md

def extract_json_key_hierarchy(json_obj, max_depth=3, keep_array_items=1):
    """
    Extract key hierarchy from JSON object, keeping only keys and limiting array items.
    
    Args:
        json_obj: JSON object to extract hierarchy from
        max_depth: Maximum depth to traverse
        keep_array_items: Number of array items to keep (default: 1)
    
    Returns:
        dict: Simplified JSON structure with key hierarchy
    """
    def _extract_recursive(obj, current_depth=0):
        if current_depth >= max_depth:
            return "..."
        
        if isinstance(obj, dict):
            result = {}
            for key, value in obj.items():
                result[key] = _extract_recursive(value, current_depth + 1)
            return result
        elif isinstance(obj, list):
            if len(obj) == 0:
                return []
            # Keep only the first item(s) from arrays
            items_to_keep = min(keep_array_items, len(obj))
            result = []
            for i in range(items_to_keep):
                result.append(_extract_recursive(obj[i], current_depth + 1))
            if len(obj) > keep_array_items:
                result.append("...")
            return result
        else:
            # For primitive types, just indicate the type
            return f"<{type(obj).__name__}>"
    
    return _extract_recursive(json_obj)


def call_claude_for_doc_explanation(key_hierarchy, function_name, api_description, code):
    """
    Call Claude 3.7 to explain the expected information in the response JSON.
    
    Args:
        key_hierarchy: Simplified JSON key hierarchy
        function_name: Name of the function
        api_description: API description for context
        code: Full Python code of the tool
    
    Returns:
        str: Claude's explanation of the expected information
    """
    try:
        client = anthropic.Anthropic()
        
        # Handle case where api_description might be a tuple (short, detailed)
        if isinstance(api_description, tuple):
            short_desc, detailed_desc = api_description
            tool_description = detailed_desc if detailed_desc else short_desc
        else:
            tool_description = api_description
        
        # Truncate very long descriptions to avoid token limits
        if len(str(tool_description)) > 1000:
            tool_description = str(tool_description)[:1000] + "..."
        
        # Truncate code if too long to avoid token limits  
        if len(code) > 2000:
            code_to_show = code[:2000] + "\n# ... (code truncated for brevity) ..."
        else:
            code_to_show = code
        
        prompt = f"""You are writing documentation for an API function. Based on the complete tool code and response structure below, write a brief 1-sentence description of what information this function returns.

Function: {function_name}

Tool Description:
{tool_description}

Complete Tool Code:
```python
{code_to_show}
```

Response structure:
{json.dumps(key_hierarchy, indent=2)}

Analyze the complete tool code to understand exactly what this function does, what API endpoints it calls, and what data it processes. Then focus on WHAT specific information/data is returned to the user. Don't mention the structure of the response. Be concise and specific about the content that users will get.

Example good responses:
- "Returns a list of products with their details, pricing, and availability status."
- "Returns customer order history with item details and shipping information."
- "Returns search results containing matching products and pagination metadata."

Write only the description, no additional text."""
        print(prompt)
        response = client.messages.create(
            model="claude-3-7-sonnet-20250219",
            max_tokens=150,
            temperature=0.1,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        
        return response.content[0].text.strip()
    
    except Exception as e:
        print(f"Error calling Claude for documentation: {str(e)}")
        return "Returns API response data as JSON object."


def update_function_docstring_with_returns(tool_path, returns_description):
    """
    Update the function docstring to include the Returns section.
    Updates the LAST function in the file (which should be the main tool function).
    
    Args:
        tool_path: Path to the tool file
        returns_description: Description of what the function returns
    """
    try:
        with open(tool_path, 'r', encoding='utf-8') as f:
            code = f.read()
        
        # Parse the AST to find ALL functions
        tree = ast.parse(code)
        functions = []
        
        for node in tree.body:
            if isinstance(node, ast.FunctionDef):
                functions.append(node)
        
        if not functions:
            print(f"No functions found in {tool_path}")
            return False
        
        # Use the LAST function (should be the main tool function)
        target_function = functions[-1]
        print(f"Updating documentation for function: {target_function.name} (last function in file)")
        
        # Check if it has a docstring
        if (target_function.body and 
            isinstance(target_function.body[0], ast.Expr) and 
            isinstance(target_function.body[0].value, ast.Constant) and
            isinstance(target_function.body[0].value.value, str)):
            
            # Get the docstring
            docstring = target_function.body[0].value.value
            
            # Handle docstring update (add or replace Returns section)
            lines = code.split('\n')
            start_line = target_function.body[0].lineno - 1
            end_line = target_function.body[0].end_lineno - 1
            
            # Get the original docstring content
            original_docstring_lines = lines[start_line:end_line + 1]
            original_content = '\n'.join(original_docstring_lines)
            
            # Check if it already has a Returns section
            has_returns = "Returns:" in docstring or "returns:" in docstring.lower()
            
            if has_returns:
                # Replace existing Returns section
                docstring_lines = docstring.split('\n')
                new_docstring_lines = []
                skip_returns_section = False
                
                for line in docstring_lines:
                    if "Returns:" in line or "returns:" in line.lower():
                        # Start of Returns section - replace it
                        new_docstring_lines.append("    Returns:")
                        new_docstring_lines.append(f"        {returns_description}")
                        skip_returns_section = True
                        continue
                    elif skip_returns_section:
                        # Skip lines that are part of the old Returns section
                        if line.strip() == "" or line.startswith("        "):
                            continue
                        else:
                            # End of Returns section, continue with rest of docstring
                            skip_returns_section = False
                            new_docstring_lines.append(line)
                    else:
                        new_docstring_lines.append(line)
                
                # Reconstruct the docstring
                new_docstring = '\n'.join(new_docstring_lines)
                
                # Determine quote style and replace
                if '"""' in original_content:
                    if original_content.strip().endswith('"""'):
                        new_content = original_content.replace(docstring, new_docstring)
                    else:
                        new_content = original_content.replace(docstring, new_docstring)
                elif "'''" in original_content:
                    new_content = original_content.replace(docstring, new_docstring)
                else:
                    new_content = original_content.replace(docstring, new_docstring)
                
                print(f"Replaced existing Returns section for {target_function.name}")
            else:
                # Add new Returns section
                # Determine the quote style and indentation
                if '"""' in original_content:
                    quote_style = '"""'
                    # Find the closing quotes and add Returns section before them
                    if original_content.strip().endswith('"""'):
                        # Multi-line docstring
                        new_content = original_content.rstrip('"""').rstrip() + f"\n    \n    Returns:\n        {returns_description}\n    \"\"\""
                    else:
                        # Single line with triple quotes
                        new_content = original_content.replace('"""', f'"""\n    \n    Returns:\n        {returns_description}\n    """')
                elif "'''" in original_content:
                    quote_style = "'''"
                    if original_content.strip().endswith("'''"):
                        new_content = original_content.rstrip("'''").rstrip() + f"\n    \n    Returns:\n        {returns_description}\n    '''"
                    else:
                        new_content = original_content.replace("'''", f"'''\n    \n    Returns:\n        {returns_description}\n    '''")
                else:
                    # Single or double quotes
                    new_content = original_content.rstrip() + f"\n    \n    Returns:\n        {returns_description}"
                
                print(f"Added new Returns section for {target_function.name}")
            
            # Replace the docstring lines
            lines[start_line:end_line + 1] = [new_content]
            
            # Write back to file
            updated_code = '\n'.join(lines)
            with open(tool_path, 'w', encoding='utf-8') as f:
                f.write(updated_code)
            
            print(f"Updated function documentation for {target_function.name} in {tool_path}")
            return True
        
        # If we found a function but no docstring, add one
        elif target_function.body:
            # Insert a new docstring as the first statement
            lines = code.split('\n')
            func_start_line = target_function.lineno - 1
            
            # Find the line after the function definition (after the colon)
            insert_line = func_start_line + 1
            while insert_line < len(lines) and lines[insert_line].strip() == '':
                insert_line += 1
            
            # Create new docstring
            new_docstring = f'    """\n    {target_function.name} function.\n    \n    Returns:\n        {returns_description}\n    """'
            
            # Insert the docstring
            lines.insert(insert_line, new_docstring)
            
            updated_code = '\n'.join(lines)
            with open(tool_path, 'w', encoding='utf-8') as f:
                f.write(updated_code)
            
            print(f"Added function documentation for {target_function.name} in {tool_path}")
            return True
        
        return False
    
    except Exception as e:
        print(f"Error updating function documentation for {tool_path}: {str(e)}")
        return False

=======
    return function_names[0]
>>>>>>> 963c487f600a8a356913b965684eb5a41275604c

def find_api_in_md(md, api_endpoint):
    chunk = md.split(api_endpoint)
    if len(chunk) < 2:
        return md

if __name__ == "__main__":
    # Example usage with new parameters:
    # main(use_response_only=True, save_response_dict_file=True)  # Use response-only mode and save response dict
    # main(use_response_only=False, save_response_dict_file=True)  # Use all knowledge bases and save response dict
    main()
