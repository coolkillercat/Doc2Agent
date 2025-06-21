import requests
import json
from urllib.parse import urlencode

def get_shopping_admin_auth_token():
    """
    get_shopping_admin_auth_token function.
    
    Returns:
        Returns a list of orders with basic information including customer email, entity ID, increment ID, and status.
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


def search_orders_with_multiple_conditions(filter_conditions: list, page_size: int = None, current_page: int = None, sort_by: str = None, sort_direction: str = 'DESC', return_fields: list = None):
    """
    Searches for orders using multiple filter conditions with logical AND between condition groups and logical OR within each group.
    
    Args:
        filter_conditions: List of dictionaries where each dictionary represents a filter group.
                          Each group should contain a 'filters' key with a list of filter dictionaries.
                          Each filter dictionary should have 'field', 'value', and optionally 'condition_type' keys.
        page_size: Maximum number of items to return
        current_page: Current page number
        sort_by: Field to sort results by
        sort_direction: Direction to sort (ASC or DESC)
        return_fields: List of fields to return in the response
        
    Returns:
        Returns a list of orders matching multiple search conditions with basic order information including customer email, IDs, and status."""
    BASE_URL = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780'
    ENDPOINT = f'{BASE_URL}/rest/default/V1/orders'
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token(),
    }
    
    # Build search criteria parameters
    params = {}
    
    # Add filter groups
    for group_idx, filter_group in enumerate(filter_conditions):
        filters = filter_group.get('filters', [])
        for filter_idx, filter_item in enumerate(filters):
            field = filter_item.get('field')
            value = filter_item.get('value')
            condition_type = filter_item.get('condition_type', 'eq')
            
            params[f'searchCriteria[filter_groups][{group_idx}][filters][{filter_idx}][field]'] = field
            params[f'searchCriteria[filter_groups][{group_idx}][filters][{filter_idx}][value]'] = value
            params[f'searchCriteria[filter_groups][{group_idx}][filters][{filter_idx}][condition_type]'] = condition_type
    
    # Add pagination
    if page_size is not None:
        params['searchCriteria[pageSize]'] = page_size
    
    if current_page is not None:
        params['searchCriteria[currentPage]'] = current_page
    
    # Add sorting
    if sort_by is not None:
        params['searchCriteria[sortOrders][0][field]'] = sort_by
        params['searchCriteria[sortOrders][0][direction]'] = sort_direction
    
    # Add fields to return
    if return_fields is not None:
        fields_str = ",".join(return_fields) if isinstance(return_fields, list) else return_fields
        params['fields'] = fields_str
    
    # Make the API call
    response = requests.get(
        url=ENDPOINT,
        headers=headers,
        params=params
    )
    
    return response


if __name__ == '__main__':
    # Example search for pending orders
    filter_conditions = [
        {
            'filters': [
                {
                    'field': 'status',
                    'value': 'pending',
                    'condition_type': 'eq'
                }
            ]
        }
    ]
    
    r = search_orders_with_multiple_conditions(
        filter_conditions=filter_conditions,
        page_size=10,
        sort_by='created_at',
        sort_direction='DESC',
        return_fields=['items[increment_id,entity_id,status,customer_email]']
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