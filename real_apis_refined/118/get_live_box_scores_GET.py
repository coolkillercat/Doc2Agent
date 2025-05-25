import requests
from urllib.parse import quote
                
def get_live_box_scores():
    api_url = f"https://api.balldontlie.io/v1/box_scores/live"
    headers = {
        "Authorization": "YOUR_ACTUAL_API_KEY_HERE"  # Replace with actual API key
    }
    querystring = {}
    
    response = requests.get(url=api_url, params=querystring, headers=headers, timeout=50, verify=True)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, headers=headers, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_live_box_scores()
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