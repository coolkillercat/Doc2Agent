import requests
from urllib.parse import quote
                
def get_bank_details_using_ifsc(ifsc=None):
    api_url = f"https://bank-apis.justinclicks.com/api/v1/getBankDetails"
    querystring = {'ifsc': ifsc, }
    assert ifsc is not None, 'Missing required parameter: ifsc'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_bank_details_using_ifsc(ifsc='''SBIN0000001''')
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

