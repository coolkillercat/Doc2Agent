import requests
from urllib.parse import quote
                
def serve_file_from_bitbucket(user=None, repo=None, tag=None, file=None):
    api_url = f"https://cdn.statically.io/bb/{quote(user, safe='')}/{quote(repo, safe='')}/{quote(tag, safe='')}/{quote(file, safe='')}"
    querystring = {'user': user, 'repo': repo, 'tag': tag, 'file': file, }
    assert user is not None, 'Missing required parameter: user'
    assert repo is not None, 'Missing required parameter: repo'
    assert tag is not None, 'Missing required parameter: tag'
    assert file is not None, 'Missing required parameter: file'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = serve_file_from_bitbucket(user='''jane_doe''', repo='''my-repo''', tag='''main''', file='''script.js''')
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

