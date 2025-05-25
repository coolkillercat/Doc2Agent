import requests, json
from urllib.parse import quote


def upload_metric_image(id=None, alert_iid=None, file=None, url=None, url_text=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/projects/:id/alert_management_alerts/:alert_iid/metric_images"
    payload = {'id': id, 'alert_iid': alert_iid, 'file': file, 'url': url, 'url_text': url_text, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert id is not None, 'Missing required parameter: id'
    assert alert_iid is not None, 'Missing required parameter: alert_iid'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = upload_metric_image(id=5, alert_iid=93, file=@/path/to/file.png, url='''http://example.com''', url_text='''Example website''')
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

