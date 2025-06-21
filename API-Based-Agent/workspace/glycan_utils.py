import json
import os
import sys
import importlib.util
import logging
from typing import Dict, List, Any

# Create a simple logger since opendevin logger isn't available in sandbox
logger = logging.getLogger(__name__)


def load_glycan_tasks(file_path: str) -> List[Dict[str, Any]]:
    """
    Load glycan tasks from glycan_tasks.jsonl and convert to WebArena format.
    
    Args:
        file_path: Path to glycan_tasks.jsonl file
        
    Returns:
        List of tasks in WebArena compatible format
    """
    tasks = []
    task_id = 0
    
    with open(file_path, 'r') as f:
        for line in f:
            if line.strip():
                glycan_task = json.loads(line)
                
                # Convert to WebArena format
                webarena_task = {
                    "task_id": task_id,
                    "sites": ["glycan"],
                    "require_login": False,
                    "storage_state": None,
                    "start_url": "GLYCAN_API",
                    "geolocation": None,
                    "intent": glycan_task["question"],
                    "require_reset": False,
                    "eval": {
                        "eval_types": ["glycan_gpt_evaluation"],
                        "reference_answer": glycan_task["expected_answer"],
                        "expected_trajectory": glycan_task["expected_trajectory"]
                    }
                }
                
                tasks.append(webarena_task)
                task_id += 1
    
    logger.info(f"Loaded {len(tasks)} glycan tasks from {file_path}")
    return tasks


def normalize_module_name(module_name: str) -> str:
    """
    Convert module name to the actual directory name.
    
    Args:
        module_name: Module name in any case (e.g., 'GlycanFormatConverter', 'glycanformatconverter')
        
    Returns:
        Normalized module name matching actual directory
    """
    # Mapping from common API names to actual directory names
    module_mapping = {
        'glycanformatconverter': 'glycanformatconverter',
        'wurcsframework': 'WURCSFramework',
        'glygen': 'glygen',
        'unilectin': 'unilectin',
        'pubchem': 'pubchem',
        'swaggerproteinapi': 'swaggerProteinAPI',
        'glytoucandata': 'glytoucandata',
        'glycanimage': 'glycanimage',
        'glycosmos-otherapis': 'glycosmos-otherapis',
        'composition': 'composition',
        'kegg': 'kegg',
        'o-glcnac': 'o-glcnac',
        'glycam': 'glycam'
    }
    
    # Try direct lookup first
    normalized = module_name.lower()
    if normalized in module_mapping:
        return module_mapping[normalized]
    
    # Try common variations
    if normalized == 'glycanformatconverter':
        return 'glycanformatconverter'
    elif normalized == 'wurcsframework':
        return 'WURCSFramework'
    elif normalized == 'glytoucandata':
        return 'glytoucandata'
    elif normalized == 'glycosmos-otherapis' or normalized == 'glycosmos_otherapis':
        return 'glycosmos-otherapis'
    elif normalized == 'swaggerproteinapi':
        return 'swaggerProteinAPI'
    
    # Return as-is if no mapping found
    return module_name


def get_glycan_modules() -> List[str]:
    """
    Get list of all glycan API modules.
    
    Returns:
        List of module names
    """
    # Try multiple possible paths
    possible_paths = [
        "/workspace/glycan",  # In sandbox
        "/Users/jianhaonan/Desktop/API-Based-Agent/glycan",  # Local development
        os.path.join(os.path.dirname(__file__), "glycan"),  # Relative to current file
    ]
    
    modules = []
    glycan_path = None
    
    for path_candidate in possible_paths:
        if os.path.exists(path_candidate):
            glycan_path = path_candidate
            break
    
    if glycan_path:
        for item in os.listdir(glycan_path):
            item_path = os.path.join(glycan_path, item)
            if os.path.isdir(item_path) and not item.startswith('.') and item != '__pycache__':
                modules.append(item)
        
        logger.info(f"Found glycan modules in {glycan_path}: {modules}")
    else:
        logger.warning(f"No glycan path found. Tried: {possible_paths}")
    
    return modules


