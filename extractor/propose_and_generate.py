import os
import re
import json
import subprocess
from typing import Optional
from pydantic import BaseModel, Field
import anthropic
from dotenv import load_dotenv
load_dotenv()

def detect_function_call(value):
    """
    Detect if a value contains a function call pattern like 'function_name()'
    Returns the function name if detected, None otherwise
    """
    if isinstance(value, str):
        # Pattern to match function calls like 'get_auth_token()' 
        pattern = r'^([a-zA-Z_][a-zA-Z0-9_]*)\(\)$'
        match = re.match(pattern, value)
        if match:
            return match.group(1)
    return None

def load_auth_function(function_name):
    """
    Load an auth function from utils/auth_functions/ directory
    Returns the function code as a string, or None if not found
    """
    auth_functions_dir = "utils/auth_functions"
    function_file = f"{function_name}.py"
    function_path = os.path.join(auth_functions_dir, function_file)
    
    if os.path.exists(function_path):
        with open(function_path, 'r', encoding='utf-8') as f:
            return f.read()
    return None

def copy_file_to_doc_md(source_file_path, file_type):
    """Copy a file to doc.md in the same directory"""
    try:
        # Get the directory of the source file
        source_dir = os.path.dirname(source_file_path)
        doc_md_path = os.path.join(source_dir, "doc.md")
        
        # Check if doc.md already exists
        if os.path.exists(doc_md_path):
            print(f"  doc.md already exists for {os.path.basename(source_file_path)}")
            return doc_md_path
        
        # Copy the file content to doc.md
        with open(source_file_path, 'r', encoding='utf-8') as source_file:
            content = source_file.read()
        
        with open(doc_md_path, 'w', encoding='utf-8') as doc_file:
            doc_file.write(content)
        
        print(f"  ✓ Copied {file_type} to doc.md for {os.path.basename(source_file_path)}")
        return doc_md_path
        
    except Exception as e:
        print(f"  ✗ Error copying {file_type} to doc.md: {e}")
        return None

def convert_html_to_markdown(html_file_path):
    """Convert HTML file to markdown using the html_to_markdown_converter"""
    try:
        # Get the directory of the HTML file
        html_dir = os.path.dirname(html_file_path)
        doc_md_path = os.path.join(html_dir, "doc.md")
        
        # Check if doc.md already exists
        if os.path.exists(doc_md_path):
            print(f"  doc.md already exists for {os.path.basename(html_file_path)}")
            return doc_md_path
        
        # Find the converter script - check if we're already in extractor/ or need to go into it
        current_dir = os.getcwd()
        if os.path.basename(current_dir) == "extractor":
            converter_script = "html_to_markdown_converter.py"
        else:
            converter_script = os.path.join("extractor", "html_to_markdown_converter.py")
        
        # Make sure the converter script exists
        if not os.path.exists(converter_script):
            print(f"  ✗ Converter script not found: {converter_script}")
            return None
        
        # Run the HTML to markdown converter
        result = subprocess.run([
            "python", converter_script, html_file_path
        ], capture_output=True, text=True, check=True)
        
        if result.returncode == 0 and os.path.exists(doc_md_path):
            print(f"  ✓ Converted HTML to doc.md for {os.path.basename(html_file_path)}")
            return doc_md_path
        else:
            print(f"  ✗ Failed to convert HTML to markdown for {os.path.basename(html_file_path)}")
            print(f"  ✗ Converter output: {result.stdout}")
            print(f"  ✗ Converter error: {result.stderr}")
            return None
            
    except subprocess.CalledProcessError as e:
        print(f"  ✗ Converter script failed with exit code {e.returncode}")
        print(f"  ✗ Stdout: {e.stdout}")
        print(f"  ✗ Stderr: {e.stderr}")
        return None
    except Exception as e:
        print(f"  ✗ Error converting HTML to markdown: {e}")
        return None

