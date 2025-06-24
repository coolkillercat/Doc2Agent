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


def save_stock(stockId=None, stock=None):
    """
    Save Stock data using the Magento API.
    
    Args:
        stockId (str): The ID of the stock to save. Required.
        stock (dict, optional): The stock data to save. Required.
            Example: {'name': 'Default Stock', 'extension_attributes': {'sales_channels': [{'type': 'website', 'code': 'base'}]}}
    
    Returns:
        requests.Response: The API response object
    
    Example:
        >>> save_stock(
        ...     stockId='1',
        ...     stock={'name': 'Default Stock', 'extension_attributes': {'sales_channels': [{'type': 'website', 'code': 'base'}]}}
        ... )
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    api_url = f"{base_url}/rest/default/V1/inventory/stocks/{stockId}"
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    
    assert stockId is not None, 'Missing required parameter: stockId'
    assert stock is not None, 'Missing required parameter: stock'
    
    payload = {'stock': stock}
    
    response = requests.put(url=api_url, json=payload, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    # Example stock data
    stock_data = {
        'name': 'Default Stock',
        'extension_attributes': {
            'sales_channels': [
                {
                    'type': 'website',
                    'code': 'base'
                }
            ]
        }
    }
    
    r = save_stock(stockId='1', stock=stock_data)
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