import os
import importlib
import importlib.util
import inspect
from fastmcp import FastMCP
from typing import Dict, Callable, Any
import json

# Create a server instance
mcp = FastMCP(name="Custom API Server")

# Dictionary to store loaded tools and their functions
tools_registry: Dict[str, Callable] = {}

def delete_previous_registry():
    """
    Delete the previous tool_registry.json file if it exists.
    """
    registry_file = "tool_registry.json"
    if os.path.exists(registry_file):
        try:
            os.remove(registry_file)
            print(f"Deleted previous {registry_file}")
        except Exception as e:
            print(f"Warning: Failed to delete {registry_file}: {str(e)}")

def create_tool_registry_json():
    """
    Create a new tool_registry.json file based on the loaded tools.
    """
    registry_data = []
    
    for tool_name, tool_func in tools_registry.items():
        # Get function signature
        sig = inspect.signature(tool_func)
        
        # Get required parameters (those without default values)
        required_params = []
        for param_name, param in sig.parameters.items():
            if param.default == inspect.Parameter.empty:
                required_params.append(param_name)
        
        # Get tool description from docstring
        doc = tool_func.__doc__
        description = "No description available"
        if doc:
            # Get first line of docstring as description
            description = doc.strip().split('\n')[0]
        
        # Create example call
        example_params = []
        for param_name, param in sig.parameters.items():
            if param.default != inspect.Parameter.empty:
                # Use default value in example
                if isinstance(param.default, str):
                    example_params.append(f"{param_name}='{param.default}'")
                else:
                    example_params.append(f"{param_name}={param.default}")
            elif param_name in required_params:
                # Add placeholder for required params
                if 'id' in param_name.lower():
                    example_params.append(f"{param_name}=123")
                elif 'coordinate' in param_name.lower():
                    example_params.append(f"{param_name}='13.388860,52.517037'")
                elif 'query' in param_name.lower() or param_name == 'q':
                    example_params.append(f"{param_name}='Berlin'")
                else:
                    example_params.append(f"{param_name}='example'")
        
        example = f"{tool_name}({', '.join(example_params)})"
        
        # Determine the method (all our tools are GET requests based on file names)
        method = "GET"
        
        # Create a pseudo URL based on tool name
        url = f"/api/{tool_name.replace('_', '-')}"
        
        tool_entry = {
            "tool_name": tool_name,
            "method": method,
            "url": url,
            "description": description,
            "required_parameters": required_params,
            "example": example,
            "total_parameters": len(sig.parameters),
            "source_file": f"MCPTools/{tool_name}_GET.py" if f"{tool_name}_GET.py" in os.listdir("MCPTools") else f"MCPTools/{tool_name}.py"
        }
        
        registry_data.append(tool_entry)
    
    # Write to tool_registry.json
    try:
        with open("tool_registry.json", "w", encoding="utf-8") as f:
            json.dump(registry_data, f, indent=2, ensure_ascii=False)
        print(f"Created new tool_registry.json with {len(registry_data)} tools")
    except Exception as e:
        print(f"Error creating tool_registry.json: {str(e)}")

def load_tools_from_directory(directory_path: str = "./MCPTools"):
    """
    Load all Python functions from files in the MCPTools directory.
    Each file should contain a function that makes an API call.
    """
    global tools_registry
    
    if not os.path.exists(directory_path):
        print(f"Directory {directory_path} does not exist")
        return
    
    # Get all Python files in the directory
    python_files = [f for f in os.listdir(directory_path) if f.endswith('.py') and not f.startswith('__')]
    
    for python_file in python_files:
        try:
            # Remove .py extension to get module name
            module_name = python_file[:-3]
            
            # Import the module dynamically
            spec = importlib.util.spec_from_file_location(
                module_name, 
                os.path.join(directory_path, python_file)
            )
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            # Find functions in the module (excluding imports and builtins)
            for name, obj in inspect.getmembers(module):
                if (inspect.isfunction(obj) and 
                    obj.__module__ == module_name and 
                    not name.startswith('_')):
                    
                    # Store the function in our registry
                    tools_registry[name] = obj
                    print(f"Loaded tool: {name} from {python_file}")
                    
        except Exception as e:
            print(f"Failed to load {python_file}: {str(e)}")

