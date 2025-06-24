import requests, json
from urllib.parse import quote

def get_shopping_admin_auth_token():
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


def search_products_by_keyword(keyword: str, boost_value: int = None):
    """
    Searches for products matching a specific keyword, with optional boost value to influence search relevance.
    
    Args:
        keyword (str): The search term to look for in products
        boost_value (int, optional): Custom boost value to influence search relevance
    
    Returns:
        Returns search results for products matching a specified keyword with optional relevance boosting."""
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780"
    
    # Build the search URL
    search_url = f"{base_url}/rest/default/V1/search"
    
    # Build the query parameters
    params = {
        "searchCriteria[requestName]": "quick_search_container",
        "searchCriteria[filterGroups][0][filters][0][field]": "search_term",
        "searchCriteria[filterGroups][0][filters][0][value]": keyword
    }
    
    # Add boost value if provided
    if boost_value is not None:
        params["searchCriteria[filterGroups][0][filters][0][boost]"] = boost_value
    
    # Make the request
    response = requests.get(search_url, headers=headers, params=params)
    
    return response

if __name__ == '__main__':
    r = search_products_by_keyword("digital watch")
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