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

def get_countries_and_regions():
    """
    Retrieves a list of all countries and their regions from the Magento API.
    
    This function makes a GET request to the Magento API endpoint for countries
    and returns the response containing country information including available regions.
    
    Returns:
        requests.Response: The API response object containing country data.
        
    Example:
        >>> response = get_countries_and_regions()
        >>> countries = response.json()
        >>> print(f"Number of countries: {len(countries)}")
        >>> # Get information about a specific country
        >>> usa = next((country for country in countries if country['id'] == 'US'), None)
        >>> if usa:
        >>>     print(f"USA has {len(usa.get('available_regions', []))} regions")
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    api_url = f"{base_url}/rest/default/V1/directory/countries"
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token()
    }
    
    response = requests.get(url=api_url, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = get_countries_and_regions()
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