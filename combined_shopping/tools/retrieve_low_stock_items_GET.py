import requests
from urllib.parse import quote
                
def retrieve_low_stock_items(scopeId=None, qty=None, currentPage=None, pageSize=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/stockItems/lowStock/"
    querystring = {'scopeId': scopeId, 'qty': qty, 'currentPage': currentPage, 'pageSize': pageSize, }
    assert scopeId is not None, 'Missing required parameter: scopeId'
    assert qty is not None, 'Missing required parameter: qty'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = retrieve_low_stock_items(scopeId=1, qty=5, currentPage=1, pageSize=20)
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

