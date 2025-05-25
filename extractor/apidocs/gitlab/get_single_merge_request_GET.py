import requests, json
from urllib.parse import quote


def get_single_merge_request(id=None, merge_request_iid=None, include_diverged_commits_count=None, include_rebase_in_progress=None, render_html=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/projects/{quote(id, safe='')}/merge_requests/{quote(merge_request_iid, safe='')}"
    querystring = {'id': id, 'merge_request_iid': merge_request_iid, 'include_diverged_commits_count': include_diverged_commits_count, 'include_rebase_in_progress': include_rebase_in_progress, 'render_html': render_html, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    assert id is not None, 'Missing required parameter: id'
    assert merge_request_iid is not None, 'Missing required parameter: merge_request_iid'
    
    response = requests.get(url=api_url, headers=headers, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_single_merge_request(id=76, merge_request_iid=1, include_diverged_commits_count=True, include_rebase_in_progress=True, render_html=True)
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

