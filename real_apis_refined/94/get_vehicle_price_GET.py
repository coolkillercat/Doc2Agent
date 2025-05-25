import requests
from urllib.parse import quote
                
def get_vehicle_price(brandId=None, modelId=None, yearId=None):
    api_url = f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{quote(brandId, safe='')}/modelos/{quote(modelId, safe='')}/anos/{quote(yearId, safe='')}"
    querystring = {'brandId': brandId, 'modelId': modelId, 'yearId': yearId, }
    assert brandId is not None, 'Missing required parameter: brandId'
    assert modelId is not None, 'Missing required parameter: modelId'
    assert yearId is not None, 'Missing required parameter: yearId'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_vehicle_price(brandId='''59''', modelId='''5940''', yearId='''2014-3''')
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

