import requests
from urllib.parse import quote
                
def dcat_catalog_search(q=None, format=None):
    api_url = f"https://ckan.govdata.de/api/3/action/dcat_catalog_search"
    querystring = {'q': q, 'format': format, }
    assert q is not None, 'Missing required parameter: q'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = dcat_catalog_search(q='''kindergarten''', format='''rdf''')
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

