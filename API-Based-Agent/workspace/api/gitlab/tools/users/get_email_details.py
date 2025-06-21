import requests, json
from urllib.parse import quote


def get_email_details(email_id: int) -> dict:
    """
    Retrieves details of a specific email including the email address and confirmation timestamp.
    Useful for verifying email status or retrieving email information for a user.
    
    Args:
        email_id (int): The ID of the email to retrieve
    
    Returns:
        dict: A dictionary containing email details including id, email address, and confirmation timestamp
        
    Example:
        >>> get_email_details(1)
        {
            "id": 1,
            "email": "email@example.com",
            "confirmed_at": "2021-03-26T19:07:56.248Z"
        }
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    base_url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4'
    endpoint = f"/user/emails/{email_id}"
    url = base_url + endpoint
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    return response

if __name__ == '__main__':
    r = get_email_details(email_id=1)
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