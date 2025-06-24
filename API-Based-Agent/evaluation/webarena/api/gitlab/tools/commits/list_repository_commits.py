import requests, json
from urllib.parse import quote



def list_repository_commits(project_id: str, ref_name: str = None, since: str = None, until: str = None, path: str = None, author: str = None, all: bool = None, with_stats: bool = False, first_parent: bool = False, order: str = 'default', trailers: bool = False, page: int = 1, per_page: int = 100):
    """
    Retrieves a list of commits from a project repository with filtering options like date range, author, and path, allowing users to track code changes over time.
    
    Args:
        project_id (str): The ID or URL-encoded path of the project.
        ref_name (str, optional): The name of a repository branch, tag or revision range.
        since (str, optional): Only commits after or on this date (ISO 8601 format).
        until (str, optional): Only commits before or on this date (ISO 8601 format).
        path (str, optional): The file path to filter commits by.
        author (str, optional): Search commits by commit author.
        all (bool, optional): Retrieve every commit from the repository.
        with_stats (bool, optional): Include stats about each commit in the response.
        first_parent (bool, optional): Follow only the first parent commit upon seeing a merge commit.
        order (str, optional): List commits in order ('default' or 'topo'). Default is 'default'.
        trailers (bool, optional): Parse and include Git trailers for every commit.
        page (int, optional): Page number for pagination. Default is 1.
        per_page (int, optional): Number of items per page. Default is 20, max is 100.
    
    Returns:
        Returns a list of repository commits with details including commit ID, author information, timestamps, commit messages, and web URLs."""
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    
    # Construct the URL
    url = f"{base_url}/projects/{quote(str(project_id), safe='')}/repository/commits"
    
    # Prepare parameters
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
    if with_stats:
        params['with_stats'] = with_stats
    if first_parent:
        params['first_parent'] = first_parent
    if order != 'default':
        params['order'] = order
    if trailers:
        params['trailers'] = trailers
    
    # Add pagination parameters
    params['page'] = page
    params['per_page'] = per_page
    
    # Make the request
    response = requests.get(url, headers=headers, params=params)
    
    return response

if __name__ == '__main__':
    r = list_repository_commits(project_id=183, per_page=10)
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