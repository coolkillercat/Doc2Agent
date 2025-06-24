import requests
import json

def get_shopping_customer_auth_token():
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
    return response.json()

def get_configurable_product_options(sku):
    """
    Retrieves all available configuration options for a configurable product, such as sizes and colors.
    
    Args:
        sku (str): The SKU of the configurable product, for example 'MH01'
        
    Returns:
        dict: The available configuration options for the product
        
    Example:
        >>> options = get_configurable_product_options('MH01')
        >>> print(options)
        [
            {
                "option_id": 93,
                "attribute_id": "93",
                "label": "Color",
                "values": [...]
            },
            {
                "option_id": 141,
                "attribute_id": "141",
                "label": "Size",
                "values": [...]
            }
        ]
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': f'Bearer {get_shopping_customer_auth_token()}'
    }
    
    response = requests.get(
        f'{base_url}/rest/default/V1/configurable-products/{sku}/options/all',
        headers=headers
    )
    
    if response.status_code == 200:
        return response.json()
    else:
        return response.text

if __name__ == '__main__':
    # Test the function with a configurable product SKU
    sku = "MH01"  # Chaz Kangeroo Hoodie
    r = get_configurable_product_options(sku)
    
    result_dict = dict()
    result_dict['status_code'] = 200 if isinstance(r, list) else 400
    result_dict['text'] = json.dumps(r) if isinstance(r, list) else r
    result_dict['json'] = r if isinstance(r, list) else None
    result_dict['content'] = json.dumps(r) if isinstance(r, list) else r
    print(json.dumps(result_dict, indent=4))