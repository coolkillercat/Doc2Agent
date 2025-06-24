import requests
import json

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


def validate_customer_data(customer=None):
    """
    Validate customer data using the Magento API.
    
    Args:
        customer (dict): Customer data to validate. Required.
            Example: {
                'email': 'john.doe@example.com',
                'firstname': 'John',
                'lastname': 'Doe',
                'addresses': [
                    {
                        'street': ['123 Main St'],
                        'city': 'Anytown',
                        'region': {'region_code': 'NY'},
                        'postcode': '12345',
                        'country_id': 'US',
                        'telephone': '555-1234'
                    }
                ]
            }
    
    Returns:
        requests.Response: The API response object
    
    Raises:
        AssertionError: If customer parameter is None
    """
    api_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/customers/validate"
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    
    assert customer is not None, 'Missing required parameter: customer'
    
    payload = {'customer': customer}
    response = requests.put(url=api_url, json=payload, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    customer_data = {
        'email': 'john.doe@example.com',
        'firstname': 'John',
        'lastname': 'Doe',
        'addresses': [
            {
                'street': ['123 Main St'],
                'city': 'Anytown',
                'region': {'region_code': 'NY'},
                'postcode': '12345',
                'country_id': 'US',
                'telephone': '555-1234'
            }
        ]
    }
    
    r = validate_customer_data(customer=customer_data)
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