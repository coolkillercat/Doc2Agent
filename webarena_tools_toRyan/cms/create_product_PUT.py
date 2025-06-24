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


def create_product(sku=None, name=None, price=None, attribute_set_id=4, type_id="simple", weight=1, status=1, visibility=4, custom_attributes=None, **kwargs):
    """
    Create or update a product in the Magento catalog.
    
    Args:
        sku (str): The SKU of the product (required)
        name (str): The name of the product (required)
        price (float): The price of the product (required)
        attribute_set_id (int, optional): The attribute set ID. Defaults to 4.
        type_id (str, optional): The product type. Defaults to "simple".
        weight (float, optional): The product weight. Defaults to 1.
        status (int, optional): Product status (1 = enabled, 2 = disabled). Defaults to 1.
        visibility (int, optional): Product visibility (1 = Not Visible, 2 = Catalog, 3 = Search, 4 = Catalog & Search). Defaults to 4.
        custom_attributes (list, optional): List of custom attributes for the product.
        **kwargs: Additional product attributes to include
    
    Returns:
        Returns detailed product information including ID, SKU, name, price, status, attributes, and inventory data after creating or updating a product in the Magento catalog.
    Example:
        >>> create_product(
        ...     sku="test-product-sku",
        ...     name="Test Product",
        ...     price=19.99,
        ...     attribute_set_id=4,
        ...     type_id="simple"
        ... )
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780"
    api_url = f"{base_url}/rest/default/V1/products/{quote(str(sku))}"
    
    assert sku is not None, 'Missing required parameter: sku'
    assert name is not None, 'Missing required parameter: name'
    assert price is not None, 'Missing required parameter: price'
    
    product_data = {
        "sku": sku,
        "name": name,
        "price": price,
        "attribute_set_id": attribute_set_id,
        "type_id": type_id,
        "weight": weight,
        "status": status,
        "visibility": visibility
    }
    
    # Add custom attributes if provided
    if custom_attributes:
        product_data["custom_attributes"] = custom_attributes
    
    # Add any additional attributes
    for key, value in kwargs.items():
        product_data[key] = value
    
    payload = {
        "product": product_data
    }
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token()
    }
    
    response = requests.put(url=api_url, json=payload, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = create_product(sku='test-product-sku', name='Test Product', price=19.99)
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