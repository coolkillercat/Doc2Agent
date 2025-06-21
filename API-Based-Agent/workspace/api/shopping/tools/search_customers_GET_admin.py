import requests
import json
from urllib.parse import quote

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


def search_customers(field=None, value=None, condition_type="eq", sort_field=None, 
                    sort_direction=None, page_size=20, current_page=1):
    """
    Search for customers based on specified criteria.
    
    Args:
        field (str): The field to filter by (e.g., 'email', 'firstname', 'lastname')
        value (str): The value to filter for
        condition_type (str): The condition type for filtering (e.g., 'eq', 'like', 'gt')
        sort_field (str): Field to sort results by (e.g., 'created_at', 'email')
        sort_direction (str): Direction to sort ('ASC' or 'DESC')
        page_size (int): Number of results per page
        current_page (int): Current page number
    
    Returns:
        Returns customer records matching the specified search criteria with their personal information, addresses, and account details.
    Example:
        >>> search_customers(field='email', value='example@example.com')
        >>> search_customers(field='firstname', value='John', sort_field='created_at', sort_direction='DESC')
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    api_url = f"{base_url}/rest/default/V1/customers/search"
    
    # Initialize query parameters
    querystring = {}
    
    # Add filter parameters if field and value are provided
    if field and value:
        querystring["searchCriteria[filterGroups][0][filters][0][field]"] = field
        querystring["searchCriteria[filterGroups][0][filters][0][value]"] = value
        querystring["searchCriteria[filterGroups][0][filters][0][conditionType]"] = condition_type
    
    # Add sorting parameters if provided
    if sort_field:
        querystring["searchCriteria[sortOrders][0][field]"] = sort_field
        querystring["searchCriteria[sortOrders][0][direction]"] = sort_direction or "ASC"
    
    # Add pagination parameters
    querystring["searchCriteria[pageSize]"] = page_size
    querystring["searchCriteria[currentPage]"] = current_page
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token()
    }
    
    response = requests.get(url=api_url, params=querystring, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = search_customers(field='email', value='emma.lopez@gmail.com', sort_field='created_at', sort_direction='ASC')
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