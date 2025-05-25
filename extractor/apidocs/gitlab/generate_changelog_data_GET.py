import requests, json
from urllib.parse import quote


def generate_changelog_data(version=None, config_file='.gitlab/changelog_config.yml', date=None, from=None, to=None, trailer='Changelog'):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/projects/:id/repository/changelog"
    querystring = {'version': version, 'config_file': config_file, 'date': date, 'from': from, 'to': to, 'trailer': trailer, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert version is not None, 'Missing required parameter: version'
    
    response = requests.get(url=api_url, headers=headers, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = generate_changelog_data(version='''1.0.0''', config_file='''config/changelog.yml''', date=2023-10-01T12:00:00Z, from='''abc123''', to='''def456''', trailer='''ReleaseNotes''')
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

