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


def get_product_aggregations(search_term: str = None, category_id: int = None):
    """
    Retrieves product aggregations and buckets from search results, useful for faceted navigation and filtering options.
    
    Args:
        search_term (str, optional): The search term to filter products by. Defaults to None.
        category_id (int, optional): The category ID to filter products by. Defaults to None.
        
    Returns:
        requests.Response: The response object containing search results with aggregations.
    """
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token(), }
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/search"
    params = {
        'searchCriteria[requestName]': 'quick_search_container'
    }
    
    filter_index = 0
    
    if search_term:
        params[f'searchCriteria[filterGroups][0][filters][{filter_index}][field]'] = 'search_term'
        params[f'searchCriteria[filterGroups][0][filters][{filter_index}][value]'] = search_term
        filter_index += 1
        
    if category_id:
        params[f'searchCriteria[filterGroups][0][filters][{filter_index}][field]'] = 'category_ids'
        params[f'searchCriteria[filterGroups][0][filters][{filter_index}][value]'] = category_id
    
    response = requests.get(base_url, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = get_product_aggregations(search_term="digital watch")  # Example with search term
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