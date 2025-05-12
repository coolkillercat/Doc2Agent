import requests
from urllib.parse import quote
                
def list_terraform_module_versions(module_namespace=None, module_name=None, module_system=None):
    api_url = f"/api/v4/packages/terraform/modules/v1/{quote(module_namespace, safe='')}/{quote(module_name, safe='')}/{quote(module_system, safe='')}/versions"
    querystring = {'module_namespace': module_namespace, 'module_name': module_name, 'module_system': module_system, }
    assert module_namespace is not None, 'Missing required parameter: module_namespace'
    assert module_name is not None, 'Missing required parameter: module_name'
    assert module_system is not None, 'Missing required parameter: module_system'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = list_terraform_module_versions(module_namespace='''namespace123''', module_name='''module123''', module_system='''system123''')
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

