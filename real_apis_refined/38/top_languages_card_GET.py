import requests
from urllib.parse import quote
                
def top_languages_card(username=None, hide=None, langs_count=5, layout='normal', exclude_repo=None, custom_title='Most Used Languages', hide_progress=None, size_weight=1, count_weight=None):
    api_url = f"https://github-readme-stats.vercel.app/api/top-langs"
    querystring = {'username': username, 'hide': hide, 'langs_count': langs_count, 'layout': layout, 'exclude_repo': exclude_repo, 'custom_title': custom_title, 'hide_progress': hide_progress, 'size_weight': size_weight, 'count_weight': count_weight, }
    assert username is not None, 'Missing required parameter: username'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = top_languages_card(username='''anuraghazra''', hide='''javascript,html''', langs_count=8, layout='''compact''', exclude_repo='''repo1,repo2''', custom_title='''Top Languages''', hide_progress=True, size_weight=0.5, count_weight=0.5)
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

