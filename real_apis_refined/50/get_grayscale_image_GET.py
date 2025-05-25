import requests
from urllib.parse import quote
                
def get_grayscale_image(width=None, height=None):
    api_url = f"https://picsum.photos/{width}/{height}?grayscale"
    querystring = {'width': width, 'height': height, }
    assert width is not None, 'Missing required parameter: width'
    assert height is not None, 'Missing required parameter: height'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_grayscale_image(width=200, height=300)
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