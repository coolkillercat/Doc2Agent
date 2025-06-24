import requests, json
from urllib.parse import quote

def get_suggestions(zim_name: str, term: str = '', count: int = 10, start: int = 0) -> requests.Response:
    """
    Retrieves title suggestions for partially typed search queries against a specific ZIM file, supporting autocomplete functionality.
    
    The function uses the Kiwix server's /suggest endpoint to get suggestions for a text string that is assumed to be a
    partially typed search for a page inside a particular ZIM file.
    
    Args:
        zim_name (str): Name of the ZIM file to search in (e.g., "stackoverflow_en")
        term (str, optional): Query text for which suggestions are needed. Defaults to empty string.
        count (int, optional): Maximum number of page suggestions to return. Defaults to 10.
        start (int, optional): Starting index for pagination of results. Defaults to 0.
    
    Returns:
        requests.Response: Response object containing suggestions in JSON format
        
    Example:
        >>> response = get_suggestions(zim_name="stackoverflow_en", term="pyth", count=5)
        >>> suggestions = response.json()
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8888"
    url = f"{base_url}/suggest"
    
    params = {
        "content": zim_name,
        "term": term,
        "count": count,
        "start": start
    }
    
    response = requests.get(url, params=params)
    return response

if __name__ == '__main__':
    r = get_suggestions(zim_name="stackoverflow_en", term="pyth", count=5, start=0)
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