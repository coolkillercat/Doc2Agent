import json
import os
import sys
import importlib.util
from typing import Dict, List, Any
from opendevin.core.logger import opendevin_logger as logger


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


def get_glycan_modules() -> List[str]:
    """
    Get list of all glycan API modules.
    
    Returns:
        List of module names
    """
    glycan_path = "/Users/jianhaonan/Desktop/API-Based-Agent/glycan"
    modules = []
    
    if os.path.exists(glycan_path):
        for item in os.listdir(glycan_path):
            item_path = os.path.join(glycan_path, item)
            if os.path.isdir(item_path) and not item.startswith('.') and item != '__pycache__':
                modules.append(item)
    
    logger.info(f"Found glycan modules: {modules}")
    return modules


def load_glycan_tool_descriptions(module: str) -> Dict[str, str]:
    """
    Load tool descriptions for a specific glycan module.
    
    Args:
        module: Name of the glycan module
        
    Returns:
        Dictionary mapping tool names to descriptions
    """
    glycan_path = "/Users/jianhaonan/Desktop/API-Based-Agent/glycan"
    description_file = os.path.join(glycan_path, module, "tool_description.json")
    
    if os.path.exists(description_file):
        with open(description_file, 'r') as f:
            return json.load(f)
    else:
        logger.warning(f"No tool_description.json found for module {module}")
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
    glycan_path = "/Users/jianhaonan/Desktop/API-Based-Agent/glycan"
    tool_file = os.path.join(glycan_path, module, f"{tool_name}.py")
    
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
        Tool documentation string
    """
    tools = load_glycan_tool_descriptions(module)
    if tool_name in tools:
        return f"Tool: {tool_name}\nModule: {module}\nDescription: {tools[tool_name]}"
    else:
        return f"Tool {tool_name} not found in module {module}"