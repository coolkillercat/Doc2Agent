import requests, json
from urllib.parse import quote

def get_available_languages() -> requests.Response:
    """
    Retrieves the list of all languages available in the ZIM file library as an OPDS Navigation Feed.
    
    Returns:
        Returns a list of all languages available in the ZIM file library as an OPDS Navigation Feed."""
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8888"
    endpoint = "/catalog/v2/languages"
    
    url = f"{base_url}{endpoint}"
    headers = {
        "Accept": "application/xml"
    }
    
    response = requests.get(url, headers=headers)
    return response

if __name__ == '__main__':
    r = get_available_languages()
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