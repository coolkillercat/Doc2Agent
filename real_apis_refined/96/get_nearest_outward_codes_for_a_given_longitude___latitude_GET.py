import requests
from urllib.parse import quote

def get_nearest_outward_codes_for_a_given_longitude___latitude(longitude=None, latitude=None):
    api_url = f"https://api.postcodes.io/outcodes?lon={str(longitude)}&lat={str(latitude)}"
    querystring = {'longitude': longitude, 'latitude': latitude, }
    assert longitude is not None, 'Missing required parameter: longitude'
    assert latitude is not None, 'Missing required parameter: latitude'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_nearest_outward_codes_for_a_given_longitude___latitude(longitude=0.629834723775309, latitude=51.7923246977375)
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