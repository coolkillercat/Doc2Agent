import requests
from urllib.parse import quote
                
def downvote_a_comment(submission_id=None, comment_id=None):
    api_url = f"http://ec2-18-219-239-190.us-east-2.compute.amazonaws.com:9999missing"
    payload = {'submission_id': submission_id, 'comment_id': comment_id, }
    assert submission_id is not None, 'Missing required parameter: submission_id'
    assert comment_id is not None, 'Missing required parameter: comment_id'
    
    response = requests.post(url=api_url, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = downvote_a_comment(submission_id=123, comment_id=456)
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

