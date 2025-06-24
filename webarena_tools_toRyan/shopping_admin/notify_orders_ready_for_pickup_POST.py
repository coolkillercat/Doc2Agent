import requests
import json

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


def notify_orders_ready_for_pickup(orderIds):
    """
    Notify customer that the orders are ready for pickup.
    
    Args:
        orderIds (list): List of order IDs to notify as ready for pickup.
            Example: [101, 102, 103]
    
    Returns:
        requests.Response: The API response object.
    
    Raises:
        AssertionError: If orderIds parameter is None or not provided.
    """
    assert orderIds is not None, 'Missing required parameter: orderIds'
    
    # Convert set of tuples to list of integers if needed
    if isinstance(orderIds, set):
        order_ids_list = [order_id[1] for order_id in orderIds if isinstance(order_id, tuple)]
    else:
        order_ids_list = orderIds
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    api_url = f"{base_url}/rest/default/V1/order/notify-orders-are-ready-for-pickup"
    
    payload = {'orderIds': order_ids_list}
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    
    response = requests.post(url=api_url, json=payload, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = notify_orders_ready_for_pickup(orderIds=[101, 102, 103])
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