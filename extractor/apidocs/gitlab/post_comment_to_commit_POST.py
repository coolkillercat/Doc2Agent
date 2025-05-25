import requests, json
from urllib.parse import quote


def post_comment_to_commit(id=None, sha=None, note=None, path=None, line=None, line_type=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/projects/:id/repository/commits/:sha/comments"
    payload = {'id': id, 'sha': sha, 'note': note, 'path': path, 'line': line, 'line_type': line_type, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    assert id is not None, 'Missing required parameter: id'
    assert sha is not None, 'Missing required parameter: sha'
    assert note is not None, 'Missing required parameter: note'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = post_comment_to_commit(id=17, sha='''18f3e63d05582537db6d183d9d557be09e1f90c8''', note='''Nice picture!''', path='''README.md''', line=11, line_type='''new''')
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

