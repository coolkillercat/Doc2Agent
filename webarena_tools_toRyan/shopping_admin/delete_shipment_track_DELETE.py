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


def delete_shipment_track(id=None):
    """
    Deletes a specified shipment track by ID.
    
    Args:
        id (int): The shipment track ID to delete.
            Example: 123
    
    Returns:
        requests.Response: The response from the API.
        
    Raises:
        AssertionError: If the required parameter 'id' is not provided.
    """
    assert id is not None, 'Missing required parameter: id'
    
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/shipment/track/{id}"
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    
    response = requests.delete(url=api_url, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = delete_shipment_track(id=123)
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