import requests, json
from urllib.parse import quote


def list_all_runners(scope=None, type=None, status=None, paused=None, tag_list=None, version_prefix=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/runners/all"
    querystring = {'scope': scope, 'type': type, 'status': status, 'paused': paused, 'tag_list': tag_list, 'version_prefix': version_prefix, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    
    response = requests.get(url=api_url, headers=headers, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = list_all_runners(scope='''shared''', type='''instance_type''', status='''offline''', paused=True, tag_list=['tag1', 'tag2'], version_prefix='''16.1.241''')
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

