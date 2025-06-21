import requests, json
from urllib.parse import quote

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


def search_products_by_category(category_id: str, page_size: int = None, current_page: int = None, sort_by: str = None, sort_direction: str = 'DESC') -> dict:
    """
    Find all products belonging to a specific category. Uses the finset condition type to match products assigned to the given category.
    
    Args:
        category_id (str): The category ID to search for
        page_size (int, optional): Maximum number of items to return
        current_page (int, optional): Current page number
        sort_by (str, optional): Field to sort by
        sort_direction (str, optional): Sort direction ('ASC' or 'DESC')
    
    Returns:
        Returns a list of products that belong to a specific category along with search metadata and total count."""
    base_url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770'
    endpoint = f'{base_url}/rest/default/V1/products'
    
    params = {
        'searchCriteria[filter_groups][0][filters][0][field]': 'category_id',
        'searchCriteria[filter_groups][0][filters][0][value]': category_id,
        'searchCriteria[filter_groups][0][filters][0][condition_type]': 'finset'
    }
    
    if page_size:
        params['searchCriteria[pageSize]'] = page_size
    
    if current_page:
        params['searchCriteria[currentPage]'] = current_page
        
    if sort_by:
        params['searchCriteria[sortOrders][0][field]'] = sort_by
        params['searchCriteria[sortOrders][0][direction]'] = sort_direction

    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    
    response = requests.get(endpoint, params=params, headers=headers)
    return response

if __name__ == '__main__':
    r = search_products_by_category('1', page_size=10, current_page=1, sort_by='name')
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