import requests, json
from urllib.parse import quote


def get_merge_request_notes(project_id: str, merge_request_iid: int, sort: str = 'desc', order_by: str = 'created_at'):
    """
    Retrieves all notes/comments for a specific merge request, with options to sort and order the results.
    
    Args:
        project_id (str): The ID or URL-encoded path of the project
        merge_request_iid (int): The IID of the project merge request
        sort (str, optional): Return merge request notes sorted in 'asc' or 'desc' order. Default is 'desc'
        order_by (str, optional): Return merge request notes ordered by 'created_at' or 'updated_at'. Default is 'created_at'
    
    Returns:
        Response: The API response containing the merge request notes
        
    Example:
        >>> get_merge_request_notes(project_id='183', merge_request_iid=1)
        >>> get_merge_request_notes(project_id='183', merge_request_iid=1, sort='asc', order_by='updated_at')
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/projects/{quote(str(project_id), safe='')}/merge_requests/{merge_request_iid}/notes"
    
    params = {
        'sort': sort,
        'order_by': order_by
    }
    
    response = requests.get(url, headers=headers, params=params)
    return response


if __name__ == '__main__':
    r = get_merge_request_notes(project_id='183', merge_request_iid=1)
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