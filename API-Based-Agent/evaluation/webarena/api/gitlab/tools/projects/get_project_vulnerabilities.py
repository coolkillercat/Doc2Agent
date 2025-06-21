import requests, json
from urllib.parse import quote

def get_project_vulnerabilities(project_id, severity=None, status=None, page=1, per_page=100):
    """
    Retrieves vulnerability data for a specified project, with optional filtering by severity and status.
    This helps users identify and manage security issues in their codebase.
    
    Args:
        project_id: The ID of the project to retrieve vulnerabilities for
        severity (str, optional): Filter vulnerabilities by severity (critical, high, medium, low, unknown)
        status (str, optional): Filter vulnerabilities by status (confirmed, dismissed, resolved)
        page (int, optional): Page number of the results to retrieve. Defaults to 1.
        per_page (int, optional): Number of results per page. Defaults to 100.
        
    Returns:
        Response: The HTTP response containing vulnerability data
        
    Example:
        >>> get_project_vulnerabilities(183)
        >>> get_project_vulnerabilities(183, severity='critical', status='confirmed')
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/projects/{project_id}/vulnerabilities"
    
    params = {
        'page': page,
        'per_page': per_page
    }
    
    if severity:
        params['severity'] = severity
        
    if status:
        params['state'] = status
    
    response = requests.get(url, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = get_project_vulnerabilities(project_id=183)
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