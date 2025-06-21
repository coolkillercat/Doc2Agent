import requests
import json
from urllib.parse import urlencode

def get_shopping_admin_auth_token():
    """
    get_shopping_admin_auth_token function.
    
    Returns:
        Returns: A response object containing search results from the Magento REST API. The response includes a status code, the raw text response, and a JSON object with three main components: 'items' (an array of matching records), 'search_criteria' (the filter criteria used in the search), and 'total_count' (the number of matching records). The 'content' field contains the raw response content as a string.
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

def create_filter_condition(field: str, value: str, condition_type: str = 'eq'):
    """
    Creates a search filter for the Magento REST API.
    
    Args:
        field (str): The field to filter on
        value (str): The value to filter by
        condition_type (str, optional): The condition type (eq, like, gt, lt, etc). Defaults to 'eq'.
    
    Returns:
        Returns order information including financial details, customer data, shipping information, and order status."""
    BASE_URL = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770'
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    
    # Build search criteria
    params = {
        'searchCriteria[filter_groups][0][filters][0][field]': field,
        'searchCriteria[filter_groups][0][filters][0][value]': value,
        'searchCriteria[filter_groups][0][filters][0][condition_type]': condition_type
    }
    
    # Construct URL with parameters
    url = f"{BASE_URL}/rest/default/V1/orders?{urlencode(params)}"
    
    # Make the request
    response = requests.get(url, headers=headers)
    return response

if __name__ == '__main__':
    r = create_filter_condition('status', 'pending')
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