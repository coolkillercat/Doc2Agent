import requests, json
from urllib.parse import quote


def list_all_projects(archived=None, id_after=None, id_before=None, imported=None, include_hidden=None, include_pending_delete=None, last_activity_after=None, last_activity_before=None, membership=None, min_access_level=None, order_by='created_at', owned=None, repository_checksum_failed=None, repository_storage=None, search_namespaces=None, search=None, simple=None, sort='desc', starred=None, statistics=None, topic_id=None, topic=None, updated_after=None, updated_before=None, visibility=None, wiki_checksum_failed=None, with_custom_attributes=None, with_issues_enabled=None, with_merge_requests_enabled=None, with_programming_language=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/projects"
    querystring = {'archived': archived, 'id_after': id_after, 'id_before': id_before, 'imported': imported, 'include_hidden': include_hidden, 'include_pending_delete': include_pending_delete, 'last_activity_after': last_activity_after, 'last_activity_before': last_activity_before, 'membership': membership, 'min_access_level': min_access_level, 'order_by': order_by, 'owned': owned, 'repository_checksum_failed': repository_checksum_failed, 'repository_storage': repository_storage, 'search_namespaces': search_namespaces, 'search': search, 'simple': simple, 'sort': sort, 'starred': starred, 'statistics': statistics, 'topic_id': topic_id, 'topic': topic, 'updated_after': updated_after, 'updated_before': updated_before, 'visibility': visibility, 'wiki_checksum_failed': wiki_checksum_failed, 'with_custom_attributes': with_custom_attributes, 'with_issues_enabled': with_issues_enabled, 'with_merge_requests_enabled': with_merge_requests_enabled, 'with_programming_language': with_programming_language, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    
    response = requests.get(url=api_url, headers=headers, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = list_all_projects(archived=False, id_after=100, id_before=200, imported=True, include_hidden=True, include_pending_delete=True, last_activity_after=2023-01-01T00:00:00Z, last_activity_before=2023-12-31T23:59:59Z, membership=True, min_access_level=30, order_by='''name''', owned=True, repository_checksum_failed=True, repository_storage='''default''', search_namespaces=True, search='''example project''', simple=True, sort='''asc''', starred=True, statistics=True, topic_id=5, topic='''example,disapora client''', updated_after=2023-01-01T00:00:00Z, updated_before=2023-12-31T23:59:59Z, visibility='''public''', wiki_checksum_failed=True, with_custom_attributes=True, with_issues_enabled=True, with_merge_requests_enabled=True, with_programming_language='''Python''')
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

