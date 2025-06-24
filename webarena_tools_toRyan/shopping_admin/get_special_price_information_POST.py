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


def get_special_price_information(skus=None):
    """
    Get special price information for the specified product SKUs.
    
    Args:
        skus (list): List of product SKUs to get special price information for.
                    Example: ['SKU123', 'SKU456']
    
    Returns:
        requests.Response: The API response object containing special price information.
        
    Raises:
        AssertionError: If skus parameter is None.
        
    Example:
        >>> response = get_special_price_information(skus=['24-MB01', '24-MB02'])
        >>> print(response.json())
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    api_url = f"{base_url}/rest/default/V1/products/special-price-information"
    
    assert skus is not None, 'Missing required parameter: skus'
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token()
    }
    
    payload = {'skus': skus}
    
    response = requests.post(url=api_url, json=payload, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = get_special_price_information(skus=['24-MB01', '24-MB02'])
    r_json = None
    try:
        r_json = r.json()
    except:
        pass
    
    result_dict = dict()
    result_dict['status_code'] = r.status_code
    result_dict['text'] = r.text
    result_dict['json'] = r_json
    result_dict['content'] = r.content.decode("utf-8")
    print(json.dumps(result_dict, indent=4))