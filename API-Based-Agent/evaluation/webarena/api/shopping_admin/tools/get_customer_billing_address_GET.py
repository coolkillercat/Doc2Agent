import requests
import json

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


def get_customer_billing_address(customerId=None):
    """
    Retrieve default billing address for the given customerId.
    
    Args:
        customerId (int): The ID of the customer whose billing address is to be retrieved.
            Example: 1
    
    Returns:
        Returns a customer's default billing address including contact information, location details, and address status.
    Raises:
        AssertionError: If customerId is not provided.
    
    Example:
        >>> response = get_customer_billing_address(customerId=1)
        >>> print(response.status_code)
        200
    """
    assert customerId is not None, 'Missing required parameter: customerId'
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780"
    api_url = f"{base_url}/rest/default/V1/customers/{customerId}/billingAddress"
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token()
    }
    
    response = requests.get(url=api_url, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = get_customer_billing_address(customerId=1)
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