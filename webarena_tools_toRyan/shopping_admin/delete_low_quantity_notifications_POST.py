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


def delete_low_quantity_notifications(source_items=None):
    """
    Delete multiple source items configuration for low quantity notifications.
    
    Args:
        source_items (list): List of source items to delete. Each item should contain source_code and sku.
            Example: [{"source_code": "default", "sku": "24-MB01"}]
    
    Returns:
        requests.Response: The API response object
    
    Example:
        >>> delete_low_quantity_notifications([{"source_code": "default", "sku": "24-MB01"}])
    """
    api_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/inventory/low-quantity-notifications-delete"
    
    if source_items is None:
        source_items = []
    
    payload = {"sourceItems": source_items}
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    
    response = requests.post(url=api_url, json=payload, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    # Example source items
    sample_source_items = [{"source_code": "default", "sku": "24-MB01"}]
    
    r = delete_low_quantity_notifications(sample_source_items)
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