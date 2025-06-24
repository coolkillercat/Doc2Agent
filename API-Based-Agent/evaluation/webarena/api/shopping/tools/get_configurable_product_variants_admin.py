import requests
import json

def get_shopping_admin_auth_token():
    """
    get_shopping_admin_auth_token function.
    
    Returns:
        Returns an empty array with no data.
    """
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

def get_configurable_product_variants(sku):
    """
    Retrieves all child products (variants) of a configurable product with their specific attributes.
    
    Args:
        sku (str): The SKU of the configurable product
        
    Returns:
        Returns a list of child product variants associated with a configurable product, including their specific attributes."""
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token()
    }
    
    url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/configurable-products/{sku}/children"
    response = requests.get(url, headers=headers)
    return response

if __name__ == '__main__':
    # Example: Get variants for a configurable product
    r = get_configurable_product_variants("B07G3DL1R8")  # Example configurable product SKU
    
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