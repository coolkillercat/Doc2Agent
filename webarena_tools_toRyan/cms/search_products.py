import requests
import json
from urllib.parse import quote


def get_shopping_admin_auth_token():
    """
    get_shopping_admin_auth_token function.
    
    Returns:
        Returns search results containing matching products along with search criteria details and total count of results.
    """
    ENDPOINT = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780'
    response = requests.post(
        url=f'{ENDPOINT}/rest/default/V1/integration/admin/token',
        headers={
            'content-type': 'application/json'
        },
        data=json.dumps({
            'username': 'admin',
            'password': 'admin1234'
        })
    )
    return "Bearer " + response.json()


def search_products(field: str, value: str, condition_type: str = 'eq', page_size: int = None, current_page: int = None, sort_by: str = None, sort_direction: str = 'DESC', return_fields: list = None):
    """
    Searches for products based on specified criteria, with support for pagination, sorting, and field selection.
    
    Args:
        field (str): The product field to search on
        value (str): The value to search for
        condition_type (str, optional): The condition type for the search. Defaults to 'eq'.
        page_size (int, optional): Maximum number of items to return. Defaults to None.
        current_page (int, optional): Current page number. Defaults to None.
        sort_by (str, optional): Field to sort results by. Defaults to None.
        sort_direction (str, optional): Sort direction ('ASC' or 'DESC'). Defaults to 'DESC'.
        return_fields (list, optional): List of specific fields to return. Defaults to None.
    
    Returns:
        Returns search results containing matching products along with search criteria details and total count of results."""
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780"
    endpoint = f"{base_url}/rest/default/V1/products"
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token()
    }
    
    # Build search criteria
    params = {
        'searchCriteria[filter_groups][0][filters][0][field]': field,
        'searchCriteria[filter_groups][0][filters][0][value]': value,
        'searchCriteria[filter_groups][0][filters][0][condition_type]': condition_type,
    }
    
    # Add pagination if specified
    if page_size is not None:
        params['searchCriteria[pageSize]'] = page_size
    
    if current_page is not None:
        params['searchCriteria[currentPage]'] = current_page
    
    # Add sorting if specified
    if sort_by is not None:
        params['searchCriteria[sortOrders][0][field]'] = sort_by
        params['searchCriteria[sortOrders][0][direction]'] = sort_direction
    
    # Add field selection if specified
    if return_fields is not None:
        fields_str = ','.join(return_fields)
        params['fields'] = f'items[{fields_str}]'
    
    response = requests.get(endpoint, headers=headers, params=params)
    return response


if __name__ == '__main__':
    # Test the function with a simple product search
    r = search_products(field='sku', value='WS12-M-Orange', condition_type='eq', page_size=10, sort_by='name')
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