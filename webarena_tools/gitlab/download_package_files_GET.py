import requests
from urllib.parse import quote
                
def download_package_files(id=None, package_name=None, package_version=None, package_username=None, package_channel=None, recipe_revision=None, conan_package_reference=None, package_revision=None, file_name=None):
    api_url = f"/api/v4/projects/{quote(id, safe='')}/packages/conan/v1/files/{quote(package_name, safe='')}/{quote(package_version, safe='')}/{quote(package_username, safe='')}/{quote(package_channel, safe='')}/{quote(recipe_revision, safe='')}/package/{quote(conan_package_reference, safe='')}/{quote(package_revision, safe='')}/{quote(file_name, safe='')}"
    querystring = {'id': id, 'package_name': package_name, 'package_version': package_version, 'package_username': package_username, 'package_channel': package_channel, 'recipe_revision': recipe_revision, 'conan_package_reference': conan_package_reference, 'package_revision': package_revision, 'file_name': file_name, }
    assert id is not None, 'Missing required parameter: id'
    assert package_name is not None, 'Missing required parameter: package_name'
    assert package_version is not None, 'Missing required parameter: package_version'
    assert package_username is not None, 'Missing required parameter: package_username'
    assert package_channel is not None, 'Missing required parameter: package_channel'
    assert recipe_revision is not None, 'Missing required parameter: recipe_revision'
    assert conan_package_reference is not None, 'Missing required parameter: conan_package_reference'
    assert package_revision is not None, 'Missing required parameter: package_revision'
    assert file_name is not None, 'Missing required parameter: file_name'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = download_package_files(id='''123''', package_name='''example_package''', package_version='''1.0.0''', package_username='''user123''', package_channel='''stable''', recipe_revision='''rev1''', conan_package_reference='''abcd1234''', package_revision='''rev2''', file_name='''package_file.tar.gz''')
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

