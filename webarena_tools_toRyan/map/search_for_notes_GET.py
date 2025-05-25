def search_for_notes(q=None, limit=100, closed=7, display_name=None, user=None, bbox=None, from_date=None, to_date=None, sort='updated_at', order='newest'):
    """
    Search for notes in the OpenStreetMap database.
    
    Parameters:
    -----------
    q : str, optional
        Text search query, matching either note text or comments.
    limit : int, optional
        Maximum number of results (between 1 and 10000). Default is 100.
    closed : int, optional
        Maximum number of days a note has been closed for. 
        0 returns only open notes, negative numbers return all notes. Default is 7.
    display_name : str, optional
        Search for notes which the given user interacted with (by display name).
    user : int, optional
        Search for notes which the given user interacted with (by user ID).
        When both display_name and user are provided, display_name takes priority.
    bbox : str, optional
        Search area as a comma-separated string "min_lon,min_lat,max_lon,max_lat".
        Area must be at most 25 square degrees.
    from_date : str, optional
        Beginning date range for created_at or updated_at (specified by sort).
        Preferably in ISO 8601 format.
    to_date : str, optional
        End date range for created_at or updated_at (specified by sort).
        Only works when from_date is supplied. Preferably in ISO 8601 format.
    sort : str, optional
        Sort results by creation or update date ('created_at' or 'updated_at').
        Default is 'updated_at'.
    order : str, optional
        Sorting order. 'oldest' is ascending, 'newest' is descending.
        Default is 'newest'.
        
    Returns:
    --------
    requests.Response
        The API response object.
        
    Examples:
    ---------
    # Search for business spam notes
    search_for_notes(q="business spam", limit=20)
    
    # Find oldest open notes near Null Island
    search_for_notes(bbox="-1,-1,1,1", sort="created_at", order="oldest", closed=0)
    
    # Get notes from a specific user in a date range
    search_for_notes(user=123, from_date="2023-01-01", to_date="2023-12-31")
    """
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:3000/api/0.6/notes/search"
    querystring = {
        'q': q, 
        'limit': limit, 
        'closed': closed, 
        'display_name': display_name, 
        'user': user, 
        'bbox': bbox, 
        'from': from_date, 
        'to': to_date, 
        'sort': sort, 
        'order': order
    }
    
    # Remove None values
    querystring = {k: v for k, v in querystring.items() if v is not None}
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50)  # in case API can't handle redundant params
        response = response2
    return response

if __name__ == '__main__':
    import requests
    import json
    
    r = search_for_notes(q='business spam', limit=20, closed=0, display_name='JohnDoe', user=123, 
                        bbox='-1,-1,1,1', from_date='2023-01-01', to_date='2023-12-31', 
                        sort='created_at', order='oldest')
    
    r_json = None
    try:
        r_json = r.json()
    except:
        pass
    
    result_dict = dict()
    result_dict['status_code'] = r.status_code
    result_dict['text'] = r.text
    result_dict['json'] = r_json
    result_dict['content'] = r.content.decode("utf-8")
    print(json.dumps(result_dict, indent=4))