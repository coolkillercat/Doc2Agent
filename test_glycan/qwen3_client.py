from qwen_agent.agents import Assistant
import json
import os
from pathlib import Path

# Define LLM
llm_cfg = {
    

    # Use the endpoint provided by Alibaba Model Studio:
    # 'model_type': 'qwen_dashscope',
    # 'api_key': os.getenv('DASHSCOPE_API_KEY'),

    # Use a custom endpoint compatible with OpenAI API:
    # 'model': 'Qwen3:32b',
    # 'model_server': 'http://localhost:11434/v1',  # ollama use

    # VLLM deploy script: vllm serve Qwen/Qwen3-32B --enable-reasoning --reasoning-parser deepseek_r1
    # 'model': 'Qwen/Qwen3-32B-FP8',
    # 'model_server': 'https://oeo1xa92vpubru-8000.proxy.runpod.net/v1', # vllm usage
    # 'api_key': 'sk-IrR7Bwxtin0haWagUnPrBgq5PurnUz86',

    # JAN server
    'model': 'Menlo:Jan-nano-gguf:jan-nano-4b-Q8_0.gguf',
    'model_server': 'http://localhost:1337',
    'api_key': '123',
    # Other parameters:
    # 'generate_cfg': {
    #         # Add: When the response content is `<think>this is the thought</think>this is the answer;
    #         # Do not add: When the response has been separated by reasoning_content and content.
    #         'thought_in_content': True,
    #     },
}

# Define Tools
# tools = [
#     {'mcpServers': {  # You can specify the MCP configuration file
#         'my_custom_mcp': {
#             "type": "steamable-http",
#             "url": "http://127.0.0.1:8000/mcp/"
#             },
#         }   
#     },
#   'code_interpreter',  # Built-in tools
# ]

tools = [
    'code_interpreter',
    {'mcpServers': {  # You can specify the MCP configuration file
            "my_custom_mcp": {
            "command": "python",
            "args": [
                "test_glycan/server.py"
                ]
            }
    },
    }
]

# Define Agent
bot = Assistant(llm=llm_cfg, function_list=tools)

def load_tasks_from_jsonl(file_path):
    """Load tasks from JSONL file"""
    tasks = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if line:
                try:
                    task = json.loads(line)
                    task['id'] = line_num  # Add line number as task ID
                    tasks.append(task)
                except json.JSONDecodeError as e:
                    print(f"Error parsing line {line_num}: {e}")
    return tasks

def format_conversation_log(conversation_history):
    """Format the conversation history for logging"""
    log_content = ""
    for i, message in enumerate(conversation_history, 1):
        role = message.get('role', 'unknown')
        content = message.get('content', '')
        log_content += f"\n{'='*80}\n"
        log_content += f"Round {(i+1)//2} - {role.upper()}\n"
        log_content += f"{'='*80}\n"
        log_content += f"{content}\n"
    return log_content

def save_conversation_to_log(folder, task_id, question, conversation_history, rounds_completed, finished_early):
    """Save entire conversation to log file"""
    # Create folder if it doesn't exist
    Path(folder).mkdir(parents=True, exist_ok=True)
    
    # Create log file path
    log_file = Path(folder) / f"task_{task_id}.log"
    
    # Write conversation to log file
    with open(log_file, 'w', encoding='utf-8') as f:
        f.write(f"Task ID: {task_id}\n")
        f.write(f"Original Question: {question}\n")
        f.write(f"Rounds Completed: {rounds_completed}\n")
        f.write(f"Finished Early: {finished_early}\n")
        f.write("=" * 80 + "\n")
        f.write("CONVERSATION HISTORY\n")
        f.write("=" * 80 + "\n")
        
        # Format and write conversation
        f.write(format_conversation_log(conversation_history))
    
    print(f"Saved conversation for task {task_id} to {log_file} ({rounds_completed} rounds, finished_early={finished_early})")

def check_finish_token(response_text):
    """Check if the response contains the <FINISH> token"""
    return '<FINISH>' in str(response_text)

def conduct_conversation(task_id, question, max_rounds=5):
    """Conduct a multi-round conversation for a single task"""
    conversation_history = []
    
    # Start with the initial question
    conversation_history.append({'role': 'user', 'content': question})
    
    for round_num in range(1, max_rounds + 1):
        print(f"  Round {round_num}/{max_rounds}")
        
        try:
            # Get current messages for this conversation
            current_messages = conversation_history.copy()
            
            # Get assistant response
            response = None
            for responses in bot.run(messages=current_messages):
                response = responses
            
            # Add assistant response to conversation history
            assistant_content = str(response) if response else "No response received"
            conversation_history.append({'role': 'assistant', 'content': assistant_content})
            
            # Check if assistant wants to finish
            if check_finish_token(assistant_content):
                print(f"  Assistant finished early with <FINISH> token in round {round_num}")
                return conversation_history, round_num, True
            
            # If this is not the last round, add a "continue" message
            if round_num < max_rounds:
                continue_message = "Please continue with your analysis until you think you have finished. Output your final answer between <FINISH></FINISH> tag."
                conversation_history.append({'role': 'user', 'content': continue_message})
                print(f"  Added continue message for next round")
            
        except Exception as e:
            error_message = f"Error in round {round_num}: {str(e)}"
            print(f"  {error_message}")
            conversation_history.append({'role': 'assistant', 'content': error_message})
            return conversation_history, round_num, False
    
    print(f"  Completed maximum {max_rounds} rounds")
    return conversation_history, max_rounds, False

def main():
    # Load tasks from JSONL file
    tasks = load_tasks_from_jsonl('glycan_tasks.jsonl')
    print(f"Loaded {len(tasks)} tasks from glycan_tasks.jsonl")
    
    # Create output folder
    output_folder = "workspace"
    
    # Process each task
    for task in tasks:
        task_id = task['id']
        question = task['question']
        
        print(f"\nProcessing Task {task_id}...")
        print(f"Question: {question[:100]}..." if len(question) > 100 else f"Question: {question}")
        
        try:
            # Conduct multi-round conversation
            conversation_history, rounds_completed, finished_early = conduct_conversation(task_id, question)
            
            # Save conversation to log file
            save_conversation_to_log(output_folder, task_id, question, conversation_history, rounds_completed, finished_early)
            
        except Exception as e:
            error_message = f"Error processing task {task_id}: {str(e)}"
            print(error_message)
            # Save error as a simple conversation
            error_conversation = [
                {'role': 'user', 'content': question},
                {'role': 'assistant', 'content': error_message}
            ]
            save_conversation_to_log(output_folder, task_id, question, error_conversation, 1, False)

if __name__ == "__main__":
    main()


