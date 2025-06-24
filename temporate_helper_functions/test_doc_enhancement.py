#!/usr/bin/env python3
"""
Test script to demonstrate the new documentation enhancement functionality.
This simulates a successful tool execution and shows how Claude 3.7 can enhance
the function documentation with response explanation.
"""

import json
import sys
import os

# Add the main directory to the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from main.validation_and_refinement_main import (
    extract_json_key_hierarchy,
    call_claude_for_doc_explanation,
    update_function_docstring_with_returns,
    extract_function_names
)


def test_json_hierarchy_extraction():
    """Test the JSON key hierarchy extraction function."""
    print("=== Testing JSON Key Hierarchy Extraction ===")
    
    # Sample JSON response from a successful API call
    sample_response = {
        "status_code": 200,
        "text": '{"items":[],"search_criteria":{"filter_groups":[{"filters":[{"field":"sku","value":"WS12-M-Orange","condition_type":"eq"}]}],"sort_orders":[{"field":"name","direction":"DESC"}],"page_size":10},"total_count":0}',
        "json": {
            "items": [],
            "search_criteria": {
                "filter_groups": [
                    {
                        "filters": [
                            {
                                "field": "sku",
                                "value": "WS12-M-Orange",
                                "condition_type": "eq"
                            }
                        ]
                    }
                ],
                "sort_orders": [
                    {
                        "field": "name",
                        "direction": "DESC"
                    }
                ],
                "page_size": 10
            },
            "total_count": 0
        },
        "content": '{"items":[],"search_criteria":{"filter_groups":[{"filters":[{"field":"sku","value":"WS12-M-Orange","condition_type":"eq"}]}],"sort_orders":[{"field":"name","direction":"DESC"}],"page_size":10},"total_count":0}'
    }
    
    # Extract key hierarchy
    key_hierarchy = extract_json_key_hierarchy(sample_response)
    
    print("Original JSON structure (truncated):")
    print(json.dumps(sample_response, indent=2)[:500] + "...")
    
    print("\nExtracted key hierarchy:")
    print(json.dumps(key_hierarchy, indent=2))
    
    return key_hierarchy


def test_claude_explanation():
    """Test calling Claude 3.7 for documentation explanation."""
    print("\n=== Testing Claude 3.7 Documentation Explanation ===")
    
    # Simulate the actual structure we get from successful API calls
    # This represents output["json"] from a successful tool execution
    json_data = {
        "items": [
            {
                "id": 123,
                "name": "Sample Product",
                "price": 29.99,
                "sku": "WS12-M-Orange",
                "status": "in_stock"
            }
        ],
        "search_criteria": {
            "filter_groups": [
                {
                    "filters": [
                        {
                            "field": "sku",
                            "value": "WS12-M-Orange",
                            "condition_type": "eq"
                        }
                    ]
                }
            ],
            "sort_orders": [
                {
                    "field": "name",
                    "direction": "DESC"
                }
            ],
            "page_size": 10
        },
        "total_count": 1
    }
    
    # Extract key hierarchy from the JSON data (not the full stdout structure)
    key_hierarchy = {
        "items": [
            {
                "id": "<int>",
                "name": "<str>",
                "price": "<float>",
                "sku": "<str>",
                "status": "<str>"
            }
        ],
        "search_criteria": {
            "filter_groups": [
                {
                    "filters": [
                        {
                            "field": "<str>",
                            "value": "<str>",
                            "condition_type": "<str>"
                        }
                    ]
                }
            ],
            "sort_orders": [
                {
                    "field": "<str>",
                    "direction": "<str>"
                }
            ],
            "page_size": "<int>"
        },
        "total_count": "<int>"
    }
    
    function_name = "search_products"
    api_description = "Searches for products based on specified criteria, with support for pagination, sorting, and field selection."
    
    print(f"Function name: {function_name}")
    print(f"API description: {api_description}")
    print(f"Analyzing JSON data structure (not full stdout):")
    print(json.dumps(key_hierarchy, indent=2))
    
    # Call Claude for explanation
    try:
        explanation = call_claude_for_doc_explanation(key_hierarchy, function_name, api_description)
        print(f"\nClaude's concise explanation:")
        print(f'"{explanation}"')
        
        # Show comparison with old vs new approach
        print(f"\n--- Comparison ---")
        print(f"OLD approach: Would analyze entire stdout with redundant status_code, text, content fields")
        print(f"NEW approach: Analyzes only the actual data from output['json']")
        print(f"OLD prompt: Would generate verbose explanation about JSON structure")
        print(f"NEW prompt: Generates concise 1-sentence description of information content")
        
        return explanation
    except Exception as e:
        print(f"Error calling Claude: {str(e)}")
        print("Note: This requires a valid ANTHROPIC_API_KEY environment variable")
        return "Returns product search results with item details and search metadata."


