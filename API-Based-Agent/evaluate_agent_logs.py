#!/usr/bin/env python3
"""
Script to evaluate agent logs from agent-output/ using the project's evaluation framework.
This script re-evaluates existing agent runs to check their correctness based on the logs.

UPDATED: Now uses the new html_match function with hybrid evaluation approach.
No longer needs URL preprocessing as the new implementation handles case sensitivity issues.
"""

import os
import sys
import json
import argparse
import logging
import re
import tempfile
from pathlib import Path
from typing import Dict, List, Any, Optional
from tqdm import tqdm

# Add the evaluation directory to the path
sys.path.append('/Users/jianhaonan/Desktop/API-Based-Agent/evaluation/webarena')

# Import the evaluation functions from the project
from utils import (
    check_correctness,
    get_task_by_task_id,
    parse_test_file
)

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def preprocess_log_for_url_matching(log_content: str) -> str:
    """
    Preprocess log content to fix URL format issues that prevent proper URL matching.
    
    Key fixes:
    1. Convert 'URL: ' to 'url: ' (case sensitivity fix)
    2. This ensures the url_match function can properly extract URLs and parameters
    
    Args:
        log_content: Raw log content from agent execution
        
    Returns:
        str: Preprocessed log content with fixed URL format
    """
    # Convert 'URL: ' to 'url: ' to match expected format in url_match function
    processed_content = re.sub(r'^URL: ', 'url: ', log_content, flags=re.MULTILINE)
    
    # Log the number of replacements made
    original_url_count = len(re.findall(r'^URL: ', log_content, flags=re.MULTILINE))
    if original_url_count > 0:
        logger.debug(f"Preprocessed {original_url_count} URL format entries")
    
    return processed_content

