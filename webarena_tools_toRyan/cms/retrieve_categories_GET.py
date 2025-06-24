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


def retrieve_categories(rootCategoryId=None, depth=None):
    """
    Retrieve list of categories from the Magento API.
    
    Args:
        rootCategoryId (int, optional): The ID of the root category to retrieve. Defaults to None.
        depth (int, optional): The depth of category tree to retrieve. Defaults to None.
    
    Returns:
        Returns a hierarchical list of product categories with their IDs, names, positions, levels, and product counts.
    Example:
        >>> response = retrieve_categories(rootCategoryId=1, depth=2)
        >>> categories = response.json()
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780"
    api_url = f"{base_url}/rest/default/V1/categories"
    
    # Remove None values from querystring
    querystring = {}
    if rootCategoryId is not None:
        querystring['rootCategoryId'] = rootCategoryId
    if depth is not None:
        querystring['depth'] = depth
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token()
    }
    
    response = requests.get(url=api_url, params=querystring, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = retrieve_categories(rootCategoryId=1, depth=2)
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