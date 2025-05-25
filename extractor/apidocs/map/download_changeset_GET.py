import requests, json
from urllib.parse import quote


def download_changeset(id=None):
    """
    Download a changeset from the OpenStreetMap API.
    
    This function retrieves the OsmChange document describing all changes associated with the specified changeset.
    
    Parameters:
    -----------
    id : int
        The ID of the changeset to download. This parameter is required.
        
    Returns:
    --------
    requests.Response
        The response object containing the OsmChange XML data.
        
    Examples:
    ---------
    >>> response = download_changeset(id=12345)
    >>> print(response.status_code)  # Should be 200 if successful
    >>> print(response.text)  # The OsmChange XML content
    """
    assert id is not None, 'Missing required parameter: id'
    
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:3000/api/0.6/changeset/{id}/download"
    
    response = requests.get(url=api_url, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = download_changeset(id=12345)
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