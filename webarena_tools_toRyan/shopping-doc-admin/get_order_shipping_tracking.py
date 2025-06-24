import requests, json
from urllib.parse import quote

def get_shopping_admin_auth_token():
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


def get_order_details(order_id: int):
    """
    Retrieves full details for a specific order based on the order ID.
    
    Args:
        order_id (int): The ID of the order to retrieve
        
    Returns:
        requests.Response: The response object containing order details including
        customer information, payment details, item information, and shipping details
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    endpoint = f"/rest/default/V1/orders/{order_id}"
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': get_shopping_admin_auth_token()
    }
    
    response = requests.get(
        url=f"{base_url}{endpoint}",
        headers=headers
    )
    
    return response

if __name__ == '__main__':
    r = get_order_details(3)  # Using order ID 3 based on the example in documentation
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