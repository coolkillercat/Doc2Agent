import requests
import json
from urllib.parse import quote

def get_shopping_admin_auth_token():
    ENDPOINT = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770'
    response = requests.post(
        url = f'{ENDPOINT}/rest/default/V1/integration/admin/token',
        headers = {
            'content-type': 'application/json'
        },
        data = json.dumps({
            'username': 'admin',
            'password': 'admin1234'
        })
    )
    return "Bearer " + response.json()


def delete_coupon_by_codes(codes, ignoreInvalidCoupons=True):
    """
    Delete coupon by coupon codes.
    
    Args:
        codes (list): List of coupon codes to delete. Required.
        ignoreInvalidCoupons (bool, optional): Whether to ignore invalid coupons. Defaults to True.
        
    Returns:
        requests.Response: The API response object.
        
    Example:
        >>> delete_coupon_by_codes(codes=['COUPON123', 'DISCOUNT456'])
        >>> delete_coupon_by_codes(codes=['COUPON123'], ignoreInvalidCoupons=False)
    """
    base_url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770'
    api_url = f"{base_url}/rest/default/V1/coupons/deleteByCodes"
    
    assert codes is not None and isinstance(codes, list), 'Missing required parameter: codes must be a list of strings'
    
    payload = {
        'codes': codes,
        'ignoreInvalidCoupons': ignoreInvalidCoupons
    }
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token()
    }
    
    response = requests.post(url=api_url, json=payload, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = delete_coupon_by_codes(codes=['COUPON123', 'DISCOUNT456'], ignoreInvalidCoupons=True)
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