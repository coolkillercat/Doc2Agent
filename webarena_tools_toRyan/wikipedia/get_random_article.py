import requests
from urllib.parse import quote

def get_random_article(zim_name: str) -> requests.Response:
    """
    Retrieves a randomly selected article from the specified ZIM file, useful for exploration features.
    
    This function uses the Kiwix server's /random endpoint to get a random article from a ZIM file.
    The server will respond with a redirect to the random article, which this function returns
    without following the redirect.
    
    Args:
        zim_name (str): The name of the ZIM file to retrieve a random article from
                        (e.g., "wikipedia_en_all_maxi")
    
    Returns:
        requests.Response: The HTTP response object containing the redirect to a random article
        
    Example:
        >>> response = get_random_article("wikipedia_en_all_maxi")
        >>> print(response.status_code)  # Should be 302 (redirect)
        >>> print(response.headers.get('Location'))  # The URL of the random article
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8888"
    url = f"{base_url}/random?content={quote(zim_name)}"
    
    response = requests.get(url, allow_redirects=False)
    return response

if __name__ == '__main__':
    r = get_random_article(zim_name="wikipedia_en_all_maxi")
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