import requests
from urllib.parse import quote

def general_request(profile=None, service=None, coordinates=None, format="json", option=None):
    """
    Make a request to the OSRM HTTP Router API.
    
    Parameters:
    -----------
    profile : str
        Mode of transportation. One of the following three values: 
        '5000' for car (driving), '5001' for bicycle (biking), and '5002' for foot (walking).
    service : str
        One of the following values: 'route', 'nearest', 'table', 'match', 'trip', 'tile'.
    coordinates : str
        String of format '{longitude},{latitude};{longitude},{latitude}[;{longitude},{latitude} ...]' 
        or 'polyline({polyline})' or 'polyline6({polyline6})'.
    format : str, optional
        'json' or 'flatbuffers'. Defaults to 'json'.
    option : str or dict, optional
        Additional options to pass to the API. Can be a string like 'overview=false' 
        or a dictionary of options.
    
    Returns:
    --------
    requests.Response
        The response from the API.
    
    Examples:
    ---------
    >>> # Get a route between two points
    >>> response = general_request(profile='5000', service='route', coordinates='13.388860,52.517037;13.397634,52.529407')
    >>> 
    >>> # Get a route with specific options
    >>> response = general_request(profile='5000', service='route', coordinates='13.388860,52.517037;13.397634,52.529407', option='overview=false')
    """
    assert profile is not None, 'Missing required parameter: profile'
    assert service is not None, 'Missing required parameter: service'
    assert coordinates is not None, 'Missing required parameter: coordinates'
    
    base_url = f"http://router.project-osrm.org/{service}/v1/test/{coordinates}"
    
    if format:
        base_url += f".{format}"
    
    params = {}
    if isinstance(option, dict):
        params.update(option)
    elif option:
        # Parse option string into dictionary
        option_pairs = option.split('&')
        for pair in option_pairs:
            if '=' in pair:
                key, value = pair.split('=', 1)
                params[key] = value
    
    response = requests.get(url=base_url, params=params, timeout=50)
    return response

if __name__ == '__main__':
    r = general_request(profile='5000', service='route', coordinates='13.388860,52.517037;13.397634,52.529407', option='overview=false')
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
