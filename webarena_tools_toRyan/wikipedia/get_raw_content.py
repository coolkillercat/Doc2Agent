import requests, json
from urllib.parse import quote

def get_raw_content(zim_name: str, path: str) -> bytes:
    """
    Retrieves raw content from a ZIM file without any server-side processing, ensuring original data is preserved.
    
    Parameters:
        zim_name (str): The name of the ZIM file to retrieve content from
        path (str): The path to the content within the ZIM file
    
    Returns:
        bytes: The raw content from the specified ZIM file path
        
    Example:
        >>> content = get_raw_content("wikipedia_en_all_maxi", "/A/Abraham_Lincoln")
        >>> print(len(content))
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8888"
    
    # Ensure path doesn't start with a slash when used in the URL
    if path.startswith('/'):
        clean_path = path[1:]
    else:
        clean_path = path
    
    url = f"{base_url}/raw/{quote(zim_name)}/content/{clean_path}"
    
    response = requests.get(url)
    response.raise_for_status()
    return response.content

if __name__ == '__main__':
    r = get_raw_content(zim_name="wikipedia_en_all_maxi", path="/A/Abraham_Lincoln") 
    r_json = None
    try:
        r_json = json.loads(r)
    except:
        pass
    import json
    result_dict = dict()
    result_dict['status_code'] = 200
    result_dict['text'] = r.decode("utf-8")
    result_dict['json'] = r_json
    result_dict['content'] = r.decode("utf-8")
    print(json.dumps(result_dict, indent=4))