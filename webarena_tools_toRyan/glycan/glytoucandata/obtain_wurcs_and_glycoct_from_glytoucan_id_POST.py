import requests
from urllib.parse import quote

def obtain_wurcs_and_glycoct_from_glytoucan_id(gtcid=None):
    """
    Obtain WURCS and GlycoCT sequence representations for a given GlyTouCan ID.
    
    Args:
        gtcid (str): GlyTouCan ID (e.g., 'G22768VO')
        
    Returns:
        dict: JSON response containing WURCS and GlycoCT sequences for the given ID
        
    Example:
        >>> obtain_wurcs_and_glycoct_from_glytoucan_id(gtcid='G22768VO')
        [
            {
                "id": "G22768VO",
                "wurcs": "WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1"
            },
            {
                "id": "G22768VO",
                "glycoct": "RES\\n1b:b-dglc-HEX-1:5\\n2s:n-acetyl\\n3b:b-dglc-HEX-1:5\\n4s:n-acetyl\\n5b:b-dman-HEX-1:5\\n6b:a-dman-HEX-1:5\\n7b:a-dman-HEX-1:5\\nLIN\\n1:1d(2+1)2n\\n2:1o(4+1)3d\\n3:3d(2+1)4n\\n4:3o(4+1)5d\\n5:5o(3+1)6d\\n6:5o(6+1)7d"
            }
        ]
    """
    api_url = "https://api.glycosmos.org/sparqlist/gtcid2seqs"
    assert gtcid is not None, 'Missing required parameter: gtcid'
    
    payload = {'gtcid': gtcid}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    
    response = requests.post(url=api_url, data=payload, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = obtain_wurcs_and_glycoct_from_glytoucan_id(gtcid='G22768VO')
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