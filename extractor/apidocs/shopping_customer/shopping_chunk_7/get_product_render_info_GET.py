import requests, json
from urllib.parse import quote

def get_shopping_customer_auth_token():
    response = requests.post(
        url = f'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/integration/customer/token',
        headers = {
            'content-type': 'application/json'
        },
        data = json.dumps({
            'username': 'emma.lopez@gmail.com',
            'password': 'Password.123'
        })
    )
    return response.json()

def get_product_render_info(storeId=None, currencyCode=None, searchCriteria=None, searchCriteria_filterGroups__0__filters__0__field_=None, searchCriteria_filterGroups__0__filters__0__value_=None, searchCriteria_filterGroups__0__filters__0__conditionType_=None, searchCriteria_sortOrders__0__field_=None, searchCriteria_sortOrders__0__direction_=None, searchCriteria_pageSize_=None, searchCriteria_currentPage_=None):
    """
    Collect and retrieve the list of product render info.
    
    This function retrieves product information including raw prices, formatted prices,
    product name, stock status, store_id, etc.
    
    Args:
        storeId (int): The store ID. Required.
        currencyCode (str): The currency code. Required.
        searchCriteria (dict, optional): Search criteria.
        searchCriteria_filterGroups__0__filters__0__field_ (str, optional): Field to filter by.
        searchCriteria_filterGroups__0__filters__0__value_ (str, optional): Value to filter by.
        searchCriteria_filterGroups__0__filters__0__conditionType_ (str, optional): Condition type for filtering.
        searchCriteria_sortOrders__0__field_ (str, optional): Field to sort by.
        searchCriteria_sortOrders__0__direction_ (str, optional): Sort direction.
        searchCriteria_pageSize_ (int, optional): Page size.
        searchCriteria_currentPage_ (int, optional): Current page.
    
    Returns:
        Response object from the API call.
    
    Example:
        >>> get_product_render_info(storeId=1, currencyCode='USD', searchCriteria_filterGroups__0__filters__0__field_='name', 
        ...                         searchCriteria_filterGroups__0__filters__0__value_='shirt', 
        ...                         searchCriteria_filterGroups__0__filters__0__conditionType_='eq',
        ...                         searchCriteria_sortOrders__0__field_='price', 
        ...                         searchCriteria_sortOrders__0__direction_='ASC',
        ...                         searchCriteria_pageSize_=20, searchCriteria_currentPage_=1)
    """
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/products-render-info"
    
    # Ensure required parameters are present
    assert storeId is not None, 'Missing required parameter: storeId'
    assert currencyCode is not None, 'Missing required parameter: currencyCode'
    
    # If searchCriteria is not provided, create it from the individual parameters
    if searchCriteria is None:
        searchCriteria = {}
        
        # Add filter groups if field is provided
        if searchCriteria_filterGroups__0__filters__0__field_ is not None:
            searchCriteria["filterGroups"] = [{
                "filters": [{
                    "field": searchCriteria_filterGroups__0__filters__0__field_,
                    "value": searchCriteria_filterGroups__0__filters__0__value_,
                    "condition_type": searchCriteria_filterGroups__0__filters__0__conditionType_
                }]
            }]
            
        # Add sort orders if field is provided
        if searchCriteria_sortOrders__0__field_ is not None:
            searchCriteria["sortOrders"] = [{
                "field": searchCriteria_sortOrders__0__field_,
                "direction": searchCriteria_sortOrders__0__direction_
            }]
            
        # Add pagination if provided
        if searchCriteria_pageSize_ is not None:
            searchCriteria["pageSize"] = searchCriteria_pageSize_
        if searchCriteria_currentPage_ is not None:
            searchCriteria["currentPage"] = searchCriteria_currentPage_
    
    querystring = {
        'storeId': storeId,
        'currencyCode': currencyCode,
        'searchCriteria': json.dumps(searchCriteria) if searchCriteria else None
    }
    
    # Remove None values
    querystring = {k: v for k, v in querystring.items() if v is not None}
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + get_shopping_customer_auth_token(),
    }
    
    response = requests.get(url=api_url, headers=headers, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        # Try without the auth token in case that's causing issues
        headers.pop("Authorization", None)
        response2 = requests.get(url=api_url, headers=headers, params=querystring, timeout=50, verify=False)
        if response2.status_code == 200:
            response = response2
    
    return response

if __name__ == '__main__':
    r = get_product_render_info(storeId=1, currencyCode='USD', searchCriteria_filterGroups__0__filters__0__field_='name', searchCriteria_filterGroups__0__filters__0__value_='shirt', searchCriteria_filterGroups__0__filters__0__conditionType_='eq', searchCriteria_sortOrders__0__field_='price', searchCriteria_sortOrders__0__direction_='ASC', searchCriteria_pageSize_=20, searchCriteria_currentPage_=1)
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