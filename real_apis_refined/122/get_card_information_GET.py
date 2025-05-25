import requests
from urllib.parse import quote
                
def get_card_information(name=None, fname=None, id=None, konami_id=None, type=None, atk=None, def=None, level=None, race=None, attribute=None, link=None, linkmarker=None, scale=None, cardset=None, archetype=None, banlist=None, sort=None, format=None, misc=None, staple=None, has_effect=None, startdate=None, enddate=None, dateregion=None):
    api_url = f"https://db.ygoprodeck.com/api/v7/cardinfo.php"
    querystring = {'name': name, 'fname': fname, 'id': id, 'konami_id': konami_id, 'type': type, 'atk': atk, 'def': def, 'level': level, 'race': race, 'attribute': attribute, 'link': link, 'linkmarker': linkmarker, 'scale': scale, 'cardset': cardset, 'archetype': archetype, 'banlist': banlist, 'sort': sort, 'format': format, 'misc': misc, 'staple': staple, 'has_effect': has_effect, 'startdate': startdate, 'enddate': enddate, 'dateregion': dateregion, }
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_card_information(name='''Dark Magician|Blue-Eyes White Dragon''', fname='''Magician''', id='''6983839,93221206''', konami_id='''12345678''', type='''Effect Monster,Spell Card''', atk='''lt2500''', def='''gte2000''', level='''lte8''', race='''Spellcaster,Warrior''', attribute='''DARK,EARTH''', link='''2''', linkmarker='''Top,Bottom''', scale='''4''', cardset='''Metal Raiders''', archetype='''Blue-Eyes''', banlist='''TCG''', sort='''atk''', format='''tcg''', misc='''yes''', staple='''yes''', has_effect=true, startdate='''2000-01-01''', enddate='''2002-08-23''', dateregion='''tcg''')
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

