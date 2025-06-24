#!/usr/bin/env python3
"""
API Documentation Reorganizer

This script reorganizes API documentation files from a source directory
into a structured format suitable for api_code_generator.

Target structure: extractor/apidocs/{filename}/{apidoc}+.config

Usage:
    python reorganize_api_docs.py <input_folder_path> <output_folder_path>
"""

import os
import sys
import shutil
from pathlib import Path


def reorganize_api_docs(input_folder, output_folder):
    """
    Reorganize API documentation files into the target structure.
    Each API document gets its own folder named after the filename.
    
    Args:
        input_folder (str): Path to the source directory containing API docs
        output_folder (str): Path to the target directory for reorganized structure
    """
    input_path = Path(input_folder)
    output_path = Path(output_folder)
    
    if not input_path.exists():
        print(f"Error: Input folder '{input_folder}' does not exist.")
        return False
    
    # Create output directory structure
    apidocs_path = output_path
    apidocs_path.mkdir(parents=True, exist_ok=True)
    
    # Find config file
    config_file = None
    api_docs = []
    
    # Scan input directory for files
    for file_path in input_path.iterdir():
        if file_path.is_file():
            if file_path.name == '.config':
                config_file = file_path
            elif file_path.suffix.lower() in ['.md', '.txt', '.json', '.yaml', '.yml']:
                api_docs.append(file_path)
    
    if not config_file:
        print(f"Warning: No .config file found in '{input_folder}'")
    
    if not api_docs:
        print(f"Warning: No API documentation files found in '{input_folder}'")
        return False
    
    # Create a separate directory for each API document
    for doc_file in api_docs:
        # Use filename without extension as folder name
        folder_name = doc_file.stem
        api_dir = apidocs_path / folder_name
        api_dir.mkdir(exist_ok=True)
        
        print(f"Creating API directory: {api_dir}")
        
        # Copy the API documentation file
        dest_file = api_dir / doc_file.name
        shutil.copy2(doc_file, dest_file)
        print(f"  Copied: {doc_file.name}")
        
        # Copy config file to the API directory
        if config_file:
            dest_config = api_dir / '.config'
            shutil.copy2(config_file, dest_config)
            print(f"  Copied: .config")
    
    print(f"\nReorganization complete!")
    print(f"Created {len(api_docs)} API directories under: {apidocs_path}")
    
    return True


def main():
    """Main function to handle command line arguments and execute reorganization."""
    if len(sys.argv) != 3:
        print("Usage: python reorganize_api_docs.py <input_folder_path> <output_folder_path>")
        print("\nExample:")
        print("  python reorganize_api_docs.py shopping-tutorial/customer output")
        sys.exit(1)
    
    input_folder = sys.argv[1]
    output_folder = sys.argv[2]
    
    print(f"Input folder: {input_folder}")
    print(f"Output folder: {output_folder}")
    print("-" * 50)
    
    success = reorganize_api_docs(input_folder, output_folder)
    
    if success:
        print("\n✅ API documentation reorganization completed successfully!")
    else:
        print("\n❌ API documentation reorganization failed!")
        sys.exit(1)


if __name__ == "__main__":
    main() 