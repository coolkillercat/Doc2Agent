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

def send_otp_with_authy(via='sms'):
    """
    Send a one-time password to a device using Authy.
    
    Args:
        via (str): The method to send the OTP. Options include 'sms', 'call', or 'push'.
                   Default is 'sms'.
    
    Returns:
        requests.Response: The response object from the API call.
    
    Example:
        >>> send_otp_with_authy(via='sms')
        <Response [200]>
        >>> send_otp_with_authy(via=None)
        <Response [200]>
    """
    # If via is None, use the default value
    if via is None:
        via = 'sms'
    
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/V1/tfa/provider/authy/send-token/{via}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + get_shopping_customer_auth_token(),
    }
    
    response = requests.post(url=api_url, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = send_otp_with_authy(via='sms')
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