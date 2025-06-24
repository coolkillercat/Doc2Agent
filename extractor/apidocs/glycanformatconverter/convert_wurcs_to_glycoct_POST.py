import requests, json
from urllib.parse import quote

def convert_wurcs_to_glycoct(wurcs=None):
    """
    Convert WURCS format to GlycoCT format using the GlycanFormatConverter API.
    
    Args:
        wurcs (str): The WURCS format text to convert.
        
    Returns:
        dict: A dictionary containing the conversion result with GlycoCT format.
        
    Example:
        >>> result = convert_wurcs_to_glycoct(wurcs="WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1")
        >>> print(result["GlycoCT"])
    """
    api_url = "https://api.glycosmos.org/glycanformatconverter/2.10.0/wurcs2glycoct"
    assert wurcs is not None, 'Missing required parameter: wurcs'
    
    payload = [wurcs]
    headers = {'Content-Type': 'application/json'}
    
    response = requests.post(url=api_url, json=payload, headers=headers, timeout=50)
    
    if response.status_code == 200:
        return response.json()[0]
    return response

if __name__ == '__main__':
    r = convert_wurcs_to_glycoct(wurcs='WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1')
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