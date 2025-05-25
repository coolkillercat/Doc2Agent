import requests
from urllib.parse import quote
                
def github_stats_card(username=None, hide=None, show=None, show_icons=None, theme='default', cache_seconds=21600, locale='en', border_radius=4.5, hide_rank=None, include_all_commits=None, line_height=25, exclude_repo=None, custom_title='<username> GitHub Stats', text_bold=True, disable_animations=None, ring_color='2f80ed', number_format='short'):
    api_url = f"https://github-readme-stats.vercel.app/api"
    querystring = {'username': username, 'hide': hide, 'show': show, 'show_icons': show_icons, 'theme': theme, 'cache_seconds': cache_seconds, 'locale': locale, 'border_radius': border_radius, 'hide_rank': hide_rank, 'include_all_commits': include_all_commits, 'line_height': line_height, 'exclude_repo': exclude_repo, 'custom_title': custom_title, 'text_bold': text_bold, 'disable_animations': disable_animations, 'ring_color': ring_color, 'number_format': number_format, }
    assert username is not None, 'Missing required parameter: username'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = github_stats_card(username='''anuraghazra''', hide='''commits,prs''', show='''reviews,discussions_started''', show_icons=True, theme='''radical''', cache_seconds=36000, locale='''es''', border_radius=10, hide_rank=True, include_all_commits=True, line_height=30, exclude_repo='''repo1,repo2''', custom_title='''My GitHub Stats''', text_bold=False, disable_animations=True, ring_color='''ff0000''', number_format='''long''')
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

