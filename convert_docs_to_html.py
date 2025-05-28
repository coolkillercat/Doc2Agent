#!/usr/bin/env python3
"""
Convert API documentation to HTML

This script converts documentation files from API-Based-Agent/workspace
to HTML format and places them in appropriate extractor/apidocs directories.
"""

import os
import sys
import json
import shutil
from pathlib import Path
import markdown
from docutils.core import publish_string

SCRIPT_DIR = Path(__file__).resolve().parent
SOURCE_DIR = SCRIPT_DIR / "documentation_webarena"/"map"
TARGET_DIR = SCRIPT_DIR / "extractor" / "apidocs"

def create_config_file(api_name, base_url):
    """Create a .config file for an API"""
    config_dir = TARGET_DIR / api_name
    os.makedirs(config_dir, exist_ok=True)
    
    config_path = config_dir / ".config"
    config = {"base_url": base_url}
    
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=4)
    print(f"Created config file for {api_name} at {config_path}")

def convert_markdown_to_html(source_path, target_dir):
    """Convert a markdown file to HTML"""
    with open(source_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Convert markdown to HTML
    html_content = markdown.markdown(md_content)
    
    # Create HTML file
    filename = source_path.stem + ".html"
    target_path = target_dir / filename
    
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>{source_path.stem} API Documentation</title>
</head>
<body>
{html_content}
</body>
</html>""")
    
    print(f"Converted {source_path} to {target_path}")
    return target_path

def convert_rst_to_html(source_path, target_dir):
    """Convert a reStructuredText file to HTML"""
    with open(source_path, 'r', encoding='utf-8') as f:
        rst_content = f.read()
    
    # Convert RST to HTML
    html_content = publish_string(
        source=rst_content,
        writer_name='html',
        settings_overrides={'output_encoding': 'unicode'}
    )
    
    # Create HTML file
    filename = source_path.stem + ".html"
    target_path = target_dir / filename
    
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Converted {source_path} to {target_path}")
    return target_path

def convert_json_to_html(source_path, target_dir):
    """Convert a JSON file to HTML"""
    with open(source_path, 'r', encoding='utf-8') as f:
        json_content = json.load(f)
    
    # Create HTML representation of JSON
    html_content = "<pre>" + json.dumps(json_content, indent=4) + "</pre>"
    
    # Create HTML file
    filename = source_path.stem + ".html"
    target_path = target_dir / filename
    
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>{source_path.stem} API Documentation</title>
</head>
<body>
{html_content}
</body>
</html>""")
    
    print(f"Converted {source_path} to {target_path}")
    return target_path

