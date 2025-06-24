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


def search_products_by_price_range(min_price: float, max_price: float, search_type: str = 'quick_search_container'):
    """
    Finds all products within a specified price range using either quick search, advanced search, or catalog view search methods.
    
    Args:
        min_price (float): The minimum price to search for
        max_price (float): The maximum price to search for
        search_type (str): The type of search to perform. Can be 'quick_search_container', 
                          'advanced_search_container', or 'catalog_view_container'
    
    Returns:
        requests.Response: The API response object
    """
    BASE_URL = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770'
    
    # Validate search_type
    valid_search_types = ['quick_search_container', 'advanced_search_container', 'catalog_view_container']
    if search_type not in valid_search_types:
        raise ValueError(f"search_type must be one of {valid_search_types}")
    
    # Construct the URL
    url = f"{BASE_URL}/rest/default/V1/search"
    
    # Construct query parameters
    params = {
        'searchCriteria[requestName]': search_type,
        'searchCriteria[filterGroups][0][filters][0][field]': 'price.from',
        'searchCriteria[filterGroups][0][filters][0][value]': min_price,
        'searchCriteria[filterGroups][0][filters][1][field]': 'price.to',
        'searchCriteria[filterGroups][0][filters][1][value]': max_price
    }
    
    # Set headers
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token()
    }
    
    # Make the request
    response = requests.get(url, params=params, headers=headers)
    
    return response

if __name__ == '__main__':
    r = search_products_by_price_range(10, 50, 'quick_search_container')
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