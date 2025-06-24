import asyncio
import json
import logging
import multiprocessing as mp
import os
import pathlib
import subprocess
import sys
import time
import shutil

from tqdm import tqdm

# Add the webarena directory to path for imports
sys.path.append('/Users/jianhaonan/Desktop/API-Based-Agent/evaluation/webarena/webarena')
sys.path.append('/Users/jianhaonan/Desktop/API-Based-Agent/evaluation/webarena/webarena/evaluation_harness')

from utils import check_correctness, get_initial_prompt_from_task, get_tests
from glycan_utils import load_glycan_tasks
from glycan_evaluation import check_correctness_glycan
from opendevin.controller.state.state import State
from opendevin.core.config import config, get_llm_config_arg, get_parser
from opendevin.core.logger import get_console_handler
from opendevin.core.logger import opendevin_logger as logger
from opendevin.core.main import main
from opendevin.events.action import MessageAction


def cleanup():
    print('Cleaning up child processes...')
    for process in mp.active_children():
        print(f'Terminating child process: {process.name}')
        process.terminate()
        process.join()


def codeact_user_response(state: State) -> str:
    # Check if the agent has already provided a Finish[answer] response
    if state and hasattr(state, 'history') and state.history:
        try:
            # Get the last few agent messages to check for completion
            recent_messages = []
            
            # Handle different types of history objects
            if hasattr(state.history, 'get_events'):
                events = state.history.get_events()
            elif isinstance(state.history, list):
                events = state.history
            else:
                events = list(state.history)
            
            # Look for agent messages in recent history
            for event in reversed(events[-10:]):  # Check last 10 events
                if (hasattr(event, 'source') and event.source == 'AGENT' and 
                    hasattr(event, 'content') and event.content):
                    recent_messages.append(event.content)
                    if len(recent_messages) >= 3:  # Check last 3 agent messages
                        break
            
            # Check if any recent message contains Finish[...]
            for message in recent_messages:
                if 'Finish[' in message and ']' in message:
                    logger.info(f"Agent provided completion signal with Finish[...], stopping task")
                    return '/exit'  # Signal to exit
                    
        except Exception as e:
            logger.warning(f"Error checking for completion signal: {e}")
    
    # If no completion detected, continue with normal prompt
    msg = (
        'Please continue working on the glycan research task using the available APIs.\n'
        'IMPORTANT: You MUST write Python code in <execute_ipython> blocks to call the glycan functions!\n\n'
        'CRITICAL GLYCAN WORKFLOW:\n'
        '1. ALWAYS start by exploring available APIs using list_tools(site="glycan") for modules\n'
        '2. ALWAYS examine API documentation using get_documentation(tool_name, site="glycan", module="module_name")\n'
        '3. ALWAYS use call_function(tool_name, site="glycan", module="module_name", **parameters) for API calls\n'
        '4. Make sure to verify your results and provide clear explanations\n\n'
        'EXAMPLE CODE FORMAT:\n'
        '<execute_ipython>\n'
        'from utils import list_tools, get_documentation, call_function\n'
        'result = list_tools(site="glycan")\n'
        'print(result)\n'
        '</execute_ipython>\n'
    )
    return (
        msg
        + '\nWhen you think you successfully finished the research task, first respond with `Finish[answer]` where you include *only* your answer to the research question in `[]`. Make sure to include all relevant findings and scientific conclusions.'
        + '\nAfter that, when you responded with your answer, you should respond with <finish></finish>.'
        + '\nThen finally, to exit, you can run <execute_bash>\nexit()\n</execute_bash>'
    )


def monologue_user_response(state: State) -> str:
    raise NotImplementedError('MonologueAgent should never ask for user responses.')


AGENT_CLS_TO_FAKE_USER_RESPONSE_FN = {
    'CodeActAgent': codeact_user_response,
    'MonologueAgent': monologue_user_response,
    'DelegatorAgent': codeact_user_response,
    'InterleavingAgent': codeact_user_response,
}

AGENT_CLS_TO_INST_SUFFIX = {
    'CodeActAgent': 'When you think you have completed the request, please run the following command: <execute_bash> exit </execute_bash>.\n'
}


