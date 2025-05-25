import requests, json
from urllib.parse import quote

def get_shopping_customer_auth_token():
    response = requests.post(
        url = f'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/integration/customer/token',
        headers = {
            'content-type': 'application/json'
        },
        data = json.dumps({
            'username': 'emma.lopez@gmail.com',
            'password': 'Password.123'
        })
    )
    return response.json()

def save_requisition_list(name="My Requisition List", description="A new requisition list"):
    """
    Save a requisition list.
    
    Args:
        name (str, optional): The name of the requisition list. Defaults to "My Requisition List".
        description (str, optional): The description of the requisition list. Defaults to "A new requisition list".
    
    Returns:
        requests.Response: The response from the API.
    
    Example:
        >>> save_requisition_list(name="Grocery List", description="Weekly grocery shopping")
        >>> save_requisition_list()
    """
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/requisition_lists"
    payload = {
        "name": name,
        "description": description
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + get_shopping_customer_auth_token(),
    }
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = save_requisition_list()
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