import requests
from urllib.parse import quote
                
def reply_to_a_comment(submission_id=None, comment_id=None, comment=None):
    api_url = f"http://ec2-18-219-239-190.us-east-2.compute.amazonaws.com:9999missing"
    payload = {'submission_id': submission_id, 'comment_id': comment_id, 'comment': comment, }
    assert submission_id is not None, 'Missing required parameter: submission_id'
    assert comment_id is not None, 'Missing required parameter: comment_id'
    assert comment is not None, 'Missing required parameter: comment'
    
    response = requests.post(url=api_url, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = reply_to_a_comment(submission_id=123, comment_id=456, comment='''This is a reply to the comment.''')
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

