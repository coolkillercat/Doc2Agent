import requests, json
from urllib.parse import quote


def list_groups(skip_groups=None, all_available=None, search=None, order_by=None, sort=None, statistics=None, visibility=None, with_custom_attributes=None, owned=None, min_access_level=None, top_level_only=None, repository_storage=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/groups"
    querystring = {'skip_groups': skip_groups, 'all_available': all_available, 'search': search, 'order_by': order_by, 'sort': sort, 'statistics': statistics, 'visibility': visibility, 'with_custom_attributes': with_custom_attributes, 'owned': owned, 'min_access_level': min_access_level, 'top_level_only': top_level_only, 'repository_storage': repository_storage, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    
    response = requests.get(url=api_url, headers=headers, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = list_groups(skip_groups=[1, 2, 3], all_available=false, search='''example-group''', order_by='''name''', sort='''asc''', statistics=true, visibility='''public''', with_custom_attributes=true, owned=true, min_access_level=30, top_level_only=true, repository_storage='''default''')
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

