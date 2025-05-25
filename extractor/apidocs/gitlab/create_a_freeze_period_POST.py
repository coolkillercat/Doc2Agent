import requests, json
from urllib.parse import quote


def create_a_freeze_period(id=None, freeze_start=None, freeze_end=None, cron_timezone=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/projects/19/freeze_periods"
    payload = {'id': id, 'freeze_start': freeze_start, 'freeze_end': freeze_end, 'cron_timezone': cron_timezone, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert id is not None, 'Missing required parameter: id'
    assert freeze_start is not None, 'Missing required parameter: freeze_start'
    assert freeze_end is not None, 'Missing required parameter: freeze_end'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = create_a_freeze_period(id=19, freeze_start='''0 23 * * 5''', freeze_end='''0 7 * * 1''', cron_timezone='''UTC''')
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

