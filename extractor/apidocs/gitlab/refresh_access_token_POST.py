import requests, json
from urllib.parse import quote


def refresh_access_token(client_id=None, refresh_token=None, grant_type=None, redirect_uri=None, code_verifier=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/oauth/token"
    payload = {'client_id': client_id, 'refresh_token': refresh_token, 'grant_type': grant_type, 'redirect_uri': redirect_uri, 'code_verifier': code_verifier, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert client_id is not None, 'Missing required parameter: client_id'
    assert refresh_token is not None, 'Missing required parameter: refresh_token'
    assert grant_type is not None, 'Missing required parameter: grant_type'
    assert redirect_uri is not None, 'Missing required parameter: redirect_uri'
    assert code_verifier is not None, 'Missing required parameter: code_verifier'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = refresh_access_token(client_id='''APP_ID''', refresh_token='''REFRESH_TOKEN''', grant_type='''refresh_token''', redirect_uri='''https://example.com/oauth/redirect''', code_verifier='''ks02i3jdikdo2k0dkfodf3m39rjfjsdk0wk349rj3jrhf''')
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

