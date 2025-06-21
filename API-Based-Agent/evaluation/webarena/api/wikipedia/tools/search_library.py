import requests, json
from urllib.parse import quote


def search_library(pattern: str, books_filter: dict = None, start: int = 1, page_length: int = 25, format: str = 'html') -> requests.Response:
    """
    Performs a full text search across specified ZIM files and returns results with snippets of matching content.
    
    Args:
        pattern (str): The text to search for
        books_filter (dict, optional): Dictionary with filter criteria like 'lang', 'category', etc.
        start (int, optional): Start index for pagination. Defaults to 1.
        page_length (int, optional): Maximum number of search results. Defaults to 25.
        format (str, optional): Format of results ('html' or 'xml'). Defaults to 'html'.
    
    Returns:
        Returns full-text search results with snippets of matching content from specified ZIM files based on the provided search pattern."""
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8888/search"
    
    params = {
        'pattern': pattern,
        'start': start,
        'pageLength': page_length,
        'format': format
    }
    
    # Add book filters if provided
    if books_filter:
        for key, value in books_filter.items():
            if key == 'name':
                params['books.name'] = value
            elif key == 'id':
                params['books.id'] = value
            else:
                params[f'books.filter.{key}'] = value
    
    response = requests.get(base_url, params=params)
    return response

if __name__ == '__main__':
    r = search_library(pattern="python", books_filter={"lang": "eng", "category": "wikipedia"}, start=1, page_length=10, format="html")
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