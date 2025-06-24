import requests, json
from urllib.parse import quote

def get_metadata(zim_name: str, metadata_id: str, base_url: str = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8888") -> requests.Response:
    """
    Retrieves a specific metadata item from a ZIM file, providing access to embedded metadata information.
    
    This function uses the /raw/{zim_name}/meta/{metadata_id} endpoint to fetch metadata from a ZIM file.
    
    Args:
        zim_name (str): The name of the ZIM file (without file extension)
        metadata_id (str): The ID of the metadata item to retrieve (e.g., 'title', 'description', 'language')
        base_url (str, optional): The base URL of the Kiwix server
        
    Returns:
        requests.Response: The HTTP response containing the requested metadata
        
    Example:
        >>> response = get_metadata("wikipedia_en_100", "title")
        >>> print(response.text)
        Wikipedia
    """
    headers = {}
    url = f"{base_url}/raw/{quote(zim_name)}/meta/{quote(metadata_id)}"
    response = requests.get(url, headers=headers)
    return response

if __name__ == '__main__':
    r = get_metadata(zim_name="wikipedia_en_100", metadata_id="title")
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