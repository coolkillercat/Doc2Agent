import requests, json
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


def get_products_in_category(category_id: int, include_subcategories: bool = False):
    """
    Retrieves all products belonging to a specific category, with an option to include products from subcategories.
    
    Args:
        category_id: The ID of the category to search for products
        include_subcategories: If True, includes products from subcategories
    
    Returns:
        Response object from the API call
    """
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token(), }
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    
    # Using catalog_view_container for category searches
    endpoint = f"{base_url}/rest/default/V1/search"
    
    # Set condition type based on whether to include subcategories
    condition_type = "in" if include_subcategories else "eq"
    
    # Construct URL with query parameters
    url = (f"{endpoint}?searchCriteria[requestName]=catalog_view_container"
           f"&searchCriteria[filterGroups][0][filters][0][field]=category_ids"
           f"&searchCriteria[filterGroups][0][filters][0][value]={category_id}"
           f"&searchCriteria[filterGroups][0][filters][0][condition_type]={condition_type}")
    
    response = requests.get(url, headers=headers)
    return response

if __name__ == '__main__':
    r = get_products_in_category(4)  # Example category ID
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