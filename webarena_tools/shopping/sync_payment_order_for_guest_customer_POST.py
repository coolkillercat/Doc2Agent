import requests
from urllib.parse import quote
                
def sync_payment_order_for_guest_customer(cartId=None, id=None):
    api_url = f"/V1/guest-carts/{cartId}/payment-order/{id}"
    payload = {'cartId': cartId, 'id': id, }
    assert cartId is not None, 'Missing required parameter: cartId'
    assert id is not None, 'Missing required parameter: id'
    
    response = requests.post(url=api_url, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = sync_payment_order_for_guest_customer(cartId='''guest123''', id='''order456''')
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

