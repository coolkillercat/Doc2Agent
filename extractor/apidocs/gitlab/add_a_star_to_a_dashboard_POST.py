import requests, json
from urllib.parse import quote


def add_a_star_to_a_dashboard(id=None, dashboard_path=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/projects/:id/metrics/user_starred_dashboards"
    payload = {'id': id, 'dashboard_path': dashboard_path, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert id is not None, 'Missing required parameter: id'
    assert dashboard_path is not None, 'Missing required parameter: dashboard_path'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = add_a_star_to_a_dashboard(id=20, dashboard_path='''config/prometheus/dashboards/common_metrics.yml''')
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

