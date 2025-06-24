#!/usr/bin/env python3
"""
Simple HTML to Markdown Converter for API Documentation

This script converts HTML documentation files to clean markdown files,
specifically designed for API documentation with embedded JavaScript/CSS.
"""

import os
import re
import argparse
import sys
from pathlib import Path
from bs4 import BeautifulSoup
from markdownify import markdownify as md

# Set up stdout to handle Unicode properly
sys.stdout.reconfigure(encoding='utf-8')


def convert_html_to_markdown(html_file: str, output_file: str = None) -> str:
    """
    Convert HTML file to clean Markdown text.
    
    Args:
        html_file: Path to the HTML file
        output_file: Optional output file path. If None, creates doc.md in the same directory
        
    Returns:
        Path to the created markdown file
    """
    try:
        print(f"Converting: {html_file}")
        
        # Read HTML file
        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Parse with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Remove script and style elements completely
        scripts_removed = 0
        for script in soup(["script", "style", "noscript"]):
            scripts_removed += 1
            script.decompose()
        
        # Look for data-title elements specifically (works for React-based docs)
        elements = soup.select('[data-title]')
        
        if elements:
            # For OSRM and similar React docs, get ALL data-title elements, not just one
            all_content_parts = []
            for element in elements:
                content_text = element.get_text().strip()
                if len(content_text) > 50:  # Only include elements with substantial content
                    all_content_parts.append(str(element))
            
            if all_content_parts:
                # Combine all content parts
                cleaned_html = '\n'.join(all_content_parts)
                print(f"  Found {len(all_content_parts)} content sections using [data-title] selector")
                total_chars = sum(len(soup.select(f'[data-title]')[i].get_text()) for i in range(len(all_content_parts)))
                print(f"  Using combined content with {total_chars} characters")
            else:
                cleaned_html = str(soup)
                print(f"  Data-title content too small, using full document")
        else:
            # Fallback: remove navigation elements and use full content
            for element in soup(["nav", "footer", "header", "aside"]):
                element.decompose()
            
            # Remove elements with common non-content classes/ids
            for element in soup.find_all(attrs={"class": re.compile(r"(nav|menu|sidebar|footer|header|ad|advertisement|translate|loading)", re.I)}):
                element.decompose()
            
            cleaned_html = str(soup)
            print(f"  No data-title elements found, using full document content")
        
        # Convert HTML to Markdown
        markdown_text = md(
            cleaned_html,
            heading_style="ATX",  # Use # style headings
            bullets="-",          # Use - for bullet points
            strip=['meta', 'link']  # Remove remaining unwanted tags
        )
        
        # Post-process to clean up the markdown (minimal filtering)
        lines = []
        for line in markdown_text.splitlines():
            line = line.strip()
            
            # Skip empty lines but preserve paragraph breaks
            if not line:
                if lines and lines[-1] != '':
                    lines.append('')
                continue
            
            # Always keep headings
            if line.startswith('#'):
                lines.append(line)
                continue
            
            # Only skip very obvious JavaScript patterns (minimal filtering)
            if any(pattern in line.lower() for pattern in [
                'function()', 'class ', 'data-reactid=', 'data-reactroot'
            ]) and len(line) < 100:  # Only skip short lines with these patterns
                continue
            
            # Keep everything else
            lines.append(line)
        
        # Join lines and clean up excessive whitespace
        cleaned_markdown = '\n'.join(lines)
        
        # Remove excessive newlines (more than 2 consecutive)
        cleaned_markdown = re.sub(r'\n{3,}', '\n\n', cleaned_markdown)
        
        # Remove any remaining data attributes or React artifacts
        cleaned_markdown = re.sub(r'data-[a-zA-Z-]+="[^"]*"', '', cleaned_markdown)
        cleaned_markdown = re.sub(r'class="[^"]*"', '', cleaned_markdown)
        
        # Determine output file path
        if output_file is None:
            html_path = Path(html_file)
            # Create doc.md in the same directory as the HTML file
            output_file = html_path.parent / 'doc.md'
        
        # Write markdown file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(cleaned_markdown)
        
        print(f"  [OK] Converted to: {output_file}")
        print(f"  [OK] Original HTML: {len(html_content):,} characters")
        print(f"  [OK] Final Markdown: {len(cleaned_markdown):,} characters")
        print(f"  [OK] Removed {scripts_removed} script/style elements")
        
        return str(output_file)
        
    except Exception as e:
        print(f"  [ERROR] Error converting {html_file}: {e}")
        return None


def convert_directory(input_dir: str, output_dir: str = None, recursive: bool = False):
    """
    Convert all HTML files in a directory to markdown.
    
    Args:
        input_dir: Directory containing HTML files
        output_dir: Output directory for markdown files (default: same as input, creates doc.md files)
        recursive: Whether to search subdirectories recursively
    """
    input_path = Path(input_dir)
    
    if not input_path.exists():
        print(f"Error: Directory {input_dir} does not exist")
        return
    
    if output_dir is None:
        output_path = input_path
    else:
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
    
    # Find HTML files
    if recursive:
        html_files = list(input_path.rglob("*.html"))
    else:
        html_files = list(input_path.glob("*.html"))
    
    if not html_files:
        print(f"No HTML files found in {input_dir}")
        return
    
    print(f"Found {len(html_files)} HTML files to convert")
    print("=" * 50)
    
    converted_count = 0
    for html_file in html_files:
        # Determine output file path
        if output_dir:
            # Preserve directory structure in output
            relative_path = html_file.relative_to(input_path)
            # Create doc.md in the corresponding directory
            output_file = output_path / relative_path.parent / 'doc.md'
            output_file.parent.mkdir(parents=True, exist_ok=True)
        else:
            # Use default behavior (doc.md in same directory as HTML file)
            output_file = None
        
        result = convert_html_to_markdown(str(html_file), str(output_file) if output_file else None)
        if result:
            converted_count += 1
        print()
    
    print("=" * 50)
    print(f"Conversion complete: {converted_count}/{len(html_files)} files converted successfully")


def main():
    """Main function with command line interface."""
    parser = argparse.ArgumentParser(
        description="Convert HTML documentation files to clean Markdown (creates doc.md by default)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Convert a single file (creates doc.md in same directory)
  python html_to_markdown_converter.py file.html
  
  # Convert a single file with custom output
  python html_to_markdown_converter.py file.html -o output.md
  
  # Convert all HTML files in a directory (creates doc.md in each subdirectory)
  python html_to_markdown_converter.py -d extractor/apidocs/
  
  # Convert directory recursively with separate output directory
  python html_to_markdown_converter.py -d docs/ -o markdown_docs/ -r
        """
    )
    
    # Input options (mutually exclusive)
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument('file', nargs='?', help='HTML file to convert')
    input_group.add_argument('-d', '--directory', help='Directory containing HTML files')
    
    # Output options
    parser.add_argument('-o', '--output', help='Output file/directory path')
    parser.add_argument('-r', '--recursive', action='store_true', 
                       help='Search subdirectories recursively (only with -d)')
    
    args = parser.parse_args()
    
    if args.file:
        # Convert single file
        result = convert_html_to_markdown(args.file, args.output)
        if result:
            print(f"\n[OK] Successfully converted to: {result}")
        else:
            print(f"\n[ERROR] Failed to convert: {args.file}")
            exit(1)
    
    elif args.directory:
        # Convert directory
        convert_directory(args.directory, args.output, args.recursive)
    
    else:
        parser.print_help()


if __name__ == "__main__":
    main() 

# Convert all HTML files in apidocs directory recursively
# python extractor/html_to_markdown_converter.py -d extractor/apidocs/ -r