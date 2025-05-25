import requests, json
from urllib.parse import quote

def get_shopping_admin_admin_auth_token():
    response = requests.post(
        url=f'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/integration/admin/token',
        headers={
            'content-type': 'application/json'
        },
        data=json.dumps({
            'username': 'admin',
            'password': 'admin1234'
        })
    )
    return response.json()

def assign_product_to_website(sku=None):
    """
    Assigns a product to a website by sending a POST request to the Magento API.
    
    Args:
        sku (str): The SKU of the product to assign to a website.
        
    Returns:
        requests.Response: The response from the API.
        
    Raises:
        AssertionError: If the required parameter 'sku' is missing.
    """
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/products/{quote(str(sku))}/websites"
    payload = {
        'productWebsiteLink': {
            'sku': sku,
            'website_id': 1  # Default website ID
        }
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + get_shopping_admin_admin_auth_token(),
    }
    assert sku is not None, 'Missing required parameter: sku'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = assign_product_to_website(sku='''ABC123''')
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