import requests
from urllib.parse import quote
                
def download_nuget_symbol_file(id=None, file_name=None, signature=None, same_file_name=None):
    api_url = f"/api/v4/projects/{quote(id, safe='')}/packages/nuget/symbolfiles/*file_name/*signature/*same_file_name"
    querystring = {'id': id, 'file_name': file_name, 'signature': signature, 'same_file_name': same_file_name, }
    assert id is not None, 'Missing required parameter: id'
    assert file_name is not None, 'Missing required parameter: file_name'
    assert signature is not None, 'Missing required parameter: signature'
    assert same_file_name is not None, 'Missing required parameter: same_file_name'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = download_nuget_symbol_file(id='''123''', file_name='''example-file''', signature='''abc123''', same_file_name='''example-file''')
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