def find_and_prepare_documentation(api_path):
    """
    Find documentation files in an API folder and prepare doc.md if needed.
    
    Priority order:
    1. Existing doc.md
    2. Other .md files (copy to doc.md)
    3. .txt files (copy to doc.md)
    4. .json files (copy to doc.md)
    5. .html files (convert to doc.md)
    
    Returns:
        str: Path to doc.md file if found/created, None otherwise
    """
    api_folder = os.path.basename(api_path)
    
    # Check for existing doc.md first
    doc_md_path = os.path.join(api_path, "doc.md")
    if os.path.exists(doc_md_path):
        print(f"  Using existing doc.md for {api_folder}")
        return doc_md_path
    
    # Look for documentation files in order of preference
    api_files = os.listdir(api_path)
    
    # Priority 1: Other markdown files
    api_markdown = [f for f in api_files if f.endswith('.md') and f != 'doc.md']
    if api_markdown:
        markdown_file_path = os.path.join(api_path, api_markdown[0])
        print(f"  Found Markdown file: {api_markdown[0]} for {api_folder}")
        return copy_file_to_doc_md(markdown_file_path, "Markdown")
    
    # Priority 2: Text files (excluding output files)
    api_txt = [f for f in api_files if f.endswith('.txt') and not f.startswith(api_folder)]
    if api_txt:
        txt_file_path = os.path.join(api_path, api_txt[0])
        print(f"  Found TXT file: {api_txt[0]} for {api_folder}")
        return copy_file_to_doc_md(txt_file_path, "TXT")
    
    # Priority 3: JSON files
    api_json = [f for f in api_files if f.endswith('.json')]
    if api_json:
        json_file_path = os.path.join(api_path, api_json[0])
        print(f"  Found JSON file: {api_json[0]} for {api_folder}")
        return copy_file_to_doc_md(json_file_path, "JSON")
    
    # Priority 4: HTML files (convert to markdown)
    api_html = [f for f in api_files if f.endswith('.html')]
    if api_html:
        html_file_path = os.path.join(api_path, api_html[0])
        print(f"  Found HTML file: {api_html[0]} for {api_folder}")
        return convert_html_to_markdown(html_file_path)
    
    # No documentation files found
    print(f"  No supported documentation files found for {api_folder}")
    print(f"    Looked for: .md, .txt, .json, .html files")
    return None

class ToolProposal(BaseModel):
    tool_definition: str = Field(..., description="Python function signature for the tool. example: function_name(param1:type , param2:type)")
    tool_description: str = Field(..., description="Brief description of the tool's purpose and functionality")

class ModelResponse(BaseModel):
    tool_proposals: list[ToolProposal] = Field(..., description="List of tool proposals")




def propose(api_doc: str, tool_number: int = 15) -> ModelResponse:
    """
    Propose tools based on API documentation using Claude 3.7 Sonnet with structured output.
    
    Args:
        api_doc: The API documentation string
        tool_number: Number of tools to generate (default: 15)
    
    Returns:
        ModelResponse containing the proposed tools
    """
    # Initialize the Anthropic client
    client = anthropic.Anthropic(
        api_key=os.getenv("ANTHROPIC_API_KEY")
    )
    
    # Read the template file
    template_path = "template/tool_proposal_template.txt"
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()
    
    # Format the template with the API doc and tool number
    prompt = template.format(api_doc=api_doc, tool_number=tool_number)
    
    response = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=16000,
        messages=[
            {
                "role": "user", 
                "content": prompt
            }
        ],
        tools=[
            {
                "name": "propose_tools",
                "description": "Propose tools based on API documentation",
                "input_schema": ModelResponse.model_json_schema()
            }
        ],
        tool_choice={"type": "tool", "name": "propose_tools"}
    )
    
    # Extract the structured response
    tool_use = response.content[0]
    if tool_use.type == "tool_use":
        return ModelResponse(**tool_use.input)
    else:
        raise ValueError("Unexpected response format from Claude")

