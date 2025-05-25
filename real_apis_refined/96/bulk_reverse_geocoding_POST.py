import requests
from urllib.parse import quote
                
def bulk_reverse_geocoding(geolocations=None):
    api_url = f"https://api.postcodes.io/postcodes"
    payload = {'geolocations': geolocations, }
    assert geolocations is not None, 'Missing required parameter: geolocations'
    
    response = requests.post(url=api_url, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = bulk_reverse_geocoding(geolocations=[{'longitude': 0.629834723775309, 'latitude': 51.7923246977375}, {'longitude': -2.49690382054704, 'latitude': 53.5351312861402, 'radius': 1000, 'limit': 5}])
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

