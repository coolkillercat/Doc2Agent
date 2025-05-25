import requests, json
from urllib.parse import quote


def download_artifacts_archive(id=None, job=None, ref_name=None, job_token=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/projects/{quote(id, safe='')}/jobs/artifacts/{quote(ref_name, safe='')}/download?job=name"
    querystring = {'id': id, 'job': job, 'ref_name': ref_name, 'job_token': job_token, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    assert id is not None, 'Missing required parameter: id'
    assert job is not None, 'Missing required parameter: job'
    assert ref_name is not None, 'Missing required parameter: ref_name'
    
    response = requests.get(url=api_url, headers=headers, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = download_artifacts_archive(id=1, job='''test''', ref_name='''main''', job_token='''$CI_JOB_TOKEN''')
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

