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


def save_attribute_set(attributeSetId, attributeSet=None, skeletonId=None):
    """
    Save attribute set data using the Magento API.
    
    Args:
        attributeSetId (str or int): The ID of the attribute set to save.
        attributeSet (dict, optional): The attribute set data. Default is None.
            Example: {
                'attribute_set_id': 1,
                'attribute_set_name': 'Default',
                'sort_order': 0,
                'entity_type_id': 4
            }
        skeletonId (int, optional): The skeleton ID. Default is None.
        
    Returns:
        requests.Response: The API response object.
        
    Example:
        >>> save_attribute_set(
        ...     attributeSetId='1',
        ...     attributeSet={
        ...         'attribute_set_id': 1,
        ...         'attribute_set_name': 'Default',
        ...         'sort_order': 0,
        ...         'entity_type_id': 4
        ...     },
        ...     skeletonId=4
        ... )
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    api_url = f"{base_url}/rest/default/V1/products/attribute-sets/{attributeSetId}"
    
    assert attributeSetId is not None, 'Missing required parameter: attributeSetId'
    
    # Default attribute set if none provided
    if attributeSet is None:
        attributeSet = {
            'attribute_set_id': int(attributeSetId),
            'attribute_set_name': 'Default',
            'sort_order': 0,
            'entity_type_id': 4
        }
    
    payload = {
        'attributeSet': attributeSet
    }
    
    # Add skeletonId if provided
    if skeletonId is not None:
        payload['skeletonId'] = skeletonId
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token()
    }
    
    response = requests.put(url=api_url, json=payload, headers=headers, timeout=50, verify=False)
    return response


if __name__ == '__main__':
    r = save_attribute_set(attributeSetId='1')
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