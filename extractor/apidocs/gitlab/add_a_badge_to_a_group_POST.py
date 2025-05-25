import requests, json
from urllib.parse import quote


def add_a_badge_to_a_group(id=None, link_url=None, image_url=None, name=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/groups/:id/badges"
    payload = {'id': id, 'link_url': link_url, 'image_url': image_url, 'name': name, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    assert id is not None, 'Missing required parameter: id'
    assert link_url is not None, 'Missing required parameter: link_url'
    assert image_url is not None, 'Missing required parameter: image_url'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = add_a_badge_to_a_group(id=123, link_url='''https://gitlab.com/gitlab-org/gitlab-foss/commits/master''', image_url='''https://shields.io/my/badge1''', name='''mybadge''')
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

