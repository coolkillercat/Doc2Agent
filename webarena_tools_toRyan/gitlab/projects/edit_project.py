import requests, json
from urllib.parse import quote



def edit_project(project_id: str, name: str = None, description: str = None, default_branch: str = None, visibility: str = None, topics: list = None, path: str = None, merge_method: str = None, ci_config_path: str = None, shared_runners_enabled: bool = None, public_jobs: bool = None, only_allow_merge_if_pipeline_succeeds: bool = None, only_allow_merge_if_all_discussions_are_resolved: bool = None, emails_enabled: bool = None, lfs_enabled: bool = None, request_access_enabled: bool = None, squash_option: str = None, remove_source_branch_after_merge: bool = None, service_desk_enabled: bool = None, auto_devops_enabled: bool = None, build_timeout: int = None, **kwargs):
    """
    Updates an existing GitLab project's configuration with specified parameters. Provides a flexible interface to modify project settings including visibility, CI/CD options, merge settings, and access controls.
    
    Args:
        project_id (str): The ID or URL-encoded path of the project to update
        name (str, optional): The name of the project
        description (str, optional): Short project description
        default_branch (str, optional): The default branch name
        visibility (str, optional): Project visibility level - 'private', 'internal', or 'public'
        topics (list, optional): The list of topics for the project
        path (str, optional): Custom repository name for the project
        merge_method (str, optional): Set the merge method used
        ci_config_path (str, optional): The path to CI configuration file
        shared_runners_enabled (bool, optional): Enable shared runners for this project
        public_jobs (bool, optional): If true, jobs can be viewed by non-project members
        only_allow_merge_if_pipeline_succeeds (bool, optional): Set whether merge requests can only be merged with successful jobs
        only_allow_merge_if_all_discussions_are_resolved (bool, optional): Set whether merge requests can only be merged when all discussions are resolved
        emails_enabled (bool, optional): Enable email notifications
        lfs_enabled (bool, optional): Enable LFS
        request_access_enabled (bool, optional): Allow users to request member access
        squash_option (str, optional): One of 'never', 'always', 'default_on', or 'default_off'
        remove_source_branch_after_merge (bool, optional): Enable 'Delete source branch' option by default for all new merge requests
        service_desk_enabled (bool, optional): Enable or disable Service Desk feature
        auto_devops_enabled (bool, optional): Enable Auto DevOps for this project
        build_timeout (int, optional): The maximum amount of time, in seconds, that a job can run
        **kwargs: Additional project parameters as specified in the API documentation
        
    Returns:
        Returns comprehensive project information including metadata, settings, access levels, CI/CD configuration, and repository details after updating a GitLab project."""
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/projects/{quote(str(project_id), safe='')}"
    
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    
    # Build payload with all provided parameters
    payload = {}
    
    # Add all non-None parameters to the payload
    if name is not None:
        payload['name'] = name
    if description is not None:
        payload['description'] = description
    if default_branch is not None:
        payload['default_branch'] = default_branch
    if visibility is not None:
        payload['visibility'] = visibility
    if topics is not None:
        payload['topics'] = topics
    if path is not None:
        payload['path'] = path
    if merge_method is not None:
        payload['merge_method'] = merge_method
    if ci_config_path is not None:
        payload['ci_config_path'] = ci_config_path
    if shared_runners_enabled is not None:
        payload['shared_runners_enabled'] = shared_runners_enabled
    if public_jobs is not None:
        payload['public_jobs'] = public_jobs
    if only_allow_merge_if_pipeline_succeeds is not None:
        payload['only_allow_merge_if_pipeline_succeeds'] = only_allow_merge_if_pipeline_succeeds
    if only_allow_merge_if_all_discussions_are_resolved is not None:
        payload['only_allow_merge_if_all_discussions_are_resolved'] = only_allow_merge_if_all_discussions_are_resolved
    if emails_enabled is not None:
        payload['emails_enabled'] = emails_enabled
    if lfs_enabled is not None:
        payload['lfs_enabled'] = lfs_enabled
    if request_access_enabled is not None:
        payload['request_access_enabled'] = request_access_enabled
    if squash_option is not None:
        payload['squash_option'] = squash_option
    if remove_source_branch_after_merge is not None:
        payload['remove_source_branch_after_merge'] = remove_source_branch_after_merge
    if service_desk_enabled is not None:
        payload['service_desk_enabled'] = service_desk_enabled
    if auto_devops_enabled is not None:
        payload['auto_devops_enabled'] = auto_devops_enabled
    if build_timeout is not None:
        payload['build_timeout'] = build_timeout
    
    # Add any additional parameters
    payload.update(kwargs)
    
    response = requests.put(url, headers=headers, json=payload)
    return response

if __name__ == '__main__':
    r = edit_project(project_id=183, name="Updated Project", description="This is an updated project description", visibility="private", shared_runners_enabled=True)
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