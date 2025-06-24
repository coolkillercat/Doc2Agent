import os
import json
import openai
import re
from datetime import datetime
from typing import Dict, Any, List
import logging

logger = logging.getLogger(__name__)

def parse_claude_conversation_log(log_content: str) -> Dict[str, Any]:
    """
    Parse Claude log format that contains only the agent's output.
    
    Args:
        log_content: Complete log file content
        
    Returns:
        Dictionary with parsed information
    """
    result = {
        'task_id': None,
        'original_question': '',
        'rounds_completed': 1,  # Default to 1 since we have at least the final output
        'finished_early': False,
        'conversation_history': [],
        'final_assistant_response': ''
    }
    
    # Try to extract task ID from filename or log content
    task_id_match = re.search(r'task_?(\d+)|/(\d+)\.log', log_content)
    if task_id_match:
        result['task_id'] = task_id_match.group(1) or task_id_match.group(2)
    
    # Since Claude logs may only contain the final output,
    # treat the entire content as the assistant's response
    result['conversation_history'] = [
        {'role': 'assistant', 'content': log_content.strip()}
    ]
    
    result['final_assistant_response'] = log_content.strip()
    
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
        api_key=os.environ.get('OPENAI_API_KEY', '')
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


def extract_api_calls_from_claude_log(log_content: str) -> List[Dict[str, Any]]:
    """
    Extract API calls and their results from the Claude log.
    This is challenging since Claude logs may not explicitly show function calls,
    but we can try to infer them from the output.
    
    Args:
        log_content: Complete Claude log content
        
    Returns:
        List of inferred API call information
    """
    api_calls = []
    
    # Patterns that might indicate API usage in Claude's outputs
    patterns = [
        r'(?:searched|queried|retrieved from|using) (\w+)(?:API|Database|Service)',
        r'using (?:the )?(\w+) (?:API|Database|Service|function)',
        r'(?:called|executed) (?:the )?(\w+)(?:API|function)',
        r'results from (\w+)(?:API|Database|Service)',
        r'according to (?:the )?(\w+)(?:API|Database|Service)',
        r'data from (\w+)'
    ]
    
    lines = log_content.split('\n')
    
    # Look for possible API usage indicators in the text
    for pattern in patterns:
        matches = re.finditer(pattern, log_content, re.IGNORECASE)
        for match in matches:
            api_name = match.group(1)
            api_calls.append({
                'tool_name': api_name,
                'parameters': {},  # Can't reliably extract parameters
                'inferred': True    # Mark as inferred rather than directly observed
            })
    
    # Add additional check for specific glycan API mentions
    glycan_api_mentions = ['GlyTouCan', 'UniCarbKB', 'GlyGen', 'UniLectin', 'GlyConnect']
    for api in glycan_api_mentions:
        if api in log_content:
            api_calls.append({
                'tool_name': api,
                'parameters': {},
                'inferred': True
            })
    
    return api_calls


def evaluate_claude_task_from_log(log_file: str, jsonl_file: str = 'glycan_tasks.jsonl', model: str = "gpt-4o") -> Dict[str, Any]:
    """
    Evaluate a single Claude task from its log file.
    
    Args:
        log_file: Path to the Claude log file
        jsonl_file: Path to JSONL task file
        model: OpenAI model to use for evaluation
        
    Returns:
        Evaluation results dictionary
    """
    logger.info(f"Evaluating Claude task from log file: {log_file}")
    
    try:
        # Read and parse the log file
        with open(log_file, 'r', encoding='utf-8') as f:
            log_content = f.read()
        
        # Extract task ID from the filename if possible
        filename = os.path.basename(log_file)
        task_id_match = re.match(r'(\d+)\.log', filename)
        task_id = int(task_id_match.group(1)) if task_id_match else None
        
        if not task_id:
            logger.error(f"Could not determine task ID from filename: {filename}")
            return {'success': False, 'error': f'Could not determine task ID from filename: {filename}'}
        
        # Load the corresponding task
        task = load_task_from_jsonl(task_id, jsonl_file)
        
        if not task:
            logger.error(f"Could not load task {task_id}")
            return {'success': False, 'error': f'Could not load task {task_id}'}
        
        # Parse the log to extract what we can
        parsed_log = parse_claude_conversation_log(log_content)
        
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
            'rounds_completed': parsed_log.get('rounds_completed', 1),
            'finished_early': parsed_log.get('finished_early', False),
            'evaluation_result': evaluation_result,
            'api_calls_detected': extract_api_calls_from_claude_log(log_content),
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
        
        return result
        
    except Exception as e:
        logger.error(f"Error evaluating Claude task from {log_file}: {str(e)}")
        return {'success': False, 'error': str(e), 'log_file': log_file}


def evaluate_all_claude_tasks(workspace_dir: str = 'test_glycan/claude_logs', jsonl_file: str = 'glycan_tasks.jsonl', 
                              model: str = "gpt-4o") -> Dict[str, Any]:
    """
    Evaluate all Claude tasks in the workspace directory.
    
    Args:
        workspace_dir: Directory containing Claude log files
        jsonl_file: Path to JSONL task file
        model: OpenAI model to use for evaluation
        
    Returns:
        Summary of all evaluations
    """
    logger.info(f"Starting evaluation of all Claude tasks in {workspace_dir}")
    
    import glob
    log_files = glob.glob(os.path.join(workspace_dir, '*.log'))
    
    results = []
    success_count = 0
    
    for log_file in sorted(log_files):
        # Skip evaluation files
        if '_evaluation' in log_file:
            continue
            
        try:
            result = evaluate_claude_task_from_log(log_file, jsonl_file, model)
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
    summary_file = os.path.join(workspace_dir, 'claude_evaluation_summary.json')
    try:
        with open(summary_file, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2)
        logger.info(f"Claude evaluation summary saved to {summary_file}")
    except Exception as e:
        logger.warning(f"Could not save Claude evaluation summary: {str(e)}")
    
    logger.info(f"Claude evaluation complete: {success_count}/{len(results)} tasks successful ({summary['success_rate']:.2%})")
    
    return summary


if __name__ == "__main__":
    # Example usage
    logging.basicConfig(level=logging.INFO)
    
    # Evaluate all Claude tasks
    summary = evaluate_all_claude_tasks()
    print(f"Claude evaluation complete: {summary['success_rate']:.2%} success rate") 