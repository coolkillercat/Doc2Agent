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


def retrieve_attributes_by_form_code(formCode=None):
    """
    Retrieve all customer attributes filtered by form code.
    
    Args:
        formCode (str): The form code to filter attributes by. 
                        Examples: 'address_form', 'customer_account_create', 'customer_account_edit'
    
    Returns:
        requests.Response: The API response object containing the attributes data
        
    Example:
        >>> response = retrieve_attributes_by_form_code(formCode='address_form')
        >>> attributes = response.json()
    """
    BASE_URL = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770'
    
    assert formCode is not None, 'Missing required parameter: formCode'
    
    api_url = f"{BASE_URL}/rest/default/V1/attributeMetadata/customer/form/{quote(formCode, safe='')}"
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    
    response = requests.get(url=api_url, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = retrieve_attributes_by_form_code(formCode='customer_account_create')
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