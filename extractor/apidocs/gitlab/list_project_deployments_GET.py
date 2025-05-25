import requests, json
from urllib.parse import quote


def list_project_deployments(id=None, order_by=None, sort=None, updated_after=None, updated_before=None, finished_after=None, finished_before=None, environment=None, status=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/projects/{quote(id, safe='')}/deployments"
    querystring = {'id': id, 'order_by': order_by, 'sort': sort, 'updated_after': updated_after, 'updated_before': updated_before, 'finished_after': finished_after, 'finished_before': finished_before, 'environment': environment, 'status': status, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    assert id is not None, 'Missing required parameter: id'
    
    response = requests.get(url=api_url, headers=headers, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = list_project_deployments(id=1, order_by='''id''', sort='''asc''', updated_after=2019-03-15T08:00:00Z, updated_before=2019-03-15T08:00:00Z, finished_after=2019-03-15T08:00:00Z, finished_before=2019-03-15T08:00:00Z, environment='''production''', status='''success''')
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

