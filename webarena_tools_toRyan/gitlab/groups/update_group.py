import requests, json
from urllib.parse import quote

def update_group(group_id: int, name: str = None, path: str = None, description: str = None, visibility: str = None, auto_devops_enabled: bool = None, default_branch: str = None, project_creation_level: str = None, subgroup_creation_level: str = None, require_two_factor_authentication: bool = None, two_factor_grace_period: int = None, request_access_enabled: bool = None, lfs_enabled: bool = None, emails_enabled: bool = None, mentions_disabled: bool = None, shared_runners_setting: str = None, prevent_sharing_groups_outside_hierarchy: bool = None, share_with_group_lock: bool = None, enabled_git_access_protocol: str = None, unique_project_download_limit: int = None, unique_project_download_limit_interval_in_seconds: int = None, unique_project_download_limit_allowlist: list = None, unique_project_download_limit_alertlist: list = None, auto_ban_user_on_excessive_projects_download: bool = None, ip_restriction_ranges: str = None, wiki_access_level: str = None, duo_features_enabled: bool = None, lock_duo_features_enabled: bool = None, math_rendering_limits_enabled: bool = None, lock_math_rendering_limits_enabled: bool = None):
    """
    Updates the settings and configuration of a GitLab group.
    
    Args:
        group_id (int): The ID of the group to update
        name (str, optional): The name of the group
        path (str, optional): The path of the group
        description (str, optional): The description of the group
        visibility (str, optional): The visibility level of the group. Can be 'private', 'internal', or 'public'
        auto_devops_enabled (bool, optional): Default to Auto DevOps pipeline for all projects within this group
        default_branch (str, optional): The default branch name for group's projects
        project_creation_level (str, optional): Determine if developers can create projects in the group. Can be 'noone', 'maintainer', or 'developer'
        subgroup_creation_level (str, optional): Allowed to create subgroups. Can be 'owner' or 'maintainer'
        require_two_factor_authentication (bool, optional): Require all users in this group to set up two-factor authentication
        two_factor_grace_period (int, optional): Time before Two-factor authentication is enforced (in hours)
        request_access_enabled (bool, optional): Allow users to request member access
        lfs_enabled (bool, optional): Enable/disable Large File Storage (LFS) for the projects in this group
        emails_enabled (bool, optional): Enable email notifications
        mentions_disabled (bool, optional): Disable the capability of a group from getting mentioned
        shared_runners_setting (str, optional): Enable or disable shared runners for a group's subgroups and projects
        prevent_sharing_groups_outside_hierarchy (bool, optional): Prevent group sharing outside the group hierarchy
        share_with_group_lock (bool, optional): Prevent sharing a project with another group within this group
        enabled_git_access_protocol (str, optional): Enabled protocols for Git access. Can be 'ssh', 'http', or 'all'
        unique_project_download_limit (int, optional): Maximum number of unique projects a user can download
        unique_project_download_limit_interval_in_seconds (int, optional): Time period for the download limit
        unique_project_download_limit_allowlist (list, optional): List of usernames excluded from the unique project download limit
        unique_project_download_limit_alertlist (list, optional): List of user IDs that are emailed when the unique project download limit is exceeded
        auto_ban_user_on_excessive_projects_download (bool, optional): Automatically ban users who exceed download limits
        ip_restriction_ranges (str, optional): Comma-separated list of IP addresses or subnet masks to restrict group access
        wiki_access_level (str, optional): The wiki access level. Can be 'disabled', 'private', or 'enabled'
        duo_features_enabled (bool, optional): Indicates whether GitLab Duo features are enabled for this group
        lock_duo_features_enabled (bool, optional): Indicates whether the GitLab Duo features enabled setting is enforced for all subgroups
        math_rendering_limits_enabled (bool, optional): Indicates if math rendering limits are used for this group
        lock_math_rendering_limits_enabled (bool, optional): Indicates if math rendering limits are locked for all descendent groups
        
    Returns:
        requests.Response: The API response
        
    Example:
        >>> update_group(5, name="Experimental", visibility="internal", description="Research group")
        >>> update_group(10, project_creation_level="developer", lfs_enabled=True)
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/groups/{group_id}"
    
    payload = {}
    
    # Add all non-None parameters to the payload
    if name is not None:
        payload['name'] = name
    if path is not None:
        payload['path'] = path
    if description is not None:
        payload['description'] = description
    if visibility is not None:
        payload['visibility'] = visibility
    if auto_devops_enabled is not None:
        payload['auto_devops_enabled'] = auto_devops_enabled
    if default_branch is not None:
        payload['default_branch'] = default_branch
    if project_creation_level is not None:
        payload['project_creation_level'] = project_creation_level
    if subgroup_creation_level is not None:
        payload['subgroup_creation_level'] = subgroup_creation_level
    if require_two_factor_authentication is not None:
        payload['require_two_factor_authentication'] = require_two_factor_authentication
    if two_factor_grace_period is not None:
        payload['two_factor_grace_period'] = two_factor_grace_period
    if request_access_enabled is not None:
        payload['request_access_enabled'] = request_access_enabled
    if lfs_enabled is not None:
        payload['lfs_enabled'] = lfs_enabled
    if emails_enabled is not None:
        payload['emails_enabled'] = emails_enabled
    if mentions_disabled is not None:
        payload['mentions_disabled'] = mentions_disabled
    if shared_runners_setting is not None:
        payload['shared_runners_setting'] = shared_runners_setting
    if prevent_sharing_groups_outside_hierarchy is not None:
        payload['prevent_sharing_groups_outside_hierarchy'] = prevent_sharing_groups_outside_hierarchy
    if share_with_group_lock is not None:
        payload['share_with_group_lock'] = share_with_group_lock
    if enabled_git_access_protocol is not None:
        payload['enabled_git_access_protocol'] = enabled_git_access_protocol
    if unique_project_download_limit is not None:
        payload['unique_project_download_limit'] = unique_project_download_limit
    if unique_project_download_limit_interval_in_seconds is not None:
        payload['unique_project_download_limit_interval_in_seconds'] = unique_project_download_limit_interval_in_seconds
    if unique_project_download_limit_allowlist is not None:
        payload['unique_project_download_limit_allowlist'] = unique_project_download_limit_allowlist
    if unique_project_download_limit_alertlist is not None:
        payload['unique_project_download_limit_alertlist'] = unique_project_download_limit_alertlist
    if auto_ban_user_on_excessive_projects_download is not None:
        payload['auto_ban_user_on_excessive_projects_download'] = auto_ban_user_on_excessive_projects_download
    if ip_restriction_ranges is not None:
        payload['ip_restriction_ranges'] = ip_restriction_ranges
    if wiki_access_level is not None:
        payload['wiki_access_level'] = wiki_access_level
    if duo_features_enabled is not None:
        payload['duo_features_enabled'] = duo_features_enabled
    if lock_duo_features_enabled is not None:
        payload['lock_duo_features_enabled'] = lock_duo_features_enabled
    if math_rendering_limits_enabled is not None:
        payload['math_rendering_limits_enabled'] = math_rendering_limits_enabled
    if lock_math_rendering_limits_enabled is not None:
        payload['lock_math_rendering_limits_enabled'] = lock_math_rendering_limits_enabled
    
    response = requests.put(url, headers=headers, json=payload)
    return response

if __name__ == '__main__':
    r = update_group(group_id=183, name="Updated Group Name", description="This is an updated description", visibility="private")
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