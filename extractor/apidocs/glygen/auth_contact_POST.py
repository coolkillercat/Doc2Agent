import requests, json
from urllib.parse import quote

def auth_contact(payload=None):
    """
    Send a contact message to the GlyGen API.
    
    Args:
        payload (dict): A dictionary containing contact information with the following keys:
            - fname (str): First name
            - lname (str): Last name
            - email (str): Email address
            - subject (str): Subject of the message
            - message (str): Content of the message
            
    Returns:
        requests.Response: The response from the API
        
    Example:
        >>> payload = {
        ...     'email': 'example@example.com',
        ...     'fname': 'John',
        ...     'lname': 'Doe',
        ...     'subject': 'Inquiry',
        ...     'message': 'Hello, I have a question.'
        ... }
        >>> response = auth_contact(payload=payload)
    """
    api_url = "https://api.glygen.org/auth/contact/"
    headers = {'Content-Type': 'application/json'}
    
    assert payload is not None, 'Missing required parameter: payload'
    assert 'email' in payload, 'Missing required field: email'
    assert 'fname' in payload, 'Missing required field: fname'
    assert 'lname' in payload, 'Missing required field: lname'
    assert 'subject' in payload, 'Missing required field: subject'
    assert 'message' in payload, 'Missing required field: message'
    
    response = requests.post(url=api_url, json=payload, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = auth_contact(payload={'email': 'example@example.com', 'fname': 'John', 'lname': 'Doe', 'subject': 'Inquiry', 'message': 'Hello, I have a question.'})
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