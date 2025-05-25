import requests, json
from urllib.parse import quote


def list_all_snippets(created_after=None, created_before=None, page=None, per_page=None, repository_storage=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/snippets/all"
    querystring = {'created_after': created_after, 'created_before': created_before, 'page': page, 'per_page': per_page, 'repository_storage': repository_storage, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    
    response = requests.get(url=api_url, headers=headers, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = list_all_snippets(created_after=2019-03-15T08:00:00Z, created_before=2019-03-15T08:00:00Z, page=1, per_page=10, repository_storage='''default''')
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

