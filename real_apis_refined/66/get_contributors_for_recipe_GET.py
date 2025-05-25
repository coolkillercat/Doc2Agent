import requests
from urllib.parse import quote
                
def get_contributors_for_recipe(recipe_type=None, recipe_slug=None):
    api_url = f"http://taco-randomizer.herokuapp.com/contributors/{quote(recipe_type, safe='')}/{quote(recipe_slug, safe='')}/"
    querystring = {'recipe_type': recipe_type, 'recipe_slug': recipe_slug, }
    assert recipe_type is not None, 'Missing required parameter: recipe_type'
    assert recipe_slug is not None, 'Missing required parameter: recipe_slug'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_contributors_for_recipe(recipe_type='''base_layers''', recipe_slug='''delengua_beef_tongue''')
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

