import requests, json
from urllib.parse import quote


def create_a_new_pipeline_schedule(cron=None, description=None, id=None, ref=None, active=None, cron_timezone=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/projects/:id/pipeline_schedules"
    payload = {'cron': cron, 'description': description, 'id': id, 'ref': ref, 'active': active, 'cron_timezone': cron_timezone, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert cron is not None, 'Missing required parameter: cron'
    assert description is not None, 'Missing required parameter: description'
    assert id is not None, 'Missing required parameter: id'
    assert ref is not None, 'Missing required parameter: ref'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = create_a_new_pipeline_schedule(cron='''0 1 * * *''', description='''Build packages''', id=29, ref='''main''', active=true, cron_timezone='''UTC''')
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

