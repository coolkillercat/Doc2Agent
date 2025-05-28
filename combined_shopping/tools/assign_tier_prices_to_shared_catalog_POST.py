import requests
from urllib.parse import quote
                
def assign_tier_prices_to_shared_catalog(sharedCatalogId=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/sharedCatalog/{sharedCatalogId}/assignTierPrices"
    payload = {'sharedCatalogId': sharedCatalogId, }
    assert sharedCatalogId is not None, 'Missing required parameter: sharedCatalogId'
    
    response = requests.post(url=api_url, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = assign_tier_prices_to_shared_catalog(sharedCatalogId=1)
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

