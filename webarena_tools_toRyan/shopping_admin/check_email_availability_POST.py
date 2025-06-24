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


def check_email_availability(customerEmail, websiteId=None):
    """
    Check if given email is associated with a customer account in given website.
    
    Args:
        customerEmail (str): The email address to check availability for.
        websiteId (int, optional): The website ID to check against. If not set, will use the current websiteId.
        
    Returns:
        requests.Response: The API response object.
        
    Example:
        >>> check_email_availability(customerEmail="example@example.com", websiteId=1)
        <Response [200]>
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    api_url = f"{base_url}/rest/default/V1/customers/isEmailAvailable"
    
    payload = {'customerEmail': customerEmail}
    if websiteId is not None:
        payload['websiteId'] = websiteId
        
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    
    response = requests.post(url=api_url, json=payload, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = check_email_availability(customerEmail="example@example.com", websiteId=1)
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