import requests
import json
from urllib.parse import quote

def get_shopping_admin_auth_token():
    """
    get_shopping_admin_auth_token function.
    
    Returns:
        Returns: A response object containing order search results. The response includes a status code, raw text content, and a JSON object with an "items" array containing the matching orders. Each order in the items array contains details such as order ID, customer information, order status, payment details, and line items, with the exact fields depending on the search criteria and any field selection parameters specified in the request.
    """
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

def search_orders(field: str, value: str, condition_type: str = 'eq', page_size: int = None, current_page: int = None, sort_by: str = None, sort_direction: str = 'DESC', return_fields: list = None):
    """
    Searches for orders based on specified criteria, with support for pagination, sorting, and field selection.
    
    Args:
        field (str): The field to search on
        value (str): The value to search for
        condition_type (str, optional): The condition type for filtering. Defaults to 'eq'.
        page_size (int, optional): Maximum number of items to return. Defaults to None.
        current_page (int, optional): Current page number. Defaults to None.
        sort_by (str, optional): Field to sort by. Defaults to None.
        sort_direction (str, optional): Sort direction, either 'ASC' or 'DESC'. Defaults to 'DESC'.
        return_fields (list, optional): List of fields to return in the response. Defaults to None.
        
    Returns:
        Returns order search results matching specified criteria, including order IDs, customer information, and order details."""
    BASE_URL = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': get_shopping_admin_auth_token(),
    }
    
    # Build the search criteria URL
    search_url = f"{BASE_URL}/rest/default/V1/orders?"
    search_url += f"searchCriteria[filter_groups][0][filters][0][field]={quote(field)}&"
    search_url += f"searchCriteria[filter_groups][0][filters][0][value]={quote(str(value))}&"
    search_url += f"searchCriteria[filter_groups][0][filters][0][condition_type]={quote(condition_type)}"
    
    # Add pagination if specified
    if page_size is not None:
        search_url += f"&searchCriteria[pageSize]={page_size}"
    if current_page is not None:
        search_url += f"&searchCriteria[currentPage]={current_page}"
    
    # Add sorting if specified
    if sort_by is not None:
        search_url += f"&searchCriteria[sortOrders][0][field]={quote(sort_by)}"
        search_url += f"&searchCriteria[sortOrders][0][direction]={quote(sort_direction)}"
    
    # Add field filtering if specified
    if return_fields is not None and len(return_fields) > 0:
        fields_str = ",".join(return_fields)
        search_url += f"&fields=items[{fields_str}]"
    
    # Make the request
    response = requests.get(search_url, headers=headers)
    return response

if __name__ == '__main__':
    # Example usage: Search for pending orders, return only increment_id and entity_id
    r = search_orders(
        field="status", 
        value="pending", 
        page_size=10, 
        sort_by="created_at", 
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