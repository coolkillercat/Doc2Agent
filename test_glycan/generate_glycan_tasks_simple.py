import os
import json
import re
import glob
import sys
import random
from typing import List, Dict, Optional

try:
    import openai
    from pydantic import BaseModel, Field
except ImportError:
    print("Error: Required packages are not installed. Please install them with: pip install openai pydantic")
    sys.exit(1)

class GlycanTool(BaseModel):
    name: str
    description: str
    parameters: str
    example: str = ""
    category: str = ""
    file_path: str = ""
    full_doc: str = ""

class GlycanTask(BaseModel):
    question: str
    expected_trajectory: str
    expected_answer: str

class SingleToolTaskResponse(BaseModel):
    question: str
    expected_trajectory: str
    expected_answer: str

class ToolTrajectory(BaseModel):
    trajectory: List[str]
    potential_applications: List[str]

class TrajectoryList(BaseModel):
    trajectories: List[ToolTrajectory] = Field(default_factory=list)

class ToolTrajectoryListResponse(BaseModel):
    trajectories: List[ToolTrajectory]

class MultiToolTaskResponse(BaseModel):
    feasible: bool
    reason: Optional[str] = None
    question: Optional[str] = None
    expected_trajectory: Optional[str] = None
    expected_answer: Optional[str] = None

def extract_tool_info(filepath):
    """Extract tool name, docstring, and parameters from a Python file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract function name
    func_name_match = re.search(r'def\s+(\w+)\s*\(', content)
    if not func_name_match:
        return None
    
    func_name = func_name_match.group(1)
    
    # Extract docstring
    docstring_match = re.search(r'"""(.*?)"""', content, re.DOTALL)
    docstring = docstring_match.group(1).strip() if docstring_match else "No description available"
    
    # Extract parameters
    params_match = re.search(r'\((.*?)\)', content)
    params = params_match.group(1) if params_match else ""
    
    # Extract example from docstring if available
    example = ""
    if "Example" in docstring or "Examples" in docstring:
        example_match = re.search(r'Example[s]?:.*?>>>(.*?)(?:>>>|\n\n|\Z)', docstring, re.DOTALL)
        if example_match:
            example = example_match.group(1).strip()
    
    # Store full file content as the complete documentation
    full_doc = content
    
    return GlycanTool(
        name=func_name,
        description=docstring,
        parameters=params,
        example=example,
        full_doc=full_doc
    )

def collect_glycan_tools():
    """Collect information about all glycan tools in the directory."""
    glycan_dir = "webarena_tools_toRyan/glycan"
    tools = []
    
    for root, dirs, files in os.walk(glycan_dir):
        for file in files:
            if file.endswith(".py") and file != "__init__.py":
                filepath = os.path.join(root, file)
                tool_info = extract_tool_info(filepath)
                if tool_info:
                    # Add the category (subdirectory name)
                    category = os.path.basename(root)
                    tool_info.category = category
                    tool_info.file_path = filepath
                    tools.append(tool_info)
    
    return tools

def generate_single_tool_tasks(tools: List[GlycanTool], num_tasks: int = 30):
    """Generate tasks using GPT-4o for single tools by randomly sampling tools"""
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    
    single_tool_tasks = []
    
    # Use modern client if available, otherwise fall back to legacy API
    client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    
    for i in range(num_tasks):
        # Randomly sample a tool
        tool = random.choice(tools)
        
        # Prepare the prompt with detailed information about the tool
        prompt = f"""Generate a high-quality research task for a glycan analysis tool.

Tool Information:
Name: {tool.name}
Category: {tool.category}
Full Documentation:
{tool.full_doc}

Your task is to create a realistic research question that would use this tool. The question must:
1. Include all necessary information for tool calling (actual values for parameters, not just parameter names)
2. Be specific enough that someone could actually execute the tool with the information given

Please provide:
1. A detailed research question that includes all required parameters for the tool
2. The expected trajectory (just the function name: {tool.name})
3. The expected answer format (focus on the information to be returned, not the data structure)

Return a JSON object with fields 'question', 'expected_trajectory', and 'expected_answer'.
"""
        
        print(f"Generating single tool task {i+1}/{num_tasks} using {tool.name}...")
        
        try:
            # Use standard JSON format rather than structured parsing
            response = client.chat.completions.create(
                model="gpt-4o",
                response_format={"type": "json_object"},
                messages=[
                    {"role": "system", "content": "You are a glycomaterial research assistant generating high-quality research tasks."},
                    {"role": "user", "content": prompt}
                ]
            )
            
            # Manually parse the JSON response
            result = json.loads(response.choices[0].message.content)
            
            # Add to tasks list
            task_data = {
                "question": result.get("question", ""),
                "expected_trajectory": result.get("expected_trajectory", ""),
                "expected_answer": result.get("expected_answer", "")
            }
            single_tool_tasks.append(task_data)
            
        except Exception as e:
            print(f"Error generating task for tool {tool.name}: {e}")
    
    return single_tool_tasks

def generate_multi_tool_tasks(tools: List[GlycanTool], num_tasks: int = 20):
    """Generate tasks requiring multiple tools using a two-step procedure"""
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    
    # Step 1: Generate potential tool trajectories
    tool_summary = []
    for tool in tools:
        tool_summary.append(f"Name: {tool.name}\nCategory: {tool.category}\nDescription: {tool.description}\nParameters: {tool.parameters}")
    
    tool_list_prompt = """I need you to generate potential tool calling trajectories for glycan research tasks. 
For each trajectory, suggest 1-2 potential research applications.

Here are the available tools:

"""
    tool_list_prompt += "\n\n".join(tool_summary)
    tool_list_prompt += f"""

