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

def get_hosted_fields_config(location=None):
    """
    Get Hosted Fields Configuration from the API.
    
    Args:
        location (str, optional): The location for which to retrieve hosted fields configuration.
                        Example: 'us', 'eu', 'global'
    
    Returns:
        requests.Response: The API response object containing hosted fields configuration.
    
    Example:
        >>> get_hosted_fields_config(location='us')
        >>> get_hosted_fields_config()
    """
    
    api_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/payment/hosted-fields/config"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + get_shopping_customer_auth_token(),
    }
    
    params = {}
    if location is not None:
        params['location'] = location
    
    response = requests.get(url=api_url, headers=headers, params=params, timeout=50, verify=False)
    
    return response

if __name__ == '__main__':
    r = get_hosted_fields_config(location='us')
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