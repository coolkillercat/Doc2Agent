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

def make_full_text_search(searchCriteria_requestName_=None, searchCriteria_filterGroups__0__filters__0__field_=None, searchCriteria_filterGroups__0__filters__0__value_=None, searchCriteria_filterGroups__0__filters__0__conditionType_=None, searchCriteria_sortOrders__0__field_=None, searchCriteria_sortOrders__0__direction_=None, searchCriteria_pageSize_=None, searchCriteria_currentPage_=None):
    """
    Make a full text search and return found documents.
    
    Args:
        searchCriteria_requestName_ (str): The name of the search request.
        searchCriteria_filterGroups__0__filters__0__field_ (str): The field to filter by.
        searchCriteria_filterGroups__0__filters__0__value_ (str): The value to filter by.
        searchCriteria_filterGroups__0__filters__0__conditionType_ (str): The condition type for filtering.
        searchCriteria_sortOrders__0__field_ (str): The field to sort by.
        searchCriteria_sortOrders__0__direction_ (str): The direction to sort (ASC or DESC).
        searchCriteria_pageSize_ (int): The number of items per page.
        searchCriteria_currentPage_ (int): The current page number.
    
    Returns:
        requests.Response: The API response object.
    
    Example:
        >>> make_full_text_search(
        ...     searchCriteria_requestName_='quick_search_container',
        ...     searchCriteria_filterGroups__0__filters__0__field_='search_term',
        ...     searchCriteria_filterGroups__0__filters__0__value_='shirt',
        ...     searchCriteria_filterGroups__0__filters__0__conditionType_='eq',
        ...     searchCriteria_sortOrders__0__field_='relevance',
        ...     searchCriteria_sortOrders__0__direction_='DESC',
        ...     searchCriteria_pageSize_=10,
        ...     searchCriteria_currentPage_=1
        ... )
    """
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/search"
    
    # Ensure at least one searchCriteria parameter is provided
    if searchCriteria_requestName_ is None:
        searchCriteria_requestName_ = 'quick_search_container'
    
    # Remove None values from querystring
    querystring = {k: v for k, v in {
        'searchCriteria[requestName]': searchCriteria_requestName_,
        'searchCriteria[filterGroups][0][filters][0][field]': searchCriteria_filterGroups__0__filters__0__field_,
        'searchCriteria[filterGroups][0][filters][0][value]': searchCriteria_filterGroups__0__filters__0__value_,
        'searchCriteria[filterGroups][0][filters][0][conditionType]': searchCriteria_filterGroups__0__filters__0__conditionType_,
        'searchCriteria[sortOrders][0][field]': searchCriteria_sortOrders__0__field_,
        'searchCriteria[sortOrders][0][direction]': searchCriteria_sortOrders__0__direction_,
        'searchCriteria[pageSize]': searchCriteria_pageSize_,
        'searchCriteria[currentPage]': searchCriteria_currentPage_,
    }.items() if v is not None}
    
    # Ensure searchCriteria is included in the request
    if not any(k.startswith('searchCriteria') for k in querystring):
        querystring['searchCriteria[requestName]'] = 'quick_search_container'
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + get_shopping_customer_auth_token(),
    }
    
    response = requests.get(url=api_url, headers=headers, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, headers=headers, params=querystring, timeout=50, verify=False)
        if response2.status_code == 200:
            response = response2
    return response

if __name__ == '__main__':
    r = make_full_text_search(
        searchCriteria_requestName_='quick_search_container',
        searchCriteria_filterGroups__0__filters__0__field_='search_term',
        searchCriteria_filterGroups__0__filters__0__value_='shirt',
        searchCriteria_filterGroups__0__filters__0__conditionType_='eq',
        searchCriteria_sortOrders__0__field_='relevance',
        searchCriteria_sortOrders__0__direction_='DESC',
        searchCriteria_pageSize_=10,
        searchCriteria_currentPage_=1
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