import requests

def table_service(coordinates=None, sources=None, destinations=None, annotations=None):
    """
    Computes the duration of the fastest route between all pairs of supplied coordinates.
    
    Args:
        coordinates (str): String of format `{longitude},{latitude};{longitude},{latitude}[;{longitude},{latitude} ...]`.
            Example: "13.388860,52.517037;13.397634,52.529407;13.428555,52.523219"
        sources (str, optional): Use location with given index as source. Format: "{index};{index}[;{index} ...]" or "all".
            Example: "0;1;2"
        destinations (str, optional): Use location with given index as destination. Format: "{index};{index}[;{index} ...]" or "all".
            Example: "0;1;2"
        annotations (str, optional): Return the requested table or tables in response. Options: "duration" (default), "distance", or "duration,distance".
            Example: "duration,distance"
    
    Returns:
        requests.Response: The response from the OSRM API.
    
    Example:
        >>> table_service(
        ...     coordinates="13.388860,52.517037;13.397634,52.529407;13.428555,52.523219",
        ...     sources="0;1;2",
        ...     destinations="0;1;2",
        ...     annotations="duration,distance"
        ... )
    """
    assert coordinates is not None, 'Missing required parameter: coordinates'
    
    base_url = "http://router.project-osrm.org/table/v1/test/"
    url = f"{base_url}{coordinates}"
    
    params = {}
    if sources is not None:
        params['sources'] = sources
    if destinations is not None:
        params['destinations'] = destinations
    if annotations is not None:
        params['annotations'] = annotations

    # Make the request
    response = requests.get(url=url, params=params, timeout=50)
    return response

if __name__ == '__main__':
    r = table_service(
        coordinates='13.388860,52.517037;13.397634,52.529407;13.428555,52.523219',
        sources='0;1;2',
        destinations='0;1;2',
        annotations='duration,distance'
    )
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