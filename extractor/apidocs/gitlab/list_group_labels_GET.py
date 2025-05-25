import requests, json
from urllib.parse import quote


def list_group_labels(id=None, with_counts=false, include_ancestor_groups=true, include_descendant_groups=false, only_group_labels=true, search=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/groups/{quote(id, safe='')}/labels"
    querystring = {'id': id, 'with_counts': with_counts, 'include_ancestor_groups': include_ancestor_groups, 'include_descendant_groups': include_descendant_groups, 'only_group_labels': only_group_labels, 'search': search, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    assert id is not None, 'Missing required parameter: id'
    
    response = requests.get(url=api_url, headers=headers, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = list_group_labels(id=5, with_counts=true, include_ancestor_groups=true, include_descendant_groups=false, only_group_labels=true, search='''bug''')
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

