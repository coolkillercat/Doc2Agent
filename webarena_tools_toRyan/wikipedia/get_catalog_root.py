import requests, json
from urllib.parse import quote

def get_catalog_root(format: str = 'xml') -> dict:
    """
    Retrieves the OPDS Catalog Root that links to all OPDS acquisition and navigation feeds available through the API.
    
    Args:
        format (str): The format of the response (xml by default)
        
    Returns:
        Retrieves the OPDS Catalog Root that links to all OPDS acquisition and navigation feeds available through the API."""
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8888"
    endpoint = "/catalog/v2/root.xml"
    url = base_url + endpoint
    
    headers = {}
    response = requests.get(url, headers=headers)
    return response

if __name__ == '__main__':
    r = get_catalog_root()
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