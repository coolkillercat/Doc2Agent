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


def get_product_cost_information(skus=None):
    """
    Get cost information for specified product SKUs.
    
    Args:
        skus (list, optional): List of product SKUs to get cost information for.
            Example: ['24-MB01', '24-MB02']
    
    Returns:
        requests.Response: The API response containing product cost information.
    
    Example:
        >>> response = get_product_cost_information(['24-MB01', '24-MB02'])
        >>> print(response.json())
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    api_url = f"{base_url}/rest/default/V1/products/cost-information"
    
    if skus is None:
        skus = ['24-MB01']  # Default value if none provided
    
    payload = {"skus": skus}
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    
    response = requests.post(url=api_url, json=payload, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = get_product_cost_information()
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