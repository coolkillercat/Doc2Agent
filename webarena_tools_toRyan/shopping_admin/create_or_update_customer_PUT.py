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


def create_or_update_customer(customer_data=None):
    """
    Create or update a customer using the Magento API.
    
    Args:
        customer_data (dict, optional): Customer data to update. Must include email.
            Example: {
                "customer": {
                    "email": "customer@example.com",
                    "firstname": "John",
                    "lastname": "Doe"
                }
            }
    
    Returns:
        requests.Response: The API response object
    
    Raises:
        ValueError: If customer email is missing
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    api_url = f"{base_url}/rest/default/V1/customers/me"
    
    if customer_data is None:
        customer_data = {
            "customer": {
                "email": "customer@example.com",
                "firstname": "John",
                "lastname": "Doe"
            }
        }
    
    # Ensure customer email is provided
    if "customer" not in customer_data or "email" not in customer_data["customer"]:
        raise ValueError("Customer email is required")
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token()
    }
    
    response = requests.put(url=api_url, json=customer_data, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    # Example customer data with email
    customer_data = {
        "customer": {
            "email": "customer@example.com",
            "firstname": "John",
            "lastname": "Doe"
        }
    }
    
    r = create_or_update_customer(customer_data)
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