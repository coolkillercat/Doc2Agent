import requests
import json
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


def check_product_salability(sku=None, stockId=None):
    """
    Check if a product is salable for a given SKU in a given Stock.
    
    Args:
        sku (str): The SKU of the product to check. Required.
        stockId (int): The stock ID to check against. Required.
        
    Returns:
        Returns a boolean indicating whether a specific product is salable in a given stock location.
    Example:
        >>> check_product_salability(sku='ABC123', stockId=1)
    """
    assert sku is not None, 'Missing required parameter: sku'
    assert stockId is not None, 'Missing required parameter: stockId'
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780"
    api_url = f"{base_url}/rest/default/V1/inventory/is-product-salable/{quote(str(sku), safe='')}/{stockId}"
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token()
    }
    
    response = requests.get(url=api_url, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = check_product_salability(sku='''ABC123''', stockId=1)
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