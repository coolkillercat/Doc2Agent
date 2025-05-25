import requests
from urllib.parse import quote
                
def fetch_raw_data_with_filters(region_res=None, age_group=None):
    api_url = f"https://covid19-api-philippines.herokuapp.com/api/get?region_res=ncr&age_group=20-24"
    querystring = {'region_res': region_res, 'age_group': age_group, }
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = fetch_raw_data_with_filters(region_res='''NCR''', age_group='''20-24''')
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

