#!/usr/bin/env python3
"""
split_json.py - Splits a large JSON API definition file into smaller chunks
and converts each chunk to HTML.
"""

import json
import os
import math
from pathlib import Path
import argparse

def split_json_file(input_file, output_dir, num_chunks=5):
    """
    Splits a JSON API definition file into multiple smaller JSON files.
    
    Args:
        input_file (str): Path to the input JSON file
        output_dir (str): Directory to store the output files
        num_chunks (int): Number of chunks to split the file into
    
    Returns:
        list: Paths to the generated JSON files
    """
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Read the input JSON file
    print(f"Reading {input_file}...")
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Extract the paths
    server_url = data.get('server_url', '')
    paths = data.get('paths', {})
    
    # Get list of path keys
    path_keys = list(paths.keys())
    total_paths = len(path_keys)
    
    if total_paths == 0:
        print("No paths found in the JSON file.")
        return []
    
    # Calculate chunk size
    paths_per_chunk = math.ceil(total_paths / num_chunks)
    print(f"Total paths: {total_paths}")
    print(f"Splitting into {num_chunks} chunks with ~{paths_per_chunk} paths each")
    
    # Generate the chunks
    output_files = []
    
    for i in range(num_chunks):
        start_idx = i * paths_per_chunk
        end_idx = min((i + 1) * paths_per_chunk, total_paths)
        
        # Skip if this chunk would be empty
        if start_idx >= total_paths:
            break
        
        # Create a new paths dictionary for this chunk
        chunk_paths = {}
        for j in range(start_idx, end_idx):
            path_key = path_keys[j]
            chunk_paths[path_key] = paths[path_key]
        
        # Create the chunk data
        chunk_data = {
            "server_url": server_url,
            "paths": chunk_paths
        }
        
        # Save the chunk to a JSON file
        base_name = Path(input_file).stem
        output_file = os.path.join(output_dir, f"{base_name}_part{i+1}.json")
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(chunk_data, f, indent=2)
        
        print(f"Created {output_file} with {len(chunk_paths)} paths")
        output_files.append(output_file)
    
    return output_files

def convert_json_to_html(json_files, output_dir):
    """
    Converts JSON API files to HTML for easier viewing.
    
    Args:
        json_files (list): List of JSON file paths to convert
        output_dir (str): Directory to store the output HTML files
    
    Returns:
        list: Paths to the generated HTML files
    """
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    html_files = []
    
    for json_file in json_files:
        # Read the JSON file
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Create HTML content
        file_name = Path(json_file).stem
        html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>{file_name} API Documentation</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        pre {{ background-color: #f5f5f5; padding: 10px; border-radius: 5px; overflow-x: auto; }}
        .endpoint {{ margin-bottom: 30px; border-bottom: 1px solid #ccc; padding-bottom: 20px; }}
        .method {{ font-weight: bold; color: #009900; }}
        .path {{ font-weight: bold; }}
        h2 {{ color: #333366; }}
        .parameter {{ margin-left: 20px; }}
        .required {{ color: #cc0000; }}
        .optional {{ color: #666666; }}
    </style>
</head>
<body>
    <h1>{file_name} API Documentation</h1>
    <p>Server URL: {data.get('server_url', '')}</p>
    
    <h2>Endpoints</h2>
"""
        
        # Add each endpoint
        for path, methods in data.get('paths', {}).items():
            for method, details in methods.items():
                html_content += f"""
    <div class="endpoint">
        <p><span class="method">{method.upper()}</span> <span class="path">{path}</span></p>
        <p>{details.get('description', '')}</p>
        
        <h3>Parameters</h3>
"""
                
                # Add parameters
                if 'parameters' in details and details['parameters']:
                    for param in details['parameters']:
                        required = param.get('required', False)
                        required_class = "required" if required else "optional"
                        required_text = "Required" if required else "Optional"
                        
                        html_content += f"""
        <div class="parameter {required_class}">
            <p><strong>{param.get('name', '')}</strong> ({param.get('in', '')}) - {required_text}</p>
            <p>{param.get('description', '')}</p>
            <p>Type: {json.dumps(param.get('schema', {}))}</p>
        </div>
"""
                else:
                    html_content += "        <p>No parameters</p>\n"
                
                # Add responses
                html_content += "        <h3>Responses</h3>\n"
                if 'responses' in details and details['responses']:
                    for status, response in details['responses'].items():
                        html_content += f"""
        <div class="response">
            <p><strong>{status}</strong> - {response.get('description', '')}</p>
        </div>
"""
                else:
                    html_content += "        <p>No response details</p>\n"
                
                html_content += "    </div>\n"
        
        # Close the HTML document
        html_content += """
</body>
</html>
"""
        
        # Save the HTML file
        output_file = os.path.join(output_dir, f"{file_name}.html")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"Created HTML file: {output_file}")
        html_files.append(output_file)
    
    return html_files

def main():
    parser = argparse.ArgumentParser(
        description='Split a large JSON API definition file into smaller chunks and convert to HTML'
    )
    parser.add_argument(
        'input_file',
        help='Path to the input JSON file'
    )
    parser.add_argument(
        '-n', '--num-chunks',
        type=int,
        default=50,
        help='Number of chunks to split the file into (default: 5)'
    )
    parser.add_argument(
        '-o', '--output-dir',
        default='split_output',
        help='Directory to store the output files (default: split_output)'
    )
    parser.add_argument(
        '--skip-html',
        action='store_true',
        help='Skip HTML conversion and only create JSON chunks'
    )
    
    args = parser.parse_args()
    
    # Validate input file
    if not os.path.isfile(args.input_file):
        print(f"Error: Input file '{args.input_file}' does not exist.")
        return 1
    
    try:
        # Create output directories
        json_output_dir = os.path.join(args.output_dir, 'json')
        html_output_dir = os.path.join(args.output_dir, 'html')
        
        # Split the JSON file
        json_files = split_json_file(args.input_file, json_output_dir, args.num_chunks)
        
        if not json_files:
            print("No output files were created.")
            return 1
        
        # Convert to HTML if not skipped
        if not args.skip_html:
            html_files = convert_json_to_html(json_files, html_output_dir)
            print(f"\nCreated {len(html_files)} HTML files in {html_output_dir}")
        
        print(f"\nSplit {args.input_file} into {len(json_files)} chunks in {json_output_dir}")
        return 0
    
    except Exception as e:
        print(f"Error: {e}")
        return 1

if __name__ == "__main__":
    import sys
    sys.exit(main()) 