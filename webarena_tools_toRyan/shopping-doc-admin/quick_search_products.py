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


def quick_search_products(search_term: str, category_ids: list = None, price_from: float = None, price_to: float = None, visibility: str = None):
    """
    Performs a storefront-like quick search for products based on a search term, with optional filtering by category, price range, and visibility.
    
    Args:
        search_term (str): The search term to look for products
        category_ids (list, optional): List of category IDs to filter products by
        price_from (float, optional): Minimum price filter
        price_to (float, optional): Maximum price filter
        visibility (str, optional): Filter by product visibility
        
    Returns:
        requests.Response: The API response object
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    endpoint = f"{base_url}/rest/default/V1/search"
    
    # Start building the search criteria
    search_url = f"{endpoint}?searchCriteria[requestName]=quick_search_container"
    
    # Add the search term filter
    search_url += f"&searchCriteria[filterGroups][0][filters][0][field]=search_term&searchCriteria[filterGroups][0][filters][0][value]={quote(search_term)}"
    
    filter_index = 1
    
    # Add category filter if provided
    if category_ids:
        category_values = "&".join([f"searchCriteria[filterGroups][0][filters][{filter_index}][value][{i}]={cat_id}" 
                                   for i, cat_id in enumerate(category_ids)])
        search_url += f"&searchCriteria[filterGroups][0][filters][{filter_index}][field]=category_ids&{category_values}"
        filter_index += 1
    
    # Add price from filter if provided
    if price_from is not None:
        search_url += f"&searchCriteria[filterGroups][0][filters][{filter_index}][field]=price.from&searchCriteria[filterGroups][0][filters][{filter_index}][value]={price_from}"
        filter_index += 1
    
    # Add price to filter if provided
    if price_to is not None:
        search_url += f"&searchCriteria[filterGroups][0][filters][{filter_index}][field]=price.to&searchCriteria[filterGroups][0][filters][{filter_index}][value]={price_to}"
        filter_index += 1
    
    # Add visibility filter if provided
    if visibility:
        search_url += f"&searchCriteria[filterGroups][0][filters][{filter_index}][field]=visibility&searchCriteria[filterGroups][0][filters][{filter_index}][value]={visibility}"
    
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    
    response = requests.get(search_url, headers=headers)
    return response

if __name__ == '__main__':
    # Test with search term "digital watch"
    r = quick_search_products(search_term="digital watch", price_from=10, price_to=100)
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