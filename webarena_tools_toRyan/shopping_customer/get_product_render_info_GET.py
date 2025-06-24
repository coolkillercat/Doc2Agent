import requests
import json
from urllib.parse import quote

def get_shopping_customer_auth_token():
    """
    Get customer authentication token from the API.
    
    Returns:
        str: Authentication token for the customer
        
    Example:
        token = get_shopping_customer_auth_token()
    """
    response = requests.post(
        url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/integration/customer/token',
        headers = {
            'content-type': 'application/json'
        },
        data = json.dumps({
            'username': 'emma.lopez@gmail.com',
            'password': 'Password.123'
        })
    )
    return "Bearer " + response.json()


def get_product_render_info(storeId, currencyCode, searchCriteria_filterGroups_0_filters_0_field=None, 
                           searchCriteria_filterGroups_0_filters_0_value=None, 
                           searchCriteria_filterGroups_0_filters_0_conditionType=None, 
                           searchCriteria_sortOrders_0_field=None, 
                           searchCriteria_sortOrders_0_direction=None, 
                           searchCriteria_pageSize=None, 
                           searchCriteria_currentPage=None):
    """
    Collect and retrieve the list of product render info.
    
    Args:
        storeId (int): Store ID (required)
        currencyCode (str): Currency code (required)
        searchCriteria_filterGroups_0_filters_0_field (str, optional): Filter field
        searchCriteria_filterGroups_0_filters_0_value (str, optional): Filter value
        searchCriteria_filterGroups_0_filters_0_conditionType (str, optional): Filter condition type
        searchCriteria_sortOrders_0_field (str, optional): Sorting field
        searchCriteria_sortOrders_0_direction (str, optional): Sorting direction
        searchCriteria_pageSize (int, optional): Page size
        searchCriteria_currentPage (int, optional): Current page
    
    Returns:
        requests.Response: API response object
        
    Example:
        response = get_product_render_info(
            storeId=1,
            currencyCode='USD',
            searchCriteria_filterGroups_0_filters_0_field='price',
            searchCriteria_filterGroups_0_filters_0_value='100',
            searchCriteria_filterGroups_0_filters_0_conditionType='eq',
            searchCriteria_sortOrders_0_field='name',
            searchCriteria_sortOrders_0_direction='ASC',
            searchCriteria_pageSize=20,
            searchCriteria_currentPage=1
        )
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    api_url = f"{base_url}/rest/default/V1/products-render-info"
    
    # Required parameters
    assert storeId is not None, 'Missing required parameter: storeId'
    assert currencyCode is not None, 'Missing required parameter: currencyCode'
    
    # Build query parameters
    querystring = {
        'storeId': storeId,
        'currencyCode': currencyCode
    }
    
    # Add optional parameters if provided
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
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': get_shopping_customer_auth_token()
    }
    
    response = requests.get(url=api_url, params=querystring, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = get_product_render_info(
        storeId=1, 
        currencyCode='USD', 
        searchCriteria_filterGroups_0_filters_0_field='price', 
        searchCriteria_filterGroups_0_filters_0_value='100', 
        searchCriteria_filterGroups_0_filters_0_conditionType='eq', 
        searchCriteria_sortOrders_0_field='name', 
        searchCriteria_sortOrders_0_direction='ASC', 
        searchCriteria_pageSize=20, 
        searchCriteria_currentPage=1
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