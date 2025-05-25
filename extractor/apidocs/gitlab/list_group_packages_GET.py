import requests, json
from urllib.parse import quote


def list_group_packages(id=None, exclude_subgroups=None, order_by=None, sort=None, package_type=None, package_name=None, package_version=None, include_versionless=None, status=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/groups/{quote(id, safe='')}/packages"
    querystring = {'id': id, 'exclude_subgroups': exclude_subgroups, 'order_by': order_by, 'sort': sort, 'package_type': package_type, 'package_name': package_name, 'package_version': package_version, 'include_versionless': include_versionless, 'status': status, }
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
    r = list_group_packages(id=456, exclude_subgroups=false, order_by='''created_at''', sort='''asc''', package_type='''npm''', package_name='''foo''', package_version='''1.0.3''', include_versionless=true, status='''error''')
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

