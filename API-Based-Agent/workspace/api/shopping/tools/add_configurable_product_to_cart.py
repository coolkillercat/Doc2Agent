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

def add_configurable_product_to_cart(sku: str, option_selections: list, qty: int = 1) -> dict:
    """
    Adds a configurable product to the cart with specific options like size and color.
    
    Args:
        sku (str): The SKU of the configurable product (e.g., "MH01" for Chaz Kangeroo Hoodie)
        option_selections (list): List of dictionaries containing option_id and option_value pairs
                                 Example: [{"option_id": "93", "option_value": 52},  # Gray color
                                          {"option_id": "141", "option_value": 168}] # Size S
        qty (int, optional): Quantity of the product to add. Defaults to 1.
    
    Returns:
        dict: Response from the API containing information about the added product
    
    Example:
        option_selections = [
            {"option_id": "93", "option_value": 52},  # Gray color
            {"option_id": "141", "option_value": 168}  # Size S
        ]
        
        response = add_configurable_product_to_cart(
            sku="MH01", 
            option_selections=option_selections, 
            qty=1
        )
    """
    # Get authentication token
    auth_token = get_shopping_customer_auth_token()
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    headers = {'Content-Type': 'application/json', 'Authorization': f"Bearer {auth_token}"}
    
    # First, create a cart to get the quote_id
    create_cart_url = f"{base_url}/rest/default/V1/carts/mine"
    cart_response = requests.post(create_cart_url, headers=headers)
    
    if cart_response.status_code != 200:
        return cart_response
    
    quote_id = cart_response.json()
    
    # Prepare the configurable item options
    configurable_item_options = []
    for option in option_selections:
        configurable_item_options.append({
            "option_id": option["option_id"],
            "option_value": option["option_value"]
        })
    
    # Add the item to the cart
    add_to_cart_url = f"{base_url}/rest/default/V1/carts/mine/items"
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
    
    response = requests.post(add_to_cart_url, headers=headers, json=payload)
    return response

if __name__ == '__main__':
    # Example usage with Chaz Kangeroo Hoodie - small gray
    option_selections = [
        {"option_id": "93", "option_value": 52},  # Gray color
        {"option_id": "141", "option_value": 168}  # Size S
    ]
    
    r = add_configurable_product_to_cart(
        sku="MH01", 
        option_selections=option_selections, 
        qty=1
    )
    
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