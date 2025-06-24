import requests, json
from urllib.parse import quote



def list_user_emails():
    """
    Retrieves a list of all email addresses associated with the authenticated user's account, showing each email's ID, address, and confirmation status.
    
    Returns:
        Returns a list of email addresses associated with the authenticated user's account, including each email's ID and confirmation status."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi', }
    url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/user/emails"
    response = requests.get(url, headers=headers)
    return response

if __name__ == '__main__':
    r = list_user_emails()
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