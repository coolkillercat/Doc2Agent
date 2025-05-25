import requests
from urllib.parse import quote
                
def get_zim_files(start=None, count=10, lang=None, category=None, tag=None, notag=None, maxsize=None, q=None, name=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8888/catalog/v2/entries"
    querystring = {'start': start, 'count': count, 'lang': lang, 'category': category, 'tag': tag, 'notag': notag, 'maxsize': maxsize, 'q': q, 'name': name, }
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_zim_files(start=10, count=50, lang='''ita''', category='''wikipedia''', tag='''wikipedia;_videos:no''', notag='''ted;youtube''', maxsize=5000000, q='''science''', name='''example_book_name''')
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