class AgentLogEvaluator:
    """
    Evaluates agent logs using the project's correctness checking framework.
    Now includes URL matching fixes for accurate evaluation.
    """
    
    def __init__(self, agent_output_dir: str = "/Users/jianhaonan/Desktop/API-Based-Agent/agent-output"):
        self.agent_output_dir = Path(agent_output_dir)
        self.logs_dir = self.agent_output_dir / "logs"
        self.webarena_dir = self.agent_output_dir / "webarena"
        
        # Load all tasks from test file
        self.all_tasks = parse_test_file()
        self.task_lookup = {task['task_id']: task for task in self.all_tasks}
        
        logger.info(f"Loaded {len(self.all_tasks)} tasks from test file")
        logger.info("Using updated evaluation with new html_match function (hybrid approach)")
    
    def find_jsonl_files(self) -> List[Path]:
        """Find all JSONL output files."""
        jsonl_files = []
        
        # Check hybrid output
        hybrid_file = self.agent_output_dir / "hybrid-output.jsonl"
        if hybrid_file.exists():
            jsonl_files.append(hybrid_file)
        
        # Check WebArena outputs
        if self.webarena_dir.exists():
            for file in self.webarena_dir.glob("*.jsonl"):
                jsonl_files.append(file)
        
        return jsonl_files
    
    def load_jsonl_results(self, file_path: Path) -> List[Dict[str, Any]]:
        """Load results from a JSONL file."""
        results = []
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line_num, line in enumerate(f, 1):
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        data = json.loads(line)
                        results.append(data)
                    except json.JSONDecodeError as e:
                        logger.warning(f"Failed to parse line {line_num} in {file_path}: {e}")
        except Exception as e:
            logger.error(f"Error reading {file_path}: {e}")
        
        return results
    
    def find_log_file(self, task_id: int, jsonl_file_path: Optional[Path] = None) -> Optional[Path]:
        """Find the log file for a given task ID. 
        
        First tries the default location, then looks in the same directory structure 
        as the JSONL file if provided.
        """
        # If JSONL file path is provided, try to find log file in same directory structure FIRST
        if jsonl_file_path:
            # Check if JSONL file is from evaluation outputs (API-based agent)
            if "evaluation_outputs" in str(jsonl_file_path):
                # Extract the base directory (e.g., .../outputs/CodeActAgent/gpt-4o_maxiter_18_N_v1.6_/)
                jsonl_parent = jsonl_file_path.parent
                potential_log_dir = jsonl_parent / "logs"
                potential_log_file = potential_log_dir / f"instance_{task_id}.log"
                
                if potential_log_file.exists():
                    logger.info(f"Found log file in evaluation outputs: {potential_log_file}")
                    return potential_log_file
                else:
                    logger.warning(f"Expected log file not found: {potential_log_file}")
        
        # Try default location as fallback
        log_file = self.logs_dir / f"instance_{task_id}.log"
        if log_file.exists():
            logger.info(f"Using fallback log file: {log_file}")
            return log_file
        
        logger.error(f"No log file found for task {task_id} in any location")
        return None
    
    def extract_agent_response(self, result: Dict[str, Any]) -> str:
        """Extract the agent's response from the result."""
        # Try different fields where the response might be stored
        response_fields = ['raw', 'response', 'answer', 'output']
        
        for field in response_fields:
            if field in result and result[field]:
                return str(result[field])
        
        logger.warning(f"No response found in result for task {result.get('task_id', 'unknown')}")
        return ""
    
    def check_agent_completion_status(self, result: Dict[str, Any]) -> Dict[str, Any]:
        """Check if the agent properly completed the task or had errors."""
        completion_issues = []
        
        # Check for explicit errors
        if result.get('error'):
            completion_issues.append(f"Agent error: {result['error']}")
        
        # Check for proper task completion indicators
        agent_response = self.extract_agent_response(result)
        has_finish_tag = 'Finish[' in agent_response and ']' in agent_response
        
        # Check for common failure patterns
        error_msg = result.get('error', '') or ''
        if 'got stuck in a loop' in str(error_msg).lower():
            completion_issues.append("Agent got stuck in a loop")
        
        if not has_finish_tag:
            # Check if response seems incomplete
            if agent_response.strip().endswith(('...', 'Let\'s', 'First,', 'Now,')):
                completion_issues.append("Response appears incomplete (no Finish[] tag and ends abruptly)")
        
        return {
            'has_completion_issues': len(completion_issues) > 0,
            'completion_issues': completion_issues,
            'has_finish_tag': has_finish_tag
        }
    
    def fixed_string_match_evaluation(self, task: Dict[str, Any], agent_response: str, completion_status: Dict[str, Any]) -> Dict[str, Any]:
        """Enhanced string matching that considers task completion."""
        
        # If agent has completion issues but provided a Finish[] tag, still evaluate the answer
        if completion_status['has_completion_issues']:
            eval_config = task.get('eval', {})
            reference_answers = eval_config.get('reference_answers', {})
            
            # If the agent has a Finish[] tag, evaluate the answer regardless of completion issues
            if completion_status['has_finish_tag']:
                # The agent provided an answer despite issues (like max iterations)
                # Let the original evaluation determine if the answer is correct
                return None  # Signal to use original evaluation
            
            # Only fail if there's no Finish[] tag AND the task requires specific answers
            if 'must_include' in reference_answers or 'exact_match' in reference_answers:
                return {
                    'score': 0.0,
                    'success': False,
                    'details': {
                        'failure_reason': 'Agent did not complete task properly (no Finish[] tag)',
                        'completion_issues': completion_status['completion_issues'],
                        'original_evaluation_bypassed': True
                    }
                }
        
        # For completed tasks, use original evaluation but with stricter Finish[] requirement
        return None  # Signal to use original evaluation
    
    def re_evaluate_task(self, task_id: int, agent_response: str, original_result: Optional[Dict[str, Any]] = None, check_all_history: bool = False, jsonl_file_path: Optional[Path] = None) -> Dict[str, Any]:
        """Re-evaluate a single task using the project's evaluation framework with new html_match function."""
        # Get task configuration
        task = self.task_lookup.get(task_id)
        if not task:
            logger.error(f"Task {task_id} not found in task definitions")
            return {
                'task_id': task_id,
                'error': f'Task {task_id} not found in task definitions',
                'correct': False,
                'evaluation_details': {}
            }
        
        # Find log file (now with smart path detection)
        log_file = self.find_log_file(task_id, jsonl_file_path)
        if not log_file:
            logger.error(f"Log file not found for task {task_id}")
            return {
                'task_id': task_id,
                'error': f'Log file not found for task {task_id}',
                'correct': False,
                'evaluation_details': {}
            }
        
        try:
            # First, check agent completion status for enhanced evaluation
            result_data = original_result or {'error': None, 'raw': agent_response}
            completion_status = self.check_agent_completion_status(result_data)
            
            # Check evaluation types
            eval_types = task.get('eval', {}).get('eval_types', [])
            requires_string_match = 'string_match' in eval_types
            requires_html_match = 'program_html' in eval_types
            
            # Apply completion-aware evaluation for string_match tasks
            if requires_string_match:
                fixed_eval = self.fixed_string_match_evaluation(task, agent_response, completion_status)
                if fixed_eval is not None:
                    # Use our enhanced evaluation that caught the completion issue
                    eval_details = {
                        'eval_types': eval_types,
                        'correct_last_response': fixed_eval['success'],
                        'correct_all_history': fixed_eval['success'],
                        'task_intent': task.get('intent', ''),
                        'task_sites': task.get('sites', []),
                        'log_file': str(log_file),
                        'agent_response_preview': agent_response[:200] + "..." if len(agent_response) > 200 else agent_response,
                        'enhanced_evaluation_applied': True,
                        'completion_status': completion_status,
                        'fixed_evaluation_details': fixed_eval,
                        'llm_reasoning': {'has_llm_evaluation': False},
                        'new_html_match_used': False
                    }
                    
                    return {
                        'task_id': task_id,
                        'correct': fixed_eval['success'],
                        'correct_all_history': fixed_eval['success'],
                        'evaluation_details': eval_details,
                        'error': None
                    }
            
            # Use the updated check_correctness function with new html_match
            is_correct, detailed_eval = check_correctness(task, agent_response, str(log_file), check_all_history=check_all_history)
            is_correct_all_history, detailed_eval_all_history = check_correctness(task, agent_response, str(log_file), check_all_history=True)
            
            eval_details = {
                'eval_types': eval_types,
                'correct_last_response': is_correct,
                'correct_all_history': is_correct_all_history,
                'task_intent': task.get('intent', ''),
                'task_sites': task.get('sites', []),
                'log_file': str(log_file),
                'agent_response_preview': agent_response[:200] + "..." if len(agent_response) > 200 else agent_response,
                'enhanced_evaluation_applied': False,
                'completion_status': None,
                'new_html_match_used': requires_html_match,
                # Add detailed evaluation information including LLM reasoning
                'detailed_evaluation_last_response': detailed_eval,
                'detailed_evaluation_all_history': detailed_eval_all_history,
                # Extract LLM reasoning if available (now includes html_match details)
                'llm_reasoning': self._extract_llm_reasoning(detailed_eval)
            }
            
            return {
                'task_id': task_id,
                'correct': is_correct,
                'correct_all_history': is_correct_all_history,
                'evaluation_details': eval_details,
                'error': None
            }
            
        except Exception as e:
            logger.error(f"Error evaluating task {task_id}: {e}")
            return {
                'task_id': task_id,
                'error': str(e),
                'correct': False,
                'evaluation_details': {}
            }
    
    def _extract_llm_reasoning(self, detailed_eval: Dict[str, Any]) -> Dict[str, Any]:
        """Extract LLM reasoning from detailed evaluation results."""
        llm_reasoning = {
            'has_llm_evaluation': False,
            'html_match_llm_details': None,
            'llm_prompts': [],
            'llm_responses': [],
            'llm_reasoning_text': []
        }
        
        if not detailed_eval or not isinstance(detailed_eval, dict):
            return llm_reasoning
        
        # Check for HTML match LLM evaluations
        html_match_details = detailed_eval.get('html_match_details')
        if html_match_details and isinstance(html_match_details, dict):
            llm_reasoning['has_llm_evaluation'] = True
            llm_reasoning['html_match_llm_details'] = html_match_details
            
            # Extract target evaluations with LLM reasoning
            target_evaluations = html_match_details.get('target_evaluations', [])
            for target_eval in target_evaluations:
                if isinstance(target_eval, dict):
                    if target_eval.get('llm_prompt'):
                        llm_reasoning['llm_prompts'].append({
                            'target_index': target_eval.get('target_index'),
                            'verification_type': target_eval.get('verification_type'),
                            'prompt': target_eval.get('llm_prompt')
                        })
                    
                    if target_eval.get('llm_response'):
                        llm_reasoning['llm_responses'].append({
                            'target_index': target_eval.get('target_index'),
                            'verification_type': target_eval.get('verification_type'),
                            'full_response': target_eval.get('llm_response'),
                            'score': target_eval.get('score', 0.0),
                            'success': target_eval.get('success', False)
                        })
                    
                    if target_eval.get('llm_reasoning'):
                        llm_reasoning['llm_reasoning_text'].append({
                            'target_index': target_eval.get('target_index'),
                            'verification_type': target_eval.get('verification_type'),
                            'reasoning': target_eval.get('llm_reasoning'),
                            'score': target_eval.get('score', 0.0),
                            'success': target_eval.get('success', False)
                        })
        
        return llm_reasoning
    
    def evaluate_jsonl_file(self, file_path: Path, output_file: Optional[Path] = None, 
                           task_filter: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Evaluate all results in a JSONL file with optional filtering."""
        logger.info(f"Evaluating file: {file_path}")
        
        # Load results
        original_results = self.load_jsonl_results(file_path)
        if not original_results:
            logger.warning(f"No results found in {file_path}")
            return {'file': str(file_path), 'results': [], 'summary': {}}
        
        # Apply filters if specified
        if task_filter:
            filtered_results = []
            for result in original_results:
                task_id = result.get('task_id')
                task = self.task_lookup.get(task_id)
                
                # Apply task ID filter
                if task_filter.get('task_ids') and task_id not in task_filter['task_ids']:
                    continue
                
                # Apply site filter
                if task_filter.get('sites') and task:
                    task_sites = task.get('sites', [])
                    if not any(site in task_sites for site in task_filter['sites']):
                        continue
                
                # Apply range filter
                if task_filter.get('task_range'):
                    start, end = task_filter['task_range']
                    if not (start <= task_id <= end):
                        continue
                
                # Apply evaluation type filter
                if task_filter.get('eval_types') and task:
                    task_eval_types = task.get('eval', {}).get('eval_types', [])
                    if not any(eval_type in task_eval_types for eval_type in task_filter['eval_types']):
                        continue
                
                filtered_results.append(result)
            
            original_results = filtered_results
            logger.info(f"After filtering: {len(original_results)} results to evaluate")
        
        if not original_results:
            logger.warning("No results match the specified filters")
            return {'file': str(file_path), 'results': [], 'summary': {}}
        
        logger.info(f"Found {len(original_results)} results to evaluate")
        
        # Re-evaluate each result
        re_evaluated_results = []
        correct_count = 0
        correct_all_history_count = 0
        error_count = 0
        
        for result in tqdm(original_results, desc="Re-evaluating tasks"):
            task_id = result.get('task_id')
            if task_id is None:
                logger.warning("Result missing task_id, skipping")
                continue
            
            agent_response = self.extract_agent_response(result)
            
            # Re-evaluate
            eval_result = self.re_evaluate_task(task_id, agent_response, result, jsonl_file_path=file_path)
            
            # Combine original and new evaluation
            combined_result = {
                'task_id': task_id,
                'original_result': result,
                'new_evaluation': eval_result,
                'original_correct': result.get('correct', False),
                'new_correct': eval_result['correct'],
                'new_correct_all_history': eval_result['correct_all_history'],
                'agreement': result.get('correct', False) == eval_result['correct']
            }
            
            re_evaluated_results.append(combined_result)
            
            # Update counts
            if eval_result['error'] is None:
                if eval_result['correct']:
                    correct_count += 1
                if eval_result['correct_all_history']:
                    correct_all_history_count += 1
            else:
                error_count += 1
        
        # Calculate summary statistics with URL matching breakdown
        total_evaluated = len(re_evaluated_results) - error_count
        url_match_tasks = [r for r in re_evaluated_results 
                          if 'url_match' in r.get('new_evaluation', {}).get('evaluation_details', {}).get('eval_types', [])]
        url_match_correct = [r for r in url_match_tasks 
                           if r.get('new_evaluation', {}).get('correct', False)]
        
        # Track LLM evaluations (program_html tasks)
        llm_evaluation_tasks = [r for r in re_evaluated_results 
                               if r.get('new_evaluation', {}).get('evaluation_details', {}).get('llm_reasoning', {}).get('has_llm_evaluation', False)]
        llm_evaluation_correct = [r for r in llm_evaluation_tasks 
                                 if r.get('new_evaluation', {}).get('correct', False)]
        
        # Count tasks with detailed LLM reasoning
        tasks_with_llm_reasoning = [r for r in re_evaluated_results 
                                   if r.get('new_evaluation', {}).get('evaluation_details', {}).get('llm_reasoning', {}).get('llm_reasoning_text')]
        
        summary = {
            'total_tasks': len(re_evaluated_results),
            'successful_evaluations': total_evaluated,
            'failed_evaluations': error_count,
            'correct_count_last_response': correct_count,
            'correct_count_all_history': correct_all_history_count,
            'accuracy_last_response': correct_count / total_evaluated if total_evaluated > 0 else 0,
            'accuracy_all_history': correct_all_history_count / total_evaluated if total_evaluated > 0 else 0,
            'original_vs_new_agreement': sum(1 for r in re_evaluated_results if r['agreement']) / len(re_evaluated_results) if re_evaluated_results else 0
        }
        
        evaluation_results = {
            'file': str(file_path),
            'results': re_evaluated_results,
            'summary': summary
        }
        
        # Save results if output file specified
        if output_file:
            output_file.parent.mkdir(parents=True, exist_ok=True)
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(evaluation_results, f, indent=2, ensure_ascii=False)
            logger.info(f"Results saved to {output_file}")
        
        return evaluation_results
    
    def evaluate_all(self, output_dir: Optional[str] = None) -> Dict[str, Any]:
        """Evaluate all JSONL files found in the agent output directory."""
        if output_dir:
            output_path = Path(output_dir)
            output_path.mkdir(parents=True, exist_ok=True)
        else:
            output_path = self.agent_output_dir / "re_evaluation_results"
            output_path.mkdir(parents=True, exist_ok=True)
        
        jsonl_files = self.find_jsonl_files()
        if not jsonl_files:
            logger.warning("No JSONL files found to evaluate")
            return {}
        
        logger.info(f"Found {len(jsonl_files)} JSONL files to evaluate")
        
        all_results = {}
        overall_summary = {
            'total_files': len(jsonl_files),
            'total_tasks': 0,
            'total_correct_last_response': 0,
            'total_correct_all_history': 0,
            'total_errors': 0
        }
        
        for jsonl_file in jsonl_files:
            # Create output file name
            output_file = output_path / f"re_eval_{jsonl_file.stem}.json"
            
            # Evaluate this file
            file_results = self.evaluate_jsonl_file(jsonl_file, output_file)
            all_results[jsonl_file.name] = file_results
            
            # Update overall summary
            summary = file_results['summary']
            overall_summary['total_tasks'] += summary['total_tasks']
            overall_summary['total_correct_last_response'] += summary['correct_count_last_response']
            overall_summary['total_correct_all_history'] += summary['correct_count_all_history']
            overall_summary['total_errors'] += summary['failed_evaluations']
        
        # Calculate overall accuracy
        if overall_summary['total_tasks'] > 0:
            overall_summary['overall_accuracy_last_response'] = overall_summary['total_correct_last_response'] / overall_summary['total_tasks']
            overall_summary['overall_accuracy_all_history'] = overall_summary['total_correct_all_history'] / overall_summary['total_tasks']
        else:
            overall_summary['overall_accuracy_last_response'] = 0
            overall_summary['overall_accuracy_all_history'] = 0
            
        # Save overall summary
        summary_file = output_path / "overall_summary.json"
        with open(summary_file, 'w', encoding='utf-8') as f:
            json.dump({
                'overall_summary': overall_summary,
                'file_summaries': {k: v['summary'] for k, v in all_results.items()},
                'url_matching_fixes_applied': True,
                'evaluation_notes': [
                    "This evaluation includes URL matching fixes",
                    "Logs were preprocessed to convert 'URL:' to 'url:' format",
                    "This should significantly improve URL matching accuracy"
                ]
            }, f, indent=2, ensure_ascii=False)
        
        logger.info(f"Overall summary saved to {summary_file}")
        logger.info(f"Overall accuracy (last response): {overall_summary['overall_accuracy_last_response']:.2%}")
        logger.info(f"Overall accuracy (all history): {overall_summary['overall_accuracy_all_history']:.2%}")
        
        return all_results
    
    def evaluate_single_task(self, task_id: int, verbose: bool = False) -> Dict[str, Any]:
        """Evaluate a single task by task ID."""
        # Find the task in available results
        task_result = None
        source_file = None
        
        # Search in all JSONL files
        jsonl_files = self.find_jsonl_files()
        for file_path in jsonl_files:
            results = self.load_jsonl_results(file_path)
            for result in results:
                if result.get('task_id') == task_id:
                    task_result = result
                    source_file = file_path
                    break
            if task_result:
                break
        
        if not task_result:
            return {
                'task_id': task_id,
                'error': f'No result found for task {task_id} in any JSONL file',
                'correct': False,
                'evaluation_details': {}
            }
        
        # Get task configuration
        task = self.task_lookup.get(task_id)
        if not task:
            return {
                'task_id': task_id,
                'error': f'Task {task_id} not found in task definitions',
                'correct': False,
                'evaluation_details': {}
            }
        
        if verbose:
            print(f"\n{'='*60}")
            print(f"EVALUATING TASK {task_id}")
            print(f"{'='*60}")
            print(f"Intent: {task.get('intent', 'N/A')}")
            print(f"Sites: {', '.join(task.get('sites', []))}")
            print(f"Evaluation Types: {', '.join(task.get('eval', {}).get('eval_types', []))}")
            print(f"Source File: {source_file}")
            print(f"Original Correct: {task_result.get('correct', 'N/A')}")
            print(f"{'='*60}")
        
        agent_response = self.extract_agent_response(task_result)
        eval_result = self.re_evaluate_task(task_id, agent_response, task_result)
        
        # Enhanced result with task info
        enhanced_result = {
            **eval_result,
            'task_info': {
                'intent': task.get('intent', ''),
                'sites': task.get('sites', []),
                'eval_types': task.get('eval', {}).get('eval_types', []),
                'source_file': str(source_file) if source_file else None
            },
            'original_result': {
                'correct': task_result.get('correct', False),
                'agent_response_preview': agent_response[:200] + "..." if len(agent_response) > 200 else agent_response
            },
            'agreement': task_result.get('correct', False) == eval_result.get('correct', False)
        }
        
        if verbose:
            self._print_detailed_results(enhanced_result)
        
        return enhanced_result
    
    def _print_detailed_results(self, result: Dict[str, Any]):
        """Print detailed evaluation results for a single task."""
        task_id = result['task_id']
        
        print(f"\n🔍 DETAILED EVALUATION RESULTS")
        print(f"✅ New Correct (Last Response): {'YES' if result.get('correct') else 'NO'}")
        print(f"✅ New Correct (All History): {'YES' if result.get('correct_all_history') else 'NO'}")
        print(f"📊 Original Correct: {'YES' if result.get('original_result', {}).get('correct') else 'NO'}")
        print(f"🔄 Agreement: {'YES' if result.get('agreement') else 'NO'}")
        
        if result.get('error'):
            print(f"❌ Error: {result['error']}")
            return
        
        eval_details = result.get('evaluation_details', {})
        if eval_details.get('url_match_preprocessing_applied'):
            print(f"🔧 URL Preprocessing: Applied")
        
        # Show LLM reasoning if available
        llm_reasoning = eval_details.get('llm_reasoning', {})
        if llm_reasoning.get('has_llm_evaluation'):
            print(f"\n🤖 LLM EVALUATION DETAILS:")
            reasoning_texts = llm_reasoning.get('llm_reasoning_text', [])
            for reasoning in reasoning_texts:
                print(f"  Target {reasoning.get('target_index', 'N/A')}: Score {reasoning.get('score', 0):.2f}")
                print(f"  Success: {'YES' if reasoning.get('success') else 'NO'}")
                print(f"  Reasoning: {reasoning.get('reasoning', 'N/A')[:200]}...")
                print()
        
        # Show agent response preview
        agent_response = result.get('original_result', {}).get('agent_response_preview', '')
        if agent_response:
            print(f"💬 Agent Response Preview:")
            print(f"   {agent_response}")


def evaluate_both_agents():
    """Evaluate both our agent and baseline agent with new html_match function."""
    logger.info("Starting evaluation of both agents with new html_match function")
    
    # Define agent configurations
    agents = [
        {
            'name': 'Our_Agent',
            'log_dir': '/Users/jianhaonan/Desktop/API-Based-Agent/evaluation/evaluation_outputs/outputs/CodeActAgent/gpt-4o_maxiter_18_N_v1.6_/logs',
            'output_dir': '/Users/jianhaonan/Desktop/API-Based-Agent/evaluation/evaluation_outputs/outputs/CodeActAgent/gpt-4o_maxiter_18_N_v1.6_'
        },
        {
            'name': 'Baseline_Agent',
            'log_dir': '/Users/jianhaonan/Desktop/API-Based-Agent/agent-output/logs',
            'output_dir': '/Users/jianhaonan/Desktop/API-Based-Agent/agent-output/webarena'
        }
    ]
    
    all_results = {}
    
    for agent_config in agents:
        logger.info(f"\n{'='*60}")
        logger.info(f"EVALUATING: {agent_config['name']}")
        logger.info(f"{'='*60}")
        
        # Check if directories exist
        log_dir = Path(agent_config['log_dir'])
        if not log_dir.exists():
            logger.error(f"Log directory not found: {log_dir}")
            continue
        
        # Use agent-output as base for evaluator
        evaluator = AgentLogEvaluator("/Users/jianhaonan/Desktop/API-Based-Agent/agent-output")
        evaluator.logs_dir = log_dir
        
        # Find log files
        log_files = {}
        for log_file in log_dir.glob("instance_*.log"):
            try:
                task_id = int(log_file.stem.split('_')[1])
                log_files[task_id] = log_file
            except (ValueError, IndexError):
                continue
        
        if not log_files:
            logger.error(f"No log files found in {log_dir}")
            continue
        
        # Load agent responses if output directory exists
        agent_responses = {}
        output_dir_path = Path(agent_config.get('output_dir', ''))
        if output_dir_path.exists():
            agent_responses = evaluator.load_agent_responses(output_dir_path)
        
        # Evaluate each task
        results = []
        correct_count = 0
        
        for task_id in tqdm(sorted(log_files.keys()), desc=f"Evaluating {agent_config['name']}"):
            task = evaluator.task_lookup.get(task_id)
            if not task:
                continue
            
            response = agent_responses.get(task_id, "")
            
            try:
                eval_result = evaluator.re_evaluate_task(task_id, response)
                results.append(eval_result)
                
                if eval_result['correct']:
                    correct_count += 1
                        
            except Exception as e:
                logger.error(f"Error evaluating task {task_id} for {agent_config['name']}: {e}")
        
        # Calculate summary
        total_tasks = len(results)
        accuracy = correct_count / total_tasks if total_tasks > 0 else 0
        
        agent_summary = {
            'name': agent_config['name'],
            'total_tasks': total_tasks,
            'correct_count': correct_count,
            'accuracy': accuracy
        }
        
        all_results[agent_config['name']] = {
            'summary': agent_summary,
            'results': results
        }
        
        logger.info(f"Results for {agent_config['name']}:")
        logger.info(f"  Total tasks: {total_tasks}")
        logger.info(f"  Correct: {correct_count}")
        logger.info(f"  Accuracy: {accuracy:.2%}")
    
    # Save comparison results
    output_file = "agent_comparison_new_html_match.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)
    
    logger.info(f"\nComparison results saved to: {output_file}")
    
    # Print final comparison
    if len(all_results) >= 2:
        logger.info(f"\n📊 FINAL COMPARISON:")
        for agent_name, results in all_results.items():
            summary = results['summary']
            logger.info(f"  {agent_name}: {summary['accuracy']:.2%} ({summary['correct_count']}/{summary['total_tasks']})")
    
    return all_results

def main():
    parser = argparse.ArgumentParser(description='Re-evaluate agent logs using project evaluation framework')
    parser.add_argument('--agent-output-dir', 
                       default='/Users/jianhaonan/Desktop/API-Based-Agent/agent-output',
                       help='Directory containing agent output files')
    parser.add_argument('--output-dir', 
                       help='Directory to save re-evaluation results (default: {agent-output-dir}/re_evaluation_results)')
    
    # Single task evaluation options
    parser.add_argument('--task-id', type=int,
                       help='Evaluate a specific task ID')
    
    # File filtering options
    parser.add_argument('--file', 
                       help='Evaluate a specific JSONL file instead of all files')
    parser.add_argument('--sites', nargs='+',
                       help='Filter by site(s): map, shopping, gitlab, reddit, etc.')
    parser.add_argument('--eval-types', nargs='+',
                       help='Filter by evaluation type(s): url_match, string_match, program_html, etc.')
    parser.add_argument('--task-range', type=int, nargs=2, metavar=('START', 'END'),
                       help='Evaluate tasks in a specific ID range (inclusive)')
    parser.add_argument('--task-ids', type=int, nargs='+',
                       help='Evaluate specific task IDs')
    
    # New option to evaluate both agents
    parser.add_argument('--compare-agents', action='store_true',
                       help='Evaluate both our agent and baseline agent')
    
    # Display options
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Enable verbose logging and detailed output')
    parser.add_argument('--list-available', action='store_true',
                       help='List available tasks and exit')
    
    args = parser.parse_args()
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Initialize evaluator
    evaluator = AgentLogEvaluator(args.agent_output_dir)
    
    try:
        if args.compare_agents:
            # Evaluate both agents
            results = evaluate_both_agents()
            return 0
        
        if args.list_available:
            # List available tasks
            jsonl_files = evaluator.find_jsonl_files()
            all_tasks = {}
            for file_path in jsonl_files:
                results = evaluator.load_jsonl_results(file_path)
                for result in results:
                    task_id = result.get('task_id')
                    if task_id and task_id in evaluator.task_lookup:
                        task = evaluator.task_lookup[task_id]
                        all_tasks[task_id] = {
                            'sites': task.get('sites', []),
                            'eval_types': task.get('eval', {}).get('eval_types', []),
                            'intent': task.get('intent', '')[:80] + "..." if len(task.get('intent', '')) > 80 else task.get('intent', ''),
                            'source_file': file_path.name
                        }
            
            print(f"📋 Available tasks ({len(all_tasks)} total):")
            for task_id in sorted(all_tasks.keys()):
                task_info = all_tasks[task_id]
                print(f"  {task_id:3d}: {task_info['intent']}")
                print(f"       Sites: {', '.join(task_info['sites'])}")
                print(f"       Eval: {', '.join(task_info['eval_types'])}")
                print(f"       File: {task_info['source_file']}")
                print()
            return 0
        
        if args.task_id:
            # Evaluate single task
            if args.file:
                # If specific file is provided, use that file for the task
                file_path = Path(args.file)
                if not file_path.exists():
                    logger.error(f"File not found: {file_path}")
                    return 1
                
                # Load results from specific file
                results = evaluator.load_jsonl_results(file_path)
                task_result = None
                for result in results:
                    if result.get('task_id') == args.task_id:
                        task_result = result
                        break
                
                if not task_result:
                    logger.error(f"Task {args.task_id} not found in {file_path}")
                    return 1
                
                # Get task configuration
                task = evaluator.task_lookup.get(args.task_id)
                if not task:
                    logger.error(f"Task {args.task_id} not found in task definitions")
                    return 1
                
                if args.verbose:
                    print(f"\n{'='*60}")
                    print(f"EVALUATING TASK {args.task_id}")
                    print(f"{'='*60}")
                    print(f"Intent: {task.get('intent', 'N/A')}")
                    print(f"Sites: {', '.join(task.get('sites', []))}")
                    print(f"Evaluation Types: {', '.join(task.get('eval', {}).get('eval_types', []))}")
                    print(f"Source File: {file_path}")
                    print(f"Original Correct: {task_result.get('correct', 'N/A')}")
                    print(f"{'='*60}")
                
                agent_response = evaluator.extract_agent_response(task_result)
                result = evaluator.re_evaluate_task(args.task_id, agent_response, task_result, jsonl_file_path=file_path)
                
                # Enhanced result with task info
                enhanced_result = {
                    **result,
                    'task_info': {
                        'intent': task.get('intent', ''),
                        'sites': task.get('sites', []),
                        'eval_types': task.get('eval', {}).get('eval_types', []),
                        'source_file': str(file_path)
                    },
                    'original_result': {
                        'correct': task_result.get('correct', False),
                        'agent_response_preview': agent_response[:200] + "..." if len(agent_response) > 200 else agent_response
                    },
                    'agreement': task_result.get('correct', False) == result.get('correct', False)
                }
                
                if args.verbose:
                    print(f"\n🔍 DETAILED EVALUATION RESULTS")
                    print(f"✅ New Correct (Last Response): {'YES' if result.get('correct') else 'NO'}")
                    print(f"✅ New Correct (All History): {'YES' if result.get('correct_all_history') else 'NO'}")
                    print(f"📊 Original Correct: {'YES' if task_result.get('correct') else 'NO'}")
                    print(f"🔄 Agreement: {'YES' if enhanced_result.get('agreement') else 'NO'}")
                    
                    if result.get('error'):
                        print(f"❌ Error: {result['error']}")
                    
                    # Show agent response preview
                    print(f"💬 Agent Response Preview:")
                    print(f"   {agent_response[:200]}...")
                
                result = enhanced_result
            else:
                # Use original single task evaluation (searches all files)
                result = evaluator.evaluate_single_task(args.task_id, verbose=args.verbose)
            
            if args.output_dir:
                output_dir = Path(args.output_dir)
                output_dir.mkdir(parents=True, exist_ok=True)
                output_file = output_dir / f"task_{args.task_id}_evaluation.json"
                with open(output_file, 'w', encoding='utf-8') as f:
                    json.dump(result, f, indent=2, ensure_ascii=False)
                print(f"\n💾 Results saved to {output_file}")
            
            if not args.verbose:
                # Show brief summary if not verbose
                print(f"\n📊 Task {args.task_id} Summary:")
                print(f"  New Correct: {'YES' if result.get('correct') else 'NO'}")
                print(f"  Original Correct: {'YES' if result.get('original_result', {}).get('correct') else 'NO'}")
                print(f"  Agreement: {'YES' if result.get('agreement') else 'NO'}")
                if result.get('error'):
                    print(f"  Error: {result['error']}")
            
            return 0
        
        # Build task filter
        task_filter = {}
        if args.sites:
            task_filter['sites'] = args.sites
        if args.eval_types:
            task_filter['eval_types'] = args.eval_types
        if args.task_range:
            task_filter['task_range'] = tuple(args.task_range)
        if args.task_ids:
            task_filter['task_ids'] = args.task_ids
        
        if args.file:
            # Evaluate specific file with filters
            file_path = Path(args.file)
            if not file_path.exists():
                logger.error(f"File not found: {file_path}")
                return 1
            
            output_file = None
            if args.output_dir:
                output_dir = Path(args.output_dir)
                output_dir.mkdir(parents=True, exist_ok=True)
                filter_suffix = ""
                if task_filter:
                    filter_parts = []
                    if task_filter.get('sites'):
                        filter_parts.append(f"sites_{'_'.join(task_filter['sites'])}")
                    if task_filter.get('eval_types'):
                        filter_parts.append(f"eval_{'_'.join(task_filter['eval_types'])}")
                    if task_filter.get('task_range'):
                        start, end = task_filter['task_range']
                        filter_parts.append(f"range_{start}_{end}")
                    if filter_parts:
                        filter_suffix = f"_{'_'.join(filter_parts)}"
                output_file = output_dir / f"re_eval_{file_path.stem}{filter_suffix}.json"
            
            results = evaluator.evaluate_jsonl_file(file_path, output_file, task_filter)
            print(f"\n📊 Results for {file_path}:")
            print(f"Total tasks: {results['summary']['total_tasks']}")
            print(f"Accuracy (last response): {results['summary']['accuracy_last_response']:.2%}")
            print(f"Accuracy (all history): {results['summary']['accuracy_all_history']:.2%}")
            
        elif task_filter:
            # Apply filters to all files
            logger.error("Filters can only be used with --file option currently. Use --file to specify a JSONL file.")
            return 1
        else:
            # Evaluate all files (original behavior)
            results = evaluator.evaluate_all(args.output_dir)
            print(f"\nEvaluation complete. Found {len(results)} files.")
            
    except KeyboardInterrupt:
        logger.info("Evaluation interrupted by user")
        return 1
    except Exception as e:
        logger.error(f"Evaluation failed: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())