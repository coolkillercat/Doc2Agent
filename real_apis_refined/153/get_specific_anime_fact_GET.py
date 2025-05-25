import requests
from urllib.parse import quote
                
def get_specific_anime_fact(anime_name=None, fact_id=None):
    if isinstance(anime_name, set) and len(anime_name) > 0:
        anime_name = list(anime_name)[0][1]
    if isinstance(fact_id, set) and len(fact_id) > 0:
        fact_id = list(fact_id)[0][1]
        
    assert anime_name is not None, 'Missing required parameter: anime_name'
    assert fact_id is not None, 'Missing required parameter: fact_id'
    
    api_url = f"https://anime-facts-rest-api.herokuapp.com/api/v1/{quote(str(anime_name), safe='')}/{str(fact_id)}"
    
    response = requests.get(url=api_url, timeout=50)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_specific_anime_fact(anime_name='''fma_brotherhood''', fact_id=2)
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