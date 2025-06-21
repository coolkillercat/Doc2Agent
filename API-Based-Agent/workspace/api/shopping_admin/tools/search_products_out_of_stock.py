import requests
import json
from urllib.parse import quote

def get_shopping_admin_auth_token():
    """
    get_shopping_admin_auth_token function.
    
    Returns:
        Returns a list of out-of-stock products with search criteria details and total count of matching items.
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


def search_products_out_of_stock(page_size: int = None, current_page: int = None, sort_by: str = None, sort_direction: str = 'DESC', return_fields: list = None):
    """
    Identifies products that are currently out of stock, useful for inventory replenishment planning.
    
    Args:
        page_size (int, optional): Maximum number of items to return per page
        current_page (int, optional): Current page number
        sort_by (str, optional): Field to sort by
        sort_direction (str, optional): Sort direction, either 'ASC' or 'DESC'
        return_fields (list, optional): List of fields to return in the response
    
    Returns:
        Returns a list of out-of-stock products with search criteria details and total count of matching items."""
    BASE_URL = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780'
    
    # Set up headers
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token()
    }
    
    # Build the URL with search criteria
    url = f"{BASE_URL}/rest/default/V1/products?"
    
    # Add filter for products that are out of stock (quantity = 0)
    url += "searchCriteria[filter_groups][0][filters][0][field]=quantity_and_stock_status"
    url += "&searchCriteria[filter_groups][0][filters][0][value]=0"
    url += "&searchCriteria[filter_groups][0][filters][0][condition_type]=eq"
    
    # Add pagination parameters if provided
    if page_size is not None:
        url += f"&searchCriteria[pageSize]={page_size}"
    
    if current_page is not None:
        url += f"&searchCriteria[currentPage]={current_page}"
    
    # Add sorting parameters if provided
    if sort_by is not None:
        url += f"&searchCriteria[sortOrders][0][field]={sort_by}"
        url += f"&searchCriteria[sortOrders][0][direction]={sort_direction}"
    
    # Add fields parameter if provided
    if return_fields is not None and len(return_fields) > 0:
        fields_str = ",".join(return_fields)
        url += f"&fields=items[{fields_str}]"
    
    # Make the request
    response = requests.get(url, headers=headers)
    
    return response


if __name__ == '__main__':
    r = search_products_out_of_stock() # no parameter inputs at current stage, need to be filled later.
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