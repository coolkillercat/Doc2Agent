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


def get_product_prices(skus=None):
    """
    Get product tier prices information by SKUs.
    
    Args:
        skus (list): List of product SKUs to get price information for.
                    Example: ["sku1", "sku2"]
    
    Returns:
        Returns tier price information for specified products by their SKUs.
    Raises:
        AssertionError: If skus parameter is not provided.
    """
    api_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/products/tier-prices-information"
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    
    assert skus is not None, 'Missing required parameter: skus'
    
    payload = {"skus": skus}
    
    response = requests.post(url=api_url, json=payload, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = get_product_prices(skus=["sku1", "sku2"])
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