import requests
from urllib.parse import quote
                
def run_an_action(connection_id=None, action_id=None, user_id=None, fields=None, user_feature_id=None):
    api_url = f"https://connect.ifttt.com/v2/connections/{{connection_id}}/actions/{{action_id}}/run"
    payload = {'connection_id': connection_id, 'action_id': action_id, 'user_id': user_id, 'fields': fields, 'user_feature_id': user_feature_id, }
    assert connection_id is not None, 'Missing required parameter: connection_id'
    assert action_id is not None, 'Missing required parameter: action_id'
    assert user_id is not None, 'Missing required parameter: user_id'
    
    response = requests.post(url=api_url, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = run_an_action(connection_id='''C8p3q9T6''', action_id='''acme_cloud_storage.upload_from_url''', user_id='''123''', fields={'folder_name': 'aBwLdm2ydHVya0BQbWFpbC8jb22=;2641ab0g', 'filename': 'screenshot_04_23_1977', 'url': 'https://my.service/path/to/resource.png'}, user_feature_id='''4da42aa6-3858-4722-9ded-6a7ecdefd91f''')
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

