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


def delete_product(sku=None):
    """
    Delete a product by its SKU.
    
    Args:
        sku (str): The SKU of the product to delete. This is required.
        
    Returns:
        requests.Response: The response from the API.
        
    Example:
        >>> response = delete_product(sku='test-product-sku')
        >>> print(response.status_code)
        200
        >>> print(response.json())
        True
    """
    assert sku is not None, 'Missing required parameter: sku'
    
    base_url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770'
    api_url = f"{base_url}/rest/default/V1/products/{quote(sku, safe='')}"
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    
    response = requests.delete(url=api_url, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = delete_product(sku='test-product-sku')
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