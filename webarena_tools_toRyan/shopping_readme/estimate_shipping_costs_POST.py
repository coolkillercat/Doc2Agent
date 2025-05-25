import requests
from urllib.parse import quote
                
def estimate_shipping_costs(address=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/carts/mine/estimate-shipping-methods"
    payload = {'address': address, }
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer eyJraWQiOiIxIiwiYWxnIjoiSFMyNTYifQ.eyJ1aWQiOjI3LCJ1dHlwaWQiOjMsImlhdCI6MTc0NzQ0MzM1NCwiZXhwIjoxNzQ3NDQ2OTU0fQ.I5TPXdqzfz5Bt3iPa5lruhK-cr8zuDJZxJlvIDOhUP8",
    }
    assert address is not None, 'Missing required parameter: address'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = estimate_shipping_costs(address={'region': 'New York', 'region_id': 43, 'region_code': 'NY', 'country_id': 'US', 'street': ['123 Oak Ave'], 'postcode': '10577', 'city': 'Purchase', 'firstname': 'Jane', 'lastname': 'Doe', 'customer_id': 4, 'email': 'jdoe@example.com', 'telephone': '(512) 555-1111', 'same_as_billing': 1})
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

