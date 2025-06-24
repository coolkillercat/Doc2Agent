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


def get_product_render_info(storeId=None, currencyCode=None, 
                           searchCriteria_filterGroups_0_filters_0_field=None, 
                           searchCriteria_filterGroups_0_filters_0_value=None, 
                           searchCriteria_filterGroups_0_filters_0_conditionType=None, 
                           searchCriteria_sortOrders_0_field=None, 
                           searchCriteria_sortOrders_0_direction=None, 
                           searchCriteria_pageSize=None, 
                           searchCriteria_currentPage=None):
    """
    Get product render information from the API.
    
    Args:
        storeId (int): The store ID (required)
        currencyCode (str): The currency code (required)
        searchCriteria_filterGroups_0_filters_0_field (str): Field to filter by
        searchCriteria_filterGroups_0_filters_0_value (str): Value to filter by
        searchCriteria_filterGroups_0_filters_0_conditionType (str): Condition type for filtering
        searchCriteria_sortOrders_0_field (str): Field to sort by
        searchCriteria_sortOrders_0_direction (str): Sort direction (ASC or DESC)
        searchCriteria_pageSize (int): Number of items per page
        searchCriteria_currentPage (int): Current page number
    
    Returns:
        requests.Response: The API response
    
    Example:
        >>> get_product_render_info(storeId=1, currencyCode='USD', 
        ...                         searchCriteria_filterGroups_0_filters_0_field='price',
        ...                         searchCriteria_filterGroups_0_filters_0_value='100',
        ...                         searchCriteria_filterGroups_0_filters_0_conditionType='eq',
        ...                         searchCriteria_sortOrders_0_field='name',
        ...                         searchCriteria_sortOrders_0_direction='ASC',
        ...                         searchCriteria_pageSize=20,
        ...                         searchCriteria_currentPage=1)
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    api_url = f"{base_url}/rest/default/V1/products-render-info"
    
    assert storeId is not None, 'Missing required parameter: storeId'
    assert currencyCode is not None, 'Missing required parameter: currencyCode'
    
    querystring = {
        'storeId': storeId,
        'currencyCode': currencyCode
    }
    
    # Add search criteria parameters
    if searchCriteria_filterGroups_0_filters_0_field is not None:
        querystring['searchCriteria[filterGroups][0][filters][0][field]'] = searchCriteria_filterGroups_0_filters_0_field
    if searchCriteria_filterGroups_0_filters_0_value is not None:
        querystring['searchCriteria[filterGroups][0][filters][0][value]'] = searchCriteria_filterGroups_0_filters_0_value
    if searchCriteria_filterGroups_0_filters_0_conditionType is not None:
        querystring['searchCriteria[filterGroups][0][filters][0][conditionType]'] = searchCriteria_filterGroups_0_filters_0_conditionType
    if searchCriteria_sortOrders_0_field is not None:
        querystring['searchCriteria[sortOrders][0][field]'] = searchCriteria_sortOrders_0_field
    if searchCriteria_sortOrders_0_direction is not None:
        querystring['searchCriteria[sortOrders][0][direction]'] = searchCriteria_sortOrders_0_direction
    if searchCriteria_pageSize is not None:
        querystring['searchCriteria[pageSize]'] = searchCriteria_pageSize
    if searchCriteria_currentPage is not None:
        querystring['searchCriteria[currentPage]'] = searchCriteria_currentPage
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': get_shopping_admin_auth_token()
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