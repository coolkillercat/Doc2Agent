import requests, json
from urllib.parse import quote



def get_user_counts() -> dict:
    """
    Retrieves counts of assigned issues, merge requests, review requests, and todos for the authenticated user. Provides an overview of the user's current workload and pending actions in GitLab.
    
    Returns:
        Returns counts of assigned issues, merge requests, review requests, and todos for the authenticated GitLab user."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi', }
    
    url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/user_counts"
    
    response = requests.get(url, headers=headers)
    
    return response

if __name__ == '__main__':
    r = get_user_counts()
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