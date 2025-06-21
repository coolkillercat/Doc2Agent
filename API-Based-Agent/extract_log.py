def extract_agent_info(log_file_path, num_last_steps=5):
    with open(log_file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Split by step markers
    steps = content.split('Step ')
    
    extracted_info = []
    
    # Start from Step 2 as specified
    for i in range(2, len(steps)):
        step = steps[i]
        if not step.strip():
            continue
        
        # Check if step contains one of the target actions
        if any(action in step for action in ['act - **BrowseInteractiveAction**', 
                                           'act - **IPythonRunCellAction**', 
                                           'act - **MessageAction** (source=EventSource.AGENT)', 
                                           'act - AgentFinishAction']):
            
            # Split by observation to get action and content
            parts = step.split('obs - ')
            if len(parts) < 2:
                continue
                
            action_part = parts[0].strip()
            
            # Skip specific error message
            if 'CONTENT: An error occurred while processing your request. Please try again.' in action_part:
                continue
            
            # Extract content based on action type
            if 'act - **IPythonRunCellAction**' in action_part:
                # Include only THOUGHT if present
                if 'THOUGHT:' in action_part:
                    thought_content = action_part.split('THOUGHT:', 1)[1]
                    if 'CODE:' in thought_content:
                        thought_content = thought_content.split('CODE:', 1)[0].strip()
                    else:
                        thought_content = thought_content.strip()
                    extracted_info.append(f"Step {i}:\n{thought_content}\n<observation not shown>")
            
            elif 'act - **BrowseInteractiveAction**' in action_part:
                # Include THOUGHT if present
                if 'THOUGHT:' in action_part:
                    thought_content = action_part.split('THOUGHT:', 1)[1]
                    if 'CONTENT:' in thought_content:
                        thought_content = thought_content.split('CONTENT:', 1)[0].strip()
                    else:
                        thought_content = thought_content.strip()
                    extracted_info.append(f"Step {i}:\n{thought_content}\n<observation not shown>")
            
            elif 'act - **MessageAction** (source=EventSource.AGENT)' in action_part:
                if 'CONTENT:' in action_part:
                    message_content = action_part.split('CONTENT:', 1)[1].strip()
                    extracted_info.append(f"Step {i}:\n{message_content}")
            
            elif 'act - AgentFinishAction' in action_part:
                if 'thought=' in action_part:
                    thought_content = action_part.split('thought=', 1)[1].strip()
                    # Remove any trailing content after the thought
                    if "'" in thought_content:
                        thought_content = thought_content.split("'", 2)[1]
                    extracted_info.append(f"Step {i}:\n{thought_content}")
    
    # Return only the specified number of most recent steps
    if num_last_steps > 0 and len(extracted_info) > num_last_steps:
        extracted_info = extracted_info[-num_last_steps:]
    
    return '\n'.join(extracted_info)


if __name__ == "__main__":
    log_file_path = "analyse_logs/HybridAgent/logs/instance_393.log"
    extracted_info = extract_agent_info(log_file_path, 5)
    print(extracted_info)