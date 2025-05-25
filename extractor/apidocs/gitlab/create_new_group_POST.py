import requests, json
from urllib.parse import quote


def create_new_group(name=None, path=None, auto_devops_enabled=None, avatar=None, default_branch=None, default_branch_protection=None, default_branch_protection_defaults=None, description=None, enabled_git_access_protocol=None, emails_disabled=None, emails_enabled=None, lfs_enabled=None, mentions_disabled=None, organization_id=None, parent_id=None, project_creation_level=None, request_access_enabled=None, require_two_factor_authentication=None, share_with_group_lock=None, subgroup_creation_level=None, two_factor_grace_period=None, visibility=None, membership_lock=None, extra_shared_runners_minutes_limit=None, shared_runners_minutes_limit=None, wiki_access_level=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/groups"
    payload = {'name': name, 'path': path, 'auto_devops_enabled': auto_devops_enabled, 'avatar': avatar, 'default_branch': default_branch, 'default_branch_protection': default_branch_protection, 'default_branch_protection_defaults': default_branch_protection_defaults, 'description': description, 'enabled_git_access_protocol': enabled_git_access_protocol, 'emails_disabled': emails_disabled, 'emails_enabled': emails_enabled, 'lfs_enabled': lfs_enabled, 'mentions_disabled': mentions_disabled, 'organization_id': organization_id, 'parent_id': parent_id, 'project_creation_level': project_creation_level, 'request_access_enabled': request_access_enabled, 'require_two_factor_authentication': require_two_factor_authentication, 'share_with_group_lock': share_with_group_lock, 'subgroup_creation_level': subgroup_creation_level, 'two_factor_grace_period': two_factor_grace_period, 'visibility': visibility, 'membership_lock': membership_lock, 'extra_shared_runners_minutes_limit': extra_shared_runners_minutes_limit, 'shared_runners_minutes_limit': shared_runners_minutes_limit, 'wiki_access_level': wiki_access_level, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    assert name is not None, 'Missing required parameter: name'
    assert path is not None, 'Missing required parameter: path'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = create_new_group(name='''New Group''', path='''new-group''', auto_devops_enabled=true, avatar=avatar.png, default_branch='''main''', default_branch_protection=2, default_branch_protection_defaults={ "allowed_to_push": [ { "access_level": 40 } ], "allow_force_push": false, "allowed_to_merge": [ { "access_level": 40 } ] }, description='''This is a new group''', enabled_git_access_protocol='''all''', emails_disabled=false, emails_enabled=true, lfs_enabled=true, mentions_disabled=false, organization_id=1, parent_id=2, project_creation_level='''developer''', request_access_enabled=true, require_two_factor_authentication=true, share_with_group_lock=false, subgroup_creation_level='''owner''', two_factor_grace_period=48, visibility='''public''', membership_lock=false, extra_shared_runners_minutes_limit=1000, shared_runners_minutes_limit=10000, wiki_access_level='''enabled''')
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

