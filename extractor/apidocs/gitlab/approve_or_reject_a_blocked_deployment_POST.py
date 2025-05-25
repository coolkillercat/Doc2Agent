import requests, json
from urllib.parse import quote


def approve_or_reject_a_blocked_deployment(id=None, deployment_id=None, status=None, comment=None, represented_as=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/projects/:id/deployments/:deployment_id/approval"
    payload = {'id': id, 'deployment_id': deployment_id, 'status': status, 'comment': comment, 'represented_as': represented_as, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    assert id is not None, 'Missing required parameter: id'
    assert deployment_id is not None, 'Missing required parameter: deployment_id'
    assert status is not None, 'Missing required parameter: status'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = approve_or_reject_a_blocked_deployment(id=1, deployment_id=42, status='''approved''', comment='''Looks good to me''', represented_as='''security''')
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

