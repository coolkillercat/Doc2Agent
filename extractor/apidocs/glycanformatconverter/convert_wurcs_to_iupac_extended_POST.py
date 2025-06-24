import requests, json
from urllib.parse import quote

def convert_wurcs_to_iupac_extended(wurcs=None):
    """
    Convert WURCS format to IUPAC Extended format using the GlycanFormatConverter API.
    
    Args:
        wurcs (str): WURCS format text to be converted.
            Example: "WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1"
    
    Returns:
        requests.Response: The API response object containing the conversion result.
        
    Example:
        >>> response = convert_wurcs_to_iupac_extended(wurcs="WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1")
        >>> print(response.json())
    """
    api_url = "https://api.glycosmos.org/glycanformatconverter/2.10.0/wurcs2iupacextended"
    assert wurcs is not None, 'Missing required parameter: wurcs'
    
    payload = [wurcs]
    headers = {'Content-Type': 'application/json'}
    
    response = requests.post(url=api_url, json=payload, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = convert_wurcs_to_iupac_extended(wurcs='WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1')
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