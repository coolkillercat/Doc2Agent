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


def search_orders_by_date_range(start_date: str, end_date: str, date_field: str = 'created_at', page_size: int = None, current_page: int = None, sort_by: str = None, sort_direction: str = 'DESC', return_fields: list[str] = None) -> dict:
    """
    Find all orders created or updated within a specific date range.
    
    Args:
        start_date (str): Start date in format 'YYYY-MM-DD HH:MM:SS'
        end_date (str): End date in format 'YYYY-MM-DD HH:MM:SS'
        date_field (str): Field to filter by date (default: 'created_at')
        page_size (int): Number of items per page
        current_page (int): Current page number
        sort_by (str): Field to sort by
        sort_direction (str): Sort direction ('ASC' or 'DESC')
        return_fields (list): List of fields to return in response
        
    Returns:
        requests.Response: API response object
    """
    base_url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770'
    endpoint = f"{base_url}/rest/default/V1/orders"
    
    params = {
        f"searchCriteria[filter_groups][0][filters][0][field]": date_field,
        f"searchCriteria[filter_groups][0][filters][0][value]": start_date,
        f"searchCriteria[filter_groups][0][filters][0][condition_type]": "gteq",
        f"searchCriteria[filter_groups][1][filters][0][field]": date_field,
        f"searchCriteria[filter_groups][1][filters][0][value]": end_date,
        f"searchCriteria[filter_groups][1][filters][0][condition_type]": "lteq"
    }
    
    if page_size:
        params["searchCriteria[pageSize]"] = page_size
        
    if current_page:
        params["searchCriteria[currentPage]"] = current_page
        
    if sort_by:
        params["searchCriteria[sortOrders][0][field]"] = sort_by
        params["searchCriteria[sortOrders][0][direction]"] = sort_direction
        
    if return_fields:
        params["fields"] = f"items[{','.join(return_fields)}]"
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': get_shopping_admin_auth_token()
    }
    
    response = requests.get(endpoint, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = search_orders_by_date_range(
        start_date="2024-01-01 00:00:00",
        end_date="2024-12-31 23:59:59",
        return_fields=["increment_id", "entity_id", "created_at"],
        page_size=10
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