import requests
from urllib.parse import quote
                
def create_a_post(title=None, body=None, userId=None):
    api_url = f"https://jsonplaceholder.typicode.com/posts"
    payload = {'title': title, 'body': body, 'userId': userId, }
    assert title is not None, 'Missing required parameter: title'
    assert body is not None, 'Missing required parameter: body'
    assert userId is not None, 'Missing required parameter: userId'
    
    response = requests.post(url=api_url, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = create_a_post(title='''My New Post''', body='''This is the content of my new post.''', userId=1)
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

