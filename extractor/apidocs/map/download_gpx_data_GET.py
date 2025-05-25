import requests, json
from urllib.parse import quote


def download_gpx_data(gpx_id=1):
    """
    Download GPX data from the OpenStreetMap API.
    
    This function retrieves GPX data for a specific GPX file ID from the OpenStreetMap API.
    
    Args:
        gpx_id (int): The ID of the GPX file to download. Defaults to 1.
        
    Returns:
        requests.Response: The response object containing the GPX data.
        
    Example:
        >>> response = download_gpx_data(836619)
        >>> print(response.status_code)
        200
    """
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:3000/api/0.6/gpx/{gpx_id}/data"
    
    response = requests.get(url=api_url, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = download_gpx_data()
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