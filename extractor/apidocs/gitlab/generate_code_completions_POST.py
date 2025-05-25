import requests, json
from urllib.parse import quote


def generate_code_completions(current_file=None, intent=None, stream=None, project_path=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/code_suggestions/completions"
    payload = {'current_file': current_file, 'intent': intent, 'stream': stream, 'project_path': project_path, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert current_file is not None, 'Missing required parameter: current_file'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = generate_code_completions(current_file={'file_name': 'car.py', 'content_above_cursor': 'class Car:\n def __init__(self):\n self.is_running = False\n self.speed = 0\n def increase_speed(self, increment):', 'content_below_cursor': ''}, intent='''completion''', stream=False, project_path='''group/project_name''')
    r_json = None
    try:
        r_json = r.json()
    except:
        pass
    import json
    result_dict = dict()
    result_dict['status_code'] = r.status_code
    result_dict['text'] = r.text
    result_dict['json'] = r_json
    result_dict['content'] = r.content.decode("utf-8")
    print(json.dumps(result_dict, indent=4))

