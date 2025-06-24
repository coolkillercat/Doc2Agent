import requests, json
from urllib.parse import quote

def normalize_glycoct(glycoct=None):
    """
    Normalize GlycoCT format using the GlycanFormatConverter API.
    
    Args:
        glycoct (str): GlycoCT format text to be normalized.
            Example:
            ```
            RES
            1b:x-dglc-HEX-1:5
            2s:n-acetyl
            3b:b-dglc-HEX-1:5
            4s:n-acetyl
            5b:b-dman-HEX-1:5
            6b:a-dman-HEX-1:5
            7b:a-dman-HEX-1:5
            LIN
            1:1d(2+1)2n
            2:1o(4+1)3d
            3:3d(2+1)4n
            4:3o(4+1)5d
            5:5o(3+1)6d
            6:5o(6+1)7d
            ```
    
    Returns:
        dict: A dictionary containing the normalized GlycoCT format.
    """
    api_url = "https://api.glycosmos.org/glycanformatconverter/2.10.0/glycoct2glycoct"
    assert glycoct is not None, 'Missing required parameter: glycoct'
    
    # The API expects an array of strings
    payload = [glycoct]
    headers = {'Content-Type': 'application/json'}
    
    response = requests.post(url=api_url, json=payload, headers=headers, timeout=50)
    
    if response.status_code == 200:
        return response.json()[0]
    else:
        return response

if __name__ == '__main__':
    r = normalize_glycoct(glycoct='''RES
1b:x-dglc-HEX-1:5
2s:n-acetyl
3b:b-dglc-HEX-1:5
4s:n-acetyl
5b:b-dman-HEX-1:5
6b:a-dman-HEX-1:5
7b:a-dman-HEX-1:5
LIN
1:1d(2+1)2n
2:1o(4+1)3d
3:3d(2+1)4n
4:3o(4+1)5d
5:5o(3+1)6d
6:5o(6+1)7d''')
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