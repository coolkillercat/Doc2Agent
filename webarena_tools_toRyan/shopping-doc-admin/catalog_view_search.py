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


def catalog_view_search(category_ids: list, price_from: float = None, price_to: float = None, visibility: str = None):
    """
    Retrieves products from specific categories with optional price range and visibility filters, similar to browsing catalog pages on a storefront.
    
    Args:
        category_ids (list): List of category IDs to search within
        price_from (float, optional): Minimum price filter for products
        price_to (float, optional): Maximum price filter for products
        visibility (str, optional): Product visibility setting
        
    Returns:
        requests.Response: The API response containing the search results
    """
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token(), }
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    endpoint = f"{base_url}/rest/default/V1/search"
    
    # Build the query parameters
    query_params = {
        "searchCriteria[requestName]": "catalog_view_container",
        "searchCriteria[filterGroups][0][filters][0][field]": "category_ids",
        "searchCriteria[filterGroups][0][filters][0][value]": json.dumps(category_ids),
        "searchCriteria[filterGroups][0][filters][0][condition_type]": "eq"
    }
    
    # Add optional price range filters
    filter_index = 1
    if price_from is not None:
        query_params[f"searchCriteria[filterGroups][0][filters][{filter_index}][field]"] = "price.from"
        query_params[f"searchCriteria[filterGroups][0][filters][{filter_index}][value]"] = price_from
        filter_index += 1
        
    if price_to is not None:
        query_params[f"searchCriteria[filterGroups][0][filters][{filter_index}][field]"] = "price.to"
        query_params[f"searchCriteria[filterGroups][0][filters][{filter_index}][value]"] = price_to
        filter_index += 1
        
    # Add visibility filter if provided
    if visibility is not None:
        query_params[f"searchCriteria[filterGroups][0][filters][{filter_index}][field]"] = "visibility"
        query_params[f"searchCriteria[filterGroups][0][filters][{filter_index}][value]"] = visibility
    
    # Make the request
    response = requests.get(endpoint, headers=headers, params=query_params)
    return response

if __name__ == '__main__':
    r = catalog_view_search(category_ids=[4])  # Example: Search in category ID 4
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