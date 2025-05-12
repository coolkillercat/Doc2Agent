import requests
from urllib.parse import quote
                
def revoke_a_gpg_key(id=None, key_id=None):
    api_url = f"/api/v4/users/{id}/gpg_keys/{key_id}/revoke"
    payload = {'id': id, 'key_id': key_id, }
    assert id is not None, 'Missing required parameter: id'
    assert key_id is not None, 'Missing required parameter: key_id'
    
    response = requests.post(url=api_url, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = revoke_a_gpg_key(id='''123''', key_id='''789''')
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

