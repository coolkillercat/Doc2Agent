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

def retrieve_attribute_metadata(attributeCode=None, entity_type="customer"):
    """
    Retrieve attribute metadata from the API.
    
    Args:
        attributeCode (str): The code of the attribute to retrieve metadata for.
                            Example: 'firstname', 'lastname', 'middlename', 'prefix', 'suffix',
                                    'region', 'country_id', 'street', 'region_id', 'company'
        entity_type (str, optional): The type of entity. Defaults to "customer".
                            Example: 'customer'
    
    Returns:
        requests.Response: The API response object.
    
    Raises:
        AssertionError: If attributeCode is not provided.
    """
    assert attributeCode is not None, 'Missing required parameter: attributeCode'
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    api_url = f"{base_url}/rest/default/V1/attributeMetadata/{entity_type}/attribute/{quote(attributeCode, safe='')}"
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token()
    }
    
    response = requests.get(url=api_url, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = retrieve_attribute_metadata(attributeCode='firstname')
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