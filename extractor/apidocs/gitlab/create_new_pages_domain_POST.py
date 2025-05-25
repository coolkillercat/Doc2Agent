import requests, json
from urllib.parse import quote


def create_new_pages_domain(id=None, domain=None, auto_ssl_enabled=None, certificate=None, key=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/projects/:id/pages/domains"
    payload = {'id': id, 'domain': domain, 'auto_ssl_enabled': auto_ssl_enabled, 'certificate': certificate, 'key': key, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert id is not None, 'Missing required parameter: id'
    assert domain is not None, 'Missing required parameter: domain'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = create_new_pages_domain(id=5, domain='''ssl.domain.example''', auto_ssl_enabled=true, certificate=@/path/to/cert.pem, key=@/path/to/key.pem)
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

