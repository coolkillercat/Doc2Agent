import requests
from urllib.parse import quote

def obtain_glytoucan_id_from_wurcs(wurcs=None):
    """
    Obtain the GlyTouCan ID from WURCS format text.
    
    Args:
        wurcs (str): WURCS format text of a glycan structure.
    
    Returns:
        Returns the GlyTouCan accession ID corresponding to a given WURCS format glycan structure.
    Example:
        >>> obtain_glytoucan_id_from_wurcs(wurcs="WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1")
        [{'id': 'G22768VO', 'wurcs': 'WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1'}]
    """
    api_url = "https://api.glycosmos.org/sparqlist/wurcs2gtcids"
    assert wurcs is not None, 'Missing required parameter: wurcs'
    
    payload = {'wurcs': wurcs}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    
    response = requests.post(url=api_url, data=payload, headers=headers, timeout=50)
    return response.json()

if __name__ == '__main__':
    r = obtain_glytoucan_id_from_wurcs(wurcs='WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1')
    r_json = None
    try:
        r_json = r
    except:
        pass
    import json
    result_dict = dict()
    result_dict['status_code'] = 200
    result_dict['text'] = json.dumps(r)
    result_dict['json'] = r_json
    result_dict['content'] = json.dumps(r)
    print(json.dumps(result_dict, indent=4))