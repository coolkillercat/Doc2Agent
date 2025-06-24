import requests, json
from urllib.parse import quote



def set_user_status(emoji: str = 'speech_balloon', message: str = None, clear_status_after: str = None, method: str = 'PUT'):
    """
    Sets or updates the current user's status with custom emoji, message, and optional auto-clear timing. Allows choosing between PUT (replace entire status) or PATCH (update only specified fields).

    Args:
        emoji (str): Name of the emoji to use as status. Default is 'speech_balloon'.
        message (str): Message to set as a status. Cannot exceed 100 characters.
        clear_status_after (str): When to automatically clear status. Allowed values: 
            '30_minutes', '3_hours', '8_hours', '1_day', '3_days', '7_days', '30_days'
        method (str): HTTP method to use, either 'PUT' (replace all fields) or 'PATCH' (update only specified fields)

    Returns:
        Returns the user's status information including emoji, message, availability, HTML-formatted message, and auto-clear timestamp."""
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    endpoint = "/user/status"
    url = f"{base_url}{endpoint}"
    
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    
    # Prepare data payload
    payload = {}
    if emoji is not None:
        payload['emoji'] = emoji
    if message is not None:
        payload['message'] = message
    if clear_status_after is not None:
        payload['clear_status_after'] = clear_status_after
    
    # Make the request using the specified method
    if method.upper() == 'PUT':
        response = requests.put(url, headers=headers, json=payload)
    elif method.upper() == 'PATCH':
        response = requests.patch(url, headers=headers, json=payload)
    else:
        raise ValueError("Method must be either 'PUT' or 'PATCH'")
    
    return response

if __name__ == '__main__':
    r = set_user_status(emoji='coffee', message='I need more coffee', clear_status_after='3_hours', method='PUT')
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