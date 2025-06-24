import requests, json
from urllib.parse import quote

import json
import requests
def get_shopping_customer_auth_token():
    """
    Get customer authentication token from the API.
    
    Returns:
        str: Authentication token for the customer
        
    Example:
        token = get_shopping_customer_auth_token()
    """
    response = requests.post(
        url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/integration/customer/token',
        headers = {
            'content-type': 'application/json'
        },
        data = json.dumps({
            'username': 'emma.lopez@gmail.com',
            'password': 'Password.123'
        })
    )
    return "Bearer " + response.json()


def add_configurable_product_to_cart(sku: str, qty: int, quote_id: str, option_selections: list) -> dict:
    """
    Adds a configurable product to the cart with specified options like size and color.
    
    Args:
        sku (str): The SKU of the configurable product
        qty (int): The quantity of the product to add
        quote_id (str): The quote ID of the cart
        option_selections (list): A list of tuples containing (option_id, option_value)
    
    Returns:
        requests.Response: The response from the API call
        
    Example:
        response = add_configurable_product_to_cart(
            'MH01', 
            1, 
            '123', 
            [('93', 52), ('141', 168)]
        )
    """
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_customer_auth_token()}
    
    # Prepare configurable_item_options from the option_selections
    configurable_item_options = []
    for option_id, option_value in option_selections:
        configurable_item_options.append({
            "option_id": str(option_id),
            "option_value": option_value
        })
    
    payload = {
        "cartItem": {
            "sku": sku,
            "qty": qty,
            "quote_id": quote_id,
            "product_option": {
                "extension_attributes": {
                    "configurable_item_options": configurable_item_options
                }
            },
            "extension_attributes": {}
        }
    }
    
    response = requests.post(
        url='http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/carts/mine/items',
        headers=headers,
        data=json.dumps(payload)
    )
    
    return response

if __name__ == '__main__':
    # Example parameters for adding a small gray Chaz Kangeroo Hoodie
    r = add_configurable_product_to_cart(
        sku='B09KBNDTWJ',
        qty=1,
        quote_id='123',  # This should be a valid quote_id from an existing cart
        option_selections=[('3681', 18941), ('3682', 18952)]  # Color (Gray) and Size (Small)
    )
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