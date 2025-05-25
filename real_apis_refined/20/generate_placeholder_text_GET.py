import requests
from urllib.parse import quote
                
def generate_placeholder_text(number_of_paragraphs=1, paragraph_length=None, decorate=None, link=None, ul=None, ol=None, dl=None, bq=None, code=None, headers=None, allcaps=None, prude=None, plaintext=None):
    api_url = "https://lipsum.com/feed/json"
    querystring = {'amount': number_of_paragraphs, 'what': 'paras', 'start': 'yes'}
    
    if paragraph_length:
        if paragraph_length.lower() == 'short':
            querystring['what'] = 'words'
            querystring['amount'] = 50
        elif paragraph_length.lower() == 'medium':
            querystring['what'] = 'words'
            querystring['amount'] = 100
        elif paragraph_length.lower() == 'long':
            querystring['what'] = 'words'
            querystring['amount'] = 200
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=True)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = generate_placeholder_text(number_of_paragraphs=1, paragraph_length='short')
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