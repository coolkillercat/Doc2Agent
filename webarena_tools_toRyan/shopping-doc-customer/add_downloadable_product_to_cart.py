import requests
import json

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


def add_downloadable_product_to_cart(sku: str, qty: int, quote_id: str = None) -> requests.Response:
    """
    Adds a downloadable product to the customer's cart using the product SKU and quantity.
    
    Args:
        sku (str): The SKU of the downloadable product to add to the cart
        qty (int): The quantity of the product to add
        quote_id (str, optional): The quote ID of the cart. If not provided, the API will use the customer's cart.
        
    Returns:
        requests.Response: The response from the API
        
    Example:
        response = add_downloadable_product_to_cart("B08B8438JS", 1)
        response = add_downloadable_product_to_cart("B08B8438JS", 1, "12345")
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    url = f"{base_url}/rest/default/V1/carts/mine/items"
    
    token = get_shopping_customer_auth_token()
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': token
    }
    
    payload = {
        "cartItem": {
            "sku": sku,
            "qty": qty
        }
    }
    
    if quote_id:
        payload["cartItem"]["quote_id"] = quote_id
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response

if __name__ == '__main__':
    # Example parameters for testing
    r = add_downloadable_product_to_cart("B0029WB97A", 1)
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