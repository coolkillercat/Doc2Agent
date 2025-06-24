import requests
import json
from urllib.parse import quote

def partial_match_wurcs_rdf(wurcs=None):
    """
    Retrieve glycan structures that partially match the provided WURCS format text.
    
    Args:
        wurcs (str): WURCS format text to match against.
            Example: "WURCS=2.0/5,5,4/[a2122h-1x_1-5][a2112h-1b_1-5][a2112h-1a_1-5][a2112h-1b_1-5_2*NCC/3=O][a2112h-1a_1-5_2*NCC/3=O]/1-2-3-4-5/a4-b1_b3-c1_c3-d1_d3-e1"
    
    Returns:
        Returns a list of glycan structures that partially match the provided WURCS format text, including their IDs and WURCS representations.
    Raises:
        AssertionError: If the required wurcs parameter is not provided.
    """
    api_url = "https://api.glycosmos.org/partialmatch/wurcsrdf"
    assert wurcs is not None, 'Missing required parameter: wurcs'
    
    querystring = {'wurcs': wurcs}
    headers = {}
    
    response = requests.get(url=api_url, params=querystring, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = partial_match_wurcs_rdf(wurcs='WURCS=2.0/5,5,4/[a2122h-1x_1-5][a2112h-1b_1-5][a2112h-1a_1-5][a2112h-1b_1-5_2*NCC/3=O][a2112h-1a_1-5_2*NCC/3=O]/1-2-3-4-5/a4-b1_b3-c1_c3-d1_d3-e1')
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