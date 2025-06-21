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


def search_products_with_filters(request_name: str, filters: list):
    """
    Performs a custom product search with multiple custom filters, providing flexibility for complex search requirements.
    
    Args:
        request_name (str): Container name for search (quick_search_container, advanced_search_container, or catalog_view_container)
        filters (list): List of dictionaries with field, value, and optional condition_type
                        Example: [{'field': 'price.from', 'value': '10'}, 
                                 {'field': 'search_term', 'value': 'watch', 'condition_type': 'like'}]
    
    Returns:
        Returns product search results with matching items, aggregated data, applied search criteria, and total count."""
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    base_url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780'
    
    # Start building the search URL
    url = f"{base_url}/rest/default/V1/search?searchCriteria[requestName]={request_name}"
    
    # Add filters to the URL
    for i, filter_data in enumerate(filters):
        field = filter_data.get('field')
        value = filter_data.get('value')
        condition_type = filter_data.get('condition_type', '')
        
        # If value is a list (for multiple values like category_ids)
        if isinstance(value, list):
            for j, val in enumerate(value):
                url += f"&searchCriteria[filterGroups][0][filters][{i}][field]={field}"
                url += f"&searchCriteria[filterGroups][0][filters][{i}][value][{j}]={val}"
        else:
            url += f"&searchCriteria[filterGroups][0][filters][{i}][field]={field}"
            url += f"&searchCriteria[filterGroups][0][filters][{i}][value]={value}"
        
        # Add condition type if specified
        if condition_type:
            url += f"&searchCriteria[filterGroups][0][filters][{i}][condition_type]={condition_type}"
    
    # Make the request
    response = requests.get(url, headers=headers)
    return response


if __name__ == '__main__':
    # Example: Search for digital watches using quick search
    r = search_products_with_filters(
        request_name="quick_search_container",
        filters=[
            {"field": "search_term", "value": "digital watch"}
        ]
    )
    
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