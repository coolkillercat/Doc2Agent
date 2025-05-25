import requests
from urllib.parse import quote
                
def latest():
    api_url = "https://api-mobilespecs.azharimm.dev/latest"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    response = requests.get(url=api_url, headers=headers, timeout=50)
    if response.status_code != 200:
        response = requests.get(url=api_url, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = latest()
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