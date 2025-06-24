import requests
import json
from urllib.parse import quote

def get_shopping_admin_auth_token():
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


def low_quantity_notification(sourceItemConfigurations=None):
    """
    Set low quantity notification configuration for specified source items.
    
    Args:
        sourceItemConfigurations (list): List of source item configurations.
            Each item should be a dict with source_code, sku, and notify_stock_qty.
            
    Example:
        sourceItemConfigurations = [
            {
                "source_code": "default",
                "sku": "24-MB01",
                "notify_stock_qty": 5
            }
        ]
        
    Returns:
        Returns a list of source items that have been configured with low quantity notification thresholds."""
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780"
    api_url = f"{base_url}/rest/default/V1/inventory/low-quantity-notification"
    
    assert sourceItemConfigurations is not None, 'Missing required parameter: sourceItemConfigurations'
    
    # Ensure sourceItemConfigurations is properly formatted
    if isinstance(sourceItemConfigurations, str):
        try:
            sourceItemConfigurations = json.loads(sourceItemConfigurations)
        except json.JSONDecodeError:
            raise ValueError("sourceItemConfigurations must be a valid JSON string or list")
    
    payload = {'sourceItemConfigurations': sourceItemConfigurations}
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    
    response = requests.post(url=api_url, json=payload, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    # Properly formatted example
    source_items = [
        {
            "source_code": "default",
            "sku": "24-MB01",
            "notify_stock_qty": 5
        }
    ]
    
    r = low_quantity_notification(sourceItemConfigurations=source_items)
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