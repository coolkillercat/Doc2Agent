import requests
from urllib.parse import quote
                
def perform_a_query(connection_id=None, query_id=None, user_id=None, fields=None, includes=None, limit=None, cursor=None):
    api_url = f"https://connect.ifttt.com/v2/connections/{{connection_id}}/queries/{{query_id}}/perform"
    payload = {'connection_id': connection_id, 'query_id': query_id, 'user_id': user_id, 'fields': fields, 'includes': includes, 'limit': limit, 'cursor': cursor, }
    assert connection_id is not None, 'Missing required parameter: connection_id'
    assert query_id is not None, 'Missing required parameter: query_id'
    assert user_id is not None, 'Missing required parameter: user_id'
    
    response = requests.post(url=api_url, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = perform_a_query(connection_id='''C8p3q9T6''', query_id='''acme_cloud_storage.list_files''', user_id='''123''', fields={'folder_name': 'aBwLdm2ydHVya0BQbWFpbC8jb22=;2641ab0g'}, includes=['versions'], limit=1, cursor='''151517700064544d60c3a02405f8bd5520d3e31571''')
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

