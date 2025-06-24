import requests, json
from urllib.parse import quote

import requests
import json
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


def search_products_by_ids(product_ids: list[int], page_size: int = None, current_page: int = None, sort_by: str = None, sort_direction: str = 'DESC') -> dict:
    """
    Retrieve multiple products by their entity IDs. Uses the in condition type to fetch specific products in a single request.
    
    Args:
        product_ids (list[int]): List of product entity IDs to search for
        page_size (int, optional): Number of items per page
        current_page (int, optional): Current page number
        sort_by (str, optional): Field to sort results by
        sort_direction (str, optional): Sort direction ('ASC' or 'DESC')
    
    Returns:
        dict: API response containing matched products
    """
    base_url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770'
    
    # Convert product IDs list to comma-separated string
    product_ids_str = ','.join(map(str, product_ids))
    
    # Build search criteria
    url = f"{base_url}/rest/default/V1/products?"
    url += f"searchCriteria[filter_groups][0][filters][0][field]=entity_id&"
    url += f"searchCriteria[filter_groups][0][filters][0][value]={product_ids_str}&"
    url += f"searchCriteria[filter_groups][0][filters][0][condition_type]=in"
    
    # Add optional parameters
    if page_size:
        url += f"&searchCriteria[pageSize]={page_size}"
    if current_page:
        url += f"&searchCriteria[currentPage]={current_page}"
    if sort_by:
        url += f"&searchCriteria[sortOrders][0][field]={sort_by}"
        url += f"&searchCriteria[sortOrders][0][direction]={sort_direction}"

    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    
    response = requests.get(url, headers=headers)
    return response

if __name__ == '__main__':
    r = search_products_by_ids([1,2,3], page_size=10, current_page=1, sort_by='name', sort_direction='DESC')
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