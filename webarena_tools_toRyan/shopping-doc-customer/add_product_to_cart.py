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


def add_product_to_cart(sku: str, qty: int, quote_id: str, product_type: str = None, options: dict = None) -> dict:
    """
    Universal function to add any type of product to the cart, automatically handling different product types based on either explicit type parameter or detection from SKU.
    
    Args:
        sku (str): Product SKU to add to the cart
        qty (int): Quantity of the product to add
        quote_id (str): The cart ID/quote ID
        product_type (str, optional): Type of product ('simple', 'configurable', 'downloadable', 'bundle')
        options (dict, optional): Additional options for configurable, bundle or downloadable products
    
    Returns:
        requests.Response: The API response object with cart item details
    
    Examples:
        # Add simple product
        response = add_product_to_cart("B0029WB97A", 1, "275")
        
        # Add configurable product
        options = {
            "configurable_item_options": [
                {"option_id": "3681", "option_value": "Black E"},
            ]
        }
        response = add_product_to_cart("B09KBNDTWJ", 1, "275", "configurable", options)
        
        # Add bundle product
        options = {
            "bundle_options": [
                {"option_id": 1, "option_qty": 1, "option_selections": [2]},
                {"option_id": 2, "option_qty": 1, "option_selections": [4]},
                {"option_id": 3, "option_qty": 1, "option_selections": [6]},
                {"option_id": 4, "option_qty": 1, "option_selections": [8]}
            ]
        }
        response = add_product_to_cart("B0029WB97A", 1, "275", "bundle", options)
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    endpoint = f"{base_url}/rest/default/V1/carts/mine/items"
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_customer_auth_token()}
    
    # Prepare the cart item payload
    cart_item = {
        "cartItem": {
            "sku": sku,
            "qty": qty,
            "quote_id": quote_id
        }
    }
    
    # Add product-specific options if provided
    if options:
        if product_type == "configurable" and "configurable_item_options" in options:
            if "product_option" not in cart_item["cartItem"]:
                cart_item["cartItem"]["product_option"] = {"extension_attributes": {}}
            cart_item["cartItem"]["product_option"]["extension_attributes"]["configurable_item_options"] = options["configurable_item_options"]
            cart_item["cartItem"]["extension_attributes"] = {}
            
        elif product_type == "bundle" and "bundle_options" in options:
            if "product_option" not in cart_item["cartItem"]:
                cart_item["cartItem"]["product_option"] = {"extension_attributes": {}}
            cart_item["cartItem"]["product_option"]["extension_attributes"]["bundle_options"] = options["bundle_options"]
            
        elif product_type == "downloadable" and "downloadable_links" in options:
            if "product_option" not in cart_item["cartItem"]:
                cart_item["cartItem"]["product_option"] = {"extension_attributes": {}}
            cart_item["cartItem"]["product_option"]["extension_attributes"]["downloadable_option"] = {
                "downloadable_links": options["downloadable_links"]
            }
    
    # Make the API request
    response = requests.post(
        url=endpoint,
        headers=headers,
        data=json.dumps(cart_item)
    )
    
    return response


if __name__ == '__main__':
    # Example usage: Add simple product to cart
    r = add_product_to_cart(
        sku="B0029WB97A", 
        qty=1, 
        quote_id="275"
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