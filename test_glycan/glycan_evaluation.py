import os
import json
import openai
import re
from datetime import datetime
from typing import Dict, Any, List
import logging

logger = logging.getLogger(__name__)

def parse_conversation_log(log_content: str) -> Dict[str, Any]:
    """
    Parse our conversation log format to extract metadata and final response.
    
    Args:
        log_content: Complete log file content
        
    Returns:
        Dictionary with parsed information
    """
    result = {
        'task_id': None,
        'original_question': '',
        'rounds_completed': 0,
        'finished_early': False,
        'conversation_history': [],
        'final_assistant_response': ''
    }
    
    lines = log_content.split('\n')
    
    # Parse header information
    for line in lines[:10]:  # Check first 10 lines for metadata
        if line.startswith('Task ID:'):
            result['task_id'] = line.split('Task ID:', 1)[1].strip()
        elif line.startswith('Original Question:'):
            result['original_question'] = line.split('Original Question:', 1)[1].strip()
        elif line.startswith('Rounds Completed:'):
            result['rounds_completed'] = int(line.split('Rounds Completed:', 1)[1].strip())
        elif line.startswith('Finished Early:'):
            result['finished_early'] = line.split('Finished Early:', 1)[1].strip().lower() == 'true'
    
    # Parse conversation history
    current_message = {'role': '', 'content': ''}
    capturing_content = False
    
    for line in lines:
        if '- USER' in line and '=' in line:
            # Save previous message if exists
            if current_message['role'] and current_message['content'].strip():
                result['conversation_history'].append(current_message.copy())
            # Start new user message
            current_message = {'role': 'user', 'content': ''}
            capturing_content = True
        elif '- ASSISTANT' in line and '=' in line:
            # Save previous message if exists
            if current_message['role'] and current_message['content'].strip():
                result['conversation_history'].append(current_message.copy())
            # Start new assistant message
            current_message = {'role': 'assistant', 'content': ''}
            capturing_content = True
        elif capturing_content and line.strip() and not line.startswith('='):
            # Add content to current message
            if current_message['content']:
                current_message['content'] += '\n' + line
            else:
                current_message['content'] = line
    
    # Save final message
    if current_message['role'] and current_message['content'].strip():
        result['conversation_history'].append(current_message)
    
    # Extract final assistant response
    assistant_responses = [msg['content'] for msg in result['conversation_history'] if msg['role'] == 'assistant']
    if assistant_responses:
        result['final_assistant_response'] = assistant_responses[-1]
    
    return result

