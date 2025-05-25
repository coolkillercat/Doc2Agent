import requests, json
from urllib.parse import quote


def preview_a_badge_from_a_project(id=None, link_url=None, image_url=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/projects/{quote(id, safe='')}/badges/render"
    querystring = {'id': id, 'link_url': link_url, 'image_url': image_url, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    assert id is not None, 'Missing required parameter: id'
    assert link_url is not None, 'Missing required parameter: link_url'
    assert image_url is not None, 'Missing required parameter: image_url'
    
    response = requests.get(url=api_url, headers=headers, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = preview_a_badge_from_a_project(id=123, link_url='''http://example.com/ci_status.svg?project=%{project_path}&ref=%{default_branch}''', image_url='''https://shields.io/my/badge''')
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

