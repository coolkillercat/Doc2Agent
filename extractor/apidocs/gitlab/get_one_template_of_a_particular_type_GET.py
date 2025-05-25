import requests, json
from urllib.parse import quote


def get_one_template_of_a_particular_type(id=None, name=None, type=None, fullname=None, project=None, source_template_project_id=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/projects/{quote(id, safe='')}/templates/{quote(type, safe='')}/{quote(name, safe='')}"
    querystring = {'id': id, 'name': name, 'type': type, 'fullname': fullname, 'project': project, 'source_template_project_id': source_template_project_id, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    assert id is not None, 'Missing required parameter: id'
    assert name is not None, 'Missing required parameter: name'
    assert type is not None, 'Missing required parameter: type'
    
    response = requests.get(url=api_url, headers=headers, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_one_template_of_a_particular_type(id=123, name='''mit''', type='''licenses''', fullname='''John Doe''', project='''MyProject''', source_template_project_id=456)
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

