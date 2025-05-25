import requests, json
from urllib.parse import quote


def create_a_new_annotation_for_cluster(dashboard_path=None, starting_at=None, description=None, ending_at=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/clusters/:id/metrics_dashboard/annotations/"
    payload = {'dashboard_path': dashboard_path, 'starting_at': starting_at, 'description': description, 'ending_at': ending_at, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    assert dashboard_path is not None, 'Missing required parameter: dashboard_path'
    assert starting_at is not None, 'Missing required parameter: starting_at'
    assert description is not None, 'Missing required parameter: description'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = create_a_new_annotation_for_cluster(dashboard_path='''.gitlab/dashboards/custom_metrics.yml''', starting_at='''2016-03-11T03:45:40Z''', description='''annotation description''', ending_at='''2016-03-11T04:45:40Z''')
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

