import requests
from urllib.parse import quote
                
def get_current_account(token=None):
    api_url = "https://api.mail.tm/me"
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    
    response = requests.get(url=api_url, headers=headers, timeout=50)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, headers=headers, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    # You would need to provide a valid JWT token here
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE2MzQ1MjY0MDAsInJvbGVzIjpbIlJPTEVfVVNFUiJdLCJ1c2VybmFtZSI6InRlc3RAdGVzdC5jb20iLCJpZCI6IjYxNjVkYjkwMjc3NTRiNzdiZDJjNjY5MyIsIm1lcmN1cmUiOnsic3Vic2NyaWJlIjpbIi9hY2NvdW50cy82MTY1ZGI5MDI3NzU0Yjc3YmQyYzY2OTMiXX19.vhRwKQUfuXQHkgBnHtRdMVF7IqRh8YBzj8qJXgqQECVmKkvCLEXfYzpAJbsHnx9-09rJTbCgNvSVx5sMeqV0Yw"
    r = get_current_account(token)
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