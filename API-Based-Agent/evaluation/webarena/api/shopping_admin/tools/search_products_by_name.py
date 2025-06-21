import requests
import json

def get_shopping_admin_auth_token():
    """
    get_shopping_admin_auth_token function.
    
    Returns:
        Returns a list of products with their SKUs, names, and prices that match the specified search pattern.
    """
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


def search_products_by_name(name_pattern: str, page_size: int = None, current_page: int = None, sort_by: str = None, sort_direction: str = 'DESC', return_fields: list = None):
    """
    Searches for products whose names match a specific pattern using SQL LIKE syntax.
    
    Args:
        name_pattern (str): The pattern to search for in product names (SQL LIKE syntax, % is used as wildcard)
        page_size (int, optional): Maximum number of items to return
        current_page (int, optional): Current page of results
        sort_by (str, optional): Field to sort by
        sort_direction (str, optional): Sort direction, 'ASC' or 'DESC'
        return_fields (list, optional): List of fields to return in the response
        
    Returns:
        Returns a list of products with their SKUs, names, and prices that match the specified name pattern search criteria."""
    BASE_URL = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780'
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token(),
    }
    
    # Prepare the URL with search criteria
    url = f"{BASE_URL}/rest/default/V1/products?"
    
    # Add the name filter
    encoded_pattern = name_pattern.replace('%', '%25')
    url += f"searchCriteria[filter_groups][0][filters][0][field]=name&"
    url += f"searchCriteria[filter_groups][0][filters][0][value]={encoded_pattern}&"
    url += f"searchCriteria[filter_groups][0][filters][0][condition_type]=like"
    
    # Add pagination if specified
    if page_size is not None:
        url += f"&searchCriteria[pageSize]={page_size}"
    
    if current_page is not None:
        url += f"&searchCriteria[currentPage]={current_page}"
    
    # Add sorting if specified
    if sort_by is not None:
        url += f"&searchCriteria[sortOrders][0][field]={sort_by}"
        url += f"&searchCriteria[sortOrders][0][direction]={sort_direction}"
    
    # Add specific fields to return if specified
    if return_fields is not None and len(return_fields) > 0:
        fields_str = ",".join(return_fields)
        url += f"&fields=items[{fields_str}]"
    
    # Make the API request
    response = requests.get(url, headers=headers)
    
    return response


if __name__ == '__main__':
    r = search_products_by_name("%Tee%", page_size=10, sort_by="name", sort_direction="ASC", return_fields=["name", "sku", "price"])
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