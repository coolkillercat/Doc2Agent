import requests
import json

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


def delete_coupons_by_ids(ids, ignoreInvalidCoupons=False):
    """
    Delete coupon by coupon ids.
    
    Args:
        ids (list): List of coupon IDs to delete. Required.
        ignoreInvalidCoupons (bool, optional): Whether to ignore invalid coupons. Defaults to False.
        
    Returns:
        requests.Response: The API response object.
        
    Example:
        >>> delete_coupons_by_ids(ids=[1, 2, 3], ignoreInvalidCoupons=True)
    """
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/coupons/deleteByIds"
    payload = {'ids': ids, 'ignoreInvalidCoupons': ignoreInvalidCoupons}
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    assert ids is not None, 'Missing required parameter: ids'
    
    response = requests.post(url=api_url, json=payload, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = delete_coupons_by_ids(ids=[1, 2, 3], ignoreInvalidCoupons=True)
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