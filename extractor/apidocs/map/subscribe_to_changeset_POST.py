import requests

def subscribe_to_changeset(changeset_id):
    """
    Subscribe to a changeset discussion to receive notifications for new comments.
    
    This function allows a user to subscribe to a changeset discussion. When subscribed,
    the user will receive notifications when new comments are added to the changeset.
    
    Args:
        changeset_id (int): The ID of the changeset to subscribe to.
        
    Returns:
        requests.Response: The response from the API.
        
    Example:
        >>> response = subscribe_to_changeset(12345)
        >>> print(response.status_code)
        200
    """
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:3000/api/0.6/changeset/{changeset_id}/subscribe"
    
    response = requests.post(url=api_url, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    # Example usage
    changeset_id = 1000  # Replace with an actual changeset ID
    r = subscribe_to_changeset(changeset_id)
    
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