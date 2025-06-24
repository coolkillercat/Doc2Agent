import requests
import json
from typing import List, Dict, Union, Any, Optional

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


def add_or_update_product_special_price(prices: List[Dict[str, Any]]) -> requests.Response:
    """
    Add or update product's special price.
    
    If any items have invalid price, store id, sku or dates, they will be marked as failed
    and excluded from the update list. The API returns information about failed items.
    
    Args:
        prices (List[Dict[str, Any]]): List of special price data dictionaries.
            Each dictionary should contain:
            - price (float): The special price
            - store_id (int): Store ID
            - sku (str): Product SKU
            - price_from (str, optional): Start date in format 'YYYY-MM-DD'
            - price_to (str, optional): End date in format 'YYYY-MM-DD'
    
    Returns:
        requests.Response: The API response object
    
    Example:
        >>> prices = [
        ...     {
        ...         "price": 99.99,
        ...         "store_id": 0,
        ...         "sku": "product-sku",
        ...         "price_from": "2023-01-01",
        ...         "price_to": "2023-12-31"
        ...     }
        ... ]
        >>> response = add_or_update_product_special_price(prices)
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    api_url = f"{base_url}/rest/default/V1/products/special-price"
    
    if not isinstance(prices, list):
        prices = [prices]
    
    payload = {"prices": prices}
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    
    response = requests.post(url=api_url, json=payload, headers=headers, timeout=50, verify=False)
    return response


if __name__ == '__main__':
    # Convert the tuple to a proper dictionary format
    price_data = [
        {
            "price": 99.99,
            "store_id": 0,
            "sku": "shopping-admin_part326",
            "price_from": "2023-01-01",
            "price_to": "2023-12-31"
        }
    ]
    
    r = add_or_update_product_special_price(price_data)
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