import requests
import json
from urllib.parse import quote
import warnings

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


def find_stocks(searchCriteria_filterGroups_0_filters_0_field=None, 
                searchCriteria_filterGroups_0_filters_0_value=None, 
                searchCriteria_filterGroups_0_filters_0_conditionType=None, 
                searchCriteria_sortOrders_0_field=None, 
                searchCriteria_sortOrders_0_direction=None, 
                searchCriteria_pageSize=None, 
                searchCriteria_currentPage=None):
    """
    Find stocks by given search criteria.
    
    Args:
        searchCriteria_filterGroups_0_filters_0_field (str, optional): Field to filter by. Example: 'name'
        searchCriteria_filterGroups_0_filters_0_value (str, optional): Value to filter by. Example: 'Default Stock'
        searchCriteria_filterGroups_0_filters_0_conditionType (str, optional): Condition type. Example: 'eq'
        searchCriteria_sortOrders_0_field (str, optional): Sorting field. Example: 'stock_id'
        searchCriteria_sortOrders_0_direction (str, optional): Sorting direction. Example: 'ASC'
        searchCriteria_pageSize (int, optional): Page size. Example: 20
        searchCriteria_currentPage (int, optional): Current page. Example: 1
    
    Returns:
        Returns a list of inventory stocks with their identifiers, names, and extension attributes based on specified search criteria.
    Example:
        >>> response = find_stocks(
        ...     searchCriteria_filterGroups_0_filters_0_field='name',
        ...     searchCriteria_filterGroups_0_filters_0_value='Default Stock',
        ...     searchCriteria_filterGroups_0_filters_0_conditionType='eq',
        ...     searchCriteria_sortOrders_0_field='stock_id',
        ...     searchCriteria_sortOrders_0_direction='ASC',
        ...     searchCriteria_pageSize=20,
        ...     searchCriteria_currentPage=1
        ... )
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780"
    api_url = f"{base_url}/rest/default/V1/inventory/stocks"
    
    querystring = {}
    if searchCriteria_filterGroups_0_filters_0_field:
        querystring['searchCriteria[filterGroups][0][filters][0][field]'] = searchCriteria_filterGroups_0_filters_0_field
    if searchCriteria_filterGroups_0_filters_0_value:
        querystring['searchCriteria[filterGroups][0][filters][0][value]'] = searchCriteria_filterGroups_0_filters_0_value
    if searchCriteria_filterGroups_0_filters_0_conditionType:
        querystring['searchCriteria[filterGroups][0][filters][0][conditionType]'] = searchCriteria_filterGroups_0_filters_0_conditionType
    if searchCriteria_sortOrders_0_field:
        querystring['searchCriteria[sortOrders][0][field]'] = searchCriteria_sortOrders_0_field
    if searchCriteria_sortOrders_0_direction:
        querystring['searchCriteria[sortOrders][0][direction]'] = searchCriteria_sortOrders_0_direction
    if searchCriteria_pageSize:
        querystring['searchCriteria[pageSize]'] = searchCriteria_pageSize
    if searchCriteria_currentPage:
        querystring['searchCriteria[currentPage]'] = searchCriteria_currentPage
    
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    
    warnings.filterwarnings('ignore', message='Unverified HTTPS request')
    response = requests.get(url=api_url, params=querystring, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = find_stocks()
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