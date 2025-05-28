import requests
from urllib.parse import quote
                
def get_distance(source_lat_=None, source_lng_=None, destination_lat_=None, destination_lng_=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/inventory/get-distance"
    querystring = {'source_lat_': source_lat_, 'source_lng_': source_lng_, 'destination_lat_': destination_lat_, 'destination_lng_': destination_lng_, }
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_distance(source_lat_=40.7128, source_lng_=-74.006, destination_lat_=34.0522, destination_lng_=-118.2437)
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

