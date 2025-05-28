import requests
from urllib.parse import quote
                
def get_product_salable_status_for_requested_quantity(stockId=None, skuRequests_0__sku_=None, skuRequests_0__qty_=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/inventory/are-product-salable-for-requested-qty/"
    querystring = {'stockId': stockId, 'skuRequests_0__sku_': skuRequests_0__sku_, 'skuRequests_0__qty_': skuRequests_0__qty_, }
    assert stockId is not None, 'Missing required parameter: stockId'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_product_salable_status_for_requested_quantity(stockId=1, skuRequests_0__sku_='''SKU123''', skuRequests_0__qty_=10)
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

