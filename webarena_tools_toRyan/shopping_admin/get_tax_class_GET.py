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


def get_tax_class(taxClassId=None):
    """
    Get a tax class with the given tax class id.
    
    Args:
        taxClassId (int): The ID of the tax class to retrieve.
        
    Returns:
        requests.Response: The response from the API.
        
    Example:
        >>> get_tax_class(taxClassId=3)
    """
    assert taxClassId is not None, 'Missing required parameter: taxClassId'
    
    base_url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770'
    api_url = f"{base_url}/rest/default/V1/taxClasses/{taxClassId}"
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    
    response = requests.get(url=api_url, headers=headers, timeout=50, verify=False)
    return response


def delete_tax_class(taxClassId=None):
    """
    Delete a tax class with the given tax class id.
    
    Args:
        taxClassId (int): The ID of the tax class to delete.
        
    Returns:
        requests.Response: The response from the API.
        
    Example:
        >>> delete_tax_class(taxClassId=3)
    """
    assert taxClassId is not None, 'Missing required parameter: taxClassId'
    
    base_url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770'
    api_url = f"{base_url}/rest/default/V1/taxClasses/{taxClassId}"
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    
    response = requests.delete(url=api_url, headers=headers, timeout=50, verify=False)
    return response


if __name__ == '__main__':
    r = get_tax_class(taxClassId=3)
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