import requests
from urllib.parse import quote
                
def fetch_quote_image_by_author(YOUR_KEY=None, author="sun-tzu"):
    api_url = f"https://zenquotes.io/api/image/author/{quote(author)}/{YOUR_KEY}"
    assert YOUR_KEY is not None, 'Missing required parameter: YOUR_KEY'
    
    response = requests.get(url=api_url, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = fetch_quote_image_by_author(YOUR_KEY='152')
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