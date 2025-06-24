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


def search_orders(field: str, value: str, condition_type: str = 'eq', page_size: int = None, current_page: int = None, sort_by: str = None, sort_direction: str = 'DESC', return_fields: list[str] = None) -> dict:
    """
    Search for orders using a single filter criterion. Can specify which fields to return in the response to optimize payload size.
    
    Args:
        field (str): The field to filter on
        value (str): The value to filter by
        condition_type (str): The condition type for filtering (default: 'eq')
        page_size (int): Number of items per page (optional)
        current_page (int): The current page number (optional)
        sort_by (str): Field to sort by (optional)
        sort_direction (str): Sort direction - 'ASC' or 'DESC' (default: 'DESC')
        return_fields (list[str]): List of fields to return in response (optional)
    
    Returns:
        requests.Response: API response
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    
    params = {
        f'searchCriteria[filter_groups][0][filters][0][field]': field,
        f'searchCriteria[filter_groups][0][filters][0][value]': value,
        f'searchCriteria[filter_groups][0][filters][0][condition_type]': condition_type
    }
    
    if page_size:
        params['searchCriteria[pageSize]'] = page_size
    
    if current_page:
        params['searchCriteria[currentPage]'] = current_page
        
    if sort_by:
        params['searchCriteria[sortOrders][0][field]'] = sort_by
        params['searchCriteria[sortOrders][0][direction]'] = sort_direction
        
    if return_fields:
        params['fields'] = f"items[{','.join(return_fields)}]"
    
    response = requests.get(
        f"{base_url}/rest/default/V1/orders",
        headers=headers,
        params=params
    )
    
    return response

if __name__ == '__main__':
    r = search_orders(
        field="status",
        value="pending",
        return_fields=["increment_id", "entity_id"]
    )
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