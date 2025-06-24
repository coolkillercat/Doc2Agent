import requests
from urllib.parse import quote

def get_content(zim_name: str, path: str = '') -> requests.Response:
    """
    Retrieves specific content from a ZIM file.
    
    Args:
        zim_name (str): The name of the ZIM file to retrieve content from.
        path (str, optional): The path to the content within the ZIM file. 
                              If empty, returns the main page of the ZIM file.
    
    Returns:
        requests.Response: The response object containing the content retrieved from the ZIM file.
    
    Examples:
        >>> response = get_content("wikipedia_en_top", "A/Albert_Einstein.html")
        >>> response = get_content("wikipedia_en_top")  # Get main page
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8888"
    
    # Build the URL based on whether a path is provided
    if path:
        # Ensure path is properly URL encoded
        encoded_path = quote(path)
        url = f"{base_url}/content/{zim_name}/{encoded_path}"
    else:
        url = f"{base_url}/content/{zim_name}"
    
    response = requests.get(url)
    return response

if __name__ == '__main__':
    r = get_content(zim_name="wikipedia_en_top", path="A/Albert_Einstein.html")
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