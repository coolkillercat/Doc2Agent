import requests
import json
from urllib.parse import quote

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


def list_credit_memos(
    searchCriteria_filterGroups_0_filters_0_field=None, 
    searchCriteria_filterGroups_0_filters_0_value=None, 
    searchCriteria_filterGroups_0_filters_0_conditionType=None, 
    searchCriteria_sortOrders_0_field=None, 
    searchCriteria_sortOrders_0_direction=None, 
    searchCriteria_pageSize=None, 
    searchCriteria_currentPage=None
):
    """
    Lists credit memos that match specified search criteria.
    
    Args:
        searchCriteria_filterGroups_0_filters_0_field (str, optional): Field to filter by. Example: 'entity_id'
        searchCriteria_filterGroups_0_filters_0_value (str, optional): Value to filter by. Example: '1001'
        searchCriteria_filterGroups_0_filters_0_conditionType (str, optional): Condition type. Example: 'eq'
        searchCriteria_sortOrders_0_field (str, optional): Sorting field. Example: 'created_at'
        searchCriteria_sortOrders_0_direction (str, optional): Sorting direction. Example: 'ASC'
        searchCriteria_pageSize (int, optional): Page size. Example: 20
        searchCriteria_currentPage (int, optional): Current page. Example: 1
    
    Returns:
        requests.Response: The API response object
    
    Example:
        >>> response = list_credit_memos(
        ...     searchCriteria_filterGroups_0_filters_0_field='entity_id',
        ...     searchCriteria_filterGroups_0_filters_0_value='1001',
        ...     searchCriteria_filterGroups_0_filters_0_conditionType='eq',
        ...     searchCriteria_sortOrders_0_field='created_at',
        ...     searchCriteria_sortOrders_0_direction='ASC',
        ...     searchCriteria_pageSize=20,
        ...     searchCriteria_currentPage=1
        ... )
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    api_url = f"{base_url}/rest/default/V1/creditmemos"
    
    # Build the query parameters with the correct format
    querystring = {}
    
    # Add required searchCriteria parameter even if empty
    if searchCriteria_filterGroups_0_filters_0_field is not None:
        querystring["searchCriteria[filterGroups][0][filters][0][field]"] = searchCriteria_filterGroups_0_filters_0_field
    if searchCriteria_filterGroups_0_filters_0_value is not None:
        querystring["searchCriteria[filterGroups][0][filters][0][value]"] = searchCriteria_filterGroups_0_filters_0_value
    if searchCriteria_filterGroups_0_filters_0_conditionType is not None:
        querystring["searchCriteria[filterGroups][0][filters][0][conditionType]"] = searchCriteria_filterGroups_0_filters_0_conditionType
    if searchCriteria_sortOrders_0_field is not None:
        querystring["searchCriteria[sortOrders][0][field]"] = searchCriteria_sortOrders_0_field
    if searchCriteria_sortOrders_0_direction is not None:
        querystring["searchCriteria[sortOrders][0][direction]"] = searchCriteria_sortOrders_0_direction
    if searchCriteria_pageSize is not None:
        querystring["searchCriteria[pageSize]"] = searchCriteria_pageSize
    if searchCriteria_currentPage is not None:
        querystring["searchCriteria[currentPage]"] = searchCriteria_currentPage
    
    # Ensure at least an empty searchCriteria is passed if no specific criteria provided
    if not querystring:
        querystring = {"searchCriteria": ""}
    
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    
    response = requests.get(url=api_url, params=querystring, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = list_credit_memos(
        searchCriteria_filterGroups_0_filters_0_field='entity_id',
        searchCriteria_filterGroups_0_filters_0_value='1001',
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