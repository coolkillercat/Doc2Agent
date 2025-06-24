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


def get_products_salable_status(skus=None, stockId=None):
    """
    Get products salable status for given SKUs and given Stock.
    
    Args:
        skus (list): List of product SKUs to check salable status.
            Example: ['shopping-admin_part223', 'shopping-admin_part209']
        stockId (int): The stock ID to check against.
            Example: 1
            
    Returns:
        requests.Response: The API response object
        
    Example:
        >>> get_products_salable_status(skus=['shopping-admin_part223', 'shopping-admin_part209'], stockId=1)
    """
    api_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/inventory/are-products-salable"
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    
    assert skus is not None, 'Missing required parameter: skus'
    assert stockId is not None, 'Missing required parameter: stockId'
    
    # Ensure skus is a list
    if isinstance(skus, str):
        skus = [skus]
    
    # If stockId is in a set of tuples, extract just the stockId value
    if isinstance(stockId, set):
        # Extract the first stockId value from the set
        for item in stockId:
            if isinstance(item, tuple) and len(item) > 1:
                stockId = item[1]
                break
    
    querystring = {'skus[]': skus, 'stockId': stockId}
    
    response = requests.get(url=api_url, params=querystring, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = get_products_salable_status(skus=['SKU123', 'SKU456'], stockId=1)
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