def generate_empty_tool_from_proposal(api_folder: str, tool_proposals: list[ToolProposal]):
    """
    Generate empty tool functions from proposals with proper auth setup.
    
    Args:
        api_folder: Path to the API folder containing .config file
        tool_proposals: List of ToolProposal objects
    """
    
    # Load configuration if exists
    config_path = os.path.join(api_folder, ".config")
    config = None
    if os.path.exists(config_path):
        with open(config_path, 'r') as config_file:
            config = json.load(config_file)
    
    # Process headers from config and collect auth functions
    headers = "{}"
    auth_functions_code = ""
    if config and "headers" in config:
        headers = "{"
        for key, value in config["headers"].items():
            function_name = detect_function_call(value)
            if function_name:
                # Load auth function code
                auth_code = load_auth_function(function_name)
                if auth_code:
                    auth_functions_code += auth_code + "\n"
                    # Replace function call with actual function call in headers
                    headers += f"'{key}': {function_name}(), "
                else:
                    print(f"Warning: Auth function '{function_name}' not found in utils/auth_functions/")
                    headers += f"'{key}': '{value}', "
            else:
                headers += f"'{key}': '{value}', "
        headers += "}"
    
    # Read the empty tool template
    template_path = "template/empty_tool_template.txt"
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()
    
    # Generate empty tools for each proposal
    for i, proposal in enumerate(tool_proposals):
        # Extract function name from tool_definition
        # Expected format: "function_name(param1: type, param2: type)" or "function_name(param1: type, param2: type) -> return_type"
        function_match = re.match(r'^([a-zA-Z_][a-zA-Z0-9_]*)\s*\(.*\)(?:\s*->\s*\w+.*)?$', proposal.tool_definition.strip())
        if not function_match:
            print(f"Warning: Could not parse function signature: {proposal.tool_definition}")
            continue
            
        function_name = function_match.group(1)
        function_signature = proposal.tool_definition.strip()
        
        # Generate the code
        generated_code = template.format(
            auth_functions_code=auth_functions_code,
            function_signature=function_signature,
            tool_description=proposal.tool_description,
            headers=headers,
            function_name=function_name
        )
        
        # Save to file
        output_filename = f"{function_name}.py"
        output_path = os.path.join(api_folder, output_filename)
        
        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_file.write(generated_code)
        
        print(f"  ✓ Generated empty tool: {output_filename}")

def process_api_folders_and_generate_tools(api_docs_path: str, tool_number: int = 15):
    """
    Process all API folders, generate proposals, and create empty tools.
    
    Args:
        api_docs_path: Path to the directory containing API folders
        tool_number: Number of tools to generate per API (default: 15)
    """
    if not os.path.exists(api_docs_path):
        print(f"Error: API docs path does not exist: {api_docs_path}")
        return
    
    api_folders = [f for f in os.listdir(api_docs_path) if os.path.isdir(os.path.join(api_docs_path, f))]
    
    for api_folder in api_folders:
        api_path = os.path.join(api_docs_path, api_folder)
        
        print(f"Processing API: {api_folder}")
        
        # Find and prepare documentation file
        doc_md_path = find_and_prepare_documentation(api_path)
        if not doc_md_path:
            print(f"  Skipping {api_folder}: No documentation found")
            continue
        
        try:
            # Read API documentation
            with open(doc_md_path, 'r', encoding='utf-8') as f:
                api_doc = f.read()
            
            # Generate tool proposals
            print(f"  Generating {tool_number} tool proposals...")
            tool_proposals_response = propose(api_doc, tool_number)
            
            # Generate empty tools
            print(f"  Generating empty tool functions...")
            generate_empty_tool_from_proposal(api_path, tool_proposals_response.tool_proposals)
            
            print(f"  ✓ Completed processing {api_folder}")
            
        except Exception as e:
            print(f"  ✗ Error processing {api_folder}: {e}")
            continue

GENERATE_TOOL_TEMPLATE_1 = '''
## Instructions

You will be given API documentation and an incomplete code snippet. Your task is to:

1. **Complete ONLY the function** based on the API documentation. Do NOT add any additional functions.
2. **Test the function** with appropriate parameters in the `if __name__ == '__main__':` section
3. **CRITICAL: Only modify the function call parameters** in the main section. DO NOT modify the result_dict structure or print statement.
4. **Include provided headers** for API calls
5. **Write function documentation**
6. Adjust (add or remove) parameters when necessary.
7. **Return the whole code snippet directly** including the imports, helper functions if they exist, your completed function and the main function. Don't explain the code. Don't put your code in ```python.
8. **If the proposed tool cannot be achieved by a single API call response**, return an empty file with just: `# Tool not implementable with single API response`
9. **IMPORTANT**: In the main section, only change the function call (e.g., `r = function_name(param1=value1, param2=value2)`). Keep the rest of the main section exactly as provided.
10. **DO NOT add helper functions, utility functions, or any functions other than completing the one specified in the code template.**
'''

GENERATE_TOOL_TEMPLATE_2 = '''
API Documentation:
{api_doc}

Code:
{code}
'''

