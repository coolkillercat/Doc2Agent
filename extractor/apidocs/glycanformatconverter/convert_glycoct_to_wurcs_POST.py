import requests
import json

def convert_glycoct_to_wurcs(glycoct=None):
    """
    Convert GlycoCT format to WURCS format using the GlycanFormatConverter API.
    
    Parameters:
    -----------
    glycoct : str, required
        GlycoCT format text to be converted.
        
    Returns:
    --------
    dict
        A dictionary containing the conversion result with WURCS format and GlyTouCan accession number.
        
    Example:
    --------
    >>> glycoct = '''RES
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
    6:5o(6+1)7d'''
    >>> result = convert_glycoct_to_wurcs(glycoct)
    """
    api_url = "https://api.glycosmos.org/glycanformatconverter/2.10.0/glycoct2wurcs"
    
    assert glycoct is not None, 'Missing required parameter: glycoct'
    
    # The API expects an array of strings
    payload = [glycoct]
    headers = {'Content-Type': 'application/json'}
    
    response = requests.post(url=api_url, data=json.dumps(payload), headers=headers, timeout=50)
    response.raise_for_status()
    
    # Return the first element of the array response
    return response.json()[0]

if __name__ == '__main__':
    r = convert_glycoct_to_wurcs(glycoct='''RES
1b:b-dglc-HEX-1:5
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
    
    result_dict = dict()
    result_dict['status_code'] = 200
    result_dict['text'] = json.dumps(r)
    result_dict['json'] = r
    result_dict['content'] = json.dumps(r)
    print(json.dumps(result_dict, indent=4))