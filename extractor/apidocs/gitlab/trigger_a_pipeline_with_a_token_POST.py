import requests, json
from urllib.parse import quote


def trigger_a_pipeline_with_a_token(id=None, ref=None, token=None, variables=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/projects/:id/trigger/pipeline"
    payload = {'id': id, 'ref': ref, 'token': token, 'variables': variables, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    assert id is not None, 'Missing required parameter: id'
    assert ref is not None, 'Missing required parameter: ref'
    assert token is not None, 'Missing required parameter: token'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = trigger_a_pipeline_with_a_token(id=123, ref='''main''', token='''2cb1840fb9dfc9fb0b7b1609cd29cb''', variables={ VAR1: "value1", VAR2: "value2" })
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

