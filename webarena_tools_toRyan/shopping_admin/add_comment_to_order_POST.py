import requests
import json
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


def add_comment_to_order(id=None, statusHistory=None):
    """
    Adds a comment to a specified order.
    
    Args:
        id (int): The order ID. Required.
        statusHistory (dict): The status history object. Required.
            Example: {
                "comment": "Order comment",
                "created_at": "2023-01-01 12:00:00",
                "entity_id": 0,
                "entity_name": "order",
                "is_customer_notified": 0,
                "is_visible_on_front": 0,
                "parent_id": 0,
                "status": "processing"
            }
    
    Returns:
        requests.Response: The API response object
    
    Example:
        add_comment_to_order(
            id=123,
            statusHistory={
                "comment": "Order is being processed",
                "is_customer_notified": 1,
                "is_visible_on_front": 1
            }
        )
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    api_url = f"{base_url}/rest/default/V1/orders/{id}/comments"
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    
    assert id is not None, 'Missing required parameter: id'
    assert statusHistory is not None, 'Missing required parameter: statusHistory'
    
    payload = {'statusHistory': statusHistory}
    
    response = requests.post(url=api_url, json=payload, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = add_comment_to_order(id=123, statusHistory={})
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