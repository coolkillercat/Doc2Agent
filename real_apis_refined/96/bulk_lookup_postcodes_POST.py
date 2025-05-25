import requests
from urllib.parse import quote
                
def bulk_lookup_postcodes(postcodes=None):
    api_url = f"https://api.postcodes.io/postcodes"
    payload = {'postcodes': postcodes, }
    assert postcodes is not None, 'Missing required parameter: postcodes'
    
    response = requests.post(url=api_url, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = bulk_lookup_postcodes(postcodes=['OX49 5NU', 'M32 0JG', 'NE30 1DP'])
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

