import requests, json
from urllib.parse import quote


def create_a_new_note(lat=None, lon=None, text=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:3000/api/0.6/notes"
    payload = {'lat': lat, 'lon': lon, 'text': text, }
    assert lat is not None, 'Missing required parameter: lat'
    assert lon is not None, 'Missing required parameter: lon'
    assert text is not None, 'Missing required parameter: text'
    
    response = requests.post(url=api_url, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = create_a_new_note(lat=51.0, lon=0.1, text='''This is a note''')
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

