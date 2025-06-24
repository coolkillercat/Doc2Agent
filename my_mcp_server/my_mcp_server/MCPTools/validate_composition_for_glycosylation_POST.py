import requests
import json
from urllib.parse import quote

def validate_composition_for_glycosylation(wurcs=None):
    """
    Determine if the composition WURCS is valid for glycosylation.
    
    Parameters:
    -----------
    wurcs : str, required
        WURCS format text.
        
    Returns:
        Returns validation results indicating whether a glycan structure in WURCS format has a valid composition for glycosylation.
    --------
    requests.Response
        Response object containing validation results.
        
    Example:
    --------
    >>> validate_composition_for_glycosylation(wurcs="WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1")
    """
    api_url = "https://api.glycosmos.org/wurcsframework/1.2.14/compositionvalidator"
    assert wurcs is not None, 'Missing required parameter: wurcs'
    
    # The API expects an array of WURCS strings
    payload = [wurcs]
    headers = {'Content-Type': 'application/json'}
    
    response = requests.post(url=api_url, json=payload, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = validate_composition_for_glycosylation(wurcs='WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1')
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