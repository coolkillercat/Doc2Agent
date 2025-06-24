import requests
import json
from urllib.parse import quote
import warnings

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


def dump_stock_index_data(salesChannelType='website', salesChannelCode='base'):
    """
    Provides stock index export from inventory_stock_% table.
    
    Args:
        salesChannelType (str): The type of sales channel (e.g., 'website')
        salesChannelCode (str): The code of sales channel (e.g., 'base')
    
    Returns:
        requests.Response: The API response object
    
    Example:
        >>> response = dump_stock_index_data(salesChannelType='website', salesChannelCode='base')
        >>> print(response.status_code)
        200
    """
    assert salesChannelType is not None, 'Missing required parameter: salesChannelType'
    assert salesChannelCode is not None, 'Missing required parameter: salesChannelCode'
    
    base_url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770'
    api_url = f"{base_url}/rest/default/V1/inventory/dump-stock-index-data/{quote(salesChannelType, safe='')}/{quote(salesChannelCode, safe='')}"
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token()
    }
    
    warnings.filterwarnings('ignore', message='Unverified HTTPS request')
    response = requests.get(url=api_url, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = dump_stock_index_data(salesChannelType='website', salesChannelCode='base')
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