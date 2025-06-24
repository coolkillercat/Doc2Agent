"""
Knowledge base builder for API tools.
Functions to build parameter and response dictionaries from API documentation.
"""

import os
import json
from collections import defaultdict

def add_to_dict(d: defaultdict, prev_path: str, object, api_doc: str):
    """
    Encode a json tree into a dictionary with root to leaf path. Sets have max length of 10.
    
    Args:
        d: defaultdict to add data to
        prev_path: Current path in the JSON tree
        object: Current object being processed
        api_doc: Name of the API doc
    """
    if isinstance(object, dict):
        for key, value in object.items():
            add_to_dict(d, prev_path + "[" + key + "]", value, api_doc)
    elif isinstance(object, list):
        for item in object:
            add_to_dict(d, prev_path, item, api_doc)
    else:
        if object:
            if len(d[prev_path]) < 10:
                d[prev_path].add((prev_path, object))


def build_dict(d, object, api_doc):
    """
    Build a dictionary from an object.
    
    Args:
        d: Dictionary to build
        object: Object to process
        api_doc: Name of the API doc
    """
    add_to_dict(d, '', object, api_doc)


def build_parameter_dict(apidocs_dir):
    """
    Build a dictionary of parameters from API docs.
    
    Args:
        apidocs_dir: Directory containing API docs
        
    Returns:
        parameter_dict: Dictionary mapping parameter paths to sets of examples
    """
    folders = os.listdir(apidocs_dir)
    parameter_dict = defaultdict(set)
    
    for folder in folders:
        path = os.path.join(apidocs_dir, folder, folder + ".txt")
        try:
            json_file = json.load(open(path))
        except:
            continue
            
        for endpoint in json_file['endpoints']:
            for param in endpoint['required_parameters']:
                name = param['name']
                example = None if not param['example'] else param['example']
                add_to_dict(parameter_dict, "["+name+"]", example, folder)
                
            if endpoint['optional_parameters']:
                for param in endpoint['optional_parameters']:
                    name = param['name']
                    example = None if not param['example'] else param['example']
                    add_to_dict(parameter_dict, "["+name+"]", example, folder)
                    
    return parameter_dict


def build_description_dicts(apidocs_dir):
    """
    Build dictionaries mapping between parameter descriptions and names.
    
    Args:
        apidocs_dir: Directory containing API docs
        
    Returns:
        description_to_param_dict: Dictionary mapping descriptions to parameter names
        param_to_description_dict: Dictionary mapping parameter names to descriptions
    """
    folders = os.listdir(apidocs_dir)
    description_to_param_dict = {}  # map description to parameter
    param_to_description_dict = {}  # map parameter to description
    
    for folder in folders:
        path = os.path.join(apidocs_dir, folder, folder + ".txt")
        try:
            json_file = json.load(open(path))
        except:
            continue
            
        for endpoint in json_file['endpoints']:
            for param in endpoint['required_parameters']:
                name = param['name']
                description = param['description']
                description_to_param_dict[description] = name
                param_to_description_dict[name] = description
                
            if endpoint['optional_parameters']:
                for param in endpoint['optional_parameters']:
                    name = param['name']
                    description = param['description']
                    description_to_param_dict[description] = name
                    param_to_description_dict[name] = description
                    
    return description_to_param_dict, param_to_description_dict


def build_response_dict(apidocs_dir):
    """
    Build a dictionary of API responses from shared metadata file.
    
    Args:
        apidocs_dir: Directory containing API docs
        
    Returns:
        response_dict: Dictionary mapping response paths to sets of examples
    """
    response_dict = defaultdict(set)
    
    # Look for the shared metadata file
    metadata_file = os.path.join(os.path.dirname(apidocs_dir), 'tool_validation_refinement_metadata.json')
    if not os.path.exists(metadata_file):
        # Fallback to looking in current directory
        metadata_file = 'tool_validation_refinement_metadata.json'
        if not os.path.exists(metadata_file):
            print("Warning: No shared metadata file found, response dictionary will be empty")
            return response_dict
    
    try:
        with open(metadata_file, 'r', encoding='utf-8') as f:
            metadata = json.load(f)
        
        # Extract successful responses from metadata
        for tool_data in metadata.get('tools', []):
            if (tool_data.get('status') == 'information' and 
                tool_data.get('response')):
                
                try:
                    # First parse the response string as JSON
                    response_str = tool_data.get('response')
                    if not response_str:
                        continue
                        
                    # Parse the response string to get the response object
                    response_obj = json.loads(response_str)
                    
                    # Only extract the JSON part of the response
                    if isinstance(response_obj, dict) and 'json' in response_obj:
                        response_json = response_obj['json']
                    else:
                        # Skip if response doesn't have json field
                        continue
                    
                    # Skip if response_json is None or empty
                    if response_json is None:
                        continue
                    
                    # Use function_name as the identifier instead of folder name
                    function_name = tool_data.get('function_name', 'unknown')
                    
                    # Build dictionary from ONLY the JSON response data with function_name as root
                    add_to_dict(response_dict, f'[{function_name}]', response_json, function_name)
                    
                except (json.JSONDecodeError, ValueError, TypeError) as e:
                    print(f"Warning: Could not parse response JSON for {tool_data.get('path', 'unknown')}: {e}")
                    continue
                    
    except Exception as e:
        print(f"Error loading shared metadata file: {e}")
        return response_dict
    
    print(f"Built response dictionary with {len(response_dict)} response paths from shared metadata")
    return response_dict 