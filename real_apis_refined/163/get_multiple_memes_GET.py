import requests
from urllib.parse import quote
                
def get_multiple_memes(count=None):
    assert count is not None, 'Missing required parameter: count'
    
    # Ensure count is an integer and within reasonable limits
    count = int(count) if isinstance(count, str) else count
    count = min(max(1, count), 50)  # Limit to reasonable range
    
    api_url = f"https://meme-api.com/gimme/{count}"
    
    # First try with SSL verification
    try:
        response = requests.get(url=api_url, timeout=50)
        if response.status_code == 200:
            return response
    except:
        pass
    
    # If first attempt fails, try without SSL verification
    response = requests.get(url=api_url, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = get_multiple_memes(count=2)
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