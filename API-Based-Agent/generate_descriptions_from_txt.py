#!/usr/bin/env python3
import json
import os


def extract_tool_name(filename):
    """Extract the base name of the tool from the filename"""
    return filename.replace('.py', '')


def extract_method_from_tool_name(tool_name):
    """Extract HTTP method from tool name"""
    if '_GET' in tool_name:
        return 'GET'
    elif '_POST' in tool_name:
        return 'POST'
    elif '_PUT' in tool_name:
        return 'PUT'
    elif '_DELETE' in tool_name:
        return 'DELETE'
    return None


def find_description_in_txt(txt_data, tool_name):
    """Find appropriate description for a tool in the txt file data"""
    # Extract the method from the tool name
    method = extract_method_from_tool_name(tool_name)
    if not method:
        return None

    # Extract base name without method
    base_name = tool_name.replace(f'_{method}', '').lower()

    # Try to find a matching endpoint in the JSON data
    endpoints = txt_data.get('endpoints', [])
    best_match = None
    best_match_score = 0

    for endpoint in endpoints:
        # Skip if method doesn't match
        if endpoint.get('method') != method:
            continue

        # Calculate a match score
        name = endpoint.get('name', '').lower()
        description = endpoint.get('description', '').lower()
        url = endpoint.get('url', '')
        if isinstance(url, list):
            url = url[0] if url else ''
        url = url.lower()

        # Convert base_name to a regex-safe string and try to match parts
        words = base_name.replace('_', ' ').split()
        score = 0

        # Check name field
        for word in words:
            if word in name:
                score += 3
            if word in description:
                score += 2
            if word in url:
                score += 1

        # Keep track of the best match
        if score > best_match_score:
            best_match_score = score
            best_match = endpoint

    # If we found a match, return its description
    if best_match and best_match_score > 0:
        return best_match.get('description')

    return None


def generate_fallback_description(tool_name):
    """Generate a fallback description if no match is found"""
    # Extract method
    method_text = ''
    if '_GET' in tool_name:
        method_text = 'Retrieve'
    elif '_POST' in tool_name:
        method_text = 'Create or update'
    elif '_PUT' in tool_name:
        method_text = 'Update'
    elif '_DELETE' in tool_name:
        method_text = 'Delete'

    # Clean up the name
    name = tool_name
    for suffix in ['_GET', '_POST', '_PUT', '_DELETE']:
        name = name.replace(suffix, '')

    # Convert snake_case to Title Case
    name = ' '.join(word.capitalize() for word in name.split('_'))

    return f'{method_text} {name} data via API.'


def load_txt_file(site_dir):
    """Load the txt file for a site, assuming it's named site_name.txt"""
    site_name = os.path.basename(site_dir)
    txt_file = os.path.join(site_dir, f'{site_name}.txt')

    if not os.path.exists(txt_file):
        return None

    try:
        with open(txt_file, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f'Error loading {txt_file}: {str(e)}')
        return None


def generate_descriptions(source_dir, target_dir):
    """Generate descriptions for all sites using txt files"""
    os.makedirs(target_dir, exist_ok=True)

    sites = [
        d for d in os.listdir(source_dir) if os.path.isdir(os.path.join(source_dir, d))
    ]

    for site in sites:
        site_source_dir = os.path.join(source_dir, site)
        tools_dir = os.path.join(site_source_dir, 'tools')

        if not os.path.exists(tools_dir):
            print(f'No tools directory found for site {site}')
            continue

        print(f'Processing site: {site}')

        # Create target directory for site
        site_target_dir = os.path.join(target_dir, site)
        os.makedirs(site_target_dir, exist_ok=True)

        # Load txt file for this site
        txt_data = load_txt_file(site_source_dir)

        # Get tool files
        tool_files = [
            f
            for f in os.listdir(tools_dir)
            if f.endswith('.py') and not f.startswith('__')
        ]

        descriptions = {}
        for tool_file in tool_files:
            tool_name = extract_tool_name(tool_file)

            # Try to find description in txt file
            description = None
            if txt_data:
                description = find_description_in_txt(txt_data, tool_name)

            # If no description found, generate a fallback
            if not description:
                description = generate_fallback_description(tool_name)

            descriptions[tool_name] = description
            print(f'  - {tool_name}: {description}')

        # Save descriptions to JSON file
        output_file = os.path.join(site_target_dir, 'tool_descriptions.json')
        with open(output_file, 'w') as f:
            json.dump(descriptions, f, indent=2)

        print(f'Created description file for {site} at {output_file}')


if __name__ == '__main__':
    source_dir = os.path.join(os.getcwd(), 'evaluation', 'webarena', 'api')
    target_dir = os.path.join(os.getcwd(), 'workspace', 'api')

    generate_descriptions(source_dir, target_dir)
    print('Tool descriptions generation complete!')
