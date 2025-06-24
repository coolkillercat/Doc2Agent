import requests, json
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


def find_products_by_sku(sku: str, match_type: str = 'exact'):
    """
    Locates products by their SKU with options for exact matching or partial/like matching, useful for inventory management.
    
    Args:
        sku (str): The product SKU to search for
        match_type (str): Type of matching - 'exact' for exact match or 'like' for partial match
    
    Returns:
        requests.Response: The API response object
    """
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token(), }
    
    base_url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770'
    
    # Determine the condition type based on match_type
    condition_type = 'eq' if match_type == 'exact' else 'like'
    
    # If using 'like' match, add wildcards to the SKU value
    if match_type == 'like':
        sku_value = f'%{sku}%'
    else:
        sku_value = sku
    
    # Build the endpoint URL with search criteria
    endpoint = f"{base_url}/rest/default/V1/search"
    params = {
        'searchCriteria[requestName]': 'advanced_search_container',
        'searchCriteria[filterGroups][0][filters][0][field]': 'sku',
        'searchCriteria[filterGroups][0][filters][0][value]': sku_value,
        'searchCriteria[filterGroups][0][filters][0][condition_type]': condition_type
    }
    
    # Make the request
    response = requests.get(endpoint, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = find_products_by_sku("shirt", "like")  # Search for products with "shirt" in the SKU
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