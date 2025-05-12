import requests
from urllib.parse import quote
                
def download_pypi_package_file(id=None, sha256=None, file_identifier=None):
    api_url = f"/api/v4/groups/{quote(id, safe='')}/-/packages/pypi/files/{quote(sha256, safe='')}/*file_identifier"
    querystring = {'id': id, 'sha256': sha256, 'file_identifier': file_identifier, }
    assert id is not None, 'Missing required parameter: id'
    assert sha256 is not None, 'Missing required parameter: sha256'
    assert file_identifier is not None, 'Missing required parameter: file_identifier'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = download_pypi_package_file(id='''123''', sha256='''abc123''', file_identifier='''file123''')
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

