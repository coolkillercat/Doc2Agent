import requests, json
from urllib.parse import quote


def list_repository_commits(project_id: str, ref_name: str = None, since: str = None, until: str = None, path: str = None, author: str = None, all: bool = None, with_stats: bool = None, first_parent: bool = None, order: str = None, trailers: bool = None):
    """
    Retrieves a list of commits from a project repository with filtering options for time period, author, path, and display preferences. Useful for analyzing project history, tracking changes, and auditing contributions.
    
    Args:
        project_id (str): The ID or URL-encoded path of the project owned by the authenticated user
        ref_name (str, optional): The name of a repository branch, tag or revision range
        since (str, optional): Only commits after or on this date in ISO 8601 format YYYY-MM-DDTHH:MM:SSZ
        until (str, optional): Only commits before or on this date in ISO 8601 format YYYY-MM-DDTHH:MM:SSZ
        path (str, optional): The file path
        author (str, optional): Search commits by commit author
        all (bool, optional): Retrieve every commit from the repository
        with_stats (bool, optional): Stats about each commit are added to the response
        first_parent (bool, optional): Follow only the first parent commit upon seeing a merge commit
        order (str, optional): List commits in order. Possible values: default, topo
        trailers (bool, optional): Parse and include Git trailers for every commit
        
    Returns:
        Returns a list of repository commits with details including commit metadata, author information, timestamps, and optionally commit statistics."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    url = f"{base_url}/projects/{quote(str(project_id), safe='')}/repository/commits"
    
    params = {}
    if ref_name is not None:
        params['ref_name'] = ref_name
    if since is not None:
        params['since'] = since
    if until is not None:
        params['until'] = until
    if path is not None:
        params['path'] = path
    if author is not None:
        params['author'] = author
    if all is not None:
        params['all'] = all
    if with_stats is not None:
        params['with_stats'] = with_stats
    if first_parent is not None:
        params['first_parent'] = first_parent
    if order is not None:
        params['order'] = order
    if trailers is not None:
        params['trailers'] = trailers
        
    response = requests.get(url, headers=headers, params=params)
    return response


if __name__ == '__main__':
    r = list_repository_commits(project_id=183, with_stats=True, trailers=True)
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