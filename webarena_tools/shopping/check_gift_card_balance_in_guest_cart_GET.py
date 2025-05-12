import requests
from urllib.parse import quote
                
def check_gift_card_balance_in_guest_cart(cartId=None, giftCardCode=None):
    api_url = f"/V1/carts/guest-carts/{quote(cartId, safe='')}/checkGiftCard/{quote(giftCardCode, safe='')}"
    querystring = {'cartId': cartId, 'giftCardCode': giftCardCode, }
    assert cartId is not None, 'Missing required parameter: cartId'
    assert giftCardCode is not None, 'Missing required parameter: giftCardCode'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = check_gift_card_balance_in_guest_cart(cartId='''guestCart123''', giftCardCode='''GIFT123''')
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

