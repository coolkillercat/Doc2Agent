import requests
from urllib.parse import quote
                
def wakatime_stats_card(username=None, hide=None, langs_count=None, layout='default', custom_title='WakaTime Stats', line_height=25, api_domain='wakatime.com', display_format='time', disable_animations=None):
    api_url = f"https://github-readme-stats.vercel.app/api/wakatime"
    querystring = {'username': username, 'hide': hide, 'langs_count': langs_count, 'layout': layout, 'custom_title': custom_title, 'line_height': line_height, 'api_domain': api_domain, 'display_format': display_format, 'disable_animations': disable_animations, }
    assert username is not None, 'Missing required parameter: username'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = wakatime_stats_card(username='''ffflabs''', hide='''javascript,html''', langs_count=5, layout='''compact''', custom_title='''My Coding Stats''', line_height=30, api_domain='''hakatime.com''', display_format='''percent''', disable_animations=True)
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

