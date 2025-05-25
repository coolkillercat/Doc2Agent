import requests, json
from urllib.parse import quote


def take_ownership_of_a_pipeline_schedule(id=None, pipeline_schedule_id=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/projects/:id/pipeline_schedules/:pipeline_schedule_id/take_ownership"
    payload = {'id': id, 'pipeline_schedule_id': pipeline_schedule_id, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert id is not None, 'Missing required parameter: id'
    assert pipeline_schedule_id is not None, 'Missing required parameter: pipeline_schedule_id'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = take_ownership_of_a_pipeline_schedule(id=29, pipeline_schedule_id=13)
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

