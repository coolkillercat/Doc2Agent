import requests, json
from urllib.parse import quote


def create_a_commit_with_multiple_files_and_actions(id=None, branch=None, commit_message=None, actions__=None, start_branch=None, start_sha=None, start_project=None, author_email=None, author_name=None, stats=None, force=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/projects/:id/repository/commits"
    payload = {'id': id, 'branch': branch, 'commit_message': commit_message, 'actions__': actions__, 'start_branch': start_branch, 'start_sha': start_sha, 'start_project': start_project, 'author_email': author_email, 'author_name': author_name, 'stats': stats, 'force': force, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert id is not None, 'Missing required parameter: id'
    assert branch is not None, 'Missing required parameter: branch'
    assert commit_message is not None, 'Missing required parameter: commit_message'
    assert actions__ is not None, 'Missing required parameter: actions__'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = create_a_commit_with_multiple_files_and_actions(id=1, branch='''main''', commit_message='''some commit message''', actions__=[{'action': 'create', 'file_path': 'foo/bar', 'content': 'some content'}], start_branch='''develop''', start_sha='''abc123''', start_project=2, author_email='''user@example.com''', author_name='''John Doe''', stats=True, force=False)
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

