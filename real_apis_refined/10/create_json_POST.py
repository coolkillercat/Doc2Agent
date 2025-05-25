import requests
from urllib.parse import quote
                
def create_json():
    api_url = f"https://json.extendsclass.com/bin"
    payload = {}
    headers = {
        "Api-Key": "YOUR_ACTUAL_API_KEY"  # Replace with your actual API key
    }
    
    response = requests.post(url=api_url, json=payload, headers=headers, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = create_json()
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