def process_instance(
    instance,
    metadata,
    reset_logger: bool = True,
):
    # Setup logging for this instance
    if reset_logger:
        # Set up logging for each instance separately
        logger.setLevel(logging.INFO)
        logger.handlers = [get_console_handler()]
        logger.info(f'Starting instance {instance["task_id"]}')

    # Get configuration
    agent_cls = metadata['agent_class']
    llm_config = metadata['llm_config']
    env_vars = metadata['env_vars']

    # Set environment variables for this instance
    for key, value in env_vars.items():
        os.environ[key] = value

    # Create logs directory
    logs_dir = os.path.join(metadata['eval_output_dir'], 'logs')
    os.makedirs(logs_dir, exist_ok=True)
    
    log_file_path = os.path.join(logs_dir, f'instance_{instance["task_id"]}.log')
    
    # Set up logging to file
    file_handler = logging.FileHandler(log_file_path, mode='w')
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.info(f'Processing glycan task {instance["task_id"]}')
    logger.info(f'Question: {instance["intent"]}')
    logger.info(f'Expected trajectory: {instance["eval"].get("expected_trajectory", "None")}')

    # Get the initial prompt for glycan tasks
    task = instance
    
    # Create glycan-specific initial prompt
    glycan_prompt = f"""You are a glycomics research assistant with access to comprehensive glycan research APIs.

RESEARCH QUESTION: {task['intent']}

You have access to 12 specialized glycan API modules:
- WURCSFramework: Structure validation and mass calculation
- GlycanFormatConverter: Format conversions (IUPAC, WURCS, etc.)
- GlyGen: Protein-glycan interaction data
- UniLectin: Lectin-glycan binding analysis
- PubChem: Chemical properties and bioassays
- SwaggerProteinAPI: Comprehensive protein analysis
- GlyTouCanData: Glycan registry and identification
- GlycanImage: Glycan structure visualization
- GlycoSMOS-OtherAPIs: Multi-format conversion tools
- Composition: Composition-based analysis
- KEGG: Pathway and metabolic context
- O-GlcNAc: Specific PTM analysis

CRITICAL WORKFLOW:
1. Start with list_tools(site='glycan') to see all available modules
2. Use list_tools(site='glycan', module='MODULE_NAME') to see tools in specific modules
3. Use get_documentation(tool_name, site='glycan', module='MODULE_NAME') for tool details
4. Use call_function(tool_name, site='glycan', module='MODULE_NAME', **parameters) to execute APIs

IMPORTANT: You MUST use Python code blocks to call these functions. Always format your code as:

<execute_ipython>
from utils import list_tools, get_documentation, call_function

# Example calls:
result = list_tools(site='glycan')
print(result)

# For specific modules:
tools = list_tools(site='glycan', module='GlycanFormatConverter')
print(tools)

# For documentation:
doc = get_documentation('convert_iupac_to_wurcs', site='glycan', module='GlycanFormatConverter')
print(doc)

# For function calls:
response = call_function('convert_iupac_to_wurcs', site='glycan', module='GlycanFormatConverter', iupac_string='your_input')
print(response)
</execute_ipython>

Remember: Always specify both site='glycan' and module='MODULE_NAME' when calling glycan functions.
"""

    task_instruction = f'{glycan_prompt}\n\nPlease solve this glycan research question step by step.'
    task_instruction += AGENT_CLS_TO_INST_SUFFIX.get(agent_cls, '')

    runtime = None
    try:
        # Set config values globally (as done in original WebArena)
        llm_config = metadata['llm_config']
        if llm_config:
            config.llm = llm_config
        
        # Set agent class in config.args
        from opendevin.core.config import args
        args.agent_cls = agent_cls
        args.max_iterations = metadata['max_iterations']
        
        # Initialize and run the agent
        final_state = asyncio.run(
            main(
                task_instruction,
                fake_user_response_fn=AGENT_CLS_TO_FAKE_USER_RESPONSE_FN[agent_cls],
            )
        )
        
        # Extract response from final state
        response = "No response from agent"
        
        try:
            if final_state:
                # Try different ways to extract the response
                if hasattr(final_state, 'history') and final_state.history:
                    # Handle different types of history objects
                    if hasattr(final_state.history, 'get_events'):
                        # Standard history object with get_events method
                        agent_messages = [event for event in final_state.history.get_events() 
                                        if hasattr(event, 'source') and event.source == 'AGENT' 
                                        and hasattr(event, 'content')]
                        if agent_messages:
                            response = agent_messages[-1].content
                    elif isinstance(final_state.history, list):
                        # History is already a list of events
                        agent_messages = [event for event in final_state.history 
                                        if hasattr(event, 'source') and event.source == 'AGENT' 
                                        and hasattr(event, 'content')]
                        if agent_messages:
                            response = agent_messages[-1].content
                    else:
                        # Try to iterate directly over history
                        try:
                            agent_messages = [event for event in final_state.history 
                                            if hasattr(event, 'source') and event.source == 'AGENT' 
                                            and hasattr(event, 'content')]
                            if agent_messages:
                                response = agent_messages[-1].content
                        except (TypeError, AttributeError):
                            # Fallback to string representation
                            response = f"Agent history: {str(final_state.history)[:500]}..."
                
                # If no response from history, try other attributes
                if response == "No response from agent":
                    if hasattr(final_state, 'last_action') and final_state.last_action:
                        if hasattr(final_state.last_action, 'content'):
                            response = final_state.last_action.content
                        else:
                            response = str(final_state.last_action)
                    elif hasattr(final_state, 'agent_task') and final_state.agent_task:
                        response = str(final_state.agent_task)
                    else:
                        response = f"Agent completed with state: {type(final_state).__name__}"
            else:
                response = "Agent completed but no final state available"
        except Exception as e:
            logger.error(f"Error extracting response from final state: {e}")
            response = f"Agent completed with error extracting response: {str(e)}"
        
        logger.info(f'Final response: {response}')
        
        # Check correctness using glycan evaluation
        success = check_correctness_glycan(task, response, log_file_path)
        
        result = {
            'task_id': instance['task_id'],
            'success': success,
            'response': response,
            'question': instance['intent'],
            'expected_trajectory': instance['eval'].get('expected_trajectory', ''),
            'expected_answer': instance['eval'].get('reference_answer', '')
        }
        
        logger.info(f'Task {instance["task_id"]} completed. Success: {success}')
        
        return result
        
    except Exception as e:
        logger.error(f'Error processing instance {instance["task_id"]}: {str(e)}')
        return {
            'task_id': instance['task_id'],
            'success': False,
            'error': str(e),
            'response': '',
            'question': instance['intent']
        }
    finally:
        if runtime:
            runtime.close()
        # Clean up file handler
        for handler in logger.handlers:
            if isinstance(handler, logging.FileHandler):
                handler.close()
                logger.removeHandler(handler)


