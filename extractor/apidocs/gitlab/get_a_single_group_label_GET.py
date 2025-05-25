import requests, json
from urllib.parse import quote


def get_a_single_group_label(id=None, label_id=None, include_ancestor_groups=true, include_descendant_groups=false, only_group_labels=true):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/groups/{quote(id, safe='')}/labels/{quote(label_id, safe='')}"
    querystring = {'id': id, 'label_id': label_id, 'include_ancestor_groups': include_ancestor_groups, 'include_descendant_groups': include_descendant_groups, 'only_group_labels': only_group_labels, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    assert id is not None, 'Missing required parameter: id'
    assert label_id is not None, 'Missing required parameter: label_id'
    
    response = requests.get(url=api_url, headers=headers, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_a_single_group_label(id=5, label_id=bug, include_ancestor_groups=true, include_descendant_groups=false, only_group_labels=true)
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

