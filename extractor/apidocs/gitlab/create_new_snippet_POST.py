import requests, json
from urllib.parse import quote


def create_new_snippet(title=None, files=None, file_name=None, content=None, description=None, visibility=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/snippets"
    payload = {'title': title, 'files': files, 'file_name': file_name, 'content': content, 'description': description, 'visibility': visibility, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert title is not None, 'Missing required parameter: title'
    assert files is not None, 'Missing required parameter: files'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = create_new_snippet(title='''This is a snippet''', files=[{'file_path': 'test.txt', 'content': 'Hello world'}], file_name='''example.rb''', content='''print('Hello World')''', description='''Hello World snippet''', visibility='''internal''')
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

