import requests, json
from urllib.parse import quote



def get_project_milestones(project_id, iids=None, state=None, title=None, search=None, include_ancestors=None, updated_before=None, updated_after=None):
    """
    Retrieves milestones for a specific project with optional filtering parameters such as milestone IIDs, state, title, or date ranges. Useful for tracking project progress, release planning, and milestone management.
    
    Args:
        project_id (int or str): The ID or URL-encoded path of the project
        iids (list, optional): Return only the milestones having the given iid
        state (str, optional): Return only 'active' or 'closed' milestones
        title (str, optional): Return only the milestones having the given title
        search (str, optional): Return only milestones with a title or description matching the provided string
        include_ancestors (bool, optional): Include milestones from all parent groups
        updated_before (str, optional): Return only milestones updated before the given datetime (ISO 8601 format)
        updated_after (str, optional): Return only milestones updated after the given datetime (ISO 8601 format)
    
    Returns:
        Returns a list of project milestones with optional filtering by IDs, state, title, search terms, or update dates."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/projects/{project_id}/milestones"
    
    params = {}
    if iids:
        params['iids[]'] = iids
    if state:
        params['state'] = state
    if title:
        params['title'] = title
    if search:
        params['search'] = search
    if include_ancestors is not None:
        params['include_ancestors'] = include_ancestors
    if updated_before:
        params['updated_before'] = updated_before
    if updated_after:
        params['updated_after'] = updated_after
    
    response = requests.get(url, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = get_project_milestones(project_id=183, state='active')
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