Please generate {num_tasks+10} different tool trajectories, each using 2-4 tools in sequence. 
For each trajectory:
1. List the tools in order of execution
2. Briefly describe 1-2 potential research applications

Your response should contain a list of trajectories with their potential applications.
"""
    
    print("Step 1: Generating potential tool trajectories...")
    
    # Use modern client
    client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    
    try:
        # Use response_format={"type": "json_object"} and manually parse
        response = client.chat.completions.create(
            model="gpt-4o",
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": "You are a glycomaterial research assistant helping to design tool workflows. Return a JSON object with a 'trajectories' field containing an array of objects, each with 'trajectory' (array of tool names) and 'potential_applications' (array of application descriptions)."},
                {"role": "user", "content": tool_list_prompt}
            ]
        )
        
        # Parse the JSON response manually
        response_json = json.loads(response.choices[0].message.content)
        
        # Create TrajectoryList object
        if "trajectories" in response_json:
            trajectories_data = response_json["trajectories"]
        else:
            # Try to extract trajectories from the response directly if it's an array
            trajectories_data = response_json
            
        # Convert to Pydantic model for validation
        trajectory_list = []
        for traj in trajectories_data:
            if isinstance(traj, dict) and "trajectory" in traj and "potential_applications" in traj:
                trajectory_list.append(
                    ToolTrajectory(
                        trajectory=traj["trajectory"],
                        potential_applications=traj["potential_applications"]
                    )
                )
    
    except Exception as e:
        print(f"Error generating trajectories: {e}")
        return []
    
    # Step 2: For each trajectory, generate detailed tasks
    multi_tool_tasks = []
    count = 0
    
    for trajectory_info in trajectory_list:
        if count >= num_tasks:
            break
            
        trajectory = trajectory_info.trajectory
        applications = trajectory_info.potential_applications
        
        if not trajectory or len(trajectory) < 2:
            continue
        
        # Collect detailed documentation for all tools in the trajectory
        tool_docs = []
        trajectory_tools = []
        valid_trajectory = True
        
        for tool_name in trajectory:
            matching_tool = next((t for t in tools if t.name == tool_name), None)
            if not matching_tool:
                valid_trajectory = False
                print(f"Warning: Tool '{tool_name}' not found in the available tools.")
                break
                
            trajectory_tools.append(matching_tool)
            tool_docs.append(f"Tool: {matching_tool.name}\nCategory: {matching_tool.category}\nFull Documentation:\n{matching_tool.full_doc}")
        
        if not valid_trajectory:
            continue
            
        # Generate a detailed task for this trajectory
        separator = "="*50
        docs_text = "\n".join(tool_docs)
        
        task_prompt = f"""Generate a high-quality research task that requires using multiple glycan analysis tools in sequence.

Proposed trajectory: {" -> ".join(trajectory)}
Potential applications: {", ".join(applications)}

Detailed documentation for each tool:

{separator}
{docs_text}
{separator}

After reviewing the detailed documentation, determine if this trajectory is feasible for a real research task.
If it's feasible, create a detailed research question that would require this exact sequence of tools.

The research question must:
1. Include all necessary information for tool calling (actual values for parameters, not just parameter names)
2. Be specific enough that someone could execute the tools with the information given
3. Logically connect the output of one tool to the input of the next tool in the sequence

Please provide:
1. A detailed research question that includes necessary parameters
2. The expected trajectory (the exact sequence of function names in order)
3. The expected answer format (focus on the information to be returned, not the data structure)

If after reviewing the documentation you determine this trajectory is NOT feasible, set feasible to false and provide a reason.
"""
        
        print(f"Step 2: Generating detailed task for trajectory {count+1}/{num_tasks}...")
        
        try:
            completion = client.beta.chat.completions.parse(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a glycomaterial research assistant generating high-quality research tasks."},
                    {"role": "user", "content": task_prompt}
                ],
                response_format=MultiToolTaskResponse
            )
            
            result = completion.choices[0].message.parsed
            
            # Check if the trajectory is feasible
            if result.feasible:
                task_data = {
                    "question": result.question,
                    "expected_trajectory": result.expected_trajectory,
                    "expected_answer": result.expected_answer
                }
                multi_tool_tasks.append(task_data)
                count += 1
            else:
                print(f"Trajectory rejected as infeasible: {', '.join(trajectory)}")
                print(f"Reason: {result.reason}")
        
        except Exception as e:
            print(f"Error generating task for trajectory: {e}")
    
    return multi_tool_tasks

def save_tasks_to_jsonl(tasks, output_file="glycan_tasks.jsonl"):
    """Save the tasks to a JSONL file."""
    with open(output_file, 'w', encoding='utf-8') as f:
        for task in tasks:
            f.write(json.dumps(task) + "\n")
    print(f"Saved {len(tasks)} tasks to {output_file}")

def main():
    # Check for API key
    if not os.environ.get("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY environment variable is not set.")
        print("Please set it or run one of the provided scripts.")
        sys.exit(1)
        
    # Collect tool information
    print("Collecting tool information...")
    tools = collect_glycan_tools()
    print(f"Found {len(tools)} glycan tools")
    
    # Generate single-tool tasks
    print("\nGenerating single-tool tasks...")
    single_tool_tasks = generate_single_tool_tasks(tools, num_tasks=30)
    
    # Generate multi-tool tasks
    print("\nGenerating multi-tool tasks...")
    multi_tool_tasks = generate_multi_tool_tasks(tools, num_tasks=20)
    
    # Combine all tasks
    all_tasks = single_tool_tasks + multi_tool_tasks
    
    # Save tasks to JSONL
    save_tasks_to_jsonl(all_tasks)

if __name__ == "__main__":
    main() 