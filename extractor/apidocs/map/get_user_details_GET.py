import requests, json
from urllib.parse import quote


def get_user_details():
    """
    Retrieves details of the currently authenticated user from the OpenStreetMap API.
    
    This function makes a GET request to the OSM API endpoint for user details.
    Authentication is required for this endpoint.
    
    Returns:
        requests.Response: The response object from the API request.
        
    Example:
        >>> response = get_user_details()
        >>> if response.status_code == 200:
        >>>     user_data = response.json()
        >>>     print(f"Logged in as: {user_data['user']['display_name']}")
        >>> else:
        >>>     print(f"Error: {response.status_code} - {response.text}")
    """
    api_url = "https://api.openstreetmap.org/api/0.6/user/details"
    
    # Authentication is required for this endpoint
    # This function assumes authentication is handled elsewhere (e.g., via session cookies or OAuth)
    
    try:
        response = requests.get(url=api_url, timeout=50)
        return response
    except requests.exceptions.RequestException as e:
        # Create a response-like object with error information
        error_response = requests.Response()
        error_response.status_code = 500
        error_response._content = str(e).encode('utf-8')
        return error_response

if __name__ == '__main__':
    r = get_user_details()
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