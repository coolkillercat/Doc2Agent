import requests
import json
from urllib.parse import quote

def get_shopping_admin_auth_token():
    ENDPOINT = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780'
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


def create_product(product_data=None):
    """
    Create a new product in the Magento catalog.
    
    Args:
        product_data (dict): A dictionary containing product information.
            Example:
            {
                "product": {
                    "sku": "test-product-sku",
                    "name": "Test Product",
                    "attribute_set_id": 4,
                    "price": 19.99,
                    "status": 1,
                    "visibility": 4,
                    "type_id": "simple",
                    "weight": "1.0"
                }
            }
    
    Returns:
        Returns a newly created product's complete details including ID, attributes, stock information, and media gallery entries."""
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780"
    api_url = f"{base_url}/rest/default/V1/products"
    
    if product_data is None:
        product_data = {
            "product": {
                "sku": "test-product-sku",
                "name": "Test Product",
                "attribute_set_id": 4,
                "price": 19.99,
                "status": 1,
                "visibility": 4,
                "type_id": "simple",
                "weight": "1.0"
            }
        }
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token()
    }
    
    response = requests.post(url=api_url, json=product_data, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = create_product()
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