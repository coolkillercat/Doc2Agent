import requests, json
from urllib.parse import quote

def update_group_push_rules(group_id: str, deny_delete_tag: bool = None, member_check: bool = None, prevent_secrets: bool = None, commit_committer_name_check: bool = None, commit_message_regex: str = None, commit_message_negative_regex: str = None, branch_name_regex: str = None, author_email_regex: str = None, file_name_regex: str = None, max_file_size: int = None, commit_committer_check: bool = None, reject_unsigned_commits: bool = None):
    """
    Configures or modifies push rules for a GitLab group to enforce code quality and security standards.
    
    Args:
        group_id (str): The ID or URL-encoded path of the group
        deny_delete_tag (bool, optional): Deny deleting a tag
        member_check (bool, optional): Allows only GitLab users to author commits
        prevent_secrets (bool, optional): Reject files that are likely to contain secrets
        commit_committer_name_check (bool, optional): Require commit author name to match GitLab account name
        commit_message_regex (str, optional): Regular expression that commit messages must match
        commit_message_negative_regex (str, optional): Regular expression that commit messages must not match
        branch_name_regex (str, optional): Regular expression that branch names must match
        author_email_regex (str, optional): Regular expression that commit author emails must match
        file_name_regex (str, optional): Regular expression for filenames that are not allowed
        max_file_size (int, optional): Maximum file size (MB) allowed
        commit_committer_check (bool, optional): Only allow commits pushed using verified emails
        reject_unsigned_commits (bool, optional): Only allow signed commits
    
    Returns:
        requests.Response: The response from the API
        
    Example:
        >>> update_group_push_rules(
        ...     group_id="183", 
        ...     deny_delete_tag=True,
        ...     prevent_secrets=True, 
        ...     commit_message_regex="^(feat|fix|docs|style|refactor|test|chore):\\s.+",
        ...     max_file_size=50
        ... )
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/groups/{quote(str(group_id), safe='')}/push_rule"
    
    data = {}
    if deny_delete_tag is not None:
        data['deny_delete_tag'] = deny_delete_tag
    if member_check is not None:
        data['member_check'] = member_check
    if prevent_secrets is not None:
        data['prevent_secrets'] = prevent_secrets
    if commit_committer_name_check is not None:
        data['commit_committer_name_check'] = commit_committer_name_check
    if commit_message_regex is not None:
        data['commit_message_regex'] = commit_message_regex
    if commit_message_negative_regex is not None:
        data['commit_message_negative_regex'] = commit_message_negative_regex
    if branch_name_regex is not None:
        data['branch_name_regex'] = branch_name_regex
    if author_email_regex is not None:
        data['author_email_regex'] = author_email_regex
    if file_name_regex is not None:
        data['file_name_regex'] = file_name_regex
    if max_file_size is not None:
        data['max_file_size'] = max_file_size
    if commit_committer_check is not None:
        data['commit_committer_check'] = commit_committer_check
    if reject_unsigned_commits is not None:
        data['reject_unsigned_commits'] = reject_unsigned_commits
    
    response = requests.put(url, headers=headers, json=data)
    return response

if __name__ == '__main__':
    r = update_group_push_rules(
        group_id="183", 
        deny_delete_tag=True,
        prevent_secrets=True, 
        commit_message_regex="^(feat|fix|docs|style|refactor|test|chore):\\s.+",
        max_file_size=50
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