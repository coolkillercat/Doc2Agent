import requests, json
from urllib.parse import quote

def calculate_mass_from_wurcs(wurcs=None):
    """
    Calculate the mass from WURCS.
    
    Parameters:
    -----------
    wurcs : str, required
        WURCS format text.
        
    Returns:
        Returns the calculated molecular mass of a glycan structure specified in WURCS format.
    --------
    dict
        A dictionary containing the input WURCS and calculated mass.
        
    Example:
    --------
    >>> calculate_mass_from_wurcs("WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1")
    """
    api_url = "https://api.glycosmos.org/wurcsframework/1.2.14/wurcs2mass"
    headers = {'Content-Type': 'application/json'}
    assert wurcs is not None, 'Missing required parameter: wurcs'
    
    payload = [wurcs]
    response = requests.post(url=api_url, json=payload, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = calculate_mass_from_wurcs(wurcs='''WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1''')
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