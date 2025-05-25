import requests
from urllib.parse import quote
                
def automeme(username=None, password=None, text=None, no_watermark=None):
    api_url = f"https://api.imgflip.com/caption_image"
    
    assert username is not None, 'Missing required parameter: username'
    assert password is not None, 'Missing required parameter: password'
    assert text is not None, 'Missing required parameter: text'
    
    # Required parameters for the API
    payload = {
        'username': username,
        'password': password,
        'template_id': '181913649',  # Default meme template ID
        'text0': text,  # First text field
        'text1': '',    # Second text field (optional)
    }
    
    if no_watermark is not None:
        payload['no_watermark'] = '1' if no_watermark else '0'
    
    response = requests.post(url=api_url, data=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = automeme(username='user123', password='password123', text='This is a meme', no_watermark=True)
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