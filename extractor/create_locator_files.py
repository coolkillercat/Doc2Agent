#!/usr/bin/env python3
"""
Create Locator Files for All APIs

This script processes all APIs in extractor/apidocs/ and creates locator.json files
that map each Python tool file to its most relevant markdown chunk from the documentation.
"""

import os
import json
from typing import Dict, List
from api_rawdoc_locator import APIRawDocLocator


def create_locator_for_api(api_name: str, apidocs_dir: str = "extractor/apidocs") -> Dict[str, str]:
    """
    Create a locator mapping for a single API.
    
    Args:
        api_name: Name of the API
        apidocs_dir: Directory containing API documentation
        
    Returns:
        Dictionary mapping tool_name.py to relevant markdown chunk
    """
    print(f"\nProcessing API: {api_name}")
    print("-" * 40)
    
    locator = APIRawDocLocator(apidocs_dir=apidocs_dir)
    api_dir = os.path.join(apidocs_dir, api_name)
    
    # Load API data to get chunking info
    api_data = locator._load_api_documentation(api_name)
    if api_data:
        print(f"  Documentation size: {api_data['raw_doc_size']:,} characters")
        print(f"  Number of endpoints: {api_data['num_endpoints']}")
        print(f"  Characters per endpoint: {api_data['chars_per_endpoint']:.0f}")
        print(f"  Dynamic chunk size: {api_data['chunk_size_used']} characters")
        print(f"  Dynamic chunk overlap: {api_data['chunk_overlap_used']} characters")
        print(f"  Total chunks created: {len(api_data['text_chunks'])}")
    
    # Get all Python files for this API
    python_files = []
    if os.path.exists(api_dir):
        for file in os.listdir(api_dir):
            if file.endswith('.py') and not file.startswith('__'):
                python_files.append(file)
    
    if not python_files:
        print(f"  No Python files found for {api_name}")
        return {}
    
    print(f"  Found {len(python_files)} Python files: {python_files}")
    
    # Create mapping for each Python file
    locator_mapping = {}
    
    for py_file in python_files:
        py_file_path = os.path.join(api_dir, py_file)
        
        print(f"  Processing: {py_file}")
        
        # Get documentation matches for this endpoint
        result = locator.locate_documentation_for_endpoint(api_name, py_file_path)
        
        if result.get('error'):
            print(f"    Error: {result['error']}")
            locator_mapping[py_file] = f"Error: {result['error']}"
            continue
        
        # Get the best match (highest scoring chunk)
        matches = result.get('matches', [])
        
        if not matches:
            print(f"    No matches found")
            locator_mapping[py_file] = "No relevant documentation found"
            continue
        
        # Take the best match
        best_match, best_score = matches[0]
        
        # Extract the text content
        if 'title' in best_match:
            # This is a structured section
            chunk_text = f"# {best_match['title']}\n\n{best_match['content']}"
            match_type = "Section"
        else:
            # This is a text chunk
            chunk_text = best_match['text']
            match_type = "Chunk"
        
        # Store the mapping
        locator_mapping[py_file] = chunk_text
        
        # Show summary
        query_info = result.get('query_info', {})
        description = query_info.get('description', 'N/A')
        query_source = query_info.get('query_source', 'N/A')
        
        print(f"    ✓ Best match: {match_type} (score: {best_score:.3f})")
        print(f"    ✓ Query source: {query_source}")
        if description != "Not found in JSON":
            print(f"    ✓ Description: {description[:100]}...")
        print(f"    ✓ Chunk length: {len(chunk_text)} characters")
    
    return locator_mapping


def save_locator_file(api_name: str, locator_mapping: Dict[str, str], apidocs_dir: str = "extractor/apidocs"):
    """Save the locator mapping to a JSON file in the API directory."""
    api_dir = os.path.join(apidocs_dir, api_name)
    locator_file = os.path.join(api_dir, "locator.json")
    
    try:
        with open(locator_file, 'w', encoding='utf-8') as f:
            json.dump(locator_mapping, f, indent=2, ensure_ascii=False)
        
        print(f"  ✓ Saved locator.json with {len(locator_mapping)} mappings")
        print(f"  ✓ File: {locator_file}")
        
    except Exception as e:
        print(f"  ✗ Error saving locator.json: {e}")


def create_all_locator_files(apidocs_dir: str = "extractor/apidocs"):
    """Create locator.json files for all APIs."""
    print("Creating Locator Files for All APIs")
    print("=" * 50)
    
    if not os.path.exists(apidocs_dir):
        print(f"Error: API docs directory not found: {apidocs_dir}")
        return
    
    # Get all API directories
    api_names = []
    for item in os.listdir(apidocs_dir):
        item_path = os.path.join(apidocs_dir, item)
        if os.path.isdir(item_path):
            api_names.append(item)
    
    if not api_names:
        print(f"No API directories found in {apidocs_dir}")
        return
    
    print(f"Found {len(api_names)} APIs: {api_names}")
    
    # Process each API
    total_mappings = 0
    successful_apis = 0
    
    for api_name in api_names:
        try:
            # Create locator mapping for this API
            locator_mapping = create_locator_for_api(api_name, apidocs_dir)
            
            if locator_mapping:
                # Save the mapping to locator.json
                save_locator_file(api_name, locator_mapping, apidocs_dir)
                total_mappings += len(locator_mapping)
                successful_apis += 1
            else:
                print(f"  No mappings created for {api_name}")
                
        except Exception as e:
            print(f"  ✗ Error processing {api_name}: {e}")
    
    # Summary
    print("\n" + "=" * 50)
    print("SUMMARY")
    print("=" * 50)
    print(f"APIs processed: {len(api_names)}")
    print(f"APIs successful: {successful_apis}")
    print(f"Total tool mappings: {total_mappings}")
    print(f"Locator files created: {successful_apis}")


def preview_locator_file(api_name: str, apidocs_dir: str = "extractor/apidocs"):
    """Preview the contents of a locator.json file."""
    locator_file = os.path.join(apidocs_dir, api_name, "locator.json")
    
    if not os.path.exists(locator_file):
        print(f"Locator file not found: {locator_file}")
        return
    
    try:
        with open(locator_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print(f"\nLocator file preview: {api_name}/locator.json")
        print("-" * 50)
        
        for tool_name, chunk_text in data.items():
            print(f"\nTool: {tool_name}")
            print(f"Chunk length: {len(chunk_text)} characters")
            
            # Show preview of the chunk
            preview = chunk_text[:200] + "..." if len(chunk_text) > 200 else chunk_text
            print(f"Preview: {preview}")
            print("-" * 30)
            
    except Exception as e:
        print(f"Error reading locator file: {e}")


def main():
    """Main function to create all locator files."""
    print("API Documentation Locator File Creator")
    print("=" * 50)
    
    # Create locator files for all APIs
    create_all_locator_files()
    
    # Preview some results
    print("\n" + "=" * 50)
    print("PREVIEW RESULTS")
    print("=" * 50)
    
    # Preview OSRM results
    preview_locator_file("OSRM")


if __name__ == "__main__":
    main()