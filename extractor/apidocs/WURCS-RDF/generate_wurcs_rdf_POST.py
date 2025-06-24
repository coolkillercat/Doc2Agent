import requests
import json
from urllib.parse import quote

def generate_wurcs_rdf(gtcid=None, wurcs=None):
    """
    Generate the WURCS-RDF from WURCS.
    
    Parameters:
    -----------
    gtcid : str, required
        GlyTouCan ID.
    wurcs : str, required
        WURCS format text.
    
    Returns:
    --------
    requests.Response
        The response from the API.
    
    Examples:
    ---------
    >>> generate_wurcs_rdf(
    ...     gtcid="G22768VO", 
    ...     wurcs="WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1"
    ... )
    """
    api_url = "https://api.glycosmos.org/wurcsrdf/1.2.6/wurcs2wurcsrdf"
    
    assert gtcid is not None, 'Missing required parameter: gtcid'
    assert wurcs is not None, 'Missing required parameter: wurcs'
    
    headers = {'Content-Type': 'application/json'}
    payload = {
        "gtcid": gtcid,
        "wurcs": wurcs
    }
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50)
    return response

if __name__ == '__main__':
    r = generate_wurcs_rdf(gtcid='G22768VO', wurcs='WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1')
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