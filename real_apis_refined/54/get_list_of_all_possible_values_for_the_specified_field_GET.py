import requests
from urllib.parse import quote
                
def get_list_of_all_possible_values_for_the_specified_field(field=None, dataset='case_information'):
    api_url = f"https://covid19-api-philippines.herokuapp.com/api/list-of/{quote(field, safe='')}"
    querystring = {'field': field, 'dataset': dataset, }
    assert field is not None, 'Missing required parameter: field'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_list_of_all_possible_values_for_the_specified_field(field='''regions''', dataset='''case_information''')
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

