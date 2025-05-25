import requests, json
from urllib.parse import quote


def add_existing_instance_cluster(name=None, platform_kubernetes_attributes_api_url_=None, platform_kubernetes_attributes_token_=None, domain=None, environment_scope=None, management_project_id=None, enabled=None, managed=None, platform_kubernetes_attributes_ca_cert_=None, platform_kubernetes_attributes_namespace_=None, platform_kubernetes_attributes_authorization_type_=None):
    api_url = f"http://gitlab.example.com/api/v4/admin/clusters/add"
    payload = {'name': name, 'platform_kubernetes_attributes_api_url_': platform_kubernetes_attributes_api_url_, 'platform_kubernetes_attributes_token_': platform_kubernetes_attributes_token_, 'domain': domain, 'environment_scope': environment_scope, 'management_project_id': management_project_id, 'enabled': enabled, 'managed': managed, 'platform_kubernetes_attributes_ca_cert_': platform_kubernetes_attributes_ca_cert_, 'platform_kubernetes_attributes_namespace_': platform_kubernetes_attributes_namespace_, 'platform_kubernetes_attributes_authorization_type_': platform_kubernetes_attributes_authorization_type_, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert name is not None, 'Missing required parameter: name'
    assert platform_kubernetes_attributes_api_url_ is not None, 'Missing required parameter: platform_kubernetes_attributes_api_url_'
    assert platform_kubernetes_attributes_token_ is not None, 'Missing required parameter: platform_kubernetes_attributes_token_'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = add_existing_instance_cluster(name='''cluster-3''', platform_kubernetes_attributes_api_url_='''https://example.com''', platform_kubernetes_attributes_token_='''12345''', domain='''example.com''', environment_scope='''production''', management_project_id=1, enabled=True, managed=True, platform_kubernetes_attributes_ca_cert_='''-----BEGIN CERTIFICATE-----qpoeiXXZafCM0ZDJkZjM...-----END CERTIFICATE-----''', platform_kubernetes_attributes_namespace_='''default''', platform_kubernetes_attributes_authorization_type_='''rbac''')
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

