import requests, json
from urllib.parse import quote

def get_shopping_admin_admin_auth_token():
    response = requests.post(
        url=f'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/integration/admin/token',
        headers={
            'content-type': 'application/json'
        },
        data=json.dumps({
            'username': 'admin',
            'password': 'admin1234'
        })
    )
    return response.json()

def get_apple_pay_auth():
    """
    Retrieves Apple Pay authentication information from the API.
    
    Returns:
        requests.Response: The API response containing Apple Pay authentication data.
    """
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/applepay/auth"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + get_shopping_admin_admin_auth_token(),
    }
    
    response = requests.get(url=api_url, headers=headers, timeout=50, verify=False)
    if response.status_code != 200:
        response = requests.get(url=api_url, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = get_apple_pay_auth()
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