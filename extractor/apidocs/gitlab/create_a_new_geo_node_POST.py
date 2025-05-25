import requests, json
from urllib.parse import quote


def create_a_new_geo_node(name=None, url=None, primary=None, enabled=None, internal_url=None, files_max_capacity=None, repos_max_capacity=None, verification_max_capacity=None, container_repositories_max_capacity=None, sync_object_storage=None, selective_sync_type=None, selective_sync_shards=None, selective_sync_namespace_ids=None, minimum_reverification_interval=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/geo_nodes"
    payload = {'name': name, 'url': url, 'primary': primary, 'enabled': enabled, 'internal_url': internal_url, 'files_max_capacity': files_max_capacity, 'repos_max_capacity': repos_max_capacity, 'verification_max_capacity': verification_max_capacity, 'container_repositories_max_capacity': container_repositories_max_capacity, 'sync_object_storage': sync_object_storage, 'selective_sync_type': selective_sync_type, 'selective_sync_shards': selective_sync_shards, 'selective_sync_namespace_ids': selective_sync_namespace_ids, 'minimum_reverification_interval': minimum_reverification_interval, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert name is not None, 'Missing required parameter: name'
    assert url is not None, 'Missing required parameter: url'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = create_a_new_geo_node(name='''himynameissomething''', url='''https://another-node.example.com/''', primary=False, enabled=True, internal_url='''https://internal.example.com/''', files_max_capacity=10, repos_max_capacity=25, verification_max_capacity=100, container_repositories_max_capacity=10, sync_object_storage=False, selective_sync_type='''namespaces''', selective_sync_shards=[], selective_sync_namespace_ids=[1, 25], minimum_reverification_interval=7)
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

