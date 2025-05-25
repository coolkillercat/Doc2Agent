import requests, json
from urllib.parse import quote


def create_a_broadcast_message(message=None, starts_at=current time in UTC, ends_at=one hour from current time in UTC, font=None, target_access_levels=None, target_path=None, broadcast_type='banner', dismissable=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/broadcast_messages"
    payload = {'message': message, 'starts_at': starts_at, 'ends_at': ends_at, 'font': font, 'target_access_levels': target_access_levels, 'target_path': target_path, 'broadcast_type': broadcast_type, 'dismissable': dismissable, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert message is not None, 'Missing required parameter: message'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = create_a_broadcast_message(message='''Deploy in progress''', starts_at=2019-03-15T08:00:00Z, ends_at=2019-03-15T09:00:00Z, font='''#FFFFFF''', target_access_levels=[10, 30], target_path='''*/welcome''', broadcast_type='''notification''', dismissable=False)
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

