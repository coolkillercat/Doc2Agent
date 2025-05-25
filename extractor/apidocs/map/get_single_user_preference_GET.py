import requests

def get_single_user_preference(your_key=None):
    """
    Retrieves a single user preference from the OpenStreetMap API.
    
    This function makes a GET request to the OpenStreetMap API to retrieve
    a specific user preference identified by the provided key.
    
    Args:
        your_key (str): The key of the preference to retrieve. Required.
        
    Returns:
        requests.Response: The response object from the API request.
        
    Raises:
        AssertionError: If your_key is None.
        
    Examples:
        >>> response = get_single_user_preference(your_key='theme')
        >>> print(response.text)  # Prints the preference value
    """
    assert your_key is not None, 'Missing required parameter: your_key'
    
    # Construct the URL with the key directly in the path
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:3000/api/0.6/user/preferences/{your_key}"
    
    # Make the request without additional query parameters
    response = requests.get(url=api_url, timeout=50, verify=False)
    
    return response

if __name__ == '__main__':
    r = get_single_user_preference(your_key='theme')
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