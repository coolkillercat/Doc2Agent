import requests
import json
from urllib.parse import quote

def get_shopping_admin_auth_token():
    """
    get_shopping_admin_auth_token function.
    
    Returns:
        Returns: A response object containing order information with status code, response text, and a JSON payload. The JSON includes a status field indicating the result of the operation and an "items" array containing the order details. The response also includes the raw content of the API call, which provides comprehensive order information such as customer details, product items, billing/shipping addresses, payment information, and order totals.
    """
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

def get_order_items(order_id: int, return_fields: list = None):
    """
    Retrieves all items in a specific order, useful for order fulfillment and inventory management.
    
    Parameters:
        order_id (int): The ID of the order to retrieve
        return_fields (list, optional): List of specific fields to return in the response.
                                       If None, all fields will be returned.
    
    Returns:
        Returns detailed information about all items in a specific order including pricing, quantities, tax details, and product metadata."""
    base_url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770'
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token(),
    }
    
    url = f"{base_url}/rest/default/V1/orders/{order_id}"
    
    # Add specific fields to return if provided
    if return_fields:
        fields_param = f"fields={','.join(return_fields)}"
        url = f"{url}?{fields_param}"
    
    response = requests.get(url, headers=headers)
    return response

if __name__ == '__main__':
    r = get_order_items(3, ["items", "status"])  # Get order #3 with only items and status fields
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