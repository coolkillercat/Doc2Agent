import requests, json
from urllib.parse import quote


def add_changelog_data_to_a_changelog_file(version=None, branch=None, config_file='.gitlab/changelog_config.yml', date=None, file='CHANGELOG.md', from=None, message='Add changelog for version X', to=None, trailer='Changelog'):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/projects/:id/repository/changelog"
    payload = {'version': version, 'branch': branch, 'config_file': config_file, 'date': date, 'file': file, 'from': from, 'message': message, 'to': to, 'trailer': trailer, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert version is not None, 'Missing required parameter: version'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = add_changelog_data_to_a_changelog_file(version='''1.0.0''', branch='''main''', config_file='''config/changelog.yml''', date=2023-10-01T12:00:00Z, file='''NEWS.md''', from='''abc123''', message='''Update changelog for version 1.0.0''', to='''def456''', trailer='''ReleaseNotes''')
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

