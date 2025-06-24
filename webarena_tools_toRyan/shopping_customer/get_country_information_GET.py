import requests
import json
from urllib.parse import quote

def get_shopping_customer_auth_token():
    """
    Get customer authentication token from the API.
    
    Returns:
        str: Authentication token for the customer
        
    Example:
        token = get_shopping_customer_auth_token()
    """
    response = requests.post(
        url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/integration/customer/token',
        headers = {
            'content-type': 'application/json'
        },
        data = json.dumps({
            'username': 'emma.lopez@gmail.com',
            'password': 'Password.123'
        })
    )
    return "Bearer " + response.json()


def get_country_information(countryId):
    """
    Get country and region information for the store.
    
    Args:
        countryId (str): The country ID to retrieve information for
    
    Returns:
        requests.Response: The API response containing country information
    
    Example:
        response = get_country_information(countryId='US')
    """
    assert countryId is not None, 'Missing required parameter: countryId'
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    api_url = f"{base_url}/rest/default/V1/directory/countries/{quote(countryId, safe='')}"
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_customer_auth_token()
    }
    
    response = requests.get(url=api_url, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = get_country_information(countryId='US')
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