def load_task_from_jsonl(task_id: int, jsonl_file: str = 'glycan_tasks.jsonl') -> Dict[str, Any]:
    """
    Load a specific task from the JSONL file.
    
    Args:
        task_id: Task ID (line number)
        jsonl_file: Path to JSONL file
        
    Returns:
        Task dictionary
    """
    try:
        with open(jsonl_file, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                if line_num == task_id:
                    task = json.loads(line.strip())
                    task['id'] = task_id
                    return task
    except Exception as e:
        logger.error(f"Error loading task {task_id} from {jsonl_file}: {str(e)}")
    
    return {}

def create_glycan_evaluation_prompt(question: str, expected_trajectory: str, expected_answer: str, 
                                   agent_log: str, agent_final_response: str) -> str:
    """
    Create comprehensive evaluation prompt for GPT-4o to evaluate glycan task performance.
    
    Args:
        question: The original research question
        expected_trajectory: Expected sequence of API calls
        expected_answer: Expected final answer
        agent_log: Complete interaction log
        agent_final_response: Agent's final response
        
    Returns:
        Formatted evaluation prompt for GPT-4o
    """
    return f"""You are an expert glycomics researcher evaluating an AI agent's performance on a glycan research task.

**RESEARCH QUESTION:**
{question}

**EXPECTED API TRAJECTORY:**
{expected_trajectory}

**EXPECTED ANSWER:**
{expected_answer}

**AGENT'S COMPLETE INTERACTION LOG:**
{agent_log}

**AGENT'S FINAL RESPONSE:**
{agent_final_response}

**EVALUATION CRITERIA:**
Evaluate whether the agent successfully completed the research task by considering ALL of the following aspects holistically:

1. **API Usage Appropriateness**: Did the agent use the right sequence of glycan APIs to address the research question? The agent should have used APIs that align with the expected trajectory, though exact matching is not required if the alternative approach is scientifically valid.

2. **Scientific Accuracy**: Are the obtained results scientifically correct and meaningful for glycomics research? Consider:
   - Correct interpretation of glycan structures and formats (WURCS, IUPAC, etc.)
   - Proper understanding of protein-glycan interactions
   - Accurate use of database cross-references
   - Valid biochemical reasoning

3. **Completeness**: Did the agent obtain all the information requested in the question? Check if:
   - All parts of multi-part questions were addressed
   - Required data fields were retrieved
   - Cross-references were properly resolved

4. **Data Integration**: If multiple API calls were needed, did the agent properly combine and interpret the results? Look for:
   - Logical workflow progression
   - Proper data passing between API calls
   - Meaningful synthesis of results from different sources

5. **Research Workflow**: Did the agent follow a logical research workflow consistent with glycomics best practices?
   - Started with appropriate tool discovery
   - Used documentation when needed
   - Handled errors gracefully
   - Drew appropriate conclusions

**IMPORTANT GUIDELINES:**
- Focus on whether the agent achieved the research objective, not just exact trajectory matching
- Consider that there may be multiple valid approaches to solve the same research question
- Evaluate the scientific validity of the final answer in the context of glycomics
- Account for API errors or limitations that may have affected the agent's performance
- Consider partial credit for agents that made significant progress but didn't fully complete the task
- Be especially attentive to:
  * Correct format conversions (e.g., IUPAC to WURCS)
  * Proper interpretation of molecular structures
  * Valid cross-database references
  * Meaningful biological insights

**RESPONSE FORMAT:**
Provide your evaluation in this exact format:

DECISION: [SUCCESS/FAILURE]

REASONING: [Detailed explanation of your decision, covering the key evaluation criteria and specific observations from the agent's performance. Include specific examples from the agent's log that support your decision.]

CRITICAL_ISSUES: [List any major problems that led to failure, or "None" if successful]

SCIENTIFIC_ACCURACY: [Assessment of the scientific validity of the results, including any concerns about data interpretation or biochemical reasoning]

API_USAGE_ASSESSMENT: [Evaluation of whether the agent used appropriate tools and followed a logical workflow]
"""


def parse_gpt_evaluation_response(gpt_response: str) -> Dict[str, Any]:
    """
    Parse GPT evaluation response and extract decision and details.
    
    Args:
        gpt_response: Raw response from GPT-4o
        
    Returns:
        Dictionary containing parsed evaluation results
    """
    result = {
        'decision': None,
        'success': False,
        'reasoning': '',
        'critical_issues': '',
        'scientific_accuracy': '',
        'api_usage_assessment': '',
        'raw_response': gpt_response
    }
    
    lines = gpt_response.strip().split('\n')
    current_section = None
    
    for line in lines:
        line = line.strip()
        
        if line.startswith('DECISION:'):
            decision = line.split('DECISION:', 1)[1].strip().upper()
            result['decision'] = decision
            result['success'] = 'SUCCESS' in decision
            
        elif line.startswith('REASONING:'):
            current_section = 'reasoning'
            content = line.split('REASONING:', 1)[1].strip()
            if content:
                result['reasoning'] = content
                
        elif line.startswith('CRITICAL_ISSUES:'):
            current_section = 'critical_issues'
            content = line.split('CRITICAL_ISSUES:', 1)[1].strip()
            if content:
                result['critical_issues'] = content
                
        elif line.startswith('SCIENTIFIC_ACCURACY:'):
            current_section = 'scientific_accuracy'
            content = line.split('SCIENTIFIC_ACCURACY:', 1)[1].strip()
            if content:
                result['scientific_accuracy'] = content
                
        elif line.startswith('API_USAGE_ASSESSMENT:'):
            current_section = 'api_usage_assessment'
            content = line.split('API_USAGE_ASSESSMENT:', 1)[1].strip()
            if content:
                result['api_usage_assessment'] = content
                
        elif line and current_section:
            # Continue previous section
            if result[current_section]:
                result[current_section] += ' ' + line
            else:
                result[current_section] = line
    
    # Default to failure if unclear
    if result['decision'] is None:
        logger.warning(f"Unclear GPT decision: {gpt_response}")
        result['success'] = False
        result['decision'] = 'FAILURE'
        result['critical_issues'] = 'Could not parse GPT evaluation response'
    
    return result


def call_gpt_evaluator(prompt: str, model: str = "gpt-4o") -> str:
    """
    Call GPT-4o for evaluation with appropriate settings.
    
    Args:
        prompt: Evaluation prompt
        model: OpenAI model to use
        
    Returns:
        GPT response text
    """
    # Debug logging to verify model and token count
    logger.info(f"DEBUG: Using model: {model}")
    logger.info(f"DEBUG: Prompt length (chars): {len(prompt)}")
    
    # Rough token estimate (1 token ≈ 4 characters for English text)
    estimated_tokens = len(prompt) // 4
    logger.info(f"DEBUG: Estimated tokens: {estimated_tokens}")
    
    client = openai.OpenAI(
        api_key=os.environ.get('OPENAI_API_KEY', 'OPENAI_KEY_REMOVED')
    )
    
    try:
        logger.info(f"DEBUG: Making API call to OpenAI with model: {model}")
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system", 
                    "content": "You are an expert glycomics researcher evaluating AI agent performance on scientific research tasks. Provide thorough, objective evaluations based on scientific accuracy and research methodology."
                },
                {
                    "role": "user", 
                    "content": prompt
                }
            ],
            temperature=0,  # Deterministic evaluation
            max_tokens=1500  # Allow for detailed reasoning
        )
        
        logger.info(f"DEBUG: API call successful, response received")
        return response.choices[0].message.content
        
    except Exception as e:
        logger.error(f"Error calling GPT evaluator with model {model}: {str(e)}")
        return f"ERROR: Could not evaluate with GPT - {str(e)}"


