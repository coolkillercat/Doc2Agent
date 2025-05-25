import requests
from urllib.parse import quote
                
def machine_readable_api(lon=None, lat=None, product=None, output=None):
    api_url = f"http://www.7timer.info/bin/api.pl?lon=113.17&lat=23.09&product=astro&output=xml"
    querystring = {'lon': lon, 'lat': lat, 'product': product, 'output': output, }
    assert lon is not None, 'Missing required parameter: lon'
    assert lat is not None, 'Missing required parameter: lat'
    assert product is not None, 'Missing required parameter: product'
    assert output is not None, 'Missing required parameter: output'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = machine_readable_api(lon=113.17, lat=23.09, product='''astro''', output='''xml''')
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

