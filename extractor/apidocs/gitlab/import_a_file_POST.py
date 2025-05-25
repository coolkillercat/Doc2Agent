import requests, json
from urllib.parse import quote


def import_a_file(file=None, path=None, name=None, namespace=None, override_params=None, overwrite=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/projects/import"
    payload = {'file': file, 'path': path, 'name': name, 'namespace': namespace, 'override_params': override_params, 'overwrite': overwrite, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    assert file is not None, 'Missing required parameter: file'
    assert path is not None, 'Missing required parameter: path'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = import_a_file(file='''@/path/to/file''', path='''api-project''', name='''My Imported Project''', namespace=example-group, override_params={}, overwrite=false)
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

