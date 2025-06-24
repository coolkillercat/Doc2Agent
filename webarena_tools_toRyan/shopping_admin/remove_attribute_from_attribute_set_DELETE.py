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


def remove_attribute_from_attribute_set(attributeSetId, attributeCode):
    """
    Remove an attribute from an attribute set.
    
    Args:
        attributeSetId (str): The ID of the attribute set.
        attributeCode (str): The code of the attribute to remove.
        
    Returns:
        requests.Response: The response from the API.
        
    Examples:
        >>> remove_attribute_from_attribute_set(attributeSetId='4', attributeCode='color')
        <Response [200]>
    """
    assert attributeSetId is not None, 'Missing required parameter: attributeSetId'
    assert attributeCode is not None, 'Missing required parameter: attributeCode'
    
    base_url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770'
    api_url = f"{base_url}/rest/default/V1/products/attribute-sets/{quote(str(attributeSetId), safe='')}/attributes/{quote(attributeCode, safe='')}"
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token()
    }
    
    response = requests.delete(url=api_url, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = remove_attribute_from_attribute_set(attributeSetId='4', attributeCode='color')
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