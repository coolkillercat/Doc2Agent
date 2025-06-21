import requests
import json
from urllib.parse import quote

def get_shopping_admin_auth_token():
    """
    get_shopping_admin_auth_token function.
    
    Returns:
        Returns a JSON object containing search results for invoices within the specified date range. The response includes an "items" array with matching invoice records, "search_criteria" that reflects the filters used in the request, and "total_count" indicating the total number of matching records. The status code and raw response content are also included for debugging purposes.
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


def search_invoices_by_date_range(start_date: str, end_date: str, page_size: int = None, current_page: int = None, sort_by: str = None, sort_direction: str = 'DESC', return_fields: list = None):
    """
    Searches for invoices created within a specific date range, useful for financial reporting.

    Parameters:
        start_date (str): Start date for the search in format 'YYYY-MM-DD HH:MM:SS'
        end_date (str): End date for the search in format 'YYYY-MM-DD HH:MM:SS'
        page_size (int, optional): Maximum number of items to return
        current_page (int, optional): Current page number for pagination
        sort_by (str, optional): Field to sort results by
        sort_direction (str, optional): Sort direction ('ASC' or 'DESC'), default is 'DESC'
        return_fields (list, optional): List of fields to return in the response

    Returns:
        Returns a list of invoices within a specified date range with detailed financial information, tax data, and related order details."""
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    endpoint = f"{base_url}/rest/default/V1/invoices"
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token(),
    }
    
    # Build query parameters
    params = {
        'searchCriteria[filter_groups][0][filters][0][field]': 'created_at',
        'searchCriteria[filter_groups][0][filters][0][value]': start_date,
        'searchCriteria[filter_groups][0][filters][0][condition_type]': 'gteq',
        'searchCriteria[filter_groups][1][filters][0][field]': 'created_at',
        'searchCriteria[filter_groups][1][filters][0][value]': end_date,
        'searchCriteria[filter_groups][1][filters][0][condition_type]': 'lteq'
    }
    
    # Add optional parameters if provided
    if page_size is not None:
        params['searchCriteria[pageSize]'] = page_size
    
    if current_page is not None:
        params['searchCriteria[currentPage]'] = current_page
    
    if sort_by is not None:
        params['searchCriteria[sortOrders][0][field]'] = sort_by
        params['searchCriteria[sortOrders][0][direction]'] = sort_direction
    
    if return_fields is not None:
        params['fields'] = ','.join(f'items[{field}]' for field in return_fields)
    
    response = requests.get(endpoint, headers=headers, params=params)
    return response


if __name__ == '__main__':
    r = search_invoices_by_date_range('2023-01-01 00:00:00', '2023-12-31 23:59:59', page_size=10, sort_by='created_at')
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