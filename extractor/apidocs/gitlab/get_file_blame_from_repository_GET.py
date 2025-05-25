import requests, json
from urllib.parse import quote


def get_file_blame_from_repository(id=None, file_path=None, ref=None, range_end_=None, range_start_=None, range=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/projects/{quote(id, safe='')}/repository/files/{quote(file_path, safe='')}/blame"
    querystring = {'id': id, 'file_path': file_path, 'ref': ref, 'range_end_': range_end_, 'range_start_': range_start_, 'range': range, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    assert id is not None, 'Missing required parameter: id'
    assert file_path is not None, 'Missing required parameter: file_path'
    assert ref is not None, 'Missing required parameter: ref'
    assert range_end_ is not None, 'Missing required parameter: range_end_'
    assert range_start_ is not None, 'Missing required parameter: range_start_'
    
    response = requests.get(url=api_url, headers=headers, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_file_blame_from_repository(id=13083, file_path='''path%2Fto%2Ffile.rb''', ref='''main''', range_end_=2, range_start_=1, range=None)
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

