import requests, json
from urllib.parse import quote

def normalize_wurcs(wurcs=None):
    """
    Normalize a WURCS format string and retrieve GlyTouCan accession number.
    
    Parameters:
    -----------
    wurcs : str, required
        WURCS format text to be normalized.
        
    Returns:
    --------
    requests.Response
        Response object containing the normalized WURCS format and GlyTouCan accession number.
        
    Example:
    --------
    >>> result = normalize_wurcs(wurcs="WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1")
    >>> print(result.json())
    """
    api_url = "https://api.glycosmos.org/glycanformatconverter/2.10.0/wurcs2wurcs"
    assert wurcs is not None, 'Missing required parameter: wurcs'
    
    # The API expects an array of WURCS strings
    payload = [wurcs]
    
    response = requests.post(url=api_url, json=payload, headers={}, timeout=50)
    return response

if __name__ == '__main__':
    r = normalize_wurcs(wurcs='WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1')
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