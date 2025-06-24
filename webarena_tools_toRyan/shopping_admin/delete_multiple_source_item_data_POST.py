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


def delete_multiple_source_item_data(source_items=None):
    """
    Delete multiple source item data from inventory.
    
    Args:
        source_items (list, optional): List of source items to delete. Each item should be a dict 
                                      containing 'source_code' and 'sku'. Defaults to None.
    
    Returns:
        requests.Response: The API response object.
    
    Example:
        >>> items = [
        ...     {"source_code": "default", "sku": "24-MB01"},
        ...     {"source_code": "default", "sku": "24-MB02"}
        ... ]
        >>> response = delete_multiple_source_item_data(source_items=items)
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    api_url = f"{base_url}/rest/default/V1/inventory/source-items-delete"
    
    if source_items is None:
        source_items = [
            {"source_code": "default", "sku": "sample-sku-1"},
            {"source_code": "default", "sku": "sample-sku-2"}
        ]
    
    payload = {"sourceItems": source_items}
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    
    response = requests.post(url=api_url, json=payload, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = delete_multiple_source_item_data()
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