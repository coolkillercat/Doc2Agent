import requests
from urllib.parse import quote
                
def get_latitude_and_longitude_from_address(address_country_=None, address_postcode_=None, address_street_=None, address_region_=None, address_city_=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/inventory/get-latlng-from-address"
    querystring = {'address_country_': address_country_, 'address_postcode_': address_postcode_, 'address_street_': address_street_, 'address_region_': address_region_, 'address_city_': address_city_, }
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_latitude_and_longitude_from_address(address_country_='''US''', address_postcode_='''10001''', address_street_='''123 Main St''', address_region_='''NY''', address_city_='''New York''')
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

