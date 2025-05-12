import requests
from urllib.parse import quote
                
def update_downloadable_link(sku=None):
    api_url = f"/V1/products/{sku}/downloadable-links"
    payload = {'sku': sku, }
    assert sku is not None, 'Missing required parameter: sku'
    
    response = requests.post(url=api_url, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = update_downloadable_link(sku='''product-sku''')
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

