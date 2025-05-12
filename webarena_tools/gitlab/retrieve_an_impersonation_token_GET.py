import requests
from urllib.parse import quote
                
def retrieve_an_impersonation_token(user_id=None, impersonation_token_id=None):
    api_url = f"/api/v4/users/{quote(user_id, safe='')}/impersonation_tokens/{quote(impersonation_token_id, safe='')}"
    querystring = {'user_id': user_id, 'impersonation_token_id': impersonation_token_id, }
    assert user_id is not None, 'Missing required parameter: user_id'
    assert impersonation_token_id is not None, 'Missing required parameter: impersonation_token_id'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = retrieve_an_impersonation_token(user_id='''123''', impersonation_token_id='''456''')
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

