import requests, json
from urllib.parse import quote

def get_library_entries(start: int = 0, count: int = 10, lang: str = None, category: str = None, 
                         tag: str = None, notag: str = None, maxsize: int = None, q: str = None, 
                         name: str = None) -> str:
    """
    Retrieves a complete list or filtered subset of ZIM files in the library as a paginated OPDS acquisition feed.
    
    Args:
        start (int, optional): Starting index for pagination. Defaults to 0.
        count (int, optional): Maximum number of entries to return. Defaults to 10. Use -1 for unlimited.
        lang (str, optional): Filter by language (3-letter language code). Defaults to None.
        category (str, optional): Filter by category. Defaults to None.
        tag (str, optional): Filter by tags (semicolon separated for multiple tags). Defaults to None.
        notag (str, optional): Exclude entries with specified tags. Defaults to None.
        maxsize (int, optional): Include only entries with size not exceeding this value in bytes. Defaults to None.
        q (str, optional): Filter by text in title or description. Defaults to None.
        name (str, optional): Filter by book name. Defaults to None.
        
    Returns:
        Returns a paginated OPDS acquisition feed of ZIM files from the library, which can be filtered by various criteria including language, category, tags, size, and text content."""
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8888/catalog/v2/entries"
    
    # Build query parameters
    params = {"start": start, "count": count}
    
    # Add optional filters if provided
    if lang:
        params["lang"] = lang
    if category:
        params["category"] = category
    if tag:
        params["tag"] = tag
    if notag:
        params["notag"] = notag
    if maxsize:
        params["maxsize"] = maxsize
    if q:
        params["q"] = q
    if name:
        params["name"] = name
    
    # Make the request
    response = requests.get(base_url, params=params)
    
    return response

if __name__ == '__main__':
    r = get_library_entries(count=5, lang="eng", category="wikipedia")
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