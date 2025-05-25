import requests, json
from urllib.parse import quote


def create_user(email=None, name=None, username=None, password=None, reset_password=None, force_random_password=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/users"
    payload = {'email': email, 'name': name, 'username': username, 'password': password, 'reset_password': reset_password, 'force_random_password': force_random_password, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert email is not None, 'Missing required parameter: email'
    assert name is not None, 'Missing required parameter: name'
    assert username is not None, 'Missing required parameter: username'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = create_user(email='''newuser@example.com''', name='''New User''', username='''newuser''', password='''securepassword''', reset_password=True, force_random_password=True)
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

