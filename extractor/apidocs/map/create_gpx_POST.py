import requests
from urllib.parse import quote

def create_gpx(file=None, description=None, tags=None, public=None, visibility=None):
    """
    Upload a GPX file to OpenStreetMap.
    
    Parameters:
    -----------
    file : file object or path
        The GPX file containing the track points. The file must contain trackpoints 
        with valid timestamps. Can also be a .tar, .tar.gz or .zip containing multiple GPX files.
    description : str
        The trace description. Cannot be empty.
    tags : str, optional
        A string containing tags for the trace, comma separated.
    public : int, optional
        1 if the trace is public, 0 if not. This exists for backwards compatibility only.
        The visibility parameter should be used instead.
    visibility : str, optional
        One of: private, public, trackable, identifiable
        
    Returns:
    --------
    requests.Response
        The response from the API call.
    
    Example:
    --------
    >>> with open('track.gpx', 'rb') as f:
    >>>     response = create_gpx(file=f, description='Morning run', tags='run, morning', visibility='public')
    """
    api_url = "https://api.openstreetmap.org/api/0.6/gpx/create"
    
    assert file is not None, 'Missing required parameter: file'
    assert description is not None, 'Missing required parameter: description'
    
    # Create form data
    payload = {
        'description': description,
    }
    
    if tags is not None:
        payload['tags'] = tags
    
    if public is not None:
        payload['public'] = public
    
    if visibility is not None:
        payload['visibility'] = visibility
    
    # Handle file parameter
    files = {'file': file}
    
    response = requests.post(url=api_url, data=payload, files=files, timeout=50)
    return response

if __name__ == '__main__':
    # Example usage - replace 'track.gpx' with an actual file path
    with open('track.gpx', 'rb') as gpx_file:
        r = create_gpx(file=gpx_file, description='Morning run', tags='run, morning', public=1, visibility='public')
    
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