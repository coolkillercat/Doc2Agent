import requests, json
from urllib.parse import quote



def get_project_badges(project_id: str) -> dict:
    """
    Retrieves the badges associated with a specified project. These badges can indicate project status, achievements, or compliance levels that are displayed in the project's profile.

    Args:
        project_id (str): The ID of the project for which to retrieve badges.

    Returns:
        Returns a list of badges associated with a specified project that indicate status, achievements, or compliance levels."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi', }
    url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/projects/{project_id}/badges"
    response = requests.get(url, headers=headers)
    return response

if __name__ == '__main__':
    r = get_project_badges(project_id="183")
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