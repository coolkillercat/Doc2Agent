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


def save_stocksourcelink_list(links=None):
    """
    Save StockSourceLink list data to the inventory system.
    
    Args:
        links (list, optional): A list of stock source links to save. Each link should be a dictionary
                               containing the required fields. Default is None.
                               
    Example:
        links = [
            {
                "stock_id": 1,
                "source_code": "default",
                "priority": 1
            }
        ]
        response = save_stocksourcelink_list(links=links)
        
    Returns:
        requests.Response: The API response object
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    api_url = f"{base_url}/rest/default/V1/inventory/stock-source-links"
    
    # If links is not provided, create a default example
    if links is None:
        links = [
            {
                "stock_id": 1,
                "source_code": "default",
                "priority": 1
            }
        ]
    
    payload = {"links": links}
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    
    response = requests.post(url=api_url, json=payload, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = save_stocksourcelink_list()
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