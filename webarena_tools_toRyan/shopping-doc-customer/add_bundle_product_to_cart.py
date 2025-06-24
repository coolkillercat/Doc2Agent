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


def add_bundle_product_to_cart(sku: str, qty: int, quote_id: str, bundle_selections: list) -> dict:
    """
    Adds a bundle product to the cart with specified component selections.
    
    Args:
        sku (str): The SKU of the bundle product
        qty (int): The quantity of the bundle product to add
        quote_id (str): The quote ID of the cart
        bundle_selections (list): List of tuples containing (option_id, option_qty, option_selections)
            where option_id is the ID of the bundle option
            option_qty is the quantity of the option
            option_selections is a list of IDs for the selected products in that option
    
    Returns:
        requests.Response: The API response object
        
    Example:
        response = add_bundle_product_to_cart(
            "B073JVQ238", 
            1, 
            "123456", 
            [(1, 1, [2]), (2, 1, [4]), (3, 1, [6]), (4, 1, [8])]
        )
    """
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_customer_auth_token()}
    
    # Create bundle options from the provided selections
    bundle_options = []
    for option_id, option_qty, option_selections in bundle_selections:
        bundle_options.append({
            "option_id": option_id,
            "option_qty": option_qty,
            "option_selections": option_selections
        })
    
    payload = {
        "cartItem": {
            "sku": sku,
            "qty": qty,
            "quote_id": quote_id,
            "product_option": {
                "extension_attributes": {
                    "bundle_options": bundle_options
                }
            }
        }
    }
    
    response = requests.post(
        url='http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/carts/mine/items',
        headers=headers,
        data=json.dumps(payload)
    )
    
    return response

if __name__ == '__main__':
    # Example adding the Sprite Yoga Companion Kit with specific options
    r = add_bundle_product_to_cart(
        sku="24-WG080", 
        qty=1, 
        quote_id="1234",  # This should be replaced with an actual quote_id
        bundle_selections=[
            (1, 1, [2]),  # 65 cm Sprite Stasis Ball
            (2, 1, [4]),  # Sprite Foam Yoga Brick
            (3, 1, [6]),  # 8 ft Sprite Yoga strap
            (4, 1, [8])   # Sprite Foam Roller
        ]
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