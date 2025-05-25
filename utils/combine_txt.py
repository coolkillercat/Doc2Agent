#!/usr/bin/env python3
"""
Script to combine multiple shopping API JSON text files into a single file
"""

import json
import os
import glob
import shutil
from pathlib import Path

def combine_shopping_files():
    # Find all shopping text files
    shopping_files = sorted(glob.glob('extractor/apidocs/*/*.txt'))
    
    # Initialize the combined data structure
    combined_data = {
        "title": "Combined Map_other_md API Documentation",
        "endpoints": []
    }
    
    # Process each file
    for file_path in shopping_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                data = json.loads(f.read())
                # Add endpoints from this file to the combined data
                if 'endpoints' in data and isinstance(data['endpoints'], list):
                    combined_data['endpoints'].extend(data['endpoints'])
                    print(f"Added {len(data['endpoints'])} endpoints from {file_path}")
                else:
                    print(f"Warning: No endpoints found in {file_path}")
            except json.JSONDecodeError:
                print(f"Error: {file_path} is not valid JSON")
    
    # Write the combined data to a file
    output_path = 'webarena_tools_toRyan/map_other_md/map_other_md.txt'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(combined_data, f, indent=4)
    
    print(f"Combined {len(combined_data['endpoints'])} endpoints into {output_path}")
    return output_path

def copy_tools():
    # Create the tools directory if it doesn't exist
    os.makedirs('webarena_tools/gitlab/tools', exist_ok=True)
    
    # Find all Python tool files from all shopping directories
    tool_files = []
    for dir_path in glob.glob('extractor/apidocs/gitlab/*'):
        python_files = glob.glob(f'{dir_path}/*.py')
        tool_files.extend(python_files)
    
    # Copy each tool file to the combined directory
    copied_count = 0
    for file_path in tool_files:
        file_name = os.path.basename(file_path)
        destination = f'webarena_tools/gitlab/tools/{file_name}'
        
        # Skip if the file is empty
        if os.path.getsize(file_path) == 0:
            print(f"Skipping empty file: {file_path}")
            continue
        
        # Read the original file
        with open(file_path, 'r', encoding='utf-8') as src:
            content = src.read()
        
        # Write to the destination
        with open(destination, 'w', encoding='utf-8') as dst:
            dst.write(content)
        
        copied_count += 1
        if copied_count % 50 == 0:
            print(f"Copied {copied_count} files so far...")
    
    print(f"Copied {copied_count} tool files to wikipedia/tools/")

def copy_config_file():
    # Create a config file with the server URL in the tools directory
    config_data = {
        "base_url": "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default"
    }
    
    config_path = 'webarena_tools/gitlab/tools/.config'
    with open(config_path, 'w', encoding='utf-8') as f:
        json.dump(config_data, f, indent=4)
    
    print(f"Created config file at {config_path}")

if __name__ == "__main__":
    # Combine the shopping text files
    combined_file = combine_shopping_files()
    
    # Copy the tools
    # copy_tools()
    
    # # Create config file
    # copy_config_file()
    
    print("Done!") 