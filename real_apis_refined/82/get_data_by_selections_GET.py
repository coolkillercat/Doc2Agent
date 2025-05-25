import requests
from urllib.parse import quote
                
def get_data_by_selections(bank_name=None, branch_name=None, city=None, state=None):
    api_url = f"https://bank-apis.justinclicks.com/api/v1/getDataBySelections"
    querystring = {'bank_name': bank_name, 'branch_name': branch_name, 'city': city, 'state': state, }
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_data_by_selections(bank_name='''State Bank of India''', branch_name='''Mumbai Main Branch''', city='''Mumbai''', state='''Maharashtra''')
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

