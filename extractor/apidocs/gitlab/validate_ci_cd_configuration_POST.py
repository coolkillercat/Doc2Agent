import requests, json
from urllib.parse import quote


def validate_ci_cd_configuration(content=None, dry_run=None, include_jobs=None, ref=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/projects/:id/ci/lint"
    payload = {'content': content, 'dry_run': dry_run, 'include_jobs': include_jobs, 'ref': ref, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    assert content is not None, 'Missing required parameter: content'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = validate_ci_cd_configuration(content='''{ "image": "ruby:2.6", "services": ["postgres"], "before_script": ["bundle install", "bundle exec rake db:create"], "variables": {"DB_NAME": "postgres"}, "types": ["test", "deploy", "notify"], "rspec": { "script": "rake spec", "tags": ["ruby", "postgres"], "only": ["branches"]}}''', dry_run=False, include_jobs=False, ref='''main''')
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

