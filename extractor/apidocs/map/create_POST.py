import requests

def create_gpx(file_path, description, tags="", visibility="private"):
    """
    Upload a GPX file to OpenStreetMap.
    
    Parameters:
    -----------
    file_path : str
        Path to the GPX file to upload. The file must contain trackpoints with valid timestamps.
        The file may also be a .tar, .tar.gz or .zip containing multiple GPX files.
    
    description : str
        A description for the GPX trace. Cannot be empty.
    
    tags : str, optional
        A string containing tags for the trace, separated by spaces or commas.
        Default is an empty string.
    
    visibility : str, optional
        The visibility level of the GPX trace. Must be one of:
        - 'private': Only visible to you
        - 'public': Visible to everyone but anonymized
        - 'trackable': Visible to everyone with timestamps
        - 'identifiable': Visible to everyone with your username
        Default is 'private'.
    
    Returns:
    --------
    int
        The ID of the newly created GPX trace.
    
    Example:
    --------
    >>> create_gpx('/path/to/my_track.gpx', 'My hiking trip', 'hiking mountain vacation', 'public')
    12345
    """
    api_url = "https://api.openstreetmap.org/api/0.6/gpx/create"
    
    # Validate visibility parameter
    valid_visibilities = ['private', 'public', 'trackable', 'identifiable']
    if visibility not in valid_visibilities:
        raise ValueError(f"Visibility must be one of {valid_visibilities}")
    
    # Validate description
    if not description:
        raise ValueError("Description cannot be empty")
    
    # Prepare the multipart form data
    files = {'file': open(file_path, 'rb')}
    data = {
        'description': description,
        'tags': tags,
        'visibility': visibility
    }
    
    # Make the request
    response = requests.post(
        url=api_url,
        files=files,
        data=data,
        timeout=50
    )
    
    # Check for errors
    response.raise_for_status()
    
    # Return the ID of the new GPX trace
    return int(response.text)