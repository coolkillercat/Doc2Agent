import requests
from urllib.parse import quote
                
def retrieve_all_comments_to_a_forum(forum_name=None):
    api_url = f"http://ec2-18-219-239-190.us-east-2.compute.amazonaws.com:9999/f/{quote(forum_name, safe='')}/comments"
    querystring = {'forum_name': forum_name, }
    assert forum_name is not None, 'Missing required parameter: forum_name'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = retrieve_all_comments_to_a_forum(forum_name='''allentown''')
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

