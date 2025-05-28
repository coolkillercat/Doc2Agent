#!/usr/bin/env python3
import importlib.util
import json
import os
import re
import sys


def extract_function_name_from_file(file_path):
    """Extract the main function name from a file"""
    try:
        with open(file_path, 'r') as f:
            content = f.read()

        # Look for function definition pattern
        match = re.search(r'def\s+([a-zA-Z0-9_]+)\s*\(', content)
        if match:
            return match.group(1)
    except Exception as e:
        print(f'Error extracting function name: {str(e)}')
    return None


def clean_tool_name(tool_name):
    """Convert tool name to a human-readable format"""
    # Replace underscores with spaces
    name = tool_name.replace('_', ' ')

    # Remove HTTP method suffix (GET, POST, etc.)
    for method in ['GET', 'POST', 'PUT', 'DELETE']:
        if name.endswith(f' {method}'):
            name = name[: -len(f' {method}')]

    # Capitalize first letter of each word
    name = ' '.join(word.capitalize() for word in name.split())

    return name


def generate_meaningful_description(tool_name, function_name):
    """Generate a meaningful description based on the tool name and function name"""
    clean_name = clean_tool_name(tool_name)

    # Common operations based on HTTP method
    method = ''
    if tool_name.endswith('_GET'):
        method = 'Retrieve'
    elif tool_name.endswith('_POST'):
        method = 'Create or update'
    elif tool_name.endswith('_PUT'):
        method = 'Update'
    elif tool_name.endswith('_DELETE'):
        method = 'Delete'

    # Common prefixes in function names
    action_prefixes = {
        'get': 'Retrieve',
        'search': 'Search for',
        'list': 'List all',
        'create': 'Create new',
        'update': 'Update existing',
        'delete': 'Delete',
        'add': 'Add',
        'remove': 'Remove',
        'save': 'Save',
        'retrieve': 'Retrieve',
        'find': 'Find',
        'check': 'Check',
        'assign': 'Assign',
        'calculate': 'Calculate',
        'estimate': 'Estimate',
    }

    action = method
    for prefix, action_word in action_prefixes.items():
        if function_name and function_name.startswith(prefix):
            action = action_word
            break

    if not action and method:
        action = method
    elif not action:
        action = 'Manage'

    return f'{action} {clean_name} data via API.'


def extract_docstring(module_path, tool_name):
    """Extract the first line of the docstring from a tool module"""
    try:
        # Extract function name directly from file
        function_name = extract_function_name_from_file(module_path)

        # Import the module dynamically
        spec = importlib.util.spec_from_file_location(tool_name, module_path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[tool_name] = module
        spec.loader.exec_module(module)

        # Try to find the main function
        base_name = tool_name.split('_')[0]
        function = getattr(module, base_name, None)

        # Try with the extracted function name if available
        if function is None and function_name:
            function = getattr(module, function_name, None)

        # If still not found, get the first function defined in the module that's not a built-in
        if function is None:
            functions = [
                f
                for f in dir(module)
                if callable(getattr(module, f)) and not f.startswith('_')
            ]
            if functions:
                function = getattr(module, functions[0])
                # Update function_name for later use
                function_name = functions[0]

        # Extract description from docstring if available
        if function and function.__doc__:
            docstring = function.__doc__.strip()
            # Get the first sentence/paragraph for a brief description
            first_line = docstring.split('\n')[0].strip()
            if first_line and not first_line.startswith('quote('):
                return first_line

        # If no docstring or useless docstring, generate a meaningful description
        return generate_meaningful_description(tool_name, function_name)

    except Exception as e:
        print(f'Error processing {tool_name}: {str(e)}')
        return generate_meaningful_description(tool_name, None)


def generate_tool_descriptions(source_dir, target_dir):
    """Generate tool descriptions for all sites"""
    # Ensure the target directory exists
    os.makedirs(target_dir, exist_ok=True)

    # Get list of site directories
    sites = [
        d for d in os.listdir(source_dir) if os.path.isdir(os.path.join(source_dir, d))
    ]

    for site in sites:
        tools_dir = os.path.join(source_dir, site, 'tools')
        if not os.path.exists(tools_dir):
            print(f'No tools directory found for site {site}')
            continue

        print(f'Processing site: {site}')

        # Create target directory for site
        site_target_dir = os.path.join(target_dir, site)
        os.makedirs(site_target_dir, exist_ok=True)

        # Get tool files
        tool_files = [
            f
            for f in os.listdir(tools_dir)
            if f.endswith('.py') and not f.startswith('__')
        ]

        # Generate descriptions
        descriptions = {}
        for tool_file in tool_files:
            tool_name = tool_file[:-3]  # Remove .py extension
            module_path = os.path.join(tools_dir, tool_file)

            # Extract description from module
            description = extract_docstring(module_path, tool_name)
            descriptions[tool_name] = description
            print(f'  - {tool_name}: {description}')

        # Save descriptions to JSON file
        output_file = os.path.join(site_target_dir, 'tool_descriptions.json')
        with open(output_file, 'w') as f:
            json.dump(descriptions, f, indent=2)

        print(f'Created description file for {site} at {output_file}')


if __name__ == '__main__':
    # Source directory with API tools
    source_dir = os.path.join(os.getcwd(), 'evaluation', 'webarena', 'api')

    # Target directory for descriptions
    target_dir = os.path.join(os.getcwd(), 'workspace', 'api')

    if not os.path.exists(source_dir):
        print(f'Source directory not found: {source_dir}')
        sys.exit(1)

    generate_tool_descriptions(source_dir, target_dir)
    print('Tool descriptions generation complete!')
