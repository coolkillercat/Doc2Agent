from urllib.parse import urlencode
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

def build_search_url(endpoint: str, filter_groups: list[list[tuple]], page_size: int = None, current_page: int = None, sort_by: list[str] = None, sort_directions: list[str] = None, return_fields: list[str] = None) -> requests.Response:
    """
    Build and execute a search request using the provided parameters
    
    Args:
        endpoint (str): API endpoint path
        filter_groups (list[list[tuple]]): List of filter groups, each containing list of (field, value, condition_type) tuples
        page_size (int, optional): Number of items per page
        current_page (int, optional): Current page number
        sort_by (list[str], optional): Fields to sort by
        sort_directions (list[str], optional): Sort directions ('ASC' or 'DESC') corresponding to sort_by fields
        return_fields (list[str], optional): Specific fields to return in response
    
    Returns:
        requests.Response: API response object
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    params = {}

    # Build filter groups
    for group_idx, filters in enumerate(filter_groups):
        for filter_idx, (field, value, condition_type) in enumerate(filters):
            params[f'searchCriteria[filter_groups][{group_idx}][filters][{filter_idx}][field]'] = field
            params[f'searchCriteria[filter_groups][{group_idx}][filters][{filter_idx}][value]'] = value
            if condition_type != 'eq':  # condition_type is optional if operator is eq
                params[f'searchCriteria[filter_groups][{group_idx}][filters][{filter_idx}][condition_type]'] = condition_type

    # Add pagination
    if page_size is not None:
        params['searchCriteria[pageSize]'] = page_size
    if current_page is not None:
        params['searchCriteria[currentPage]'] = current_page

    # Add sorting
    if sort_by and sort_directions:
        for idx, (field, direction) in enumerate(zip(sort_by, sort_directions)):
            params[f'searchCriteria[sortOrders][{idx}][field]'] = field
            params[f'searchCriteria[sortOrders][{idx}][direction]'] = direction

    # Add return fields
    if return_fields:
        params['fields'] = f"items[{','.join(return_fields)}]"

    # Build final URL and make request
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    full_url = f"{base_url}{endpoint}?{urlencode(params)}"
    
    return requests.get(full_url, headers=headers)

if __name__ == '__main__':
    # Example usage
    filter_groups = [
        [('status', 'pending', 'eq')]  # Single filter group with one filter
    ]
    r = build_search_url(
        endpoint='/rest/V1/orders',
        filter_groups=filter_groups,
        sort_by=['increment_id'],
        sort_directions=['DESC'],
        return_fields=['increment_id', 'entity_id']
    )
    
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