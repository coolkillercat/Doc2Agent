import requests
from urllib.parse import quote
                
def show_a_connection(connection_id=None, user_id=None):
    assert connection_id is not None, 'Missing required parameter: connection_id'
    api_url = f"https://connect.ifttt.com/v2/connections/{connection_id}"
    
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    
    response = requests.get(url=api_url, headers=headers, timeout=50)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = show_a_connection(connection_id='C8p3q9T6', user_id='123')
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