import json
import os
import glob
from collections import defaultdict

def load_task_info():
    """Load task information from glycan_tasks_classified.jsonl"""
    tasks = {}
    with open("glycan_tasks_classified.jsonl", "r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            task_data = json.loads(line)
            tasks[i] = {
                'site': task_data.get('site', ''),
                'task_type': task_data.get('task_type', ''),
                'expected_trajectory': task_data.get('expected_trajectory', ''),
                'is_multi_tool': i > 30  # Tasks 31-50 are multi-tool tasks
            }
    return tasks

def load_claude_results():
    """Load Claude evaluation results"""
    results = {}
    eval_files = glob.glob("claude_logs/*_evaluation.json")
    for file_path in eval_files:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            task_id = data.get('task_id')
            success = data.get('evaluation_result', {}).get('success', False)
            results[task_id] = success
    return results

def load_codeact_results():
    """Load CodeAct evaluation results"""
    results = {}
    eval_files = glob.glob("codeact_logs/instance_*_evaluation.json")
    for file_path in eval_files:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            task_id = data.get('task_id') + 1  # CodeAct seems to be 0-indexed
            success = data.get('evaluation_result', {}).get('success', False)
            results[task_id] = success
    return results

def load_qwen3_results():
    """Load Qwen3 evaluation results"""
    results = {}
    eval_files = glob.glob("qwen3_logs/task_*_evaluation.json")
    for file_path in eval_files:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            task_id = data.get('task_id')
            success = data.get('evaluation_result', {}).get('success', False)
            results[task_id] = success
    return results

def categorize_task_type(task_type):
    """Categorize task types into broader categories"""
    # Category 1: Data Retrieval & Query
    if any(term in task_type.lower() for term in ['retrieval', 'query', 'database', 'search', 'identification', 'mapping', 'data']):
        return "Data Retrieval & Query"
    
    # Category 2: Analysis & Visualization
    if any(term in task_type.lower() for term in ['analysis', 'visualization', 'validation', 'comparison', 'interaction', 'characterization', 'investigation']):
        return "Analysis & Visualization"
    
    # Category 3: Transformation & Conversion
    if any(term in task_type.lower() for term in ['conversion', 'format', 'mass', 'property', 'calculation']):
        return "Transformation & Conversion"
    
    # Default category for anything that doesn't clearly fit
    return "Analysis & Visualization"  # Using most common as default

def main():
    # Load task information and results
    tasks = load_task_info()
    claude_results = load_claude_results()
    codeact_results = load_codeact_results()
    qwen3_results = load_qwen3_results()
    
    # Find achievable tasks (union of successful tasks across all approaches)
    achievable_tasks = set()
    for task_id in tasks:
        if (claude_results.get(task_id, False) or 
            codeact_results.get(task_id, False) or 
            qwen3_results.get(task_id, False)):
            achievable_tasks.add(task_id)
    
    print(f"Achievable tasks: {sorted(list(achievable_tasks))}")
    print(f"Total achievable tasks: {len(achievable_tasks)} out of {len(tasks)}\n")
    
    # Calculate overall success rates for achievable tasks only
    claude_success_rate = sum(claude_results.get(t, False) for t in achievable_tasks) / len(achievable_tasks) * 100
    codeact_success_rate = sum(codeact_results.get(t, False) for t in achievable_tasks) / len(achievable_tasks) * 100
    qwen3_success_rate = sum(qwen3_results.get(t, False) for t in achievable_tasks) / len(achievable_tasks) * 100
    
    print(f"Overall success rates (achievable tasks only):")
    print(f"Claude: {claude_success_rate:.2f}%")
    print(f"CodeAct: {codeact_success_rate:.2f}%")
    print(f"Qwen3: {qwen3_success_rate:.2f}%\n")
    
    # Success rates by task difficulty
    single_tool_tasks = [t for t in achievable_tasks if not tasks[t]['is_multi_tool']]
    multi_tool_tasks = [t for t in achievable_tasks if tasks[t]['is_multi_tool']]
    
    if single_tool_tasks:
        claude_single_tool_rate = sum(claude_results.get(t, False) for t in single_tool_tasks) / len(single_tool_tasks) * 100
        codeact_single_tool_rate = sum(codeact_results.get(t, False) for t in single_tool_tasks) / len(single_tool_tasks) * 100
        qwen3_single_tool_rate = sum(qwen3_results.get(t, False) for t in single_tool_tasks) / len(single_tool_tasks) * 100
        
        print(f"Success rates by task difficulty (achievable tasks only):")
        print(f"Single-tool tasks (1-30):")
        print(f"  Claude: {claude_single_tool_rate:.2f}%")
        print(f"  CodeAct: {codeact_single_tool_rate:.2f}%")
        print(f"  Qwen3: {qwen3_single_tool_rate:.2f}%")
    
    if multi_tool_tasks:
        claude_multi_tool_rate = sum(claude_results.get(t, False) for t in multi_tool_tasks) / len(multi_tool_tasks) * 100
        codeact_multi_tool_rate = sum(codeact_results.get(t, False) for t in multi_tool_tasks) / len(multi_tool_tasks) * 100
        qwen3_multi_tool_rate = sum(qwen3_results.get(t, False) for t in multi_tool_tasks) / len(multi_tool_tasks) * 100
        
        print(f"\nMulti-tool tasks (31-50):")
        print(f"  Claude: {claude_multi_tool_rate:.2f}%")
        print(f"  CodeAct: {codeact_multi_tool_rate:.2f}%")
        print(f"  Qwen3: {qwen3_multi_tool_rate:.2f}%\n")
    
    # Success rates by task site
    site_tasks = defaultdict(list)
    achievable_sites = set()
    
    # Only include sites from achievable tasks
    for task_id in achievable_tasks:
        sites = tasks[task_id]['site'].split(' → ')
        for site in sites:
            site_tasks[site].append(task_id)
            achievable_sites.add(site)
    
    print(f"Success rates by task site (achievable tasks only):")
    for site, task_ids in sorted(site_tasks.items()):
        if len(task_ids) == 0:
            continue
        
        claude_site_rate = sum(claude_results.get(t, False) for t in task_ids) / len(task_ids) * 100
        codeact_site_rate = sum(codeact_results.get(t, False) for t in task_ids) / len(task_ids) * 100
        qwen3_site_rate = sum(qwen3_results.get(t, False) for t in task_ids) / len(task_ids) * 100
        
        print(f"\n{site} ({len(task_ids)} tasks):")
        print(f"  Claude: {claude_site_rate:.2f}%")
        print(f"  CodeAct: {codeact_site_rate:.2f}%")
        print(f"  Qwen3: {qwen3_site_rate:.2f}%")
    
    # Success rates by task type
    type_tasks = defaultdict(list)
    achievable_types = set()
    
    # Only include types from achievable tasks
    for task_id in achievable_tasks:
        task_type = tasks[task_id]['task_type'].strip('"')
        type_tasks[task_type].append(task_id)
        achievable_types.add(task_type)
    
    print(f"\nSuccess rates by task type (achievable tasks only):")
    for task_type, task_ids in sorted(type_tasks.items()):
        if len(task_ids) == 0:
            continue
        
        claude_type_rate = sum(claude_results.get(t, False) for t in task_ids) / len(task_ids) * 100
        codeact_type_rate = sum(codeact_results.get(t, False) for t in task_ids) / len(task_ids) * 100
        qwen3_type_rate = sum(qwen3_results.get(t, False) for t in task_ids) / len(task_ids) * 100
        
        print(f"\n{task_type} ({len(task_ids)} tasks):")
        print(f"  Claude: {claude_type_rate:.2f}%")
        print(f"  CodeAct: {codeact_type_rate:.2f}%")
        print(f"  Qwen3: {qwen3_type_rate:.2f}%")
        
    # Success rates by abstract categories
    print("\n" + "="*50)
    print("Success rates by abstract task categories (achievable tasks only):")
    print("="*50)
    
    # Initialize dictionaries to track tasks by category
    category_tasks = defaultdict(list)
    
    # Categorize each achievable task
    for task_id in achievable_tasks:
        task_type = tasks[task_id]['task_type'].strip('"')
        category = categorize_task_type(task_type)
        category_tasks[category].append(task_id)
    
    # Print success rates for each category
    total_tasks_by_category = {}
    
    for category, task_ids in sorted(category_tasks.items()):
        total_tasks_by_category[category] = len(task_ids)
        
        claude_category_rate = sum(claude_results.get(t, False) for t in task_ids) / len(task_ids) * 100
        codeact_category_rate = sum(codeact_results.get(t, False) for t in task_ids) / len(task_ids) * 100
        qwen3_category_rate = sum(qwen3_results.get(t, False) for t in task_ids) / len(task_ids) * 100
        
        print(f"\n{category} ({len(task_ids)} tasks):")
        print(f"  Claude: {claude_category_rate:.2f}%")
        print(f"  CodeAct: {codeact_category_rate:.2f}%")
        print(f"  Qwen3: {qwen3_category_rate:.2f}%")
        
        # Print the tasks in each category
        print("  Tasks in this category:")
        for task_id in task_ids:
            task_type = tasks[task_id]['task_type'].strip('"')
            print(f"    Task {task_id}: {task_type}")
    
    # Print total tasks by category
    print("\nTotal tasks by category:")
    for category, count in total_tasks_by_category.items():
        print(f"  {category}: {count} tasks")

if __name__ == "__main__":
    main()
