import requests
import json
from urllib.parse import quote

def convert_gws_format_to_wurcs_format(gws=None):
    """
    Convert GWS format to WURCS format using the GlycoSMOS API.
    
    Args:
        gws (str): GWS format text. Required.
            Example: "freeEnd--?b1D-GlcNAc,p--4b1D-GlcNAc,p--4b1D-Man,p--?a1D-Man,p$MONO,Und,0,0,freeEnd"
    
    Returns:
        Returns the conversion of a GWS format glycan structure to WURCS format with glycan ID and other optional format representations.
    Raises:
        AssertionError: If the required gws parameter is not provided.
        
    Example:
        >>> result = convert_gws_format_to_wurcs_format(gws="freeEnd--?b1D-GlcNAc,p--4b1D-GlcNAc,p--4b1D-Man,p--?a1D-Man,p$MONO,Und,0,0,freeEnd")
        >>> print(result[0]["id"])
        G03717EM
    """
    api_url = "https://api.glycosmos.org/gws2wurcs"
    assert gws is not None, 'Missing required parameter: gws'
    
    # The API expects a JSON array with the GWS string
    payload = [gws] if isinstance(gws, str) else gws
    headers = {'Content-Type': 'application/json'}
    
    response = requests.post(url=api_url, json=payload, headers=headers, timeout=50)
    return response.json()

if __name__ == '__main__':
    r = convert_gws_format_to_wurcs_format(gws='''freeEnd--?b1D-GlcNAc,p--4b1D-GlcNAc,p--4b1D-Man,p--?a1D-Man,p$MONO,Und,0,0,freeEnd''')
    r_json = r
    import json
    result_dict = dict()
    result_dict['status_code'] = 200
    result_dict['text'] = json.dumps(r)
    result_dict['json'] = r_json
    result_dict['content'] = json.dumps(r)
    print(json.dumps(result_dict, indent=4))