def extract_api_calls_from_log(log_content: str) -> List[Dict[str, Any]]:
    """
    Extract API calls and their results from the agent interaction log.
    
    Args:
        log_content: Complete interaction log
        
    Returns:
        List of API call information
    """
    api_calls = []
    
    # Look for patterns indicating API calls - updated for MCP/function calling patterns
    patterns = [
        r'call_function\([\'"]([^\'\"]+)[\'"].*?site=[\'"]glycan[\'"].*?module=[\'"]([^\'\"]+)[\'"]',
        r'Calling glycan function: ([^.]+)\.([^\\s]+)',
        r'Successfully called ([^.]+)\.([^\\s]+)',
        r'invoke.*?name="([^"]+)"',  # MCP pattern
        r'antml:function_calls.*?antml:invoke name="([^"]+)"',  # Our MCP pattern
    ]
    
    lines = log_content.split('\n')
    
    for i, line in enumerate(lines):
        for pattern in patterns:
            match = re.search(pattern, line)
            if match:
                tool_name = match.group(1)
                
                # Look for parameters in surrounding lines
                params = {}
                for j in range(max(0, i-2), min(len(lines), i+5)):
                    param_line = lines[j]
                    # Simple parameter extraction for our format
                    if 'antml:parameter' in param_line:
                        # Extract parameter name and value
                        param_match = re.search(r'name="([^"]+)"[^>]*>([^<]*)', param_line)
                        if param_match:
                            params[param_match.group(1)] = param_match.group(2)
                
                api_calls.append({
                    'tool_name': tool_name,
                    'parameters': params,
                    'line_number': i + 1
                })
    
    return api_calls