def get_glycan_base_path() -> str:
    """Get the base path for glycan modules."""
    possible_paths = [
        "/workspace/glycan",  # In sandbox
        "/Users/jianhaonan/Desktop/API-Based-Agent/glycan",  # Local development
        os.path.join(os.path.dirname(__file__), "glycan"),  # Relative to current file
    ]
    
    for path_candidate in possible_paths:
        if os.path.exists(path_candidate):
            return path_candidate
    
    return "/workspace/glycan"  # Default fallback


def load_glycan_tool_descriptions(module: str) -> Dict[str, str]:
    """
    Load tool descriptions for a specific glycan module.
    
    Args:
        module: Name of the glycan module
        
    Returns:
        Dictionary mapping tool names to descriptions
    """
    glycan_path = get_glycan_base_path()
    normalized_module = normalize_module_name(module)
    description_file = os.path.join(glycan_path, normalized_module, "tool_description.json")
    
    if os.path.exists(description_file):
        with open(description_file, 'r') as f:
            return json.load(f)
    else:
        logger.warning(f"No tool_description.json found for module {module} (normalized: {normalized_module}) at {description_file}")
        return {}


def get_all_glycan_tools() -> Dict[str, Dict[str, str]]:
    """
    Get all glycan tools organized by module.
    
    Returns:
        Dictionary with module names as keys and tool descriptions as values
    """
    all_tools = {}
    modules = get_glycan_modules()
    
    for module in modules:
        tools = load_glycan_tool_descriptions(module)
        if tools:
            all_tools[module] = tools
    
    return all_tools


def dynamically_import_glycan_tool(module: str, tool_name: str):
    """
    Dynamically import a glycan tool function.
    
    Args:
        module: Name of the glycan module
        tool_name: Name of the tool function
        
    Returns:
        The imported function or None if not found
    """
    glycan_path = get_glycan_base_path()
    normalized_module = normalize_module_name(module)
    tool_file = os.path.join(glycan_path, normalized_module, f"{tool_name}.py")
    
    if not os.path.exists(tool_file):
        logger.error(f"Tool file not found: {tool_file}")
        return None
    
    try:
        # Load the module
        spec = importlib.util.spec_from_file_location(f"{module}_{tool_name}", tool_file)
        if spec is None or spec.loader is None:
            logger.error(f"Could not load spec for {tool_file}")
            return None
            
        module_obj = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module_obj)
        
        # Find the main function (usually same name as file without extension)
        function_name = tool_name.replace('.py', '')
        if hasattr(module_obj, function_name):
            return getattr(module_obj, function_name)
        else:
            # Try common function naming patterns
            possible_names = [
                function_name,
                function_name.split('_')[-1],  # Last part of underscore-separated name
                function_name.replace('_POST', '').replace('_GET', '')  # Remove HTTP method
            ]
            
            for name in possible_names:
                if hasattr(module_obj, name):
                    return getattr(module_obj, name)
            
            logger.error(f"Function {function_name} not found in {tool_file}")
            return None
            
    except Exception as e:
        logger.error(f"Error importing {tool_file}: {str(e)}")
        return None


def call_glycan_function(module: str, tool_name: str, **kwargs):
    """
    Call a glycan API function with the given parameters.
    
    Args:
        module: Name of the glycan module
        tool_name: Name of the tool function
        **kwargs: Parameters to pass to the function
        
    Returns:
        Result of the function call
    """
    logger.info(f"Calling glycan function: {module}.{tool_name} with params: {kwargs}")
    
    function = dynamically_import_glycan_tool(module, tool_name)
    if function is None:
        raise ValueError(f"Could not import function {tool_name} from module {module}")
    
    try:
        result = function(**kwargs)
        logger.info(f"Successfully called {module}.{tool_name}")
        return result
    except Exception as e:
        logger.error(f"Error calling {module}.{tool_name}: {str(e)}")
        raise


