import requests, json
from urllib.parse import quote

def get_shopping_customer_auth_token():
    response = requests.post(
        url = f'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/integration/customer/token',
        headers = {
            'content-type': 'application/json'
        },
        data = json.dumps({
            'username': 'emma.lopez@gmail.com',
            'password': 'Password.123'
        })
    )
    return response.json()

def estimate_shipping_methods(registryId=None):
    """
    Estimate shipping methods for a gift registry.
    
    Args:
        registryId (int, tuple): The ID of the registry to estimate shipping for.
            Example: 456 or ('shopping_chunk_3', 456)
    
    Returns:
        requests.Response: The API response object.
    
    Raises:
        AssertionError: If registryId is not provided.
    """
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/gift-registry/estimate-shipping-methods"
    
    assert registryId is not None, 'Missing required parameter: registryId'
    
    if isinstance(registryId, tuple) and len(registryId) == 2:
        registryId = registryId[1]
    
    payload = {'registryId': registryId}
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + get_shopping_customer_auth_token(),
    }
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = estimate_shipping_methods(registryId=456)
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