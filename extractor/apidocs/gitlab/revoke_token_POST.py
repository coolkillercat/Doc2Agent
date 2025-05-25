import requests, json
from urllib.parse import quote


def revoke_token(client_id=None, client_secret=None, token=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/oauth/revoke"
    payload = {'client_id': client_id, 'client_secret': client_secret, 'token': token, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    assert client_id is not None, 'Missing required parameter: client_id'
    assert client_secret is not None, 'Missing required parameter: client_secret'
    assert token is not None, 'Missing required parameter: token'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = revoke_token(client_id='''APP_ID''', client_secret='''APP_SECRET''', token='''TOKEN''')
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