def get_prompt_for_api(api_folder):
    '''check the .config in the api_folder. If base_url is set, add it to the prompt.'''
    config_path = os.path.join(api_folder, ".config")
    additional_prompt = ""
    if os.path.exists(config_path):
        with open(config_path, 'r') as config_file:
            config = json.load(config_file)
        
        # Add base_url instruction if present
        if "base_url" in config:
            additional_prompt += f"Ignore the base url in the API doc and use {config['base_url']} as base url."
        
        # Add info instruction if present
        if "info" in config:
            info_values = []
            for key, value in config["info"].items():
                info_values.append(f"{key}: {value}")
            info_str = ", ".join(info_values)
            additional_prompt += f" Use the following information for testing the function: {info_str}. These values should be used as realistic test parameters when the function needs user-specific data like user IDs, project IDs, usernames, etc."
        
        template = GENERATE_TOOL_TEMPLATE_1 + additional_prompt + GENERATE_TOOL_TEMPLATE_2
        return template
    return GENERATE_TOOL_TEMPLATE_1 + GENERATE_TOOL_TEMPLATE_2

def complete_tool_implementation(api_folder: str, api_doc: str, code: str) -> str:
    """
    Complete tool implementation using Claude with the API documentation and empty code.
    
    Args:
        api_folder: Path to the API folder (for config)
        api_doc: The API documentation string
        code: The empty tool code to complete
    
    Returns:
        Completed tool code as a string, or None if tool is not implementable
    """
    # Initialize the Anthropic client
    client = anthropic.Anthropic(
        api_key=os.getenv("ANTHROPIC_API_KEY")
    )
    
    # Get the prompt template for this API
    template = get_prompt_for_api(api_folder)
    
    # Format the template with the API doc and code
    prompt = template.format(api_doc=api_doc, code=code)
    
    # Call Claude to complete the implementation
    response = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=16000,
        messages=[
            {
                "role": "user", 
                "content": prompt
            }
        ]
    )
    
    # Extract the completed code
    completed_code = response.content[0].text
    
    # Check if Claude indicated the tool is not implementable
    if "# Tool not implementable with single API response" in completed_code:
        return None
    
    return completed_code

def generate_and_complete_tools(api_docs_path: str, tool_number: int = 15):
    """
    Process all API folders, generate proposals, create empty tools, and complete implementations.
    
    Args:
        api_docs_path: Path to the directory containing API folders
        tool_number: Number of tools to generate per API (default: 15)
    """
    if not os.path.exists(api_docs_path):
        print(f"Error: API docs path does not exist: {api_docs_path}")
        return
    
    api_folders = [f for f in os.listdir(api_docs_path) if os.path.isdir(os.path.join(api_docs_path, f))]
    
    for api_folder in api_folders:
        api_path = os.path.join(api_docs_path, api_folder)
        
        print(f"Processing API: {api_folder}")
        
        # Find and prepare documentation file
        doc_md_path = find_and_prepare_documentation(api_path)
        if not doc_md_path:
            print(f"  Skipping {api_folder}: No documentation found")
            continue
        
        try:
            # Read API documentation
            with open(doc_md_path, 'r', encoding='utf-8') as f:
                api_doc = f.read()
            
            # Generate tool proposals
            print(f"  Generating {tool_number} tool proposals...")
            tool_proposals_response = propose(api_doc, tool_number)
            
            # Generate empty tools
            print(f"  Generating empty tool functions...")
            generate_empty_tool_from_proposal(api_path, tool_proposals_response.tool_proposals)
            
            # Complete tool implementations
            print(f"  Completing tool implementations...")
            for proposal in tool_proposals_response.tool_proposals:
                # Extract function name
                function_match = re.match(r'^([a-zA-Z_][a-zA-Z0-9_]*)\s*\(.*\)(?:\s*->\s*\w+.*)?$', proposal.tool_definition.strip())
                if not function_match:
                    print(f"    Skipping invalid function signature: {proposal.tool_definition}")
                    continue
                    
                function_name = function_match.group(1)
                empty_tool_path = os.path.join(api_path, f"{function_name}.py")
                
                if os.path.exists(empty_tool_path):
                    # Read the empty tool code
                    with open(empty_tool_path, 'r', encoding='utf-8') as f:
                        empty_code = f.read()
                    
                    # Complete the implementation
                    try:
                        completed_code = complete_tool_implementation(api_path, api_doc, empty_code)
                        
                        if completed_code is None:
                            # Tool is not implementable, remove the empty file
                            os.remove(empty_tool_path)
                            print(f"    ✗ Removed: {function_name}.py (not implementable with single API response)")
                        else:
                            # Save the completed code
                            with open(empty_tool_path, 'w', encoding='utf-8') as f:
                                f.write(completed_code)
                            
                            print(f"    ✓ Completed: {function_name}.py")
                        
                    except Exception as e:
                        print(f"    ✗ Failed to complete {function_name}.py: {e}")
                        continue
            
            print(f"  ✓ Completed processing {api_folder}")
            
        except Exception as e:
            print(f"  ✗ Error processing {api_folder}: {e}")
            continue

