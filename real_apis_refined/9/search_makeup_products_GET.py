import requests
from urllib.parse import quote
                
def search_makeup_products(product_type=None, product_category=None, product_tags=None, brand=None, price_greater_than=None, price_less_than=None, rating_greater_than=None, rating_less_than=None):
    api_url = f"http://makeup-api.herokuapp.com/api/v1/products.json"
    querystring = {'product_type': product_type, 'product_category': product_category, 'product_tags': product_tags, 'brand': brand, 'price_greater_than': price_greater_than, 'price_less_than': price_less_than, 'rating_greater_than': rating_greater_than, 'rating_less_than': rating_less_than, }
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = search_makeup_products(product_type='''lipstick''', product_category='''lip gloss''', product_tags=vegan,gluten free, brand='''maybelline''', price_greater_than=10, price_less_than=50, rating_greater_than=4, rating_less_than=3)
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

