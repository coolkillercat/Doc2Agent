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


def search_documents(searchCriteria_requestName=None, field=None, value=None, conditionType=None, 
                    sortField=None, sortDirection=None, pageSize=None, currentPage=None):
    """
    Make Full Text Search and return found Documents.
    
    Args:
        searchCriteria_requestName (str, optional): Request name for the search.
        field (str, optional): Field to filter by.
        value (str, optional): Value to filter with.
        conditionType (str, optional): Condition type for filtering (e.g., 'eq', 'like').
        sortField (str, optional): Field to sort by.
        sortDirection (str, optional): Sort direction ('ASC' or 'DESC').
        pageSize (int, optional): Number of results per page.
        currentPage (int, optional): Current page number.
    
    Returns:
        requests.Response: Response from the API
        
    Example:
        response = search_documents(
            searchCriteria_requestName='quick_search_container',
            field='search_term',
            value='shirt',
            conditionType='eq',
            sortField='relevance',
            sortDirection='DESC',
            pageSize=20,
            currentPage=1
        )
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    api_url = f"{base_url}/rest/default/V1/search"
    
    querystring = {}
    
    if searchCriteria_requestName:
        querystring['searchCriteria[requestName]'] = searchCriteria_requestName
    
    if field:
        querystring['searchCriteria[filterGroups][0][filters][0][field]'] = field
    
    if value:
        querystring['searchCriteria[filterGroups][0][filters][0][value]'] = value
    
    if conditionType:
        querystring['searchCriteria[filterGroups][0][filters][0][conditionType]'] = conditionType
    
    if sortField:
        querystring['searchCriteria[sortOrders][0][field]'] = sortField
    
    if sortDirection:
        querystring['searchCriteria[sortOrders][0][direction]'] = sortDirection
    
    if pageSize:
        querystring['searchCriteria[pageSize]'] = str(pageSize)
    
    if currentPage:
        querystring['searchCriteria[currentPage]'] = str(currentPage)
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_customer_auth_token()
    }
    
    response = requests.get(url=api_url, params=querystring, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = search_documents(
        searchCriteria_requestName='quick_search_container',
        field='search_term',
        value='shirt',
        conditionType='eq',
        sortField='relevance',
        sortDirection='DESC',
        pageSize=20,
        currentPage=1
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