def complete_existing_tools(api_docs_path: str):
    """
    Complete existing empty tool implementations without generating new proposals.
    
    Args:
        api_docs_path: Path to the directory containing API folders
    """
    if not os.path.exists(api_docs_path):
        print(f"Error: API docs path does not exist: {api_docs_path}")
        return
    
    api_folders = [f for f in os.listdir(api_docs_path) if os.path.isdir(os.path.join(api_docs_path, f))]
    
    for api_folder in api_folders:
        api_path = os.path.join(api_docs_path, api_folder)
        
        print(f"Completing tools for API: {api_folder}")
        
        # Find and prepare documentation file
        doc_md_path = find_and_prepare_documentation(api_path)
        if not doc_md_path:
            print(f"  Skipping {api_folder}: No documentation found")
            continue
        
        try:
            # Read API documentation
            with open(doc_md_path, 'r', encoding='utf-8') as f:
                api_doc = f.read()
            
            # Find existing Python tool files
            python_files = [f for f in os.listdir(api_path) if f.endswith('.py') and f != '__init__.py']
            
            if not python_files:
                print(f"  No Python tool files found in {api_folder}")
                continue
            
            print(f"  Found {len(python_files)} tool files to complete...")
            
            for py_file in python_files:
                tool_path = os.path.join(api_path, py_file)
                
                try:
                    # Read the existing tool code
                    with open(tool_path, 'r', encoding='utf-8') as f:
                        existing_code = f.read()
                    
                    # Check if it's an empty tool (contains 'pass')
                    if 'pass' in existing_code:
                        # Complete the implementation
                        completed_code = complete_tool_implementation(api_path, api_doc, existing_code)
                        
                        if completed_code is None:
                            # Tool is not implementable, remove the file
                            os.remove(tool_path)
                            print(f"    ✗ Removed: {py_file} (not implementable with single API response)")
                        else:
                            # Save the completed code
                            with open(tool_path, 'w', encoding='utf-8') as f:
                                f.write(completed_code)
                            
                            print(f"    ✓ Completed: {py_file}")
                    else:
                        print(f"    - Skipped: {py_file} (already implemented)")
                        
                except Exception as e:
                    print(f"    ✗ Failed to complete {py_file}: {e}")
                    continue
            
            print(f"  ✓ Completed processing {api_folder}")
            
        except Exception as e:
            print(f"  ✗ Error processing {api_folder}: {e}")
            continue

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python propose_and_generate.py <api_docs_path> [tool_number] [options]")
        print("Options:")
        print("  --empty-only    : Only generate empty tools (don't complete)")
        print("  --complete-only : Only complete existing empty tools")
        print("  (no option)     : Full workflow - propose, generate empty, and complete")
        sys.exit(1)
    
    api_docs_path = sys.argv[1]
    tool_number = 1
    mode = "full"  # default: full workflow
    
    # Parse arguments
    for i, arg in enumerate(sys.argv[2:], 2):
        if arg == "--empty-only":
            mode = "empty"
        elif arg == "--complete-only":
            mode = "complete"
        elif arg.isdigit():
            tool_number = int(arg)
    
    if mode == "empty":
        print("Generating empty tools only...")
        process_api_folders_and_generate_tools(api_docs_path, tool_number)
    elif mode == "complete":
        print("Completing existing empty tools only...")
        complete_existing_tools(api_docs_path)
    else:
        print("Running full workflow: propose, generate empty, and complete tools...")
        generate_and_complete_tools(api_docs_path, tool_number)