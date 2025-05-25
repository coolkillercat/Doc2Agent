import requests
from urllib.parse import quote
                
def ai_meme(username=None, password=None, template_id=None, prefix_text=None, no_watermark=None):
    api_url = f"https://api.imgflip.com/ai_meme"
    
    # Move assertions before creating payload to fail early
    assert username is not None, 'Missing required parameter: username'
    assert password is not None, 'Missing required parameter: password'
    
    payload = {'username': username, 'password': password}
    
    if template_id is not None:
        payload['template_id'] = template_id
    if prefix_text is not None:
        payload['text_lines'] = [prefix_text]  # Changed prefix_text to text_lines array
    if no_watermark is not None:
        payload['no_watermark'] = int(no_watermark)  # Convert boolean to int
        
    response = requests.post(url=api_url, data=payload, timeout=50)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = ai_meme(username='anuraghazra', password='your_password_here', template_id='89370399', prefix_text='Eric', no_watermark=True)
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