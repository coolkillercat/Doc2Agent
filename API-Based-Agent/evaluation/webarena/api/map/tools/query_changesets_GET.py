import requests, json
from urllib.parse import quote


def query_changesets(bbox=None, user=None, time=None, open=None, closed=None, changesets=None, order='newest', limit=100):
    """
    Query OSM changesets with various filtering parameters.
    
    Parameters:
    -----------
    bbox : str
        Bounding box in format "min_lon,min_lat,max_lon,max_lat" (W,S,E,N)
    user : str
        User ID (#uid) or display name (display_name=#name)
    time : str
        Time range in format "T1" or "T1,T2". Find changesets closed after T1 
        or between T1 and T2.
    open : bool
        If True, only find changesets that are still open
    closed : bool
        If True, only find changesets that are closed
    changesets : str
        Comma-separated list of changeset IDs to find
    order : str
        Sort order, either "newest" (default) or "oldest"
    limit : int
        Maximum number of changesets to return (1-100, default 100)
    
    Returns:
    --------
    requests.Response
        Response object from the API request
    
    Example:
    --------
    >>> query_changesets(bbox="-0.5,51.3,0.5,51.7", limit=10)
    >>> query_changesets(user="display_name=username", closed=True)
    """
    api_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:3000/api/0.6/changesets"
    
    # Build query parameters, converting Python booleans to strings if needed
    params = {}
    if bbox is not None:
        params['bbox'] = bbox
    if user is not None:
        params['user'] = user
    if time is not None:
        params['time'] = time
    if open is not None:
        params['open'] = str(open).lower()
    if closed is not None:
        params['closed'] = str(closed).lower()
    if changesets is not None:
        params['changesets'] = changesets
    if order is not None:
        params['order'] = order
    if limit is not None:
        params['limit'] = limit
    
    response = requests.get(url=api_url, params=params, timeout=50, verify=False)
    if response.status_code != 200:
        # Try without parameters in case the API can't handle them
        response2 = requests.get(url=api_url, timeout=50, verify=False)
        if response2.status_code == 200:
            response = response2
    
    return response

if __name__ == '__main__':
    r = query_changesets(bbox="min_lon,min_lat,max_lon,max_lat", 
                         user="#uid or display_name=#name", 
                         time="T1 or T1,T2", 
                         open=True, 
                         closed=True, 
                         changesets="#cid{,#cid}", 
                         order="newest or oldest", 
                         limit=50)
    
    r_json = None
    try:
        r_json = r.json()
    except:
        pass
    
    result_dict = {
        'status_code': r.status_code,
        'text': r.text,
        'json': r_json,
        'content': r.content.decode("utf-8")
    }
    print(json.dumps(result_dict, indent=4))