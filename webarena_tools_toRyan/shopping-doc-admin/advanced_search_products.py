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


def advanced_search_products(sku: str = None, category_ids: list = None, price_from: float = None, price_to: float = None, condition_type: str = 'eq'):
    """
    Executes an advanced product search with more complex criteria, allowing for different comparison types like 'eq', 'like', or 'finset' when searching by SKU or other attributes.
    
    Args:
        sku (str, optional): Product SKU to search for
        category_ids (list, optional): List of category IDs to filter by
        price_from (float, optional): Minimum price for filtering
        price_to (float, optional): Maximum price for filtering
        condition_type (str, optional): Comparison type ('eq', 'like', 'finset', etc.). Defaults to 'eq'
    
    Returns:
        requests.Response: The API response containing search results
    """
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token(), }
    
    base_url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770'
    search_url = f'{base_url}/rest/default/V1/search'
    
    url = f'{search_url}?searchCriteria[requestName]=advanced_search_container'
    
    filter_index = 0
    
    if sku:
        url += f'&searchCriteria[filterGroups][0][filters][{filter_index}][field]=sku'
        url += f'&searchCriteria[filterGroups][0][filters][{filter_index}][value]={quote(sku)}'
        url += f'&searchCriteria[filterGroups][0][filters][{filter_index}][condition_type]={condition_type}'
        filter_index += 1
    
    if category_ids:
        for i, category_id in enumerate(category_ids):
            url += f'&searchCriteria[filterGroups][0][filters][{filter_index}][field]=category_ids'
            url += f'&searchCriteria[filterGroups][0][filters][{filter_index}][value][{i}]={category_id}'
            url += f'&searchCriteria[filterGroups][0][filters][{filter_index}][condition_type]=eq'
        filter_index += 1
    
    if price_from:
        url += f'&searchCriteria[filterGroups][0][filters][{filter_index}][field]=price.from'
        url += f'&searchCriteria[filterGroups][0][filters][{filter_index}][value]={price_from}'
        filter_index += 1
    
    if price_to:
        url += f'&searchCriteria[filterGroups][0][filters][{filter_index}][field]=price.to'
        url += f'&searchCriteria[filterGroups][0][filters][{filter_index}][value]={price_to}'
    
    response = requests.get(url, headers=headers)
    return response


if __name__ == '__main__':
    # Test with a sample search for products with 'shirt' in the SKU
    r = advanced_search_products(sku='shirt', condition_type='like', price_from=10, price_to=100)
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