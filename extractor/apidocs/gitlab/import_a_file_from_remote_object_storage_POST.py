import requests, json
from urllib.parse import quote


def import_a_file_from_remote_object_storage(path=None, url=None, name=None, namespace=None, overwrite=None, override_params=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/projects/remote-import"
    payload = {'path': path, 'url': url, 'name': name, 'namespace': namespace, 'overwrite': overwrite, 'override_params': override_params, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    assert path is not None, 'Missing required parameter: path'
    assert url is not None, 'Missing required parameter: url'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = import_a_file_from_remote_object_storage(path='''remote-project''', url='''https://remoteobject/file?token=123123''', name='''Remote Project''', namespace=example-group, overwrite=false, override_params={})
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

