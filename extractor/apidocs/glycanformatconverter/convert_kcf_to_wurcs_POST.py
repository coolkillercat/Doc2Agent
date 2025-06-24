import requests, json
from urllib.parse import quote

def convert_kcf_to_wurcs(kcf=None):
    """
    Convert KCF format to WURCS format and retrieve GlyTouCan accession number.
    
    Parameters:
    -----------
    kcf : str, required
        KCF format text. Spaces and line breaks must be encoded.
        
    Returns:
    --------
    response : requests.Response
        Response object containing the conversion result.
        
    Example:
    --------
    >>> kcf = '''ENTRY XYZ Glycan
    NODE 5
    1 GlcNAc 15.0 7.0
    2 GlcNAc 8.0 7.0
    3 Man 1.0 7.0
    4 Man -6.0 12.0
    5 Man -6.0 2.0
    EDGE 4
    1 2:b1 1:4
    2 3:b1 2:4
    3 5:a1 3:3
    4 4:a1 3:6
    ///'''
    >>> response = convert_kcf_to_wurcs(kcf=kcf)
    """
    api_url = "https://api.glycosmos.org/glycanformatconverter/2.10.0/kcf2wurcs"
    assert kcf is not None, 'Missing required parameter: kcf'
    
    # The API expects an array of strings, not a dictionary
    payload = [kcf]
    headers = {'Content-Type': 'application/json'}
    
    response = requests.post(url=api_url, json=payload, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = convert_kcf_to_wurcs(kcf='''ENTRY XYZ Glycan
NODE 5
1 GlcNAc 15.0 7.0
2 GlcNAc 8.0 7.0
3 Man 1.0 7.0
4 Man -6.0 12.0
5 Man -6.0 2.0
EDGE 4
1 2:b1 1:4
2 3:b1 2:4
3 5:a1 3:3
4 4:a1 3:6
///''')
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