def main_eval():
    # Parse arguments
    parser = get_parser()
    parser.add_argument(
        '--glycan-tasks-file',
        type=str,
        default='/Users/jianhaonan/Desktop/API-Based-Agent/glycan/glycan_tasks.jsonl',
        help='Path to glycan tasks file'
    )
    parser.add_argument(
        '--glycan-start-task-id',
        type=int,
        default=0,
        help='Starting task ID for glycan evaluation'
    )
    parser.add_argument(
        '--glycan-num-tasks', 
        type=int,
        default=10,
        help='Number of glycan tasks to evaluate'
    )
    parser.add_argument(
        '--glycan-output-dir',
        type=str,
        default='evaluation_outputs/glycan',
        help='Output directory for glycan evaluation results'
    )
    
    args, _ = parser.parse_known_args()
    
    # Setup directories  
    eval_output_dir = args.glycan_output_dir
    os.makedirs(eval_output_dir, exist_ok=True)
    
    # Load glycan tasks
    logger.info(f'Loading glycan tasks from {args.glycan_tasks_file}')
    all_tasks = load_glycan_tasks(args.glycan_tasks_file)
    
    # Select tasks to evaluate
    start_idx = args.glycan_start_task_id
    end_idx = min(start_idx + args.glycan_num_tasks, len(all_tasks))
    tasks_to_eval = all_tasks[start_idx:end_idx]
    
    logger.info(f'Evaluating {len(tasks_to_eval)} glycan tasks (IDs {start_idx} to {end_idx-1})')
    
    # Setup metadata
    metadata = {
        'agent_class': args.agent_cls,
        'llm_config': get_llm_config_arg(args.llm_config),
        'max_iterations': args.max_iterations,
        'eval_output_dir': eval_output_dir,
        'env_vars': {
            'GLYCAN_API_MODE': 'true',
            'LOG_LEVEL': 'INFO'
        }
    }
    
    # Process tasks
    results = []
    
    for task in tqdm(tasks_to_eval, desc="Processing glycan tasks"):
        logger.info(f'Starting task {task["task_id"]}: {task["intent"][:100]}...')
        
        result = process_instance(task, metadata)
        results.append(result)
        
        # Add small delay between tasks
        time.sleep(1)
    
    # Save results
    output_file = os.path.join(eval_output_dir, f'glycan_evaluation_results_{start_idx}_{end_idx}.json')
    
    summary = {
        'metadata': {
            'agent_class': metadata['agent_class'],
            'total_tasks': len(results),
            'successful_tasks': sum(1 for r in results if r.get('success', False)),
            'start_task_id': start_idx,
            'end_task_id': end_idx - 1,
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
        },
        'results': results
    }
    
    with open(output_file, 'w') as f:
        json.dump(summary, f, indent=2)
    
    # Print summary
    success_count = summary['metadata']['successful_tasks']
    total_count = summary['metadata']['total_tasks']
    success_rate = (success_count / total_count) * 100 if total_count > 0 else 0
    
    print(f"\n=== GLYCAN EVALUATION SUMMARY ===")
    print(f"Total tasks: {total_count}")
    print(f"Successful tasks: {success_count}")
    print(f"Success rate: {success_rate:.1f}%")
    print(f"Results saved to: {output_file}")
    
    logger.info(f'Glycan evaluation completed. Results: {success_count}/{total_count} ({success_rate:.1f}%)')


if __name__ == '__main__':
    main_eval()