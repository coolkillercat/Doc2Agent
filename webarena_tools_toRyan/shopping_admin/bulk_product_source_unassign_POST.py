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


def bulk_product_source_unassign(skus=None, source_codes=None):
    """
    Run mass product to source un-assignment.
    
    Args:
        skus (list): List of product SKUs to unassign from sources. Required.
        source_codes (list): List of source codes to unassign products from. Required.
    
    Returns:
        requests.Response: The API response object.
    
    Example:
        >>> bulk_product_source_unassign(skus=["test-product-sku"], source_codes=["default"])
        >>> bulk_product_source_unassign(skus=["SKU123", "SKU456"], source_codes=["default"])
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    api_url = f"{base_url}/rest/default/V1/inventory/bulk-product-source-unassign"
    
    # Validate required parameters
    if skus is None or not skus:
        raise ValueError("Missing required parameter: skus")
    if source_codes is None or not source_codes:
        raise ValueError("Missing required parameter: source_codes")
    
    # Ensure parameters are lists of strings
    if isinstance(skus, str):
        skus = [skus]
    if isinstance(source_codes, str):
        source_codes = [source_codes]
    
    payload = {
        "skus": skus,
        "sourceCodes": source_codes
    }
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token()
    }
    
    response = requests.post(url=api_url, json=payload, headers=headers, timeout=50, verify=False)
    return response


if __name__ == '__main__':
    # Example usage with required parameters
    r = bulk_product_source_unassign(skus=["test-product-sku"], source_codes=["default"])
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