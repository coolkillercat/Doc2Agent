import requests
from urllib.parse import quote
                
def generate_quote_image_by_keyword(YOUR_KEY=None, keyword=None):
    api_url = f"https://zenquotes.io/api/image/[YOUR_KEY]&keyword=[keyword]"
    querystring = {'YOUR_KEY': YOUR_KEY, 'keyword': keyword, }
    assert YOUR_KEY is not None, 'Missing required parameter: YOUR_KEY'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = generate_quote_image_by_keyword(YOUR_KEY='''your_api_key''', keyword='''motivation''')
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

