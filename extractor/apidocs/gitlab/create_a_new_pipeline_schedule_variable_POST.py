import requests, json
from urllib.parse import quote


def create_a_new_pipeline_schedule_variable(id=None, key=None, pipeline_schedule_id=None, value=None, variable_type=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/projects/:id/pipeline_schedules/:pipeline_schedule_id/variables"
    payload = {'id': id, 'key': key, 'pipeline_schedule_id': pipeline_schedule_id, 'value': value, 'variable_type': variable_type, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    assert id is not None, 'Missing required parameter: id'
    assert key is not None, 'Missing required parameter: key'
    assert pipeline_schedule_id is not None, 'Missing required parameter: pipeline_schedule_id'
    assert value is not None, 'Missing required parameter: value'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = create_a_new_pipeline_schedule_variable(id=29, key='''NEW_VARIABLE''', pipeline_schedule_id=13, value='''new value''', variable_type='''env_var''')
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

