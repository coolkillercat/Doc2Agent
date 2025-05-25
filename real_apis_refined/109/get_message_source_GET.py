import requests
from urllib.parse import quote
                
def get_message_source(id=None):
    assert id is not None, 'Missing required parameter: id'
    api_url = f"https://api.mail.tm/sources/{quote(id, safe='')}"
    
    headers = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2FwaS5tYWlsLnRtIiwiaWF0IjoxNjE2NDI5NjMwLCJleHAiOjE2MTY0MzMyMzAsInN1YiI6IjYwNTRjMjVlYzg2ZmVkNGIzZmJiYzIyMCIsIm1lcmN1cmUiOnsic3Vic2NyaWJlIjpbIi9hY2NvdW50cy82MDU0YzI1ZWM4NmZlZDRiM2ZiYmMyMjAiXX19.v-kcgWvL9jPg6EBjQOFwvDM8Vmy8uQKGEXVdvDOr1yk'
    }
    
    response = requests.get(url=api_url, headers=headers, timeout=50)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, headers=headers, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_message_source(id='12345')
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