def evaluate_task_from_log(log_file: str, jsonl_file: str = 'glycan_tasks.jsonl', model: str = "gpt-4o") -> Dict[str, Any]:
    """
    Evaluate a single task from its log file.
    
    Args:
        log_file: Path to the log file
        jsonl_file: Path to JSONL task file
        model: OpenAI model to use for evaluation
        
    Returns:
        Evaluation results dictionary
    """
    logger.info(f"Evaluating task from log file: {log_file}")
    
    try:
        # Read and parse the log file
        with open(log_file, 'r', encoding='utf-8') as f:
            log_content = f.read()
        
        parsed_log = parse_conversation_log(log_content)
        
        # Load the corresponding task
        task_id = int(parsed_log['task_id'])
        task = load_task_from_jsonl(task_id, jsonl_file)
        
        if not task:
            logger.error(f"Could not load task {task_id}")
            return {'success': False, 'error': f'Could not load task {task_id}'}
        
        # Extract information for evaluation
        question = task.get('question', '')
        expected_trajectory = task.get('expected_trajectory', '')
        expected_answer = task.get('expected_answer', '')
        agent_final_response = parsed_log['final_assistant_response']
        
        # Create evaluation prompt
        evaluation_prompt = create_glycan_evaluation_prompt(
            question=question,
            expected_trajectory=expected_trajectory,
            expected_answer=expected_answer,
            agent_log=log_content,
            agent_final_response=agent_final_response
        )
        
        # Get GPT evaluation
        logger.info(f"Calling {model} for evaluation...")
        gpt_response = call_gpt_evaluator(evaluation_prompt, model=model)
        
        if gpt_response.startswith("ERROR:"):
            logger.error(f"GPT evaluation failed: {gpt_response}")
            return {'success': False, 'error': gpt_response}
        
        # Parse GPT response
        evaluation_result = parse_gpt_evaluation_response(gpt_response)
        
        # Create comprehensive result
        result = {
            'task_id': task_id,
            'log_file': log_file,
            'question': question,
            'expected_trajectory': expected_trajectory,
            'expected_answer': expected_answer,
            'agent_final_response': agent_final_response,
            'rounds_completed': parsed_log['rounds_completed'],
            'finished_early': parsed_log['finished_early'],
            'evaluation_result': evaluation_result,
            'api_calls_detected': extract_api_calls_from_log(log_content),
            'timestamp': datetime.now().isoformat(),
            'model_used': model,
            'success': evaluation_result['success']
        }
        
        # Save detailed evaluation
        eval_file = log_file.replace('.log', '_evaluation.json')
        try:
            with open(eval_file, 'w', encoding='utf-8') as f:
                json.dump(result, f, indent=2)
            logger.info(f"Detailed evaluation saved to {eval_file}")
        except Exception as e:
            logger.warning(f"Could not save evaluation details: {str(e)}")
        
        # Log summary
        logger.info(f"Task {task_id} Evaluation Results:")
        logger.info(f"  Decision: {evaluation_result['decision']}")
        logger.info(f"  Success: {evaluation_result['success']}")
        logger.info(f"  Rounds: {parsed_log['rounds_completed']}")
        logger.info(f"  Finished Early: {parsed_log['finished_early']}")
        
        return result
        
    except Exception as e:
        logger.error(f"Error evaluating task from {log_file}: {str(e)}")
        return {'success': False, 'error': str(e), 'log_file': log_file}


def evaluate_all_tasks(workspace_dir: str = 'workspace', jsonl_file: str = 'glycan_tasks.jsonl', 
                      model: str = "gpt-4o") -> Dict[str, Any]:
    """
    Evaluate all tasks in the workspace directory.
    
    Args:
        workspace_dir: Directory containing log files
        jsonl_file: Path to JSONL task file
        model: OpenAI model to use for evaluation
        
    Returns:
        Summary of all evaluations
    """
    logger.info(f"Starting evaluation of all tasks in {workspace_dir}")
    
    import glob
    log_files = glob.glob(os.path.join(workspace_dir, 'task_*.log'))
    
    results = []
    success_count = 0
    
    for log_file in sorted(log_files):
        try:
            result = evaluate_task_from_log(log_file, jsonl_file, model)
            results.append(result)
            if result.get('success', False):
                success_count += 1
        except Exception as e:
            logger.error(f"Failed to evaluate {log_file}: {str(e)}")
            results.append({'log_file': log_file, 'success': False, 'error': str(e)})
    
    # Create summary
    summary = {
        'total_tasks': len(results),
        'successful_tasks': success_count,
        'success_rate': success_count / len(results) if results else 0,
        'timestamp': datetime.now().isoformat(),
        'model_used': model,
        'results': results
    }
    
    # Save summary
    summary_file = os.path.join(workspace_dir, 'evaluation_summary.json')
    try:
        with open(summary_file, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2)
        logger.info(f"Evaluation summary saved to {summary_file}")
    except Exception as e:
        logger.warning(f"Could not save evaluation summary: {str(e)}")
    
    logger.info(f"Evaluation complete: {success_count}/{len(results)} tasks successful ({summary['success_rate']:.2%})")
    
    return summary


# Legacy compatibility function
def check_correctness_glycan(task: Dict[str, Any], response: str, log_file: str, 
                           check_all_history: bool = False) -> bool:
    """
    Legacy compatibility function for existing evaluation pipelines.
    
    Args:
        task: Task configuration (not used in our format)
        response: Agent response (not used, extracted from log)
        log_file: Path to interaction log
        check_all_history: Whether to check all history (compatibility parameter)
        
    Returns:
        True if task completed successfully, False otherwise
    """
    try:
        result = evaluate_task_from_log(log_file)
        return result.get('success', False)
    except Exception as e:
        logger.error(f"Legacy evaluation failed for {log_file}: {str(e)}")
        return False


if __name__ == "__main__":
    # Example usage
    logging.basicConfig(level=logging.INFO)
    
    # Evaluate all tasks
    summary = evaluate_all_tasks()
    print(f"Evaluation complete: {summary['success_rate']:.2%} success rate")