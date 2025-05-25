import requests
from urllib.parse import quote
                
def get_multiple_memes_from_subreddit(subreddit=None, count=None):
    assert subreddit is not None, 'Missing required parameter: subreddit'
    assert count is not None, 'Missing required parameter: count'
    
    api_url = f"https://meme-api.com/gimme/{quote(str(subreddit), safe='')}/{str(count)}"
    
    response = requests.get(url=api_url, timeout=50)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_multiple_memes_from_subreddit(subreddit='wholesomememes', count=2)
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