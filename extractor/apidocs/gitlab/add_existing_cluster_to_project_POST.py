import requests, json
from urllib.parse import quote


def add_existing_cluster_to_project(id=None, name=None, platform_kubernetes_attributes_api_url_=None, platform_kubernetes_attributes_token_=None, domain=None, management_project_id=None, enabled=None, managed=None, platform_kubernetes_attributes_ca_cert_=None, platform_kubernetes_attributes_namespace_=None, platform_kubernetes_attributes_authorization_type_=None, environment_scope=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/projects/:id/clusters/user"
    payload = {'id': id, 'name': name, 'platform_kubernetes_attributes_api_url_': platform_kubernetes_attributes_api_url_, 'platform_kubernetes_attributes_token_': platform_kubernetes_attributes_token_, 'domain': domain, 'management_project_id': management_project_id, 'enabled': enabled, 'managed': managed, 'platform_kubernetes_attributes_ca_cert_': platform_kubernetes_attributes_ca_cert_, 'platform_kubernetes_attributes_namespace_': platform_kubernetes_attributes_namespace_, 'platform_kubernetes_attributes_authorization_type_': platform_kubernetes_attributes_authorization_type_, 'environment_scope': environment_scope, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert id is not None, 'Missing required parameter: id'
    assert name is not None, 'Missing required parameter: name'
    assert platform_kubernetes_attributes_api_url_ is not None, 'Missing required parameter: platform_kubernetes_attributes_api_url_'
    assert platform_kubernetes_attributes_token_ is not None, 'Missing required parameter: platform_kubernetes_attributes_token_'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = add_existing_cluster_to_project(id=26, name='''cluster-5''', platform_kubernetes_attributes_api_url_='''https://35.111.51.20''', platform_kubernetes_attributes_token_='''12345''', domain='''example.com''', management_project_id=2, enabled=true, managed=true, platform_kubernetes_attributes_ca_cert_='''-----BEGIN CERTIFICATE-----\r\n...''', platform_kubernetes_attributes_namespace_='''cluster-5-namespace''', platform_kubernetes_attributes_authorization_type_='''rbac''', environment_scope='''*''')
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

