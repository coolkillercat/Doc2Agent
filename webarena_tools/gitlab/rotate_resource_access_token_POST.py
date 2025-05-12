import requests
from urllib.parse import quote
                
def rotate_resource_access_token(id=None, token_id=None):
    api_url = f"/api/v4/groups/{id}/access_tokens/{token_id}/rotate"
    payload = {'id': id, 'token_id': token_id, }
    assert id is not None, 'Missing required parameter: id'
    assert token_id is not None, 'Missing required parameter: token_id'
    
    response = requests.post(url=api_url, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = rotate_resource_access_token(id='''123''', token_id='''456''')
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

