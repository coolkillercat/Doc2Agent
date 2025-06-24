import os
import re
from pathlib import Path

def split_gitlab_md_files(input_dir, output_dir=None):
    """
    Split GitLab API documentation files by '##' headers.
    
    Args:
        input_dir (str): Directory containing the markdown files to process
        output_dir (str): Directory to save the split files. If None, uses input_dir + '_split'
    """
    input_path = Path(input_dir)
    if not input_path.exists():
        print(f"Error: Input directory '{input_dir}' does not exist")
        return
    
    if output_dir is None:
        output_path = Path(str(input_path) + '_split')
    else:
        output_path = Path(output_dir)
    
    # Create output directory if it doesn't exist
    output_path.mkdir(exist_ok=True)
    
    # Process each markdown file in the input directory
    for md_file in input_path.glob('*.md'):
        print(f"Processing {md_file.name}...")
        process_file(md_file, output_path)
    
    print(f"Processing complete! Split files saved to '{output_path}'")

def process_file(file_path, output_dir):
    """
    Process a single markdown file, splitting it by '##' headers.
    
    Args:
        file_path (Path): Path to the markdown file to process
        output_dir (Path): Directory to save the split files
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Get the base name without extension
    base_name = file_path.stem
    
    # Split content by ## headers
    sections = split_by_headers(content)
    
    # Save each section to a separate file
    for i, section in enumerate(sections):
        if section.strip():  # Only save non-empty sections
            # Generate filename
            part_filename = f"{base_name}_part{i+1:02d}.md"
            output_file = output_dir / part_filename
            
            # Write section to file
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(section)
            
            print(f"  Created: {part_filename}")

def split_by_headers(content):
    """
    Split markdown content by '##' headers.
    
    Args:
        content (str): The markdown content to split
        
    Returns:
        list: List of content sections
    """
    # Find all ## headers and their positions
    header_pattern = r'^## (.+)$'
    sections = []
    
    # Split by ## headers while preserving the headers in the content
    parts = re.split(r'(^## .+$)', content, flags=re.MULTILINE)
    
    # The first part might be content before any ## header
    current_section = parts[0] if parts else ""
    
    # Process the remaining parts (alternating between headers and content)
    for i in range(1, len(parts), 2):
        if i < len(parts):
            header = parts[i]
            content_after_header = parts[i + 1] if i + 1 < len(parts) else ""
            
            # Save the previous section if it has content
            if current_section.strip():
                sections.append(current_section)
            
            # Start new section with the header
            current_section = header + content_after_header
    
    # Don't forget the last section
    if current_section.strip():
        sections.append(current_section)
    
    return sections

def main():
    """Main function to run the script."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Split GitLab API documentation files by ## headers')
    parser.add_argument('input_dir', help='Directory containing markdown files to process')
    parser.add_argument('-o', '--output', help='Output directory for split files (default: input_dir + "_split")')
    
    args = parser.parse_args()
    
    split_gitlab_md_files(args.input_dir, args.output)

if __name__ == '__main__':
    # If run directly, process the default GitLab API directory
    default_input = 'documentation_webarena/gitlab_api_clean'
    if os.path.exists(default_input):
        print(f"Processing default directory: {default_input}")
        split_gitlab_md_files(default_input)
    else:
        print("Default directory not found. Running main function for argument parsing...")
        main()
