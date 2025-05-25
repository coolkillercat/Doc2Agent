import requests
from urllib.parse import quote
                
def get_character_by_id(id=None):
    assert id is not None, 'Missing required parameter: id'
    api_url = f"https://anapioficeandfire.com/api/characters/{id}"
    
    response = requests.get(url=api_url, timeout=50)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_character_by_id(id=583)
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