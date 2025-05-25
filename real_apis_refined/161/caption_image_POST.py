import requests
from urllib.parse import quote
                
def caption_image(template_id=None, username=None, password=None, text0=None, text1=None, font=None, max_font_size=None, no_watermark=None, boxes=None):
    api_url = f"https://api.imgflip.com/caption_image"
    payload = {'template_id': template_id, 'username': username, 'password': password, 'text0': text0, 'text1': text1, 'font': font, 'max_font_size': max_font_size, 'no_watermark': no_watermark}
    
    if boxes:
        for i, box in enumerate(boxes):
            for key, value in box.items():
                payload[f'boxes[{i}][{key}]'] = value
    
    assert template_id is not None, 'Missing required parameter: template_id'
    assert username is not None, 'Missing required parameter: username'
    assert password is not None, 'Missing required parameter: password'
    
    response = requests.post(url=api_url, data=payload, timeout=50)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = caption_image(template_id='61579', username='anuraghazra', password='your_actual_password', text0='Top text example', text1='Bottom text example', font='arial', max_font_size='50', no_watermark=True, boxes=[{'text': 'One does not simply', 'x': 10, 'y': 10, 'width': 548, 'height': 100, 'color': '#ffffff', 'outline_color': '#000000'}, {'text': 'Make custom memes on the web via imgflip API', 'x': 10, 'y': 225, 'width': 548, 'height': 100, 'color': '#ffffff', 'outline_color': '#000000'}])
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