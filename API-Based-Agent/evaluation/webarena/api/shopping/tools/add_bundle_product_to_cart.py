import requests
import json

def get_shopping_customer_auth_token():
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
    return response.json()

def add_bundle_product_to_cart(sku: str, bundle_options: list, qty: int = 1) -> dict:
    """
    Adds a bundle product to the cart with specific bundle item selections.
    
    Args:
        sku (str): The SKU of the bundle product (e.g., "24-WG080" for Sprite Yoga Companion Kit).
        bundle_options (list): List of dictionaries containing option_id, option_qty, and option_selections.
            Example:
            [
                {
                    "option_id": 1,
                    "option_qty": 1,
                    "option_selections": [2]  # 65 cm Sprite Stasis Ball
                },
                {
                    "option_id": 2,
                    "option_qty": 1,
                    "option_selections": [4]  # Sprite Foam Yoga Brick
                }
            ]
        qty (int, optional): Quantity of the bundle product. Defaults to 1.
    
    Returns:
        dict: Response from the API containing information about the added bundle product.
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {get_shopping_customer_auth_token()}'}
    
    # First create a cart
    create_cart_url = f"{base_url}/rest/default/V1/carts/mine"
    cart_response = requests.post(create_cart_url, headers=headers)
    quote_id = cart_response.json()
    
    # Add bundle product to cart
    add_item_url = f"{base_url}/rest/default/V1/carts/mine/items"
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
    
    response = requests.post(add_item_url, headers=headers, json=payload)
    return response.json()

if __name__ == '__main__':
    # Example bundle options for Sprite Yoga Companion Kit
    bundle_options = [
        {
            "option_id": 1,
            "option_qty": 1,
            "option_selections": [2]  # 65 cm Sprite Stasis Ball
        },
        {
            "option_id": 2,
            "option_qty": 1,
            "option_selections": [4]  # Sprite Foam Yoga Brick
        },
        {
            "option_id": 3,
            "option_qty": 1,
            "option_selections": [6]  # 8 ft Sprite Yoga strap
        },
        {
            "option_id": 4,
            "option_qty": 1,
            "option_selections": [8]  # Sprite Foam Roller
        }
    ]
    
    r = add_bundle_product_to_cart(sku="24-WG080", bundle_options=bundle_options)
    r_json = r
    
    result_dict = dict()
    result_dict['status_code'] = 200
    result_dict['text'] = json.dumps(r_json)
    result_dict['json'] = r_json
    result_dict['content'] = json.dumps(r_json)
    print(json.dumps(result_dict, indent=4))