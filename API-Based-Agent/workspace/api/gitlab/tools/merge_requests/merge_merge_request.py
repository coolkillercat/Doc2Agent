import requests, json
from urllib.parse import quote

def merge_merge_request(project_id, merge_request_iid, merge_commit_message=None, merge_when_pipeline_succeeds=False, sha=None, should_remove_source_branch=False, squash=False, squash_commit_message=None):
    """
    Accepts and merges changes submitted with a merge request in GitLab. Allows customization of merge behavior including options for squashing commits, removing source branches, and waiting for pipeline completion.
    
    Args:
        project_id (int or str): The ID or URL-encoded path of the project owned by the authenticated user.
        merge_request_iid (int): The internal ID of the merge request.
        merge_commit_message (str, optional): Custom merge commit message.
        merge_when_pipeline_succeeds (bool, optional): If True, the merge request is merged when the pipeline succeeds.
        sha (str, optional): If present, then this SHA must match the HEAD of the source branch, otherwise the merge fails.
        should_remove_source_branch (bool, optional): If True, removes the source branch.
        squash (bool, optional): If True, the commits are squashed into a single commit on merge.
        squash_commit_message (str, optional): Custom squash commit message.
        
    Returns:
        requests.Response: The response from the API call.
        
    Example:
        >>> merge_merge_request(183, 1, should_remove_source_branch=True, squash=True)
        <Response [200]>
        
        >>> merge_merge_request(
        ...     project_id=183,
        ...     merge_request_iid=20,
        ...     merge_commit_message="Merging feature branch",
        ...     sha="c834c419354b5d2cd185a0952c377c3b03809baf"
        ... )
        <Response [200]>
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/projects/{quote(str(project_id), safe='')}/merge_requests/{merge_request_iid}/merge"
    
    data = {}
    if merge_commit_message is not None:
        data['merge_commit_message'] = merge_commit_message
    if merge_when_pipeline_succeeds is not None:
        data['merge_when_pipeline_succeeds'] = merge_when_pipeline_succeeds
    if sha is not None:
        data['sha'] = sha
    if should_remove_source_branch is not None:
        data['should_remove_source_branch'] = should_remove_source_branch
    if squash is not None:
        data['squash'] = squash
    if squash_commit_message is not None:
        data['squash_commit_message'] = squash_commit_message
    
    response = requests.put(url, headers=headers, json=data)
    return response

if __name__ == '__main__':
    r = merge_merge_request(project_id=183, merge_request_iid=1, should_remove_source_branch=True, squash=True)
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