import requests, json
from urllib.parse import quote


def unsubscribe_from_changeset(changeset_id):
    """
    Unsubscribe from the discussion of a changeset to stop receiving notifications.
    
    This function sends a POST request to the OpenStreetMap API to unsubscribe
    from a changeset discussion. The request must be made as an authenticated user.
    
    Args:
        changeset_id (int): The ID of the changeset to unsubscribe from.
        
    Returns:
        requests.Response: The response from the API.
        
    Example:
        >>> response = unsubscribe_from_changeset(1000)
        >>> print(response.status_code)
        200
    """
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:3000/api/0.6/changeset/{changeset_id}/unsubscribe"
    
    response = requests.post(url=api_url, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    # Example usage with changeset ID 1000
    r = unsubscribe_from_changeset(1000)
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