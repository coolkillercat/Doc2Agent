import requests, json
from urllib.parse import quote


def create_new_file_in_repository(branch=None, commit_message=None, content=None, file_path=None, id=None, author_email=None, author_name=None, encoding=None, execute_filemode=None, start_branch=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/projects/:id/repository/files/:file_path"
    payload = {'branch': branch, 'commit_message': commit_message, 'content': content, 'file_path': file_path, 'id': id, 'author_email': author_email, 'author_name': author_name, 'encoding': encoding, 'execute_filemode': execute_filemode, 'start_branch': start_branch, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert branch is not None, 'Missing required parameter: branch'
    assert commit_message is not None, 'Missing required parameter: commit_message'
    assert content is not None, 'Missing required parameter: content'
    assert file_path is not None, 'Missing required parameter: file_path'
    assert id is not None, 'Missing required parameter: id'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = create_new_file_in_repository(branch='''main''', commit_message='''create a new file''', content='''some content''', file_path='''app%2Fproject%2Erb''', id=13083, author_email='''author@example.com''', author_name='''Firstname Lastname''', encoding='''base64''', execute_filemode=False, start_branch='''main''')
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

