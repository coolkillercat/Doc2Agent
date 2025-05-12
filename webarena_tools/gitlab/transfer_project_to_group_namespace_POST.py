import requests
from urllib.parse import quote
                
def transfer_project_to_group_namespace(id=None, project_id=None):
    api_url = f"/api/v4/groups/{id}/projects/{project_id}"
    payload = {'id': id, 'project_id': project_id, }
    assert id is not None, 'Missing required parameter: id'
    assert project_id is not None, 'Missing required parameter: project_id'
    
    response = requests.post(url=api_url, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = transfer_project_to_group_namespace(id='''123''', project_id='''456''')
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

