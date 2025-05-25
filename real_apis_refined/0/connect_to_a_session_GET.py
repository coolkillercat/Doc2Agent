import requests
from urllib.parse import quote
                
def connect_to_a_session(sessionid=None):
    assert sessionid is not None, 'Missing required parameter: sessionid'
    
    # Extract the actual sessionid value if it's in a tuple format
    if isinstance(sessionid, set) and len(sessionid) > 0:
        sessionid_tuple = list(sessionid)[0]
        if isinstance(sessionid_tuple, tuple) and len(sessionid_tuple) > 0:
            sessionid = sessionid_tuple[1]
    
    api_url = f"https://fourconnect.onrender.com/api/sessions/{quote(str(sessionid), safe='')}/connect"
    
    response = requests.get(url=api_url, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = connect_to_a_session(sessionid='''abc123''')
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