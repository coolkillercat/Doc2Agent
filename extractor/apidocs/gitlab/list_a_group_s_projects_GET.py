import requests, json
from urllib.parse import quote


def list_a_group_s_projects(id=None, archived=None, visibility=None, order_by=None, sort=None, search=None, simple=None, owned=None, starred=None, topic=None, with_issues_enabled=None, with_merge_requests_enabled=None, with_shared=None, include_subgroups=None, min_access_level=None, with_custom_attributes=None, with_security_reports=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/groups/{quote(id, safe='')}/projects"
    querystring = {'id': id, 'archived': archived, 'visibility': visibility, 'order_by': order_by, 'sort': sort, 'search': search, 'simple': simple, 'owned': owned, 'starred': starred, 'topic': topic, 'with_issues_enabled': with_issues_enabled, 'with_merge_requests_enabled': with_merge_requests_enabled, 'with_shared': with_shared, 'include_subgroups': include_subgroups, 'min_access_level': min_access_level, 'with_custom_attributes': with_custom_attributes, 'with_security_reports': with_security_reports, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert id is not None, 'Missing required parameter: id'
    
    response = requests.get(url=api_url, headers=headers, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = list_a_group_s_projects(id=123, archived=false, visibility='''public''', order_by='''created_at''', sort='''desc''', search='''example-project''', simple=true, owned=true, starred=true, topic='''devops''', with_issues_enabled=true, with_merge_requests_enabled=true, with_shared=true, include_subgroups=false, min_access_level=30, with_custom_attributes=true, with_security_reports=false)
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

