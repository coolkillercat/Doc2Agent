import requests
from urllib.parse import quote
                
def nuget_metadata_service___package_name_and_version(id=None, package_name=None, package_version=None):
    api_url = f"/api/v4/groups/{quote(id, safe='')}/-/packages/nuget/metadata/*package_name/*package_version"
    querystring = {'id': id, 'package_name': package_name, 'package_version': package_version, }
    assert id is not None, 'Missing required parameter: id'
    assert package_name is not None, 'Missing required parameter: package_name'
    assert package_version is not None, 'Missing required parameter: package_version'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = nuget_metadata_service___package_name_and_version(id='''123''', package_name='''mypackage''', package_version='''1.0.0''')
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

