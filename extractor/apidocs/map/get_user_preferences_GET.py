import requests, json
from urllib.parse import quote


def get_user_preferences():
    """
    Retrieves the preferences of the currently authenticated user from the OpenStreetMap API.
    
    Returns:
        requests.Response: The response object from the API request.
        
    Example:
        >>> response = get_user_preferences()
        >>> if response.status_code == 200:
        ...     preferences = response.json()
        ... else:
        ...     print(f"Error: {response.status_code}, {response.text}")
    """
    api_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:3000/api/0.6/user/preferences"
    
    # Set up authentication headers
    headers = {
        "Authorization": "Bearer YOUR_ACCESS_TOKEN"  # Replace with actual OAuth token
    }
    
    try:
        response = requests.get(url=api_url, headers=headers, timeout=50)
        return response
    except requests.exceptions.RequestException as e:
        # Create a response-like object for error handling
        class ErrorResponse:
            def __init__(self, status_code, text):
                self.status_code = status_code
                self.text = text
                self.content = text.encode('utf-8')
            
            def json(self):
                return None
        
        return ErrorResponse(500, f"Request failed: {str(e)}")

if __name__ == '__main__':
    r = get_user_preferences()
    r_json = None
    try:
        r_json = r.json()
    except:
        pass
    
    result_dict = dict()
    result_dict['status_code'] = r.status_code
    result_dict['text'] = r.text
    result_dict['json'] = r_json
    result_dict['content'] = r.content.decode("utf-8") if hasattr(r, 'content') else r.text
    
    print(json.dumps(result_dict, indent=4))