import requests
import json
from urllib.parse import quote

def get_sparql_query_for_substructure_search(wurcs, rootnode='false'):
    """
    Get SPARQL query for substructure search from WURCS.
    
    Parameters:
    -----------
    wurcs : str
        WURCS format text. Required.
    rootnode : str, optional
        Whether to include root node in the query. Default is 'false'.
        
    Returns:
    --------
    requests.Response
        Response object from the API request.
        
    Example:
    --------
    >>> wurcs_str = "WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1"
    >>> response = get_sparql_query_for_substructure_search(wurcs=wurcs_str, rootnode='true')
    """
    api_url = "https://api.glycosmos.org/wurcsrdf/1.2.6/wurcs2sparql"
    payload = {
        'wurcs': wurcs,
        'rootnode': rootnode
    }
    headers = {'Content-Type': 'application/json'}
    
    assert wurcs is not None, 'Missing required parameter: wurcs'
    
    response = requests.post(url=api_url, data=json.dumps(payload), headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = get_sparql_query_for_substructure_search(
        wurcs="WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1",
        rootnode="true"
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