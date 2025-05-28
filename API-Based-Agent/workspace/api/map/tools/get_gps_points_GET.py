import requests, json
from urllib.parse import quote


def get_gps_points(bbox=None, page=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:3000/api/0.6/trackpoints"
    querystring = {'bbox': bbox, 'page': page, }
    assert bbox is not None, 'Missing required parameter: bbox'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_gps_points(bbox='''0,51.5,0.25,51.75''', page=0)
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

