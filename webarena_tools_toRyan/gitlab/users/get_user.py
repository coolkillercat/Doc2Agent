import requests, json
from urllib.parse import quote



def get_user(user_id: int, include_custom_attributes: bool = False) -> dict:
    """
    Retrieves detailed information about a specific user by their ID. This function allows fetching comprehensive user profile data, with an option to include custom attributes.
    
    Args:
        user_id: The ID of the user to retrieve information for
        include_custom_attributes: Whether to include custom attributes in the response
    
    Returns:
        Returns detailed profile information for a specific user including personal details, social media links, activity metrics, and optional custom attributes."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED', }
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/users/{user_id}"
    
    params = {}
    if include_custom_attributes:
        params['with_custom_attributes'] = 'true'
    
    response = requests.get(url, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = get_user(user_id=2330, include_custom_attributes=True)
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