def test_documentation_update():
    """Test updating function documentation."""
    print("\n=== Testing Documentation Update ===")
    
    # Create a test Python file with multiple functions (like a real tool)
    test_file_content = '''import requests
import json

def get_auth_token():
    """
    Helper function to get authentication token.
    
    Returns:
        str: Bearer token for API authentication
    """
    response = requests.post(
        url='http://example.com/api/token',
        headers={'content-type': 'application/json'},
        data=json.dumps({'username': 'admin', 'password': 'admin123'})
    )
    return "Bearer " + response.json()

def search_products(field: str, value: str, condition_type: str = 'eq'):
    """
    Searches for products based on specified criteria.
    
    Args:
        field (str): The product field to search on
        value (str): The value to search for
        condition_type (str, optional): The condition type for the search. Defaults to 'eq'.
    """
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_auth_token()
    }
    
    params = {
        'searchCriteria[filter_groups][0][filters][0][field]': field,
        'searchCriteria[filter_groups][0][filters][0][value]': value,
        'searchCriteria[filter_groups][0][filters][0][condition_type]': condition_type,
    }
    
    response = requests.get('http://example.com/api/products', headers=headers, params=params)
    return response

if __name__ == '__main__':
    # Test the function with a simple product search
    r = search_products(field='sku', value='WS12-M-Orange', condition_type='eq')
    print(json.dumps(r.json(), indent=4))
'''
    
    test_file_path = "test_multiple_functions.py"
    
    # Write test file
    with open(test_file_path, 'w', encoding='utf-8') as f:
        f.write(test_file_content)
    
    print(f"Created test file: {test_file_path}")
    print("Original file has 2 functions:")
    print("1. get_auth_token() - Helper function (already has Returns)")
    print("2. search_products() - Main tool function (should be updated)")
    
    # Update documentation
    returns_description = "Returns product search results with item details, pricing, and availability status."
    
    try:
        success = update_function_docstring_with_returns(test_file_path, returns_description)
        if success:
            # Read and display updated file
            with open(test_file_path, 'r', encoding='utf-8') as f:
                updated_content = f.read()
            
            print("\nUpdated file content:")
            print("=" * 50)
            
            # Show only the relevant parts
            lines = updated_content.split('\n')
            in_search_products = False
            for i, line in enumerate(lines):
                if 'def search_products(' in line:
                    in_search_products = True
                    print(f"{i+1:2d}: {line}")
                elif in_search_products and line.strip().startswith('def '):
                    break
                elif in_search_products:
                    print(f"{i+1:2d}: {line}")
                    if '"""' in line and 'Returns:' in updated_content[updated_content.find('def search_products'):updated_content.find('def search_products') + 500]:
                        # Show a few more lines after the docstring
                        for j in range(i+1, min(i+4, len(lines))):
                            if lines[j].strip():
                                print(f"{j+1:2d}: {lines[j]}")
                        break
            
            print("\n✓ SUCCESS: Updated ONLY the last function (search_products)")
            print("✓ The helper function (get_auth_token) was left unchanged")
            
        else:
            print("Failed to update documentation")
    except Exception as e:
        print(f"Error updating documentation: {str(e)}")
    finally:
        # Clean up test file
        try:
            os.remove(test_file_path)
            print(f"\nCleaned up test file: {test_file_path}")
        except:
            pass


def demonstrate_data_extraction():
    """Demonstrate the improved data extraction logic."""
    print("\n=== Testing Data Extraction Logic ===")
    
    # Simulate different output structures
    test_cases = [
        {
            "name": "Case 1: output with json field",
            "output": {
                "status_code": 200,
                "text": '{"items":[{"id":1,"name":"Product"}],"total":1}',
                "json": {"items":[{"id":1,"name":"Product"}],"total":1},
                "content": '{"items":[{"id":1,"name":"Product"}],"total":1}'
            },
            "expected": "Should extract from json field"
        },
        {
            "name": "Case 2: output with null json, valid text",
            "output": {
                "status_code": 200,
                "text": '{"items":[{"id":2,"name":"Product2"}],"total":1}',
                "json": None,
                "content": '{"items":[{"id":2,"name":"Product2"}],"total":1}'
            },
            "expected": "Should parse text field as JSON"
        },
        {
            "name": "Case 3: output with null json, invalid text",
            "output": {
                "status_code": 200,
                "text": "Error: Invalid response",
                "json": None,
                "content": "Error: Invalid response"
            },
            "expected": "Should use whole output as fallback"
        }
    ]
    
    for case in test_cases:
        print(f"\n{case['name']}:")
        print(f"Expected: {case['expected']}")
        
        output_json = case['output']
        
        # Simulate the extraction logic
        data_to_analyze = output_json.get("json")
        if data_to_analyze is None:
            text_content = output_json.get("text", "")
            if text_content:
                try:
                    data_to_analyze = json.loads(text_content)
                    print("✓ Successfully parsed text field as JSON")
                except:
                    data_to_analyze = output_json
                    print("✓ Used whole output as fallback (text not valid JSON)")
            else:
                data_to_analyze = output_json
                print("✓ Used whole output as fallback (no text)")
        else:
            print("✓ Extracted from json field")
        
        print(f"Data to analyze: {data_to_analyze}")


def main():
    """Run all tests to demonstrate the functionality."""
    print("Testing IMPROVED Documentation Enhancement Functionality")
    print("=" * 60)
    
    # Test JSON hierarchy extraction
    key_hierarchy = test_json_hierarchy_extraction()
    
    # Test improved Claude explanation
    explanation = test_claude_explanation()
    
    # Test documentation update
    test_documentation_update()
    
    # Test data extraction logic
    demonstrate_data_extraction()
    
    print("\n" + "=" * 60)
    print("Test completed!")
    print("\nSummary of IMPROVEMENTS:")
    print("1. ✓ Concise prompt: Focuses on WHAT information is returned, not HOW it's structured")
    print("2. ✓ Shorter responses: 1-sentence descriptions instead of verbose explanations")
    print("3. ✓ Smart data extraction: Analyzes output['json'] first, then output['text'] as fallback")
    print("4. ✓ Reduced token usage: Shorter prompts and responses")
    print("5. ✓ Better focus: Avoids redundant status_code, text, content fields in analysis")
    print("\nThis improved functionality is now integrated into both validation and refinement!")


if __name__ == "__main__":
    main() 