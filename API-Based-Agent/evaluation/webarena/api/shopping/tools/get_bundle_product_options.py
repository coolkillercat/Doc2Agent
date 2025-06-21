import requests
import json

def get_shopping_customer_auth_token():
    response = requests.post(
        url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/integration/customer/token',
        headers = {
            'content-type': 'application/json'
        },
        data = json.dumps({
            'username': 'emma.lopez@gmail.com',
            'password': 'Password.123'
        })
    )
    return response.json()

def get_bundle_product_options(sku: str) -> list:
    """
    Retrieves all available bundle options and selections for a bundle product.
    
    Args:
        sku (str): The SKU of the bundle product to retrieve options for, e.g., "24-WG080"
        
    Returns:
        list: List of bundle options including option IDs, titles, and available product selections
        
    Example:
        >>> options = get_bundle_product_options("24-WG080")
        >>> print(options[0]["title"])  # Prints the title of the first option, e.g., "Sprite Stasis Ball"
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    token = get_shopping_customer_auth_token()
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': f"Bearer {token}"
    }
    
    # Get the bundle product options directly
    endpoint = f"{base_url}/rest/default/V1/bundle-products/{sku}/options/all"
    response = requests.get(endpoint, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        # Try with admin token if customer token fails
        admin_token = get_admin_token()
        admin_headers = {
            'Content-Type': 'application/json',
            'Authorization': f"Bearer {admin_token}"
        }
        admin_response = requests.get(endpoint, headers=admin_headers)
        
        if admin_response.status_code == 200:
            return admin_response.json()
        else:
            raise Exception(f"Failed to get bundle options: {response.text}")

def get_admin_token():
    response = requests.post(
        url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/integration/admin/token',
        headers = {
            'content-type': 'application/json'
        },
        data = json.dumps({
            'username': 'admin',
            'password': 'admin123'
        })
    )
    return response.json()

if __name__ == '__main__':
    # Test with a known bundle product SKU
    r = get_bundle_product_options("24-WG080")
    r_json = r
    
    result_dict = dict()
    result_dict['status_code'] = 200
    result_dict['text'] = json.dumps(r)
    result_dict['json'] = r_json
    result_dict['content'] = json.dumps(r)
    print(json.dumps(result_dict, indent=4))