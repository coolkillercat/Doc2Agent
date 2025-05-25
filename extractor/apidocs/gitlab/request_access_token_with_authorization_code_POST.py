import requests, json
from urllib.parse import quote


def request_access_token_with_authorization_code(client_id=None, code=None, grant_type=None, redirect_uri=None, code_verifier=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/oauth/token"
    payload = {'client_id': client_id, 'code': code, 'grant_type': grant_type, 'redirect_uri': redirect_uri, 'code_verifier': code_verifier, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    assert client_id is not None, 'Missing required parameter: client_id'
    assert code is not None, 'Missing required parameter: code'
    assert grant_type is not None, 'Missing required parameter: grant_type'
    assert redirect_uri is not None, 'Missing required parameter: redirect_uri'
    assert code_verifier is not None, 'Missing required parameter: code_verifier'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = request_access_token_with_authorization_code(client_id='''APP_ID''', code='''RETURNED_CODE''', grant_type='''authorization_code''', redirect_uri='''https://example.com/oauth/redirect''', code_verifier='''ks02i3jdikdo2k0dkfodf3m39rjfjsdk0wk349rj3jrhf''')
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

