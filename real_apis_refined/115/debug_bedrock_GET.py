import requests
from urllib.parse import quote
                
def debug_bedrock(address=None):
    if address is None:
        return {"error": "No address to query."}
    
    api_url = f"https://api.mcsrvstat.us/debug/bedrock/{quote(address, safe='')}"
    
    response = requests.get(url=api_url, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = debug_bedrock(address='play.example.com')
    r_json = None
    try:
        r_json = r.json()
    except:
        pass
    import json
    result_dict = dict()
    result_dict['status_code'] = r.status_code if hasattr(r, 'status_code') else 200
    result_dict['text'] = r.text if hasattr(r, 'text') else json.dumps(r)
    result_dict['json'] = r_json if r_json is not None else r
    result_dict['content'] = r.content.decode("utf-8") if hasattr(r, 'content') else json.dumps(r)
    print(json.dumps(result_dict, indent=4))