import requests
from urllib.parse import quote
                
def consultar_encomenda(provider=None, codigo_rastreio=None, format='json'):
    api_url = f"https://api.postmon.com.br/v1/rastreio/{quote(provider, safe='')}/{quote(codigo_rastreio, safe='')}"
    querystring = {'provider': provider, 'codigo_rastreio': codigo_rastreio, 'format': format, }
    assert provider is not None, 'Missing required parameter: provider'
    assert codigo_rastreio is not None, 'Missing required parameter: codigo_rastreio'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = consultar_encomenda(provider='''ect''', codigo_rastreio='''AB123456789BR''', format='''xml''')
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

