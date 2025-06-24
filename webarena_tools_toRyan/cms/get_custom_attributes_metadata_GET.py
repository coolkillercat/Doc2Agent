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


def get_custom_attributes_metadata(dataInterfaceName=None):
    """
    Get custom attributes metadata for customer address.
    
    Args:
        dataInterfaceName (str, optional): The data interface name. 
            Example: 'customerAddressInterface'
    
    Returns:
        Returns custom attributes metadata for customer addresses.
    Example:
        >>> response = get_custom_attributes_metadata(dataInterfaceName='customerAddressInterface')
        >>> print(response.status_code)
        200
        >>> print(response.json())
        [...]
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780"
    api_url = f"{base_url}/rest/default/V1/attributeMetadata/customerAddress/custom"
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token()
    }
    
    params = {}
    if dataInterfaceName:
        params['dataInterfaceName'] = dataInterfaceName
    
    response = requests.get(
        url=api_url, 
        params=params, 
        headers=headers, 
        timeout=50, 
        verify=False
    )
    
    return response

if __name__ == '__main__':
    r = get_custom_attributes_metadata(dataInterfaceName='customerAddressInterface')
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