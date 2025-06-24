import requests
from urllib.parse import quote

def nearest_service(coordinates=None, number=1, profile=5000):
    """
    Finds the nearest street segments for a given coordinate.
    
    Args:
        coordinates (str): A string of format '{longitude},{latitude}'. Required.
        number (int, optional): Number of nearest segments that should be returned. Defaults to 1.
        profile (int, optional): Mode of transportation. 5000 for car, 5001 for bicycle, 5002 for foot. Defaults to 5000.
    
    Returns:
        requests.Response: The response from the OSRM nearest service API.
    
    Example:
        >>> nearest_service(coordinates='13.388860,52.517037', number=3)
        >>> nearest_service(coordinates='13.388860,52.517037', number=1, profile=5001)
    """
    assert coordinates is not None, 'Missing required parameter: coordinates'
    
    # Format the URL correctly
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:{profile}/nearest/v1/test/{quote(coordinates, safe='')}"
    
    # Add query parameters
    params = {'number': number}
    
    response = requests.get(url=api_url, params=params, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = nearest_service(coordinates='13.388860,52.517037', number=3)
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