import requests, json
from urllib.parse import quote


def create_new_snippet_thread(body=None, id=None, snippet_id=None, created_at=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/projects/:id/snippets/:snippet_id/discussions"
    payload = {'body': body, 'id': id, 'snippet_id': snippet_id, 'created_at': created_at, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    assert body is not None, 'Missing required parameter: body'
    assert id is not None, 'Missing required parameter: id'
    assert snippet_id is not None, 'Missing required parameter: snippet_id'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = create_new_snippet_thread(body='''This is a new snippet discussion.''', id=5, snippet_id=11, created_at='''2016-03-11T03:45:40Z''')
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

