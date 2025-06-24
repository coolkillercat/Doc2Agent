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

def retrieve_product_types():
    """
    Retrieve available product types from the Magento API.
    
    This function makes a GET request to the Magento API endpoint for retrieving
    product types. It returns the response object which can be further processed
    to extract the product types information.
    
    Returns:
        requests.Response: The API response object containing product types information.
        
    Example:
        >>> response = retrieve_product_types()
        >>> product_types = response.json()
        >>> print(product_types)
        [
            {
                "name": "simple",
                "label": "Simple Product"
            },
            {
                "name": "virtual",
                "label": "Virtual Product"
            },
            ...
        ]
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    api_url = f"{base_url}/rest/default/V1/products/types"
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token()
    }
    
    response = requests.get(url=api_url, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = retrieve_product_types()
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