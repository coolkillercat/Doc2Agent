#!/usr/bin/env python3

import os
import json
import inspect
import importlib.util
import sys
from pathlib import Path

def extract_docstring(file_path):
    """Extract the docstring from a Python file."""
    try:
        # Load the module
        module_name = os.path.basename(file_path).replace('.py', '')
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # Find the main function in the module
        main_function = None
        for name, obj in inspect.getmembers(module):
            if inspect.isfunction(obj) and name != '__main__':
                main_function = obj
                break
        
        if main_function:
            # Extract the docstring
            docstring = inspect.getdoc(main_function)
            # Get the first sentence or paragraph for a concise description
            if docstring:
                # Split by period followed by space or newline
                first_sentence = docstring.split('.\n', 1)[0].split('. ', 1)[0]
                # Add period if it doesn't end with one
                if not first_sentence.endswith('.'):
                    first_sentence += '.'
                return first_sentence
            return "No description available."
        else:
            return "No description available."
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")
        return "No description available."

def generate_tool_description(directory):
    """Generate a tool_description.json file for a directory."""
    tools_dict = {}
    
    # List all Python files in the directory
    for file_path in Path(directory).glob('*.py'):
        if file_path.name == '__init__.py':
            continue
            
        # Extract the function name (file name without extension)
        tool_name = file_path.stem
        
        # Extract the description from the docstring
        description = extract_docstring(str(file_path))
        
        # Add to tools dictionary
        tools_dict[tool_name] = description
    
    # Create the tool_description.json file
    output_path = os.path.join(directory, 'tool_description.json')
    with open(output_path, 'w') as f:
        json.dump(tools_dict, f, indent=2)
    
    print(f"Created tool_description.json in {directory} with {len(tools_dict)} tools")

def process_all_directories(base_directory):
    """Process all subdirectories in the GitLab tools directory."""
    # Get all subdirectories
    subdirectories = [d for d in os.listdir(base_directory) if os.path.isdir(os.path.join(base_directory, d))]
    
    for subdir in subdirectories:
        dir_path = os.path.join(base_directory, subdir)
        print(f"Processing directory: {dir_path}")
        generate_tool_description(dir_path)

def generate_main_description(base_directory):
    """Generate a main tool_descriptions.json file that combines all subdirectory tools."""
    all_tools = {}
    
    # Get all subdirectories
    subdirectories = [d for d in os.listdir(base_directory) if os.path.isdir(os.path.join(base_directory, d))]
    
    for subdir in subdirectories:
        dir_path = os.path.join(base_directory, subdir)
        
        # List all Python files in the directory
        for file_path in Path(dir_path).glob('*.py'):
            if file_path.name == '__init__.py':
                continue
                
            # Extract the function name (file name without extension)
            tool_name = file_path.stem
            
            # Extract the description from the docstring
            description = extract_docstring(str(file_path))
            
            # Add to tools dictionary
            all_tools[tool_name] = description
    
    # Create the main tool_descriptions.json file
    output_path = os.path.join(os.path.dirname(base_directory), 'tool_descriptions.json')
    with open(output_path, 'w') as f:
        json.dump(all_tools, f, indent=2)
    
    print(f"Created main tool_descriptions.json with {len(all_tools)} tools")

if __name__ == "__main__":
    # Base directory for GitLab tools
    base_dir = "/Users/jianhaonan/Desktop/API-Based-Agent/evaluation/webarena/api/gitlab/tools"
    
    if len(sys.argv) > 1:
        # Process a specific directory if provided
        process_dir = os.path.join(base_dir, sys.argv[1])
        if os.path.isdir(process_dir):
            generate_tool_description(process_dir)
        else:
            print(f"Directory not found: {process_dir}")
    else:
        # Process all directories
        process_all_directories(base_dir)
        # Generate the main tool_descriptions.json file
        generate_main_description(base_dir)
        print("All tool descriptions generated successfully!") 