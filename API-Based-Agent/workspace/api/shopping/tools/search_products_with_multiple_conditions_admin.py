import requests
import json
from urllib.parse import urlencode

def get_shopping_admin_auth_token():
    """
    get_shopping_admin_auth_token function.
    
    Returns:
        Returns a list of products with their basic details including ID, SKU, name, and price.
    """
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


def search_products_with_multiple_conditions(filter_conditions: list, page_size: int = None, current_page: int = None, sort_by: str = None, sort_direction: str = 'DESC', return_fields: list = None):
    """
    Searches for products using multiple filter conditions with logical AND between filter groups and OR within each group.
    
    Args:
        filter_conditions: List of dictionaries where each dictionary represents a filter group.
                          Each filter group should contain a 'filters' key with a list of filter dictionaries.
                          Each filter dictionary should have 'field', 'value', and optionally 'condition_type' keys.
        page_size: Maximum number of items to return per page.
        current_page: The current page number.
        sort_by: Field name to sort results by.
        sort_direction: Direction to sort results (ASC or DESC).
        return_fields: List of fields to return in the response.
    
    Returns:
        Returns a list of products matching multiple search criteria with their basic details and pricing information."""
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    endpoint = f"{base_url}/rest/default/V1/products"
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token(),
    }
    
    params = {}
    
    # Add filter conditions
    for group_idx, filter_group in enumerate(filter_conditions):
        for filter_idx, filter_item in enumerate(filter_group.get('filters', [])):
            field = filter_item.get('field')
            value = filter_item.get('value')
            condition_type = filter_item.get('condition_type', 'eq')
            
            params[f'searchCriteria[filter_groups][{group_idx}][filters][{filter_idx}][field]'] = field
            params[f'searchCriteria[filter_groups][{group_idx}][filters][{filter_idx}][value]'] = value
            params[f'searchCriteria[filter_groups][{group_idx}][filters][{filter_idx}][condition_type]'] = condition_type
    
    # Add pagination parameters
    if page_size is not None:
        params['searchCriteria[pageSize]'] = page_size
    
    if current_page is not None:
        params['searchCriteria[currentPage]'] = current_page
    
    # Add sorting parameters
    if sort_by:
        params['searchCriteria[sortOrders][0][field]'] = sort_by
        params['searchCriteria[sortOrders][0][direction]'] = sort_direction
    
    # Add fields parameter to limit returned fields
    if return_fields:
        fields_str = ','.join(return_fields)
        params['fields'] = fields_str
    
    # Make the request
    response = requests.get(endpoint, headers=headers, params=params)
    
    return response


if __name__ == '__main__':
    # Example usage: Search for products that are either "Jacket" or "Pant" in their name AND price less than 100
    filter_conditions = [
        {
            'filters': [
                {'field': 'name', 'value': '%Jacket%', 'condition_type': 'like'},
                {'field': 'name', 'value': '%Pant%', 'condition_type': 'like'}
            ]
        },
        {
            'filters': [
                {'field': 'price', 'value': '100', 'condition_type': 'lt'}
            ]
        }
    ]
    
    r = search_products_with_multiple_conditions(
        filter_conditions=filter_conditions,
        page_size=10,
        current_page=1,
        sort_by='name',
        sort_direction='ASC',
        return_fields=['items[id,name,price,sku]']
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