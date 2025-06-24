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


def update_stock_item(productSku=None, itemId=None, stockItem=None):
    """
    Update stock information for a product.
    
    Args:
        productSku (str): The SKU of the product to update (required)
        itemId (str or int): The ID of the stock item to update (required)
        stockItem (dict): Stock information to update (required)
            Example: {'qty': 100, 'is_in_stock': True}
    
    Returns:
        Returns the stock item ID after updating a product's inventory information.
    Example:
        update_stock_item(
            productSku='test-product-sku',
            itemId='1',
            stockItem={'qty': 100, 'is_in_stock': True}
        )
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780"
    api_url = f"{base_url}/rest/default/V1/products/{quote(str(productSku))}/stockItems/{quote(str(itemId))}"
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    
    assert productSku is not None, 'Missing required parameter: productSku'
    assert itemId is not None, 'Missing required parameter: itemId'
    assert stockItem is not None, 'Missing required parameter: stockItem'
    
    payload = {'stockItem': stockItem}
    
    response = requests.put(url=api_url, json=payload, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = update_stock_item(productSku='test-product-sku', itemId='1', stockItem={'qty': 100, 'is_in_stock': True})
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