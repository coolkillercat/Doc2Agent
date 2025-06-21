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


def get_bundle_product_option_types():
    """
    Get all types for options for bundle products.
    
    Returns:
        Returns a list of available option types for bundle products with their labels and codes.
    Example:
        >>> response = get_bundle_product_option_types()
        >>> option_types = response.json()
        >>> print(option_types)
        [
            {
                "label": "Drop-down",
                "code": "select"
            },
            {
                "label": "Radio Buttons",
                "code": "radio"
            },
            {
                "label": "Checkbox",
                "code": "checkbox"
            },
            {
                "label": "Multiple Select",
                "code": "multi"
            }
        ]
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780"
    api_url = f"{base_url}/rest/default/V1/bundle-products/options/types"
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token()
    }
    
    response = requests.get(url=api_url, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = get_bundle_product_option_types()
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