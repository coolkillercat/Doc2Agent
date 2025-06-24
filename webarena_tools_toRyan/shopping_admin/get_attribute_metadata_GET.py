import requests
import json
from typing import Dict, List, Optional, Any

def get_shopping_admin_auth_token() -> str:
    """
    Get admin authentication token for Magento API.
    
    Returns:
        str: Bearer token for API authentication
    """
    ENDPOINT = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770'
    response = requests.post(
        url=f'{ENDPOINT}/rest/default/V1/integration/admin/token',
        headers={
            'content-type': 'application/json'
        },
        data=json.dumps({
            'username': 'admin',
            'password': 'admin1234'
        })
    )
    return "Bearer " + response.json()


def get_attribute_metadata(base_url: str = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770") -> Dict[str, Any]:
    """
    Retrieve customer attribute metadata from Magento API.
    
    This function fetches all customer attribute metadata including field types,
    validation rules, and display properties.
    
    Args:
        base_url (str, optional): Base URL for the Magento API. 
            Defaults to "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770".
    
    Returns:
        Dict[str, Any]: Response object containing attribute metadata
        
    Example:
        >>> response = get_attribute_metadata()
        >>> print(response.status_code)  # Should be 200 if successful
        >>> attributes = response.json()
        >>> for attr in attributes:
        >>>     print(attr['attribute_code'], attr['frontend_label'])
    """
    api_url = f"{base_url}/rest/default/V1/attributeMetadata/customer"
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token()
    }
    
    response = requests.get(
        url=api_url, 
        headers=headers, 
        timeout=50, 
        verify=False
    )
    
    return response


if __name__ == '__main__':
    r = get_attribute_metadata()
    r_json = None
    try:
        r_json = r.json()
    except:
        pass
    
    result_dict = {
        'status_code': r.status_code,
        'text': r.text,
        'json': r_json,
        'content': r.content.decode("utf-8")
    }
    print(json.dumps(result_dict, indent=4))