def convert_text_to_html(source_path, target_dir):
    """Convert a text file to HTML"""
    with open(source_path, 'r', encoding='utf-8') as f:
        text_content = f.read()
    
    # Convert plain text to HTML
    html_content = f"<pre>{text_content}</pre>"
    
    # Create HTML file
    filename = source_path.stem + ".html"
    target_path = target_dir / filename
    
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>{source_path.stem} API Documentation</title>
</head>
<body>
{html_content}
</body>
</html>""")
    
    print(f"Converted {source_path} to {target_path}")
    return target_path

def process_reddit():
    """Process Reddit API documentation"""
    print("\nProcessing Reddit API...")
    reddit_source = SOURCE_DIR / "reddit.md"
    reddit_target_dir = TARGET_DIR / "reddit"
    
    # Create target directory
    os.makedirs(reddit_target_dir, exist_ok=True)
    
    # Convert Reddit markdown to HTML
    if reddit_source.exists():
        convert_markdown_to_html(reddit_source, reddit_target_dir)
        
        # Create Reddit config file
        create_config_file("reddit", "http://ec2-18-219-239-190.us-east-2.compute.amazonaws.com:9999")
    else:
        print(f"Warning: Reddit source file not found at {reddit_source}")

def process_wikipedia():
    """Process Wikipedia API documentation"""
    print("\nProcessing Wikipedia API...")
    wikipedia_source = SOURCE_DIR / "wikipedia.rst"
    wikipedia_target_dir = TARGET_DIR / "wikipedia"
    
    # Create target directory
    os.makedirs(wikipedia_target_dir, exist_ok=True)
    
    # Convert Wikipedia RST to HTML
    if wikipedia_source.exists():
        convert_rst_to_html(wikipedia_source, wikipedia_target_dir)
        
        # Create Wikipedia config file (placeholder URL, update if known)
        create_config_file("wikipedia", "http://localhost:8080")
    else:
        print(f"Warning: Wikipedia source file not found at {wikipedia_source}")

def process_map():
    """Process Map API documentation"""
    print("\nProcessing Map API...")
    map_source = SOURCE_DIR / "map.txt"
    map_target_dir = TARGET_DIR / "map"
    
    # Create target directory
    os.makedirs(map_target_dir, exist_ok=True)
    
    # Convert Map text to HTML
    if map_source.exists():
        convert_text_to_html(map_source, map_target_dir)
        
        # Create Map config file (placeholder URL, update if known)
        create_config_file("map", "http://localhost:8080")
    else:
        print(f"Warning: Map source file not found at {map_source}")

def process_shopping():
    """Process Shopping API documentation"""
    print("\nProcessing Shopping API...")
    shopping_source = SOURCE_DIR / "shopping-admin.json"
    shopping_admin_target_dir = TARGET_DIR / "shopping-admin"
    shopping_target_dir = TARGET_DIR / "shopping"
    
    # Create target directories
    os.makedirs(shopping_admin_target_dir, exist_ok=True)
    os.makedirs(shopping_target_dir, exist_ok=True)
    
    # Convert Shopping JSON to HTML
    if shopping_source.exists():
        convert_json_to_html(shopping_source, shopping_admin_target_dir)
        
        # Copy to shopping directory too
        shutil.copy(shopping_admin_target_dir / "shopping-admin.html", 
                   shopping_target_dir / "shopping.html")
                   
        # Check if there's a shopping_readme directory with additional documentation
        shopping_readme_dir = SOURCE_DIR / "shopping_readme"
        if shopping_readme_dir.exists() and shopping_readme_dir.is_dir():
            for file in shopping_readme_dir.glob("*"):
                if file.suffix.lower() == '.md':
                    convert_markdown_to_html(file, shopping_target_dir)
                elif file.suffix.lower() == '.json':
                    convert_json_to_html(file, shopping_target_dir)
                elif file.suffix.lower() == '.txt':
                    convert_text_to_html(file, shopping_target_dir)
        
        # Create Shopping config files
        create_config_file("shopping-admin", "http://ec2-18-219-239-190.us-east-2.compute.amazonaws.com:7770/rest/default")
        create_config_file("shopping", "http://ec2-18-219-239-190.us-east-2.compute.amazonaws.com:7770/rest/default")
    else:
        print(f"Warning: Shopping source file not found at {shopping_source}")

def process_gitlab():
    """Process GitLab API documentation"""
    print("\nProcessing GitLab API...")
    gitlab_api_dir = SOURCE_DIR / "gitlab_api"
    gitlab_target_dir = TARGET_DIR / "gitlab"
    
    # Create target directory
    os.makedirs(gitlab_target_dir, exist_ok=True)
    
    # Convert all GitLab API markdown files to HTML
    if gitlab_api_dir.exists() and gitlab_api_dir.is_dir():
        for file in gitlab_api_dir.glob("*.md"):
            convert_markdown_to_html(file, gitlab_target_dir)
        
        # Create index.html that links to all API files
        index_content = "<h1>GitLab API Documentation</h1>\n<ul>\n"
        
        for file in sorted(gitlab_target_dir.glob("*.html")):
            if file.name != "index.html":
                index_content += f'<li><a href="{file.name}">{file.stem}</a></li>\n'
        
        index_content += "</ul>"
        
        with open(gitlab_target_dir / "index.html", 'w', encoding='utf-8') as f:
            f.write(f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>GitLab API Documentation</title>
</head>
<body>
{index_content}
</body>
</html>""")
        
        # Create GitLab config file
        create_config_file("gitlab", "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023")
    else:
        print(f"Warning: GitLab API directory not found at {gitlab_api_dir}")

def main():
    """Main function to process all API documentation"""
    print("Converting API documentation to HTML...\n")
    
    # Check if source directory exists
    if not SOURCE_DIR.exists():
        print(f"Error: Source directory not found at {SOURCE_DIR}")
        return 1
    
    # Process each API
    process_reddit()
    process_wikipedia()
    process_map()
    process_shopping()
    process_gitlab()
    
    print("\nConversion complete!")
    return 0

if __name__ == "__main__":
    sys.exit(main()) 