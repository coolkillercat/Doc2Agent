import requests
from urllib.parse import quote
                
def get_poems_by_combination(input_field1=None, input_field2=None, search_term1=None, search_term2=None, output_field=None, format='json'):
    api_url = f"https://poetrydb.org/{quote(input_field1, safe='')},{quote(input_field2, safe='')}/{quote(search_term1, safe='')};{quote(search_term2, safe='')}"
    querystring = {'input_field1': input_field1, 'input_field2': input_field2, 'search_term1': search_term1, 'search_term2': search_term2, 'output_field': output_field, 'format': format, }
    assert input_field1 is not None, 'Missing required parameter: input_field1'
    assert input_field2 is not None, 'Missing required parameter: input_field2'
    assert search_term1 is not None, 'Missing required parameter: search_term1'
    assert search_term2 is not None, 'Missing required parameter: search_term2'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_poems_by_combination(input_field1='''title''', input_field2='''author''', search_term1='''Winter''', search_term2='''William Shakespeare''', output_field='''author,title''', format='''json''')
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

