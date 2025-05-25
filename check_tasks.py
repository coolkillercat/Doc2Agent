import json

# Load the task.json file
with open('task.json', 'r') as f:
    tasks = json.load(f)

# Find all map tasks and their intent templates
map_tasks = []
unique_templates = set()  # Initialize set for unique templates

for task in tasks:
    if task.get('start_url') == '__SHOPPING__':
        template = task.get('intent_template')
        map_tasks.append({
            'task_id': task.get('task_id'),
            'intent_template': template
        })
        unique_templates.add(template)  # Add template to set

# Print unique intent templates
print("\nUnique intent templates for shopping tasks:")
for template in sorted(unique_templates):
    print(f"- {template}")

# # Print all map tasks with their templates
# print("\nAll map tasks:")
# for task in map_tasks:
#     print(f"Task {task['task_id']}: {task['intent_template']}")
