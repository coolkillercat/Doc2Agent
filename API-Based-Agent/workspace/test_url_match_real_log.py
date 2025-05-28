import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), '../evaluation/webarena'))
)
from evaluation.webarena.utils import url_match

# Set up configs for the test (negative case: non-existent endpoint)
configs = {
    'eval': {
        'eval_types': ['url_match'],
        'reference_url': 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/does_not_exist',
        'url_note': 'GOLD in PRED',
    }
}

pred = ''

# Read the real log file
log_path = '../evaluation/evaluation_outputs/outputs/CodeActAgent/gpt-4o_maxiter_18_N_v1.6_/logs/instance_375.log'
with open(log_path, 'r') as f:
    history = f.read()

# Run url_match
result = url_match(configs, pred, history, check_all_history=True)
print('url_match result:', result)
