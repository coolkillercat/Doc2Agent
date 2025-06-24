import requests

def table_service(coordinates=None, sources='all', destinations='all', annotations='duration', profile=5000, fallback_speed=None, fallback_coordinate=None, scale_factor=None):
    """
    Computes the duration or distance of the fastest route between all pairs of supplied coordinates.
    
    Parameters:
    -----------
    coordinates : str
        String of format '{longitude},{latitude};{longitude},{latitude}[;{longitude},{latitude} ...]'
        Example: '13.388860,52.517037;13.397634,52.529407;13.428555,52.523219'
    
    sources : str, default 'all'
        Use location with given indices as sources. Format: '{index};{index}[;{index} ...]' or 'all'
        Example: '0;1;2' or 'all'
    
    destinations : str, default 'all'
        Use location with given indices as destinations. Format: '{index};{index}[;{index} ...]' or 'all'
        Example: '0;1;2' or 'all'
    
    annotations : str, default 'duration'
        Return the requested table or tables in response. Options: 'duration', 'distance', or 'duration,distance'
    
    profile : int, default 5000
        Mode of transportation. 5000 for car (driving), 5001 for bicycle (biking), and 5002 for foot (walking).
    
    fallback_speed : float, optional
        If no route found between a source/destination pair, calculate the as-the-crow-flies distance, 
        then use this speed to estimate duration.
    
    fallback_coordinate : str, optional
        When using a fallback_speed, use the user-supplied coordinate ('input'), 
        or the snapped location ('snapped') for calculating distances. Default is 'input'.
    
    scale_factor : float, optional
        Use in conjunction with annotations=durations. Scales the table duration values by this number.
    
    Returns:
    --------
    response : requests.Response
        The HTTP response from the OSRM API
    
    Examples:
    ---------
    >>> table_service(coordinates='13.388860,52.517037;13.397634,52.529407;13.428555,52.523219')
    >>> table_service(coordinates='13.388860,52.517037;13.397634,52.529407;13.428555,52.523219', 
                      sources='0;1', destinations='1;2', annotations='distance')
    >>> table_service(coordinates='13.388860,52.517037;13.397634,52.529407;13.428555,52.523219',
                      fallback_speed=5.5, fallback_coordinate='snapped')
    """
    assert coordinates is not None, 'Missing required parameter: coordinates'
    
    base_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:{profile}/table/v1/test/{coordinates}"
    
    params = {}
    if sources != 'all':
        params['sources'] = sources
    if destinations != 'all':
        params['destinations'] = destinations
    if annotations:
        params['annotations'] = annotations
    if fallback_speed is not None:
        params['fallback_speed'] = fallback_speed
    if fallback_coordinate is not None:
        params['fallback_coordinate'] = fallback_coordinate
    if scale_factor is not None:
        params['scale_factor'] = scale_factor
    
    response = requests.get(url=base_url, params=params, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = table_service(coordinates='13.388860,52.517037;13.397634,52.529407;13.428555,52.523219')
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