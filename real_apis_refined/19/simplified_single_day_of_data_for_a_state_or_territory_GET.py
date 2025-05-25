import requests
from urllib.parse import quote
                
def simplified_single_day_of_data_for_a_state_or_territory(state_code=None, date_iso_format=None):
    api_url = f"https://api.covidtracking.com/v2/states/[state-code]/[date-iso-format]/simple.json"
    querystring = {'state_code': state_code, 'date_iso_format': date_iso_format, }
    assert state_code is not None, 'Missing required parameter: state_code'
    assert date_iso_format is not None, 'Missing required parameter: date_iso_format'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = simplified_single_day_of_data_for_a_state_or_territory(state_code='''ca''', date_iso_format='''2021-01-10''')
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

