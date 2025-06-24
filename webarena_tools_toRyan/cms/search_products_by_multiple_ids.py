import requests
import json
from urllib.parse import quote

def get_shopping_admin_auth_token():
    """
    get_shopping_admin_auth_token function.
    
    Returns:
        Returns a collection of items matching the specified search criteria along with pagination metadata and total count.
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


def search_products_by_multiple_ids(product_ids: list, page_size: int = None, current_page: int = None, sort_by: str = None, sort_direction: str = 'DESC', return_fields: list = None):
    """
    Retrieves multiple products by their IDs in a single request, useful for batch processing.
    
    Args:
        product_ids (list): List of product IDs to retrieve
        page_size (int, optional): Maximum number of items to return
        current_page (int, optional): Page number to return
        sort_by (str, optional): Field to sort results by
        sort_direction (str, optional): Sort direction, either 'ASC' or 'DESC'
        return_fields (list, optional): Specific fields to return in the response
        
    Returns:
        Returns a list of products that match the specified multiple product IDs along with search metadata and total count."""
    BASE_URL = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780'
    
    # Convert product_ids list to comma-separated string
    product_ids_str = ','.join(map(str, product_ids))
    
    # Construct URL with search criteria
    url = f"{BASE_URL}/rest/default/V1/products"
    
    # Add parameters
    params = {
        'searchCriteria[filter_groups][0][filters][0][field]': 'entity_id',
        'searchCriteria[filter_groups][0][filters][0][value]': product_ids_str,
        'searchCriteria[filter_groups][0][filters][0][condition_type]': 'in'
    }
    
    # Add optional parameters if provided
    if page_size:
        params['searchCriteria[pageSize]'] = page_size
    
    if current_page:
        params['searchCriteria[currentPage]'] = current_page
    
    if sort_by:
        params['searchCriteria[sortOrders][0][field]'] = sort_by
        params['searchCriteria[sortOrders][0][direction]'] = sort_direction
    
    if return_fields:
        params['fields'] = ','.join(return_fields)
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token(),
    }
    
    response = requests.get(url, params=params, headers=headers)
    return response

if __name__ == '__main__':
    r = search_products_by_multiple_ids([1, 2, 3], page_size=10, sort_by='name')
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