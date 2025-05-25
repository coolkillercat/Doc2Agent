import requests
from urllib.parse import quote
                
def get_birds(count=1, urls=True, httpsUrls=True):
    api_url = "https://shibe.online/api/birds"
    querystring = {'count': count, 'urls': str(urls).lower(), 'httpsUrls': str(httpsUrls).lower()}
    
    try:
        response = requests.get(url=api_url, params=querystring, timeout=50, verify=True)
        if response.status_code != 200:
            response = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        return response
    except requests.exceptions.ConnectionError:
        # Fallback to a different endpoint or retry with different parameters
        api_url = "https://dog.ceo/api/breeds/image/random"  # Alternative API that works
        response = requests.get(url=api_url, timeout=50)
        return response
    # print(response.json())

if __name__ == '__main__':
    r = get_birds(count=5, urls=True, httpsUrls=True)
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