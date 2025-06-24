import os
import json
import openai
import re
from datetime import datetime
from typing import Dict, Any, List
from opendevin.core.logger import opendevin_logger as logger


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


def extract_api_calls_from_log(log_content: str) -> List[Dict[str, Any]]:
    """
    Extract API calls and their results from the agent interaction log.
    
    Args:
        log_content: Complete interaction log
        
    Returns:
        List of API call information
    """
    api_calls = []
    
    # Look for patterns indicating API calls
    patterns = [
        r'call_function\([\'"]([^\'\"]+)[\'"].*?site=[\'"]glycan[\'"].*?module=[\'"]([^\'\"]+)[\'"]',
        r'Calling glycan function: ([^.]+)\.([^\\s]+)',
        r'Successfully called ([^.]+)\.([^\\s]+)',
    ]
    
    lines = log_content.split('\n')
    
    for i, line in enumerate(lines):
        for pattern in patterns:
            match = re.search(pattern, line)
            if match:
                if len(match.groups()) >= 2:
                    tool_name = match.group(1) if 'call_function' in pattern else match.group(2)
                    module = match.group(2) if 'call_function' in pattern else match.group(1)
                    
                    # Look for parameters in surrounding lines
                    params = {}
                    for j in range(max(0, i-2), min(len(lines), i+3)):
                        param_line = lines[j]
                        # Simple parameter extraction
                        if '=' in param_line and not param_line.strip().startswith('#'):
                            parts = param_line.split('=')
                            if len(parts) == 2:
                                key = parts[0].strip().split()[-1]
                                value = parts[1].strip().rstrip(',')
                                params[key] = value
                    
                    api_calls.append({
                        'tool_name': tool_name,
                        'module': module,
                        'parameters': params,
                        'line_number': i + 1
                    })
    
    return api_calls


def glycan_gpt_evaluation(task: Dict[str, Any], agent_response: str, log_file: str, model: str = "gpt-4o") -> bool:
    """
    Unified GPT-4o evaluation for glycan tasks.
    
    Args:
        task: Task configuration
        agent_response: Agent's final response
        log_file: Path to interaction log
        model: OpenAI model to use for evaluation
        
    Returns:
        True if task was completed successfully, False otherwise
    """
    logger.info(f"Starting GPT evaluation for glycan task {task.get('task_id', 'unknown')}")
    
    try:
        # Read the complete interaction log
        with open(log_file, 'r') as f:
            interaction_log = f.read()
    except Exception as e:
        logger.error(f"Could not read log file {log_file}: {str(e)}")
        return False
    
    # Extract key information from task
    question = task.get('intent', '')
    expected_trajectory = task.get('eval', {}).get('expected_trajectory', '')
    expected_answer = task.get('eval', {}).get('reference_answer', '')
    
    # Create evaluation prompt
    evaluation_prompt = create_glycan_evaluation_prompt(
        question=question,
        expected_trajectory=expected_trajectory,
        expected_answer=expected_answer,
        agent_log=interaction_log,
        agent_final_response=agent_response
    )
    
    # Get GPT evaluation
    logger.info(f"Calling {model} for evaluation...")
    gpt_response = call_gpt_evaluator(evaluation_prompt, model=model)
    
    if gpt_response.startswith("ERROR:"):
        logger.error(f"GPT evaluation failed: {gpt_response}")
        return False
    
    # Parse GPT response
    evaluation_result = parse_gpt_evaluation_response(gpt_response)
    
    # Log detailed evaluation results
    logger.info(f"GPT Evaluation Results:")
    logger.info(f"  Decision: {evaluation_result['decision']}")
    logger.info(f"  Success: {evaluation_result['success']}")
    logger.info(f"  Reasoning: {evaluation_result['reasoning'][:200]}...")
    if evaluation_result['critical_issues'] and evaluation_result['critical_issues'] != 'None':
        logger.info(f"  Critical Issues: {evaluation_result['critical_issues']}")
    
    # Save detailed evaluation to separate file for analysis
    task_id = task.get('task_id', 'unknown')
    eval_file = log_file.replace('.log', '_evaluation.json')
    
    evaluation_summary = {
        'task_id': task_id,
        'question': question,
        'expected_trajectory': expected_trajectory,
        'agent_response': agent_response,
        'evaluation_result': evaluation_result,
        'timestamp': datetime.now().isoformat(),
        'api_calls_detected': extract_api_calls_from_log(interaction_log),
        'model_used': model
    }
    
    try:
        with open(eval_file, 'w') as f:
            json.dump(evaluation_summary, f, indent=2)
        logger.info(f"Detailed evaluation saved to {eval_file}")
    except Exception as e:
        logger.warning(f"Could not save evaluation details: {str(e)}")
    
    return evaluation_result['success']


def check_correctness_glycan(task: Dict[str, Any], response: str, log_file: str, 
                           check_all_history: bool = False) -> bool:
    """
    Glycan task evaluation entry point - integrates with existing WebArena pipeline.
    
    Args:
        task: Task configuration
        response: Agent response
        log_file: Path to interaction log
        check_all_history: Whether to check all history (compatibility parameter)
        
    Returns:
        True if task completed successfully, False otherwise
    """
    # Check if this is a glycan task
    if task.get('sites') == ['glycan'] or 'glycan_gpt_evaluation' in task.get('eval', {}).get('eval_types', []):
        return glycan_gpt_evaluation(task, response, log_file)
    else:
        # Not a glycan task, should not be evaluated here
        logger.warning(f"check_correctness_glycan called on non-glycan task {task.get('task_id')}")
        return False