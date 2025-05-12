import requests
from urllib.parse import quote
                
def get_binary_files_index_by_hash(id=None, distribution=None, component=None, architecture=None, file_sha256=None):
    api_url = f"/api/v4/groups/{quote(id, safe='')}/-/packages/debian/dists/*distribution/{quote(component, safe='')}/binary-{quote(architecture, safe='')}/by-hash/SHA256/{quote(file_sha256, safe='')}"
    querystring = {'id': id, 'distribution': distribution, 'component': component, 'architecture': architecture, 'file_sha256': file_sha256, }
    assert id is not None, 'Missing required parameter: id'
    assert distribution is not None, 'Missing required parameter: distribution'
    assert component is not None, 'Missing required parameter: component'
    assert architecture is not None, 'Missing required parameter: architecture'
    assert file_sha256 is not None, 'Missing required parameter: file_sha256'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_binary_files_index_by_hash(id='''123''', distribution='''buster''', component='''main''', architecture='''amd64''', file_sha256='''abc123''')
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

