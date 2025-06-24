import requests, json
from urllib.parse import quote

def get_entry_details(zim_id: str) -> requests.Response:
    """
    Retrieves full metadata information about a specific ZIM file identified by its UUID.
    
    This function calls the Kiwix server's OPDS API endpoint to get detailed information
    about a ZIM file using its UUID.
    
    Args:
        zim_id (str): The UUID of the ZIM file to retrieve information for.
                      Example: "a107b4b6-09cd-53f0-beea-75a573d03da1"
        
    Returns:
        requests.Response: The HTTP response containing entry details in OPDS format
        
    Example:
        >>> response = get_entry_details("a107b4b6-09cd-53f0-beea-75a573d03da1")
        >>> print(response.status_code)
        200
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8888"
    endpoint = f"/catalog/v2/entry/{quote(zim_id)}"
    
    response = requests.get(f"{base_url}{endpoint}")
    return response

if __name__ == '__main__':
    r = get_entry_details(zim_id="a107b4b6-09cd-53f0-beea-75a573d03da1")
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