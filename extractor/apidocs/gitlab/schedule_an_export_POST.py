import requests, json
from urllib.parse import quote


def schedule_an_export(id=None, upload_url_=None, description=None, upload=None, upload_http_method_=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/projects/:id/export"
    payload = {'id': id, 'upload_url_': upload_url_, 'description': description, 'upload': upload, 'upload_http_method_': upload_http_method_, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert id is not None, 'Missing required parameter: id'
    assert upload_url_ is not None, 'Missing required parameter: upload_url_'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = schedule_an_export(id=1, upload_url_='''https://example-bucket.s3.eu-west-3.amazonaws.com/backup''', description='''My Project Export''', upload={ "http_method": "PUT" }, upload_http_method_='''PUT''')
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

