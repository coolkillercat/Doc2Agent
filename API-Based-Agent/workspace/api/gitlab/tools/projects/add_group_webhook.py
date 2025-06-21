import requests, json
from urllib.parse import quote

def add_group_webhook(group_id: str, webhook_url: str, token: str = None, push_events: bool = True, 
                     issues_events: bool = False, confidential_issues_events: bool = False,
                     merge_requests_events: bool = False, tag_push_events: bool = False, 
                     note_events: bool = False, confidential_note_events: bool = False,
                     job_events: bool = False, pipeline_events: bool = False, 
                     wiki_page_events: bool = False, deployment_events: bool = False,
                     releases_events: bool = False, subgroup_events: bool = False,
                     member_events: bool = False, enable_ssl_verification: bool = True,
                     push_events_branch_filter: str = None, resource_access_token_events: bool = False,
                     custom_webhook_template: str = None):
    """
    Creates a new webhook for a GitLab group that will send notifications for selected events to the specified URL.
    This allows automating workflows and integrating GitLab group activities with external systems.
    
    Args:
        group_id (str): The ID or URL-encoded path of the group
        webhook_url (str): The hook URL where events will be sent
        token (str, optional): Secret token to validate received payloads
        push_events (bool, optional): Trigger hook on push events. Defaults to True.
        push_events_branch_filter (str, optional): Trigger hook on push events for matching branches only.
        issues_events (bool, optional): Trigger hook on issues events. Defaults to False.
        confidential_issues_events (bool, optional): Trigger hook on confidential issues events. Defaults to False.
        merge_requests_events (bool, optional): Trigger hook on merge requests events. Defaults to False.
        tag_push_events (bool, optional): Trigger hook on tag push events. Defaults to False.
        note_events (bool, optional): Trigger hook on note events. Defaults to False.
        confidential_note_events (bool, optional): Trigger hook on confidential note events. Defaults to False.
        job_events (bool, optional): Trigger hook on job events. Defaults to False.
        pipeline_events (bool, optional): Trigger hook on pipeline events. Defaults to False.
        wiki_page_events (bool, optional): Trigger hook on wiki page events. Defaults to False.
        deployment_events (bool, optional): Trigger hook on deployment events. Defaults to False.
        releases_events (bool, optional): Trigger hook on release events. Defaults to False.
        subgroup_events (bool, optional): Trigger hook on subgroup events. Defaults to False.
        member_events (bool, optional): Trigger hook on member events. Defaults to False.
        enable_ssl_verification (bool, optional): Do SSL verification when triggering the hook. Defaults to True.
        resource_access_token_events (bool, optional): Trigger hook on project access token expiry events. Defaults to False.
        custom_webhook_template (str, optional): Custom webhook template for the hook.
        
    Returns:
        requests.Response: The HTTP response from the API
        
    Example:
        >>> response = add_group_webhook(
        ...     group_id="2597",
        ...     webhook_url="https://example.com/webhook",
        ...     token="secret_token",
        ...     push_events=True,
        ...     issues_events=True,
        ...     merge_requests_events=True
        ... )
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/groups/{quote(str(group_id), safe='')}/hooks"
    
    payload = {
        "url": webhook_url,
        "push_events": push_events,
        "issues_events": issues_events,
        "confidential_issues_events": confidential_issues_events,
        "merge_requests_events": merge_requests_events,
        "tag_push_events": tag_push_events,
        "note_events": note_events,
        "confidential_note_events": confidential_note_events,
        "job_events": job_events,
        "pipeline_events": pipeline_events,
        "wiki_page_events": wiki_page_events,
        "deployment_events": deployment_events,
        "releases_events": releases_events,
        "subgroup_events": subgroup_events,
        "member_events": member_events,
        "enable_ssl_verification": enable_ssl_verification,
        "resource_access_token_events": resource_access_token_events
    }
    
    if token:
        payload["token"] = token
        
    if push_events_branch_filter:
        payload["push_events_branch_filter"] = push_events_branch_filter
        
    if custom_webhook_template:
        payload["custom_webhook_template"] = custom_webhook_template
    
    response = requests.post(url, headers=headers, json=payload)
    return response

if __name__ == '__main__':
    r = add_group_webhook(
        group_id="183", 
        webhook_url="https://example.com/webhook", 
        token="secret_token",
        push_events=True,
        issues_events=True,
        merge_requests_events=True
    )
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