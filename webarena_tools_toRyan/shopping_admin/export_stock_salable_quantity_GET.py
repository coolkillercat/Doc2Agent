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


def export_stock_salable_quantity(salesChannelType, salesChannelCode, 
                                 searchCriteria_field=None, searchCriteria_value=None, 
                                 searchCriteria_conditionType=None, searchCriteria_sortField=None, 
                                 searchCriteria_sortDirection=None, searchCriteria_pageSize=None, 
                                 searchCriteria_currentPage=None):
    """
    Export product stock data filtered by search criteria.
    
    Args:
        salesChannelType (str): The sales channel type (required)
        salesChannelCode (str): The sales channel code (required)
        searchCriteria_field (str, optional): Field to filter by
        searchCriteria_value (str, optional): Value to filter by
        searchCriteria_conditionType (str, optional): Condition type for filtering (e.g., 'eq')
        searchCriteria_sortField (str, optional): Field to sort by
        searchCriteria_sortDirection (str, optional): Sort direction ('ASC' or 'DESC')
        searchCriteria_pageSize (int, optional): Number of items per page
        searchCriteria_currentPage (int, optional): Current page number
    
    Returns:
        requests.Response: The API response
    
    Example:
        response = export_stock_salable_quantity(
            salesChannelType='website',
            salesChannelCode='base',
            searchCriteria_field='sku',
            searchCriteria_value='24-MB01',
            searchCriteria_conditionType='eq',
            searchCriteria_sortField='name',
            searchCriteria_sortDirection='ASC',
            searchCriteria_pageSize=20,
            searchCriteria_currentPage=1
        )
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    api_url = f"{base_url}/rest/default/V1/inventory/export-stock-salable-qty/{quote(salesChannelType, safe='')}/{quote(salesChannelCode, safe='')}"
    
    querystring = {}
    
    # Add search criteria parameters
    if searchCriteria_field is not None:
        querystring["searchCriteria[filterGroups][0][filters][0][field]"] = searchCriteria_field
    if searchCriteria_value is not None:
        querystring["searchCriteria[filterGroups][0][filters][0][value]"] = searchCriteria_value
    if searchCriteria_conditionType is not None:
        querystring["searchCriteria[filterGroups][0][filters][0][conditionType]"] = searchCriteria_conditionType
    if searchCriteria_sortField is not None:
        querystring["searchCriteria[sortOrders][0][field]"] = searchCriteria_sortField
    if searchCriteria_sortDirection is not None:
        querystring["searchCriteria[sortOrders][0][direction]"] = searchCriteria_sortDirection
    if searchCriteria_pageSize is not None:
        querystring["searchCriteria[pageSize]"] = searchCriteria_pageSize
    if searchCriteria_currentPage is not None:
        querystring["searchCriteria[currentPage]"] = searchCriteria_currentPage
    
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    
    assert salesChannelType is not None, 'Missing required parameter: salesChannelType'
    assert salesChannelCode is not None, 'Missing required parameter: salesChannelCode'
    
    response = requests.get(url=api_url, params=querystring, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = export_stock_salable_quantity(
        salesChannelType='website',
        salesChannelCode='base',
        searchCriteria_field='sku',
        searchCriteria_value='24-MB01',
        searchCriteria_conditionType='eq',
        searchCriteria_sortField='name',
        searchCriteria_sortDirection='ASC',
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