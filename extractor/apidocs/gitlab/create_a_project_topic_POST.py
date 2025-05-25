import requests, json
from urllib.parse import quote


def create_a_project_topic(name=None, title=None, avatar=None, description=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/topics"
    payload = {'name': name, 'title': title, 'avatar': avatar, 'description': description, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert name is not None, 'Missing required parameter: name'
    assert title is not None, 'Missing required parameter: title'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = create_a_project_topic(name='''topic1''', title='''Topic 1''', avatar=http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/path/to/avatar.png, description='''A description of the topic''')
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

