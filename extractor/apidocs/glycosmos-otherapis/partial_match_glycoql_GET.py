import requests
import json
from urllib.parse import quote

def partial_match_glycoql(glycoct=None, wurcs=None):
    """
    Query the GlycosmoS API for partial matches using GlycoCT or WURCS format.
    
    Parameters:
    -----------
    glycoct : str, optional
        GlycoCT format text.
        Example: 
        ```
        RES
        1b:x-dglc-HEX-1:5
        2b:b-dgal-HEX-1:5
        3b:a-dgal-HEX-1:5
        4b:b-dgal-HEX-1:5
        5s:n-acetyl
        6b:a-dgal-HEX-1:5
        7s:n-acetyl
        LIN
        1:1o(4+1)2d
        2:2o(3+1)3d
        3:3o(3+1)4d
        4:4d(2+1)5n
        5:4o(3+1)6d
        6:6d(2+1)7n
        ```
    
    wurcs : str, optional
        WURCS format text.
        Example: 
        ```
        WURCS=2.0/5,5,4/[a2122h-1x_1-5][a2112h-1b_1-5][a2112h-1a_1-5][a2112h-1b_1-5_2*NCC/3=O][a2112h-1a_1-5_2*NCC/3=O]/1-2-3-4-5/a4-b1_b3-c1_c3-d1_d3-e1
        ```
    
    Returns:
    --------
    requests.Response
        The API response object containing the matching results.
    """
    api_url = "https://api.glycosmos.org/partialmatch/glycoql"
    
    # Only include non-None parameters
    params = {}
    if glycoct is not None:
        params['glycoct'] = glycoct
    if wurcs is not None:
        params['wurcs'] = wurcs
    
    response = requests.get(
        url=api_url,
        params=params,
        timeout=50,
        verify=True  # Enable SSL verification for security
    )
    
    return response

if __name__ == '__main__':
    r = partial_match_glycoql(
        glycoct='''RES
1b:x-dglc-HEX-1:5
2b:b-dgal-HEX-1:5
3b:a-dgal-HEX-1:5
4b:b-dgal-HEX-1:5
5s:n-acetyl
6b:a-dgal-HEX-1:5
7s:n-acetyl
LIN
1:1o(4+1)2d
2:2o(3+1)3d
3:3o(3+1)4d
4:4d(2+1)5n
5:4o(3+1)6d
6:6d(2+1)7n''',
        wurcs=None  # Only use one parameter at a time to avoid confusion
    )
    
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