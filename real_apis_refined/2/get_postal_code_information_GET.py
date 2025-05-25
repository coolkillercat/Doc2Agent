import requests
from urllib.parse import quote
                
def get_postal_code_information(postal_code=None):
    api_url = f"https://postali.app/codigo-postal/{quote(str(postal_code), safe='')}.json"
    assert postal_code is not None, 'Missing required parameter: postal_code'
    
    headers = {
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'Mozilla/5.0'
    }
    
    response = requests.get(url=api_url, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = get_postal_code_information(postal_code='65936')
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
    try:
        result_dict['content'] = r.content.decode("utf-8")
    except:
        result_dict['content'] = str(r.content)
    print(json.dumps(result_dict, indent=4))