import requests
from urllib.parse import quote
                
def get_gift_message_for_item(cartId=None, itemId=None):
    api_url = f"/V1/carts/{quote(cartId, safe='')}/gift-message/{quote(itemId, safe='')}"
    querystring = {'cartId': cartId, 'itemId': itemId, }
    assert cartId is not None, 'Missing required parameter: cartId'
    assert itemId is not None, 'Missing required parameter: itemId'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_gift_message_for_item(cartId='''12345''', itemId='''67890''')
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

