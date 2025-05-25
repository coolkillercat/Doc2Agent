import requests, json
from urllib.parse import quote


def request_authorization_code_with_pkce(client_id=None, redirect_uri=None, response_type=None, state=None, scope=None, code_challenge=None, code_challenge_method=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/oauth/authorize"
    querystring = {'client_id': client_id, 'redirect_uri': redirect_uri, 'response_type': response_type, 'state': state, 'scope': scope, 'code_challenge': code_challenge, 'code_challenge_method': code_challenge_method, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert client_id is not None, 'Missing required parameter: client_id'
    assert redirect_uri is not None, 'Missing required parameter: redirect_uri'
    assert response_type is not None, 'Missing required parameter: response_type'
    assert state is not None, 'Missing required parameter: state'
    assert scope is not None, 'Missing required parameter: scope'
    assert code_challenge is not None, 'Missing required parameter: code_challenge'
    assert code_challenge_method is not None, 'Missing required parameter: code_challenge_method'
    
    response = requests.get(url=api_url, headers=headers, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = request_authorization_code_with_pkce(client_id='''APP_ID''', redirect_uri='''https://example.com/oauth/redirect''', response_type='''code''', state='''random_state_value''', scope='''read_user profile''', code_challenge='''2i0WFA-0AerkjQm4X4oDEhqA17QIAKNjXpagHBXmO_U''', code_challenge_method='''S256''')
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

