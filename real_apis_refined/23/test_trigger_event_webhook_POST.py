import requests
from urllib.parse import quote
                
def test_trigger_event_webhook(connection_id=None, trigger_id=None, user_id=None, user_feature_id=None):
    api_url = f"https://connect.ifttt.com/v2/connections/{{connection_id}}/triggers/{{trigger_id}}/test"
    payload = {'connection_id': connection_id, 'trigger_id': trigger_id, 'user_id': user_id, 'user_feature_id': user_feature_id, }
    assert connection_id is not None, 'Missing required parameter: connection_id'
    assert trigger_id is not None, 'Missing required parameter: trigger_id'
    assert user_id is not None, 'Missing required parameter: user_id'
    
    response = requests.post(url=api_url, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = test_trigger_event_webhook(connection_id='''C8p3q9T6''', trigger_id='''acme_cloud_storage.new_file_added''', user_id='''123''', user_feature_id='''90276cb1-e8ff-4718-a34f-c73cf75c49cf''')
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

