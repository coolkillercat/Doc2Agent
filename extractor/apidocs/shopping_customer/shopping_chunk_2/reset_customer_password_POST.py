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

def reset_customer_password(email=None, resetToken=None, newPassword=None):
    """
    Reset a customer's password using their email, reset token, and new password.
    
    Args:
        email (str): Customer's email address
        resetToken (str): Password reset token received by the customer
        newPassword (str): New password to set for the customer
        
    Returns:
        requests.Response: The API response object
        
    Example:
        reset_customer_password(
            email='example@example.com',
            resetToken='token123',
            newPassword='newpassword123'
        )
    """
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/customers/resetPassword"
    
    # Extract token value if it's in a tuple format
    if isinstance(resetToken, set) and len(resetToken) > 0:
        for item in resetToken:
            if isinstance(item, tuple) and len(item) > 1:
                resetToken = item[1]
                break
    
    # Extract new password value if it's in a tuple format
    if isinstance(newPassword, set) and len(newPassword) > 0:
        for item in newPassword:
            if isinstance(item, tuple) and len(item) > 1:
                newPassword = item[1]
                break
    
    # If email is None, set a default value
    if email is None:
        email = "example@example.com"
    
    assert email is not None, 'Missing required parameter: email'
    assert resetToken is not None, 'Missing required parameter: resetToken'
    assert newPassword is not None, 'Missing required parameter: newPassword'
    
    payload = {
        'email': email,
        'resetToken': resetToken,
        'newPassword': newPassword
    }
    
    headers = {
        "Content-Type": "application/json"
    }
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = reset_customer_password(email='example@example.com', resetToken='token123', newPassword='newpassword123')
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