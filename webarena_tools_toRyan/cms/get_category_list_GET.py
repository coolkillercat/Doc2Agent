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


def get_category_list(searchCriteria_field=None, searchCriteria_value=None, searchCriteria_conditionType=None, 
                     searchCriteria_sortField=None, searchCriteria_sortDirection=None, 
                     searchCriteria_pageSize=None, searchCriteria_currentPage=None):
    """
    Get category list from the API.
    
    Args:
        searchCriteria_field (str, optional): Field to filter by. Example: 'name'
        searchCriteria_value (str, optional): Value to filter by. Example: 'electronics'
        searchCriteria_conditionType (str, optional): Condition type for filtering. Example: 'eq'
        searchCriteria_sortField (str, optional): Field to sort by. Example: 'name'
        searchCriteria_sortDirection (str, optional): Sort direction. Example: 'ASC'
        searchCriteria_pageSize (int, optional): Number of items per page. Example: 20
        searchCriteria_currentPage (int, optional): Current page number. Example: 1
    
    Returns:
        Returns a list of product categories with their hierarchical structure, metadata, and custom attributes."""
    base_url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780'
    api_url = f"{base_url}/rest/default/V1/categories/list"
    
    # Initialize the searchCriteria parameter
    querystring = {
        'searchCriteria[pageSize]': searchCriteria_pageSize,
        'searchCriteria[currentPage]': searchCriteria_currentPage
    }
    
    # Add filter parameters if provided
    if searchCriteria_field and searchCriteria_value and searchCriteria_conditionType:
        querystring['searchCriteria[filterGroups][0][filters][0][field]'] = searchCriteria_field
        querystring['searchCriteria[filterGroups][0][filters][0][value]'] = searchCriteria_value
        querystring['searchCriteria[filterGroups][0][filters][0][conditionType]'] = searchCriteria_conditionType
    
    # Add sort parameters if provided
    if searchCriteria_sortField and searchCriteria_sortDirection:
        querystring['searchCriteria[sortOrders][0][field]'] = searchCriteria_sortField
        querystring['searchCriteria[sortOrders][0][direction]'] = searchCriteria_sortDirection
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token()
    }
    
    response = requests.get(url=api_url, params=querystring, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = get_category_list(
        searchCriteria_field='name',
        searchCriteria_value='electronics',
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