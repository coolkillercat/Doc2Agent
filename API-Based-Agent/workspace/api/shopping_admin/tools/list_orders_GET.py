import requests
import json
from urllib.parse import quote

def get_shopping_admin_auth_token():
    ENDPOINT = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780'
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


def list_orders(searchCriteria_filterGroups_0_filters_0_field=None, 
                searchCriteria_filterGroups_0_filters_0_value=None, 
                searchCriteria_filterGroups_0_filters_0_conditionType=None, 
                searchCriteria_sortOrders_0_field=None, 
                searchCriteria_sortOrders_0_direction=None, 
                searchCriteria_pageSize=None, 
                searchCriteria_currentPage=None):
    """
    Lists orders that match specified search criteria.
    
    Args:
        searchCriteria_filterGroups_0_filters_0_field (str): Field to filter by (e.g., 'status')
        searchCriteria_filterGroups_0_filters_0_value (str): Value to filter by (e.g., 'pending')
        searchCriteria_filterGroups_0_filters_0_conditionType (str): Condition type (e.g., 'eq')
        searchCriteria_sortOrders_0_field (str): Sorting field (e.g., 'created_at')
        searchCriteria_sortOrders_0_direction (str): Sorting direction (e.g., 'ASC')
        searchCriteria_pageSize (int): Page size
        searchCriteria_currentPage (int): Current page
    
    Returns:
        Returns a list of orders matching specified search criteria with detailed information including customer data, billing, items, payment, and status history.
    Example:
        >>> list_orders(
        ...     searchCriteria_filterGroups_0_filters_0_field='status',
        ...     searchCriteria_filterGroups_0_filters_0_value='pending',
        ...     searchCriteria_filterGroups_0_filters_0_conditionType='eq',
        ...     searchCriteria_sortOrders_0_field='created_at',
        ...     searchCriteria_sortOrders_0_direction='ASC',
        ...     searchCriteria_pageSize=20,
        ...     searchCriteria_currentPage=1
        ... )
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780"
    api_url = f"{base_url}/rest/default/V1/orders"
    
    # Prepare query parameters with correct format
    querystring = {}
    
    # Add searchCriteria parameters
    if searchCriteria_filterGroups_0_filters_0_field:
        querystring["searchCriteria[filterGroups][0][filters][0][field]"] = searchCriteria_filterGroups_0_filters_0_field
    if searchCriteria_filterGroups_0_filters_0_value:
        querystring["searchCriteria[filterGroups][0][filters][0][value]"] = searchCriteria_filterGroups_0_filters_0_value
    if searchCriteria_filterGroups_0_filters_0_conditionType:
        querystring["searchCriteria[filterGroups][0][filters][0][conditionType]"] = searchCriteria_filterGroups_0_filters_0_conditionType
    if searchCriteria_sortOrders_0_field:
        querystring["searchCriteria[sortOrders][0][field]"] = searchCriteria_sortOrders_0_field
    if searchCriteria_sortOrders_0_direction:
        querystring["searchCriteria[sortOrders][0][direction]"] = searchCriteria_sortOrders_0_direction
    if searchCriteria_pageSize:
        querystring["searchCriteria[pageSize]"] = searchCriteria_pageSize
    if searchCriteria_currentPage:
        querystring["searchCriteria[currentPage]"] = searchCriteria_currentPage
    
    # Ensure at least an empty searchCriteria is provided if no specific criteria
    if not querystring:
        querystring["searchCriteria"] = ""
    
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    
    response = requests.get(url=api_url, params=querystring, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = list_orders(
        searchCriteria_filterGroups_0_filters_0_field='status',
        searchCriteria_filterGroups_0_filters_0_value='pending',
        searchCriteria_filterGroups_0_filters_0_conditionType='eq',
        searchCriteria_sortOrders_0_field='created_at',
        searchCriteria_sortOrders_0_direction='ASC',
        searchCriteria_pageSize=20,
        searchCriteria_currentPage=1
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