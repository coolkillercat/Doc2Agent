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

sys.path.append('/API-Based-Agent/evaluation/webarena/webarena')
sys.path.append('/API-Based-Agent/evaluation/webarena/webarena/evaluation_harness')
from utils import check_correctness, get_initial_prompt_from_task, get_tests
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
    msg = (
        'Please continue working on the task on whatever approach you think is suitable.\n'
        #'IMPORTANT: YOU SHOULD NEVER ASK FOR HUMAN HELP OR USE THE INTERNET TO SOLVE THIS TASK.\n'
        #'HINT: use the function get_api_documentation(api) to retrieve documentation of APIs that are useful to solving the task.'
    )
    return (
        msg
        + '\nWhen you think you successfully finished the task, first respond with `Finish[answer]` where you include *only* your answer to the questionin `[]` if the user asks for an answer, make sure you should only include the answer to the question but not any additional explanation, details, or commentary unless specifically requested.'
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


def process_instance(task, agent_class, metadata, reset_logger: bool = True):
    # create process-specific workspace dir
    # we will create a workspace directory for EACH process
    # so that different agent don't interfere with each other.
    workspace_mount_path = config.workspace_mount_path
    pathlib.Path(workspace_mount_path).mkdir(parents=True, exist_ok=True)

    # Setup the logger properly, so you can run multi-processing to parallelize the evaluation
    eval_output_dir = metadata['eval_output_dir']
    task_id = task['task_id']

    # Set up the workspace for shopping tasks and copy necessary files
    if 'shopping' in task.get('sites', []):
        curr_dir = os.path.dirname(os.path.abspath(__file__))
        print(f"Setting up shopping tools and API documentation for task {task_id}")
        
        # Create directory structure for shopping tools in the agent's workspace
        api_dir = os.path.join(workspace_mount_path, 'api')
        shopping_dir = os.path.join(api_dir, 'shopping')
        tools_dir = os.path.join(shopping_dir, 'tools')
        
        os.makedirs(tools_dir, exist_ok=True)
        print(f"Created directory structure: {tools_dir}")
        
        # Copy shopping.txt
        source_doc = os.path.join(curr_dir, 'api', 'shopping', 'shopping.txt')
        target_doc = os.path.join(shopping_dir, 'shopping.txt')
        
        if os.path.exists(source_doc):
            shutil.copy(source_doc, target_doc)
            print(f"Copied shopping.txt to {target_doc}")
            # Verify the file was copied correctly
            if os.path.exists(target_doc):
                print(f"Verified shopping.txt exists at {target_doc}")
            else:
                print(f"ERROR: Failed to copy shopping.txt to {target_doc}")
        else:
            print(f"WARNING: Source documentation {source_doc} not found")
        
        # Copy all tool files
        source_tools_dir = os.path.join(curr_dir, 'api', 'shopping', 'tools')
        
        if os.path.exists(source_tools_dir):
            tool_files = [f for f in os.listdir(source_tools_dir) if f.endswith('.py')]
            copied_count = 0
            
            for tool_file in tool_files:
                source_tool = os.path.join(source_tools_dir, tool_file)
                target_tool = os.path.join(tools_dir, tool_file)
                shutil.copy(source_tool, target_tool)
                
                # Verify file was copied
                if os.path.exists(target_tool):
                    copied_count += 1
                else:
                    print(f"ERROR: Failed to copy tool {tool_file}")
            
            print(f"Copied {copied_count}/{len(tool_files)} tools to {tools_dir}")
        else:
            print(f"WARNING: Source tools directory {source_tools_dir} not found")
        
        # Create __init__.py files
        init_api = os.path.join(api_dir, '__init__.py')
        init_shopping = os.path.join(shopping_dir, '__init__.py')
        init_tools = os.path.join(tools_dir, '__init__.py')
        
        with open(init_api, 'w') as f:
            f.write('# API modules\n')
        with open(init_shopping, 'w') as f:
            f.write('# Shopping API module\n')
        with open(init_tools, 'w') as f:
            f.write('# Shopping API tools module\n')
        
        # Verify init files exist
        for init_file in [init_api, init_shopping, init_tools]:
            if os.path.exists(init_file):
                print(f"Created {init_file}")
            else:
                print(f"ERROR: Failed to create {init_file}")
        
        # Now also verify that the workspace/utils.py file contains the required functions
        workspace_utils = os.path.join(workspace_mount_path, 'utils.py')
        
        # NEW CODE: Copy our custom utils.py file to override the default one
        custom_utils_path = "/API-Based-Agent/custom_utils.py"
        if os.path.exists(custom_utils_path):
            shutil.copy(custom_utils_path, workspace_utils)
            print(f"Successfully replaced utils.py with custom version from {custom_utils_path}")
        else:
            print(f"Warning: Custom utils.py file not found at {custom_utils_path}")
        
        # Continue with validation (it will now check our custom file)
        if os.path.exists(workspace_utils):
            with open(workspace_utils, 'r') as f:
                utils_content = f.read()
                
            for func_name in ['list_tools', 'get_documentation', 'call_function', 'call_direct']:
                if f"def {func_name}" in utils_content:
                    print(f"Utils function {func_name} found in workspace")
                else:
                    print(f"ERROR: Utils function {func_name} NOT found in workspace")
        else:
            print(f"ERROR: utils.py not found in workspace at {workspace_utils}")
        
        print(f"Workspace setup complete for shopping task")

    # Set up the workspace for wikipedia tasks
    if 'wikipedia' in task.get('sites', []):
        curr_dir = os.path.dirname(os.path.abspath(__file__))
        print(f"Setting up Wikipedia tools and API documentation for task {task_id}")
        
        # Create directory structure for Wikipedia tools in the agent's workspace
        api_dir = os.path.join(workspace_mount_path, 'api')
        wikipedia_dir = os.path.join(api_dir, 'wikipedia')
        tools_dir = os.path.join(wikipedia_dir, 'tools')
        
        os.makedirs(tools_dir, exist_ok=True)
        print(f"Created directory structure: {tools_dir}")
        
        # Copy wikipedia.txt
        source_doc = os.path.join(curr_dir, 'api', 'wikipedia', 'wikipedia.txt')
        target_doc = os.path.join(wikipedia_dir, 'wikipedia.txt')
        
        if os.path.exists(source_doc):
            shutil.copy(source_doc, target_doc)
            print(f"Copied wikipedia.txt to {target_doc}")
            # Verify the file was copied correctly
            if os.path.exists(target_doc):
                print(f"Verified wikipedia.txt exists at {target_doc}")
            else:
                print(f"ERROR: Failed to copy wikipedia.txt to {target_doc}")
        else:
            print(f"WARNING: Source documentation {source_doc} not found")
        
        # Copy all tool files
        source_tools_dir = os.path.join(curr_dir, 'api', 'wikipedia', 'tools')
        
        if os.path.exists(source_tools_dir):
            # If tools directory doesn't exist, copy Python files directly
            if not os.path.exists(source_tools_dir):
                source_tools_dir = os.path.join(curr_dir, 'api', 'wikipedia')
                tool_files = [f for f in os.listdir(source_tools_dir) if f.endswith('.py') and f != '__init__.py']
            else:
                tool_files = [f for f in os.listdir(source_tools_dir) if f.endswith('.py')]
            
            copied_count = 0
            
            for tool_file in tool_files:
                source_tool = os.path.join(source_tools_dir, tool_file)
                target_tool = os.path.join(tools_dir, tool_file)
                shutil.copy(source_tool, target_tool)
                
                # Verify file was copied
                if os.path.exists(target_tool):
                    copied_count += 1
                else:
                    print(f"ERROR: Failed to copy tool {tool_file}")
            
            print(f"Copied {copied_count}/{len(tool_files)} tools to {tools_dir}")
        else:
            print(f"WARNING: Source tools directory {source_tools_dir} not found")
        
        # Create __init__.py files if not exists
        init_api = os.path.join(api_dir, '__init__.py')
        init_wikipedia = os.path.join(wikipedia_dir, '__init__.py')
        init_tools = os.path.join(tools_dir, '__init__.py')
        
        if not os.path.exists(init_api):
            with open(init_api, 'w') as f:
                f.write('# API modules\n')
        
        with open(init_wikipedia, 'w') as f:
            f.write('# Wikipedia API module\n')
        with open(init_tools, 'w') as f:
            f.write('# Wikipedia API tools module\n')
        
        # Verify init files exist
        for init_file in [init_api, init_wikipedia, init_tools]:
            if os.path.exists(init_file):
                print(f"Created {init_file}")
            else:
                print(f"ERROR: Failed to create {init_file}")
    
    # Set up the workspace for map tasks
    if 'map' in task.get('sites', []):
        curr_dir = os.path.dirname(os.path.abspath(__file__))
        print(f"Setting up Map tools and API documentation for task {task_id}")
        
        # Create directory structure for Map tools in the agent's workspace
        api_dir = os.path.join(workspace_mount_path, 'api')
        map_dir = os.path.join(api_dir, 'map')
        tools_dir = os.path.join(map_dir, 'tools')
        
        os.makedirs(tools_dir, exist_ok=True)
        print(f"Created directory structure: {tools_dir}")
        
        # Copy map.txt
        source_doc = os.path.join(curr_dir, 'api', 'map', 'map.txt')
        target_doc = os.path.join(map_dir, 'map.txt')
        
        if os.path.exists(source_doc):
            shutil.copy(source_doc, target_doc)
            print(f"Copied map.txt to {target_doc}")
            # Verify the file was copied correctly
            if os.path.exists(target_doc):
                print(f"Verified map.txt exists at {target_doc}")
            else:
                print(f"ERROR: Failed to copy map.txt to {target_doc}")
        else:
            print(f"WARNING: Source documentation {source_doc} not found")
        
        # Copy all tool files
        source_tools_dir = os.path.join(curr_dir, 'api', 'map', 'tools')
        
        if os.path.exists(source_tools_dir):
            # If tools directory doesn't exist, copy Python files directly
            if not os.path.exists(source_tools_dir):
                source_tools_dir = os.path.join(curr_dir, 'api', 'map')
                tool_files = [f for f in os.listdir(source_tools_dir) if f.endswith('.py') and f != '__init__.py']
            else:
                tool_files = [f for f in os.listdir(source_tools_dir) if f.endswith('.py')]
            
            copied_count = 0
            
            for tool_file in tool_files:
                source_tool = os.path.join(source_tools_dir, tool_file)
                target_tool = os.path.join(tools_dir, tool_file)
                shutil.copy(source_tool, target_tool)
                
                # Verify file was copied
                if os.path.exists(target_tool):
                    copied_count += 1
                else:
                    print(f"ERROR: Failed to copy tool {tool_file}")
            
            print(f"Copied {copied_count}/{len(tool_files)} tools to {tools_dir}")
        else:
            print(f"WARNING: Source tools directory {source_tools_dir} not found")
        
        # Create __init__.py files if not exists
        init_api = os.path.join(api_dir, '__init__.py')
        init_map = os.path.join(map_dir, '__init__.py')
        init_tools = os.path.join(tools_dir, '__init__.py')
        
        if not os.path.exists(init_api):
            with open(init_api, 'w') as f:
                f.write('# API modules\n')
        
        with open(init_map, 'w') as f:
            f.write('# Map API module\n')
        with open(init_tools, 'w') as f:
            f.write('# Map API tools module\n')
        
        # Verify init files exist
        for init_file in [init_api, init_map, init_tools]:
            if os.path.exists(init_file):
                print(f"Created {init_file}")
            else:
                print(f"ERROR: Failed to create {init_file}")
        
    # Now also verify that the workspace/utils.py file contains the required functions
    workspace_utils = os.path.join(workspace_mount_path, 'utils.py')
    
    # NEW CODE: Copy our custom utils.py file to override the default one
    custom_utils_path = "/API-Based-Agent/custom_utils.py"
    if os.path.exists(custom_utils_path):
        shutil.copy(custom_utils_path, workspace_utils)
        print(f"Successfully replaced utils.py with custom version from {custom_utils_path}")
    else:
        print(f"Warning: Custom utils.py file not found at {custom_utils_path}")
    
    # Continue with validation (it will now check our custom file)
    if os.path.exists(workspace_utils):
        with open(workspace_utils, 'r') as f:
            utils_content = f.read()
            
        for func_name in ['list_tools', 'get_documentation', 'call_function', 'call_direct']:
            if f"def {func_name}" in utils_content:
                print(f"Utils function {func_name} found in workspace")
            else:
                print(f"ERROR: Utils function {func_name} NOT found in workspace")
    else:
        print(f"ERROR: utils.py not found in workspace at {workspace_utils}")
    
    print(f"Workspace setup complete for task")

    if reset_logger:
        # Set up logger
        log_file = os.path.join(eval_output_dir, 'logs', f'instance_{task_id}.log')
        # Remove all existing handlers from logger
        for handler in logger.handlers[:]:
            logger.removeHandler(handler)
        # add back the console handler to print ONE line
        logger.addHandler(get_console_handler())
        logger.info(
            f'Starting evaluation for instance {task_id}.\nHint: run "tail -f {log_file}" to see live logs in a separate shell'
        )
        # Remove all existing handlers from logger
        for handler in logger.handlers[:]:
            logger.removeHandler(handler)
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(
            logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        )
        logger.addHandler(file_handler)
    logger.info(f'Process-specific workspace mounted at {workspace_mount_path}')

    # Prepare instruction
    instruction = get_initial_prompt_from_task(task)
    instruction += 'IMPORTANT: You should ONLY interact with the environment provided to you AND NEVER ASK FOR HUMAN HELP.\n'
    instruction += AGENT_CLS_TO_INST_SUFFIX.get(agent_class, '')
    logger.info(f'Instruction:\n{instruction}', extra={'msg_type': 'OBSERVATION'})

    # Here's how you can run the agent (similar to the `main` function) and get the final task state
    state: State = asyncio.run(
        main(
            instruction,
            fake_user_response_fn=AGENT_CLS_TO_FAKE_USER_RESPONSE_FN.get(agent_class),
        )
    )
    if state is None:
        raise ValueError('State should not be None.')

    output_log = ''
    for i, (act, obs) in enumerate(state.history):
        output_log += f"Step {i}:\nact - {act}\nobs - {obs}\n\n"
    log_file = os.path.join(eval_output_dir, 'logs', f'instance_{task_id}.log')
    with open(log_file, 'w') as f: f.write(output_log)

    model_answer_raw = ''
    model_answer_last = ''
    for act, obs in state.history:
        if isinstance(act, MessageAction) and act.source == 'agent':
            if (
                act.content.strip() != ''
                and act.content.strip() != 'Too many errors encountered. Task failed.'
            ):
                model_answer_raw += f"{act.content}\n"
                model_answer_last = f"{act.content}\n"
        elif act.source == 'agent':
            if (
                act.thought.strip() != ''
                and act.thought.strip()
                != 'Too many errors encountered. Task failed.'
            ):
                model_answer_last = f"{act.thought}\n"
                model_answer_raw += f"{act.thought}\n"
                model_answer_raw += f"{obs}\n"
    # attempt to parse model_answer
    correct = check_correctness(task, model_answer_raw, log_file)
    correct_all_history = check_correctness(task, model_answer_raw, log_file, check_all_history=True)
    metrics = state.metrics.get() if state.metrics else None
    logger.info(f'Raw Answer: {model_answer_raw} | Correct: {correct} | Correct (All History): {correct_all_history}')
    # Save the output for last URL check
    output = {
        'task_id': task_id,
        'raw': model_answer_last,  # Only contains the last agent response
        'answer_id': 'None',
        'model_id': metadata['model_name'],
        'metadata': metadata,
        'metrics': metrics,
        'error': state.error if state and state.error else None,
        'correct': correct,
    }
    
    # Save the output for all history URL check
    # model_answer_raw contains the full history of agent responses and observations
    output_all_history = {
        'task_id': task_id,
        'raw': model_answer_last,  # Use the full history including agent thoughts and observations
        'answer_id': 'None',
        'model_id': metadata['model_name'],
        'metadata': metadata,
        'metrics': metrics,
        'error': state.error if state and state.error else None,
        'correct': correct_all_history,
    }
    
    return output, output_all_history


if __name__ == '__main__':
    parser = get_parser()
    parser.add_argument(
        '--start_task_id',
        type=int,
        help='which task_id to start from',
        default=132,
    )
    args, _ = parser.parse_known_args()
    if args.directory:
        config.workspace_base = os.path.abspath(args.directory)
        print(f'Setting workspace base to {config.workspace_base}')
    # Check https://github.com/OpenDevin/OpenDevin/blob/main/evaluation/swe_bench/README.md#configure-opendevin-and-your-llm
    # for details of how to set `llm_config`
    if args.llm_config:
        specified_llm_config = get_llm_config_arg(args.llm_config)
        if specified_llm_config:
            config.llm = specified_llm_config
    logger.info(f'Config for evaluation: {config}')
    agent_class = args.agent_cls
    assert (
        agent_class in AGENT_CLS_TO_FAKE_USER_RESPONSE_FN
    ), f'Unsupported agent class: {agent_class}'
    model_name = config.llm.model.split('/')[-1]
    max_iterations = args.max_iterations
    eval_note = ''
    if args.eval_note is not None:
        eval_note += '_N_' + args.eval_note
    eval_output_dir = os.path.join(
        args.eval_output_dir,
        agent_class,
        model_name + '_maxiter_' + str(max_iterations) + eval_note,
    )
    pathlib.Path(eval_output_dir).mkdir(parents=True, exist_ok=True)
    pathlib.Path(os.path.join(eval_output_dir, 'logs')).mkdir(
        parents=True, exist_ok=True
    )
    logger.info(f'Using evaluation output directory: {eval_output_dir}')
    logger.info('Evaluating Webarena tests')
    workspace_mount_path = config.workspace_mount_path
    pathlib.Path(workspace_mount_path).mkdir(parents=True, exist_ok=True)
    tests = get_tests(args.start_task_id)
    print(f'len(tests) is {len(tests)}')
    # TEST METADATA
    metadata = {
        'agent_class': agent_class,
        'model_name': model_name,
        'max_iterations': max_iterations,
        'eval_output_dir': eval_output_dir,
        'start_time': time.strftime('%Y-%m-%d %H:%M:%S'),
        # get the commit id of current repo for reproduciblity
        'git_commit': subprocess.check_output(['git', 'rev-parse', 'HEAD'])
        .decode('utf-8')
        .strip(),
    }
    logger.info(f'Metadata: {metadata}')
    with open(os.path.join(eval_output_dir, 'metadata.json'), 'w') as f:
        json.dump(metadata, f)
    # LIMIT EVALUATION
    eval_n_limit = args.eval_n_limit
    if eval_n_limit:
        tests = tests[:eval_n_limit]
        logger.info(
            f'Limiting evaluation to a total of first {eval_n_limit} instances. ({len(tests)})'
        )
    if tests[0]['sites'] == ['reddit', 'gitlab'] or tests[0]['sites'] == [
        'gitlab',
        'reddit',
    ]:
        output_file = os.path.join(
            eval_output_dir, f'output_gitlab_reddit_{model_name}.jsonl'
        )
    elif tests[0]['sites'] == ['map', 'wikipedia'] or tests[0]['sites'] == [
        'wikipedia',
        'map',
    ]:
        output_file = os.path.join(
            eval_output_dir, f'output_map_wikipedia_{model_name}.jsonl'
        )
    elif tests[0]['sites'] == ['map', 'shopping_admin'] or tests[0]['sites'] == [
        'shopping_admin',
        'map',
    ]:
        output_file = os.path.join(
            eval_output_dir, f'output_map_shopping_admin_{model_name}.jsonl'
        )
    elif tests[0]['sites'] == ['gitlab', 'wikipedia'] or tests[0]['sites'] == [
        'wikipedia',
        'gitlab',
    ]:
        output_file = os.path.join(
            eval_output_dir, f'output_gitlab_wikipedia_{model_name}.jsonl'
        )
    elif tests[0]['sites'] == ['shopping', 'reddit'] or tests[0]['sites'] == [
        'shopping',
        'reddit',
    ]:
        output_file = os.path.join(
            eval_output_dir, f'output_shopping_reddit_{model_name}.jsonl'
        )
    elif tests[0]['sites'] == ['shopping_admin']:
        output_file = os.path.join(
            eval_output_dir, f'output_shopping_admin_{model_name}.jsonl'
        )
    elif tests[0]['sites'] == ['shopping']:
        output_file = os.path.join(
            eval_output_dir, f'output_shopping_{model_name}.jsonl'
        )
    elif tests[0]['sites'] == ['gitlab']:
        output_file = os.path.join(
            eval_output_dir, f'output_gitlab_{model_name}.jsonl'
        )
    elif tests[0]['sites'] == ['reddit']:
        output_file = os.path.join(
            eval_output_dir, f'output_reddit_{model_name}.jsonl'
        )
    elif tests[0]['sites'] == ['map']:
        output_file = os.path.join(
            eval_output_dir, f'output_map_{model_name}.jsonl'
        )
    else:
        assert 1 == 2
        output_file = os.path.join(eval_output_dir, f'output_{model_name}.jsonl')
    logger.info(f'Writing evaluation output to {output_file}')
    finished_task_ids = set()
    if os.path.exists(output_file):
        try:
            with open(output_file, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line:  # Skip empty lines
                        try:
                            task = json.loads(line)
                            finished_task_ids.add(task['task_id'])
                        except json.JSONDecodeError as e:
                            logger.warning(f'Failed to parse line in output file: {e}')
                            continue
            logger.warning(
                f'Output file {output_file} already exists. Loaded {len(finished_task_ids)} finished instances.'
            )
        except Exception as e:
            logger.error(f'Error reading output file: {e}')
            # If there's an error reading the file, we'll start fresh
            finished_task_ids = set()
    
    output_fp = open(output_file, 'a')
    
    # Create site-specific all-history output file based on the site being evaluated
    site_prefix = ""
    if tests[0]['sites'] == ['reddit', 'gitlab'] or tests[0]['sites'] == ['gitlab', 'reddit']:
        site_prefix = "gitlab_reddit"
    elif tests[0]['sites'] == ['map', 'wikipedia'] or tests[0]['sites'] == ['wikipedia', 'map']:
        site_prefix = "map_wikipedia"
    elif tests[0]['sites'] == ['map', 'shopping_admin'] or tests[0]['sites'] == ['shopping_admin', 'map']:
        site_prefix = "map_shopping_admin"
    elif tests[0]['sites'] == ['gitlab', 'wikipedia'] or tests[0]['sites'] == ['wikipedia', 'gitlab']:
        site_prefix = "gitlab_wikipedia"
    elif tests[0]['sites'] == ['shopping', 'reddit'] or tests[0]['sites'] == ['shopping', 'reddit']:
        site_prefix = "shopping_reddit"
    elif tests[0]['sites'] == ['shopping_admin']:
        site_prefix = "shopping_admin"
    elif tests[0]['sites'] == ['shopping']:
        site_prefix = "shopping"
    elif tests[0]['sites'] == ['gitlab']:
        site_prefix = "gitlab"
    elif tests[0]['sites'] == ['reddit']:
        site_prefix = "reddit"
    elif tests[0]['sites'] == ['map']:
        site_prefix = "map"
    else:
        site_prefix = "unknown"
    
    all_history_output_file = os.path.join(eval_output_dir, f'allhistory_output_{site_prefix}_{model_name}.jsonl')
    logger.info(f"Writing all-history evaluation output to {all_history_output_file}")
    output_fp_all_history = open(all_history_output_file, 'a')
    
    logger.info(
        f'Evaluation started with Agent {agent_class}, model {model_name}, max iterations {max_iterations}.'
    )
    # =============================================
    # filter out finished instances
    new_tests = []
    for task in tests:
        task_id = task['task_id']
        if task_id in finished_task_ids:
            logger.info(f'Skipping instance {task_id} as it is already finished.')
            continue
        new_tests.append(task)
    finished_task_number = len(finished_task_ids)
    tests = new_tests
    logger.info(
        f'Finished instances: {finished_task_number}, Remaining instances: {len(tests)}'
    )

    # =============================================
    pbar = tqdm(total=len(tests))
    num_workers = args.eval_num_workers
    logger.info(f'Using {num_workers} workers for evaluation.')
    for task in tests:
        if True:
            pbar.update(1)
            output, output_all_history = process_instance(
                task,
                agent_class,
                metadata,
                reset_logger=bool(num_workers > 1),
            )
            pbar.set_description(f'Instance {output["task_id"]}')
            logger.info(
                f'Finished evaluation for instance {output["task_id"]}: correctness - {output["correct"]}; correctness (all history) - {output_all_history["correct"]}; answer - {output["raw"]}'
            )
            output_fp.write(json.dumps(output) + '\n')
            output_fp_all_history.write(json.dumps(output_all_history) + '\n')
            output_fp.flush()
            output_fp_all_history.flush()
            finished_task_ids.add(output['task_id'])
        else:
            logger.info(f"task failed for task_id {task['task_id']} - {e}")
    output_fp.close()
    output_fp_all_history.close()
