import requests
import json
from urllib.parse import quote

def get_shopping_admin_auth_token():
    """
    get_shopping_admin_auth_token function.
    
    Returns:
        Returns: A response object containing order information with HTTP status code, response text, and a JSON object with key order details. The JSON includes the customer's email address, the order's increment ID (unique identifier), and the current order status. The full response content is also available as a string in the 'content' field.
    """
    ENDPOINT = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780'
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


def get_order_by_id(order_id: int, return_fields: list = None):
    """
    Retrieves detailed information about a specific order by its ID, with option to specify which fields to return.
    
    Args:
        order_id (int): The ID of the order to retrieve
        return_fields (list, optional): List of fields to include in the response. If None, all fields are returned.
    
    Returns:
        Returns detailed order information including customer email, order ID, and status for a specific order."""
    base_url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780'
    endpoint = f'{base_url}/rest/default/V1/orders/{order_id}'
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token(),
    }
    
    params = {}
    if return_fields:
        fields_str = ','.join(return_fields)
        params['fields'] = fields_str
    
    response = requests.get(endpoint, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = get_order_by_id(3, ['increment_id', 'customer_email', 'status'])
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