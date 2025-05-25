import requests, json
from urllib.parse import quote


def create_secure_file(project_id=None, file=None, name=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/projects/:project_id/secure_files"
    payload = {'project_id': project_id, 'file': file, 'name': name, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert project_id is not None, 'Missing required parameter: project_id'
    assert file is not None, 'Missing required parameter: file'
    assert name is not None, 'Missing required parameter: name'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = create_secure_file(project_id=1, file=@/path/to/file/myfile.jks, name='''myfile.jks''')
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

