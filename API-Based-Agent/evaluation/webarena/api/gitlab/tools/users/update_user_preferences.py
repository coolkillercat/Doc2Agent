import requests, json
from urllib.parse import quote



def update_user_preferences(view_diffs_file_by_file: bool, show_whitespace_in_diffs: bool, pass_user_identities_to_ci_jwt: bool) -> dict:
    """
    Updates the current user's preferences for viewing diffs and handling CI authentication. Returns the updated user preference settings.

    Args:
        view_diffs_file_by_file (bool): Flag indicating the user sees only one file diff per page.
        show_whitespace_in_diffs (bool): Flag indicating the user sees whitespace changes in diffs.
        pass_user_identities_to_ci_jwt (bool): Flag indicating the user passes their external identities as CI information.

    Returns:
        Returns the updated user preferences for viewing diffs and handling CI authentication."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    
    url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/user/preferences"
    
    data = {
        "view_diffs_file_by_file": view_diffs_file_by_file,
        "show_whitespace_in_diffs": show_whitespace_in_diffs,
        "pass_user_identities_to_ci_jwt": pass_user_identities_to_ci_jwt
    }
    
    response = requests.put(url, headers=headers, data=json.dumps(data))
    return response

if __name__ == '__main__':
    r = update_user_preferences(view_diffs_file_by_file=True, show_whitespace_in_diffs=False, pass_user_identities_to_ci_jwt=False)
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