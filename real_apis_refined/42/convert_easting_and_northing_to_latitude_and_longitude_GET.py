import requests
from urllib.parse import quote
                
def convert_easting_and_northing_to_latitude_and_longitude(easting=None, northing=None, format='json'):
    api_url = f"https://api.getthedata.com/bng2latlong/{easting}/{northing}"
    querystring = {'format': format}
    assert easting is not None, 'Missing required parameter: easting'
    assert northing is not None, 'Missing required parameter: northing'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = convert_easting_and_northing_to_latitude_and_longitude(easting=529090, northing=179645, format="json")
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