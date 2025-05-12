import requests
from urllib.parse import quote
                
def get_conan_recipe_snapshot(package_name=None, package_version=None, package_username=None, package_channel=None):
    api_url = f"/api/v4/packages/conan/v1/conans/{quote(package_name, safe='')}/{quote(package_version, safe='')}/{quote(package_username, safe='')}/{quote(package_channel, safe='')}"
    querystring = {'package_name': package_name, 'package_version': package_version, 'package_username': package_username, 'package_channel': package_channel, }
    assert package_name is not None, 'Missing required parameter: package_name'
    assert package_version is not None, 'Missing required parameter: package_version'
    assert package_username is not None, 'Missing required parameter: package_username'
    assert package_channel is not None, 'Missing required parameter: package_channel'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_conan_recipe_snapshot(package_name='''conan-package''', package_version='''1.0.0''', package_username='''user123''', package_channel='''stable''')
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

