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


def search_invoices_since(timestamp: str = '2023-01-01 00:00:00', page_size: int = None, current_page: int = None, sort_by: str = None, sort_direction: str = 'DESC', return_fields: list[str] = None) -> dict:
    """
    Find all invoices created after a specific timestamp. Useful for synchronization and polling for changes since last check.

    Args:
        timestamp (str): Timestamp in format 'YYYY-MM-DD HH:MM:SS'
        page_size (int, optional): Maximum number of items to return
        current_page (int, optional): Page number to return
        sort_by (str, optional): Field to sort by
        sort_direction (str, optional): Sort direction ('ASC' or 'DESC')
        return_fields (list[str], optional): List of fields to return in response

    Returns:
        dict: API response containing matching invoices
    """
    ENDPOINT = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770'
    
    url = f'{ENDPOINT}/rest/default/V1/invoices?'
    url += f'searchCriteria[filter_groups][0][filters][0][field]=created_at'
    url += f'&searchCriteria[filter_groups][0][filters][0][value]={quote(timestamp)}'
    url += f'&searchCriteria[filter_groups][0][filters][0][condition_type]=gt'

    if page_size:
        url += f'&searchCriteria[pageSize]={page_size}'
    if current_page:
        url += f'&searchCriteria[currentPage]={current_page}'
    if sort_by:
        url += f'&searchCriteria[sortOrders][0][field]={sort_by}'
        url += f'&searchCriteria[sortOrders][0][direction]={sort_direction}'
    if return_fields:
        url += f'&fields=items[{",".join(return_fields)}]'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': get_shopping_admin_auth_token()
    }

    response = requests.get(url, headers=headers)
    return response

if __name__ == '__main__':
    r = search_invoices_since('2023-01-01 00:00:00', 
                            page_size=10,
                            current_page=1,
                            sort_by='created_at',
                            sort_direction='DESC',
                            return_fields=['entity_id', 'created_at'])
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