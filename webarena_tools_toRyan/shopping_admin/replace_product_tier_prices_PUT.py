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


def replace_product_tier_prices(prices=None):
    """
    Replace existing tier prices and replace them with new ones.
    
    Args:
        prices (list): List of price objects with the following structure:
            [
                {
                    "sku": "product_sku",
                    "price": 10.99,
                    "price_type": "fixed", # or "discount"
                    "website_id": 0,
                    "customer_group": "ALL GROUPS",
                    "quantity": 1
                }
            ]
    
    Returns:
        requests.Response: The API response object
    
    Example:
        prices = [
            {
                "sku": "24-MB01",
                "price": 10.99,
                "price_type": "fixed",
                "website_id": 0,
                "customer_group": "ALL GROUPS",
                "quantity": 1
            }
        ]
        response = replace_product_tier_prices(prices)
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    api_url = f"{base_url}/rest/default/V1/products/tier-prices"
    
    if prices is None:
        prices = [
            {
                "sku": "24-MB01",
                "price": 10.99,
                "price_type": "fixed",
                "website_id": 0,
                "customer_group": "ALL GROUPS",
                "quantity": 1
            }
        ]
    
    payload = {"prices": prices}
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    
    response = requests.put(url=api_url, json=payload, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = replace_product_tier_prices()
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