def register_tools_with_mcp():
    """
    Register all loaded tools with the FastMCP server.
    Creates wrapper functions that extract meaningful content from Response objects.
    """
    def create_response_wrapper(tool_func, tool_name):
        """
        Create a wrapper function that extracts meaningful data from Response objects.
        """
        def wrapper(*args, **kwargs):
            try:
                # Call the original tool function
                response = tool_func(*args, **kwargs)
                
                # Check if it's a Response object
                if hasattr(response, 'status_code'):
                    result = {
                        'status_code': response.status_code,
                        'url': getattr(response, 'url', 'N/A'),
                    }
                    
                    # Try to extract JSON content first (most common for APIs)
                    try:
                        json_data = response.json()
                        result['data'] = json_data
                        result['content_type'] = 'json'
                        
                        # Add summary for large JSON responses to avoid overwhelming output
                        if isinstance(json_data, list) and len(json_data) > 5:
                            result['summary'] = f"Retrieved {len(json_data)} items. Showing first 5 items in data field."
                            result['data'] = json_data[:5]  # Limit to first 5 items
                            result['total_items'] = len(json_data)
                        elif isinstance(json_data, dict) and len(str(json_data)) > 5000:
                            result['summary'] = "Large JSON response. Content truncated. Full data available in data field."
                            
                    except (ValueError, json.JSONDecodeError):
                        # If not JSON, try text content
                        text_content = response.text
                        result['content_type'] = 'text'
                        
                        # Truncate very long text responses
                        if len(text_content) > 2000:
                            result['data'] = text_content[:2000] + "... [truncated]"
                            result['summary'] = f"Text response truncated. Full length: {len(text_content)} characters."
                        else:
                            result['data'] = text_content
                    
                    # Add error information if status code indicates an error
                    if response.status_code >= 400:
                        result['error'] = f"HTTP {response.status_code} Error"
                        if hasattr(response, 'reason'):
                            result['error_reason'] = response.reason
                    
                    return result
                else:
                    # If not a Response object, return as-is
                    return response
                    
            except Exception as e:
                return {
                    'error': f"Tool execution failed: {str(e)}",
                    'tool_name': tool_name,
                    'status_code': None
                }
        
        # Preserve the original function's signature and docstring
        wrapper.__name__ = tool_func.__name__
        wrapper.__doc__ = tool_func.__doc__
        wrapper.__signature__ = inspect.signature(tool_func)
        
        return wrapper
    
    for tool_name, tool_func in tools_registry.items():
        try:
            # Create a wrapper function that processes the Response object
            wrapped_func = create_response_wrapper(tool_func, tool_name)
            
            # Register the wrapped function with MCP
            mcp.tool(name=tool_name)(wrapped_func)
            print(f"Registered MCP tool with response wrapper: {tool_name}")
            
        except Exception as e:
            print(f"Failed to register tool {tool_name}: {str(e)}")

@mcp.tool()
def get_tool_documentation(tool_name: str) -> str:
    """
    Helper function that takes a tool name and returns the __doc__ of the corresponding tool.
    
    Args:
        tool_name (str): The name of the tool to get documentation for
        
    Returns:
        str: The docstring of the specified tool, or an error message if not found
    """
    if tool_name not in tools_registry:
        available_tools = list(tools_registry.keys())
        return f"Tool '{tool_name}' not found. Available tools: {', '.join(available_tools)}"
    
    tool_func = tools_registry[tool_name]
    doc = tool_func.__doc__
    
    if doc:
        return doc.strip()
    else:
        return f"No documentation available for tool '{tool_name}'"

@mcp.tool()
def list_available_tools() -> str:
    """
    List all available tools loaded in the MCP server.
    
    Returns:
        str: JSON string containing all available tool names and their descriptions
    """
    tools_info = {}
    for tool_name, tool_func in tools_registry.items():
        # Get first line of docstring as description
        doc = tool_func.__doc__
        if doc:
            description = doc.strip().split('\n')[0]
        else:
            description = "No description available"
        
        tools_info[tool_name] = {
            "description": description,
            "has_documentation": bool(doc)
        }
    
    return json.dumps(tools_info, indent=2)

# Load and register tools
print("=" * 60)
print("🚀 Starting MCP Server with Tool Registry Management")
print("=" * 60)

print("🗑️  Step 1: Cleaning up previous registry...")
delete_previous_registry()

print("\n📂 Step 2: Loading tools from MCPTools directory...")
load_tools_from_directory()

print("\n📝 Step 3: Creating new tool registry...")
create_tool_registry_json()

print("\n🔧 Step 4: Registering tools with MCP server...")
register_tools_with_mcp()

print("\n" + "=" * 60)
print(f"✅ MCP Server setup complete! Loaded {len(tools_registry)} tools.")
print(f"📋 Available tools: {list(tools_registry.keys())}")
print("📁 New tool_registry.json file created")
print("=" * 60)

def main():
    # Your existing server code here (the entire content you showed)
    # Just wrap everything in this main() function
    print("=" * 60)
    print("🚀 Starting MCP Server with Tool Registry Management")
    # ... rest of your code ...
    mcp.run(transport="streamable-http", host="127.0.0.1", port=8000, path="/mcp")

if __name__ == "__main__":
    main()