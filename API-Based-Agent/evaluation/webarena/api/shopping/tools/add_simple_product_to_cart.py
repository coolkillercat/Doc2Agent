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

def add_simple_product_to_cart(sku: str, qty: int = 1) -> dict:
    """
    Adds a simple product to the customer's cart by providing the product SKU and quantity.
    
    This function first creates a cart if one doesn't exist, then adds the specified product to it.
    
    Args:
        sku (str): The SKU of the product to add to the cart (e.g., "WS12-M-Orange")
        qty (int): The quantity of the product to add (default: 1)
        
    Returns:
        dict: The response containing information about the added item including:
              - item_id: The ID of the item in the cart
              - sku: The SKU of the added product
              - qty: The quantity added
              - name: The product name
              - price: The product price
              - product_type: The type of product (e.g., "simple")
              - quote_id: The cart ID
    
    Example:
        >>> add_simple_product_to_cart("WS12-M-Orange", 2)
        {
            "item_id": 7,
            "sku": "WS12-M-Orange",
            "qty": 2,
            "name": "Radiant Tee-M-Orange",
            "price": 19.99,
            "product_type": "simple",
            "quote_id": "123"
        }
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    auth_token = f"Bearer {get_shopping_customer_auth_token()}"
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': auth_token
    }
    
    # First, create a cart to get the quote_id
    create_cart_url = f"{base_url}/rest/default/V1/carts/mine"
    cart_response = requests.post(create_cart_url, headers=headers)
    
    if cart_response.status_code != 200:
        return cart_response
    
    quote_id = cart_response.json()
    
    # Add the product to the cart
    add_item_url = f"{base_url}/rest/default/V1/carts/mine/items"
    
    payload = {
        "cartItem": {
            "sku": sku,
            "qty": qty,
            "quote_id": quote_id
        }
    }
    
    response = requests.post(add_item_url, headers=headers, json=payload)
    return response

if __name__ == '__main__':
    r = add_simple_product_to_cart("WS12-M-Orange", 1)
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