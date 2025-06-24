import requests
import json
from urllib.parse import quote

def build3dstructure(sequence, buildOptions=None):
    """
    Build a 3D structure for a given sequence using the GEMS API.
    
    This function sends a request to the GEMS API to build a 3D structure for the provided
    glycan sequence. It can optionally include build options to customize the structure generation.
    
    Parameters:
    -----------
    sequence : str
        The glycan sequence to build, e.g., "DManpa1-6DManpa1-OH"
    buildOptions : dict, optional
        Dictionary of build options. For example, {'conformers': 64} to request 64 conformers.
    
    Returns:
    --------
    dict
        The JSON response from the API request
    
    Examples:
    ---------
    >>> response = build3dstructure("DManpa1-6DManpa1-OH")
    >>> response = build3dstructure("DManpa1-6DManpa1-OH", buildOptions={'conformers': 64})
    """
    api_url = "https://glycam.org/json/api/build3dstructure/"
    
    payload = {
        'entity': {
            'type': 'sequence',
            'sequence': sequence
        }
    }
    
    if buildOptions:
        payload['entity']['buildOptions'] = buildOptions
    
    headers = {
        'Content-Type': 'application/json'
    }
    
    assert sequence is not None, 'Missing required parameter: sequence'
    
    response = requests.post(url=api_url, json=payload, headers=headers, timeout=50)
    
    if response.status_code == 200:
        return response.json()
    return response

if __name__ == '__main__':
    r = build3dstructure(sequence='''DManpa1-6DManpa1-OH''', buildOptions={'conformers': 64})
    r_json = None
    try:
        if isinstance(r, dict):
            r_json = r
            r_content = json.dumps(r)
            r_text = json.dumps(r)
            r_status_code = 200
        else:
            r_json = None
            r_content = r.content.decode("utf-8")
            r_text = r.text
            r_status_code = r.status_code
    except:
        if isinstance(r, dict):
            r_json = r
            r_content = json.dumps(r)
            r_text = json.dumps(r)
            r_status_code = 200
        else:
            r_content = r.content.decode("utf-8")
            r_text = r.text
            r_status_code = r.status_code
    
    result_dict = dict()
    result_dict['status_code'] = r_status_code
    result_dict['text'] = r_text
    result_dict['json'] = r_json
    result_dict['content'] = r_content
    print(json.dumps(result_dict, indent=4))