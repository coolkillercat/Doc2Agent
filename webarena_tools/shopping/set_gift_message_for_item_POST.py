import requests
from urllib.parse import quote
                
def set_gift_message_for_item(cartId=None, itemId=None):
    api_url = f"/V1/carts/{cartId}/gift-message/{itemId}"
    payload = {'cartId': cartId, 'itemId': itemId, }
    assert cartId is not None, 'Missing required parameter: cartId'
    assert itemId is not None, 'Missing required parameter: itemId'
    
    response = requests.post(url=api_url, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = set_gift_message_for_item(cartId='''12345''', itemId='''67890''')
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

