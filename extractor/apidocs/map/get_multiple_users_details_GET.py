import requests, json
from urllib.parse import quote


def get_multiple_users_details(user_ids=None):
    """
    Retrieves details for multiple OSM users by their IDs.
    
    This function makes a request to the OpenStreetMap API to get information about
    multiple users at once. The user IDs should be provided as a list or comma-separated string.
    
    Args:
        user_ids (list or str, optional): A list of user IDs or a comma-separated string of user IDs.
            If not provided, the function will return an error as the API requires at least one user ID.
    
    Returns:
        requests.Response: The response object from the API request.
        
    Example:
        >>> response = get_multiple_users_details([123, 456, 789])
        >>> response = get_multiple_users_details("123,456,789")
    """
    if not user_ids:
        raise ValueError("At least one user ID must be provided")
    
    # Convert list to comma-separated string if necessary
    if isinstance(user_ids, list):
        user_ids = ','.join(map(str, user_ids))
    
    api_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:3000/api/0.6/users"
    querystring = {"users": user_ids}
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    try:
        # Example with some user IDs - replace with actual IDs when testing
        r = get_multiple_users_details("1,2,3")
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
    except Exception as e:
        print(f"Error: {e}")