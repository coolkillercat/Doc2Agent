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


def assign_attribute_to_attribute_set(attributeSetId, attributeGroupId, attributeCode, sortOrder):
    """
    Assign an attribute to an attribute set.
    
    Args:
        attributeSetId (int): The ID of the attribute set.
        attributeGroupId (int): The ID of the attribute group.
        attributeCode (str): The code of the attribute to assign.
        sortOrder (int): The sort order for the attribute.
        
    Returns:
        requests.Response: The response from the API.
        
    Examples:
        >>> assign_attribute_to_attribute_set(4, 7, 'color', 1)
        >>> assign_attribute_to_attribute_set(4, 7, 'size', 2)
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    api_url = f"{base_url}/rest/default/V1/products/attribute-sets/attributes"
    
    # Convert string IDs to integers if needed
    if isinstance(attributeSetId, str):
        attributeSetId = int(attributeSetId)
    if isinstance(attributeGroupId, str):
        attributeGroupId = int(attributeGroupId)
    if isinstance(sortOrder, str):
        sortOrder = int(sortOrder)
    
    payload = {
        'attributeSetId': attributeSetId,
        'attributeGroupId': attributeGroupId,
        'attributeCode': attributeCode,
        'sortOrder': sortOrder
    }
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': get_shopping_admin_auth_token()
    }
    
    response = requests.post(url=api_url, json=payload, headers=headers, timeout=50, verify=False)
    return response


if __name__ == '__main__':
    r = assign_attribute_to_attribute_set(attributeSetId=4, attributeGroupId=7, attributeCode='color', sortOrder=1)
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