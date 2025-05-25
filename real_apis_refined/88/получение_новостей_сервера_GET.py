import requests
from urllib.parse import quote
                
def 锌芯谢褍褔械薪懈械_薪芯胁芯褋褌械泄_褋械褉胁械褉邪():
    api_url = f"http://www.cbr.ru/scripts/XML_News.asp"
    querystring = {}
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = 锌芯谢褍褔械薪懈械_薪芯胁芯褋褌械泄_褋械褉胁械褉邪()
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
    result_dict['content'] = r.content.decode("windows-1251")
    print(json.dumps(result_dict, indent=4))