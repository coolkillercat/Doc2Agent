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


def search_orders_by_status(status: str, page_size: int = None, current_page: int = None, sort_by: str = None, sort_direction: str = 'DESC', return_fields: list[str] = None) -> dict:
    """
    Find all orders with a specific status (e.g., 'pending', 'processing', 'complete'). Returns customizable fields for each order.
    
    Args:
        status (str): Order status to filter by
        page_size (int, optional): Number of items per page
        current_page (int, optional): Current page number
        sort_by (str, optional): Field to sort results by
        sort_direction (str, optional): Sort direction ('ASC' or 'DESC')
        return_fields (list[str], optional): List of fields to return in response
    
    Returns:
        dict: API response containing matching orders
    """
    ENDPOINT = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770'
    
    # Build base URL with status filter
    url = f"{ENDPOINT}/rest/default/V1/orders?"
    url += f"searchCriteria[filter_groups][0][filters][0][field]=status&"
    url += f"searchCriteria[filter_groups][0][filters][0][value]={status}"
    
    # Add optional parameters
    if page_size:
        url += f"&searchCriteria[pageSize]={page_size}"
    if current_page:
        url += f"&searchCriteria[currentPage]={current_page}"
    if sort_by:
        url += f"&searchCriteria[sortOrders][0][field]={sort_by}"
        url += f"&searchCriteria[sortOrders][0][direction]={sort_direction}"
    if return_fields:
        fields_str = "items[" + ",".join(return_fields) + "]"
        url += f"&fields={quote(fields_str)}"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': get_shopping_admin_auth_token()
    }

    response = requests.get(url, headers=headers)
    return response

if __name__ == '__main__':
    r = search_orders_by_status(
        status='pending',
        page_size=10,
        current_page=1,
        sort_by='created_at',
        sort_direction='DESC',
        return_fields=['increment_id', 'entity_id', 'status']
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