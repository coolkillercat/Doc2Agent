import requests, json
from urllib.parse import quote


def list_epics_for_a_group(id=None, author_id=None, author_username=None, labels=None, with_labels_details=None, order_by='created_at', sort='desc', search=None, state='all', created_after=None, created_before=None, updated_after=None, updated_before=None, include_ancestor_groups=None, include_descendant_groups=True, my_reaction_emoji=None, not=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/groups/{quote(id, safe='')}/epics"
    querystring = {'id': id, 'author_id': author_id, 'author_username': author_username, 'labels': labels, 'with_labels_details': with_labels_details, 'order_by': order_by, 'sort': sort, 'search': search, 'state': state, 'created_after': created_after, 'created_before': created_before, 'updated_after': updated_after, 'updated_before': updated_before, 'include_ancestor_groups': include_ancestor_groups, 'include_descendant_groups': include_descendant_groups, 'my_reaction_emoji': my_reaction_emoji, 'not': not, }
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
    r = list_epics_for_a_group(id=1, author_id=5, author_username='''john_doe''', labels='''bug,reproduced''', with_labels_details=True, order_by='''updated_at''', sort='''asc''', search='''fix bug''', state='''opened''', created_after=2019-03-15T08:00:00Z, created_before=2019-03-15T08:00:00Z, updated_after=2019-03-15T08:00:00Z, updated_before=2019-03-15T08:00:00Z, include_ancestor_groups=True, include_descendant_groups=False, my_reaction_emoji='''thumbsup''', not={'author_id': 5})
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

