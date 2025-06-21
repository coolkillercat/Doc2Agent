import requests, json
from urllib.parse import quote

def approve_user(user_id: int) -> dict:
    """
    Approves a pending user account. This function allows administrators to grant system access to users who require approval before their accounts are activated.
    
    Args:
        user_id (int): The ID of the user to be approved.
        
    Returns:
        dict: The response object from the API call containing the status and message.
        
    Example:
        >>> approve_user(user_id=2330)
        {'message': 'Success'}
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/users/{user_id}/approve"
    
    response = requests.post(url, headers=headers)
    
    result = {}
    result['status_code'] = response.status_code
    result['text'] = response.text
    
    try:
        result['json'] = response.json()
    except:
        result['json'] = None
    
    result['content'] = response.content.decode("utf-8")
    
    return result

if __name__ == '__main__':
    r = approve_user(user_id=2330)
    r_json = None
    try:
        r_json = r['json']
    except:
        pass
    import json
    result_dict = dict()
    result_dict['status_code'] = r['status_code']
    result_dict['text'] = r['text']
    result_dict['json'] = r_json
    result_dict['content'] = r['content']
    print(json.dumps(result_dict, indent=4))