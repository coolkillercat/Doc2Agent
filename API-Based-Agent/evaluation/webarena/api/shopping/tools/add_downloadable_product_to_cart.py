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

def add_downloadable_product_to_cart(sku: str, qty: int = 1) -> dict:
    """
    Adds a downloadable product to the customer's cart by providing the product SKU and quantity.
    
    This function first creates a cart if one doesn't exist, then adds the specified downloadable
    product to the cart.
    
    Args:
        sku (str): The SKU of the downloadable product to add to the cart.
                   Example: "240-LV08" for Advanced Pilates & Yoga.
        qty (int): The quantity of the product to add, defaults to 1.
    
    Returns:
        dict: The response containing information about the added item including:
              - item_id: The ID of the item in the cart
              - sku: The SKU of the added product
              - qty: The quantity added
              - name: The product name
              - price: The product price
              - product_type: The type of product (downloadable)
              - quote_id: The cart ID
              - product_option: Contains downloadable product options
    """
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': f'Bearer {get_shopping_customer_auth_token()}'
    }
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    
    # Create a cart first to get the quote_id
    create_cart_url = f"{base_url}/rest/default/V1/carts/mine"
    cart_response = requests.post(create_cart_url, headers=headers)
    quote_id = cart_response.json()
    
    # Add the downloadable product to the cart
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
    r = add_downloadable_product_to_cart("240-LV08")  # Adding the Advanced Pilates & Yoga product
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