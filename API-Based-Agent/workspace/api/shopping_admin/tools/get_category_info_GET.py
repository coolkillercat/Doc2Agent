import requests
import json

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


def get_category_info(categoryId=None, storeId=None):
    """
    Get information about a category by its ID.
    
    Args:
        categoryId (int): The ID of the category to retrieve (required).
        storeId (int, optional): The ID of the store to filter by.
        
    Returns:
        requests.Response: The API response object.
        
    Example:
        >>> response = get_category_info(categoryId=11)
        >>> response = get_category_info(categoryId=11, storeId=1)
    """
    assert categoryId is not None, 'Missing required parameter: categoryId'
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780"
    api_url = f"{base_url}/rest/default/V1/categories/{categoryId}"
    
    params = {}
    if storeId is not None:
        params['storeId'] = storeId
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token()
    }
    
    response = requests.get(url=api_url, params=params, headers=headers, timeout=50, verify=False)
    return response


def delete_category(categoryId=None):
    """
    Delete a category by its ID.
    
    Args:
        categoryId (int): The ID of the category to delete (required).
        
    Returns:
        Returns information about a deleted category including its ID, name, hierarchy details, status, and custom attributes.
    Example:
        >>> response = delete_category(categoryId=11)
    """
    assert categoryId is not None, 'Missing required parameter: categoryId'
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780"
    api_url = f"{base_url}/rest/default/V1/categories/{categoryId}"
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token()
    }
    
    response = requests.delete(url=api_url, headers=headers, timeout=50, verify=False)
    return response


if __name__ == '__main__':
    r = get_category_info(categoryId=11, storeId=1)
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