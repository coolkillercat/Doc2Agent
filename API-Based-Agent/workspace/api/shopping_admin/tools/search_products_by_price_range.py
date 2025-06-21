
import requests
import json
from urllib.parse import quote

def get_shopping_admin_auth_token():
    """
    get_shopping_admin_auth_token function.
    
    Returns:
        Returns a list of products with their SKUs, names, and prices.
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

def search_products_by_price_range(min_price: float, max_price: float, page_size: int = None, current_page: int = None, sort_by: str = None, sort_direction: str = 'DESC', return_fields: list = None):
    """
    Searches for products within a specified price range, useful for price-based filtering.
    
    Args:
        min_price (float): Minimum price to filter by
        max_price (float): Maximum price to filter by
        page_size (int, optional): Number of items to return per page
        current_page (int, optional): Current page number
        sort_by (str, optional): Field to sort results by
        sort_direction (str, optional): Sort direction ('ASC' or 'DESC')
        return_fields (list, optional): List of fields to return in the response
        
    Returns:
        Returns a list of products that fall within a specified price range, including their SKU, name, and price."""
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780"
    endpoint = f"{base_url}/rest/default/V1/products"
    
    # Build query parameters for price range
    params = {
        'searchCriteria[filter_groups][0][filters][0][field]': 'price',
        'searchCriteria[filter_groups][0][filters][0][value]': str(min_price),
        'searchCriteria[filter_groups][0][filters][0][condition_type]': 'gteq',
        'searchCriteria[filter_groups][1][filters][0][field]': 'price',
        'searchCriteria[filter_groups][1][filters][0][value]': str(max_price),
        'searchCriteria[filter_groups][1][filters][0][condition_type]': 'lteq'
    }
    
    # Add optional parameters if provided
    if page_size is not None:
        params['searchCriteria[pageSize]'] = str(page_size)
    
    if current_page is not None:
        params['searchCriteria[currentPage]'] = str(current_page)
    
    if sort_by is not None:
        params['searchCriteria[sortOrders][0][field]'] = sort_by
        params['searchCriteria[sortOrders][0][direction]'] = sort_direction
    
    if return_fields is not None:
        fields_str = ','.join(return_fields)
        params['fields'] = f'items[{fields_str}]'
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': get_shopping_admin_auth_token()
    }
    
    response = requests.get(endpoint, params=params, headers=headers)
    return response

if __name__ == '__main__':
    # Example usage with a price range of $20 to $50, sorted by price in ascending order
    r = search_products_by_price_range(
        min_price=20.0, 
        max_price=50.0, 
        page_size=10, 
        sort_by='price', 
        sort_direction='ASC',
        return_fields=['sku', 'name', 'price']
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