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


def delete_product_tier_prices(prices=None):
    """
    Delete product tier prices.
    
    Args:
        prices (list, optional): List of tier prices to delete. Each item should contain
            price, price_type, website_id, sku, customer_group, and quantity.
            
    Example:
        prices = [
            {
                "price": 10.99,
                "price_type": "fixed",
                "website_id": 0,
                "sku": "product-sku",
                "customer_group": "ALL GROUPS",
                "quantity": 1
            }
        ]
        
    Returns:
        requests.Response: The API response object
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    api_url = f"{base_url}/rest/default/V1/products/tier-prices-delete"
    
    if prices is None:
        prices = []
    
    payload = {"prices": prices}
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    
    response = requests.post(url=api_url, json=payload, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = delete_product_tier_prices()
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