def list_glycan_tools(module: str = None) -> str:
    """
    List available glycan tools, optionally filtered by module.
    
    Args:
        module: Optional module name to filter by
        
    Returns:
        Formatted string listing available tools
    """
    if module:
        # List tools for specific module
        tools = load_glycan_tool_descriptions(module)
        if tools:
            result = f'Available tools in glycan module "{module}":\n'
            for tool_name, description in tools.items():
                result += f'- {tool_name}: {description}\n'
            return result.strip()
        else:
            return f'No tools found for glycan module "{module}"'
    else:
        # List all modules
        modules = get_glycan_modules()
        if modules:
            result = 'Available glycan modules:\n'
            for mod in sorted(modules):
                tool_count = len(load_glycan_tool_descriptions(mod))
                result += f'- {mod} ({tool_count} tools)\n'
            result += '\nUse list_tools(site="glycan", module="<module_name>") to see tools in a specific module.'
            return result.strip()
        else:
            return 'No glycan modules found'


def get_glycan_documentation(tool_name: str, module: str) -> str:
    """
    Get documentation for a specific glycan tool.
    
    Args:
        tool_name: Name of the tool
        module: Name of the glycan module
        
    Returns:
        Tool documentation string with parameters - formatted like other sites
    """
    import inspect
    import re
    
    # Try to get detailed documentation from the Python file
    glycan_path = get_glycan_base_path()
    normalized_module = normalize_module_name(module)
    tool_file = os.path.join(glycan_path, normalized_module, f"{tool_name}.py")
    
    if not os.path.exists(tool_file):
        # Fallback to basic description
        tools = load_glycan_tool_descriptions(module)
        basic_description = tools.get(tool_name, "No description available")
        return f'"""\n{basic_description}\n"""'
    
    try:
        # Import the module dynamically to get function and its docstring
        spec = importlib.util.spec_from_file_location(f"{module}_{tool_name}", tool_file)
        if spec is None or spec.loader is None:
            tools = load_glycan_tool_descriptions(module)
            basic_description = tools.get(tool_name, "No description available")
            return f'"""\n{basic_description}\n"""'
            
        module_obj = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module_obj)
        
        # Find the main function in the module
        function_name = tool_name.replace('_POST', '').replace('_GET', '').replace('_PUT', '').replace('_DELETE', '')
        target_function = getattr(module_obj, function_name, None)
        
        if target_function is None:
            # Try to find any callable function in the module
            functions = [f for f in dir(module_obj) if callable(getattr(module_obj, f)) and not f.startswith('_')]
            if functions:
                target_function = getattr(module_obj, functions[0])
        
        if target_function and callable(target_function):
            # Get the docstring - this is the key part that was missing!
            docstring = target_function.__doc__
            if docstring:
                # Return the docstring formatted like other sites
                return f'"""\n{docstring.strip()}\n"""'
            else:
                # No docstring, try to get basic description and signature
                try:
                    sig = inspect.signature(target_function)
                    params = []
                    for param_name, param in sig.parameters.items():
                        if param.default == inspect.Parameter.empty:
                            params.append(f"- {param_name} (required)")
                        else:
                            params.append(f"- {param_name} (optional, default: {param.default})")
                    
                    tools = load_glycan_tool_descriptions(module)
                    basic_description = tools.get(tool_name, "No description available")
                    param_text = '\n'.join(params) if params else "No parameters documented"
                    
                    return f'"""\n{basic_description}\n\nParameters:\n{param_text}\n"""'
                    
                except Exception as e:
                    logger.warning(f"Error getting signature for {tool_name}: {e}")
    
    except Exception as e:
        logger.warning(f"Error extracting documentation for {tool_name}: {e}")
    
    # Final fallback
    tools = load_glycan_tool_descriptions(module)
    basic_description = tools.get(tool_name, "No description available")
    return f'"""\n{basic_description}\n"""'