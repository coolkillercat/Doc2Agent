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


def add_invoice_comment(entity=None):
    """
    Add a comment to an invoice using the Magento API.
    
    Args:
        entity (dict): A dictionary containing the invoice comment data.
            Required fields:
                - parent_id (int): The ID of the invoice
                - comment (str): The comment text
            Optional fields:
                - is_visible_on_front (int): Whether the comment is visible to customers (0 or 1)
                - is_customer_notified (int): Whether the customer was notified (0 or 1)
    
    Returns:
        requests.Response: The API response object
    
    Example:
        >>> add_invoice_comment(entity={
        ...     'parent_id': 1,
        ...     'comment': 'This is a sample comment',
        ...     'is_visible_on_front': 1,
        ...     'is_customer_notified': 0
        ... })
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    api_url = f"{base_url}/rest/default/V1/invoices/comments"
    
    assert entity is not None, 'Missing required parameter: entity'
    
    # Convert boolean values to integers
    if 'is_visible_on_front' in entity and isinstance(entity['is_visible_on_front'], bool):
        entity['is_visible_on_front'] = 1 if entity['is_visible_on_front'] else 0
    
    if 'is_customer_notified' in entity and isinstance(entity['is_customer_notified'], bool):
        entity['is_customer_notified'] = 1 if entity['is_customer_notified'] else 0
    
    payload = {'entity': entity}
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    
    response = requests.post(url=api_url, json=payload, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = add_invoice_comment(entity={
        'parent_id': 1,
        'comment': 'This is a sample comment',
        'is_visible_on_front': 1,
        'is_customer_notified': 0
    })
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