import requests
from urllib.parse import quote
                
def raw_content_access(ZIMNAME=None, PATH_IN_ZIMFILE=None):
    assert ZIMNAME is not None, 'Missing required parameter: ZIMNAME'
    assert PATH_IN_ZIMFILE is not None, 'Missing required parameter: PATH_IN_ZIMFILE'
    
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8888/raw/{ZIMNAME}/content/{PATH_IN_ZIMFILE}"
    
    response = requests.get(url=api_url, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = raw_content_access(ZIMNAME='example.zim', PATH_IN_ZIMFILE='articles/index.html')
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