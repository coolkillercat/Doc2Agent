import requests, json
from urllib.parse import quote

def search_geospatial(pattern: str, latitude: float, longitude: float, distance: float, books_filter: dict = None, start: int = 1, page_length: int = 25, format: str = 'html') -> requests.Response:
    """
    Performs a geospatial search to find content within a specified distance of geographical coordinates.
    
    Args:
        pattern: Text to search for
        latitude: Latitude coordinate for geospatial search
        longitude: Longitude coordinate for geospatial search
        distance: Maximum distance in meters from the specified coordinates
        books_filter: Dictionary of filtering criteria for books selection (e.g., {'lang': 'eng', 'category': 'wikipedia'})
        start: Starting index for pagination (1-based)
        page_length: Maximum number of results to return (capped at 140)
        format: Format of results ('html' or 'xml')
        
    Returns:
        Returns geospatial search results for content located within a specified distance of geographical coordinates."""
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8888/search"
    
    params = {
        'pattern': pattern,
        'latitude': latitude,
        'longitude': longitude,
        'distance': distance,
        'start': start,
        'pageLength': min(page_length, 140),  # Capped at 140 as per documentation
        'format': format
    }
    
    # Add book filtering parameters if provided
    if books_filter:
        for key, value in books_filter.items():
            params[f'books.filter.{key}'] = value
    
    response = requests.get(base_url, params=params)
    return response

if __name__ == '__main__':
    r = search_geospatial(
        pattern="mountain",
        latitude=45.5017, 
        longitude=-73.5673, 
        distance=10000,
        books_filter={'lang': 'eng', 'category': 'wikipedia'},
        start=1,
        page_length=25,
        format='html'
    )
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