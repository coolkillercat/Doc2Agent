import requests
from urllib.parse import quote
                
def get_conan_package_upload_urls(package_name=None, package_version=None, package_username=None, package_channel=None, conan_package_reference=None):
    api_url = f"/api/v4/packages/conan/v1/conans/{package_name}/{package_version}/{package_username}/{package_channel}/packages/{conan_package_reference}/upload_urls"
    payload = {'package_name': package_name, 'package_version': package_version, 'package_username': package_username, 'package_channel': package_channel, 'conan_package_reference': conan_package_reference, }
    assert package_name is not None, 'Missing required parameter: package_name'
    assert package_version is not None, 'Missing required parameter: package_version'
    assert package_username is not None, 'Missing required parameter: package_username'
    assert package_channel is not None, 'Missing required parameter: package_channel'
    assert conan_package_reference is not None, 'Missing required parameter: conan_package_reference'
    
    response = requests.post(url=api_url, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_conan_package_upload_urls(package_name='''conan-package''', package_version='''1.0.0''', package_username='''user123''', package_channel='''stable''', conan_package_reference='''ref123''')
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

