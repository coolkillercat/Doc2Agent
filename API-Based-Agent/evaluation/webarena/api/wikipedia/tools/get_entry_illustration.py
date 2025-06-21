import requests, json
from urllib.parse import quote

def get_entry_illustration(zim_id: str, size: int = 48) -> bytes:
    """
    Retrieves the illustration/cover image of specified size for a ZIM file identified by its UUID.
    
    This function calls the Kiwix server API to get the illustration image for a ZIM file.
    The image is returned as binary data that can be saved to a file or displayed.
    
    Args:
        zim_id (str): The UUID of the ZIM file
        size (int, optional): The size in pixels for the illustration. Defaults to 48.
                             Common sizes are 48, 96, 320 pixels.
    
    Returns:
        bytes: The binary data of the illustration image
    
    Example:
        >>> image_data = get_entry_illustration(zim_id="3d39ae65-9763-43af-ac74-38d33553efe0", size=48)
        >>> with open("illustration.jpg", "wb") as f:
        ...     f.write(image_data)
    """
    headers = {}
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8888"
    
    # Construct the URL with the size parameter
    url = f"{base_url}/catalog/v2/illustration/{zim_id}?size={size}"
    
    # Try with the requested size
    response = requests.get(url, headers=headers)
    
    # If the requested size is not available, try with common fallback sizes
    if response.status_code == 404:
        fallback_sizes = [48, 96, 320]
        for fallback_size in fallback_sizes:
            if fallback_size != size:  # Skip if it's the same as the requested size
                fallback_url = f"{base_url}/catalog/v2/illustration/{zim_id}?size={fallback_size}"
                fallback_response = requests.get(fallback_url, headers=headers)
                if fallback_response.status_code == 200:
                    return fallback_response.content
    
    # If we got a successful response with the original size, return it
    if response.status_code == 200:
        return response.content
        
    # If all attempts failed, raise the error
    response.raise_for_status()
    return response.content

if __name__ == '__main__':
    r = get_entry_illustration(zim_id="3d39ae65-9763-43af-ac74-38d33553efe0", size=48)
    r_json = None
    try:
        r_json = r.json()
    except:
        pass
    import json
    result_dict = dict()
    result_dict['status_code'] = 200
    result_dict['text'] = "Binary image data"
    result_dict['json'] = r_json
    result_dict['content'] = "Binary image data"
    print(json.dumps(result_dict, indent=4))