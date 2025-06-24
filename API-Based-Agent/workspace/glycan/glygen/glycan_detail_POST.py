import requests
from urllib.parse import quote

def glycan_detail(glytoucan_ac='G17689DH', payload=None):
    """
    Retrieve detailed information about a glycan using its GlyTouCan accession.
    
    Parameters:
    -----------
    glytoucan_ac : str, optional
        The GlyTouCan accession number of the glycan. Default is 'G17689DH'.
    payload : dict, optional
        Additional parameters to send with the request. If None, a dict with glytoucan_ac will be used.
        
    Returns:
        Returns detailed information about a glycan including its chemical properties, biological associations, classifications, and cross-references based on a GlyTouCan accession number.
    --------
    requests.Response
        The response object from the API request.
        
    Examples:
    ---------
    >>> response = glycan_detail('G17689DH')
    >>> response = glycan_detail(glytoucan_ac='G01543ZX')
    """
    base_url = "https://api.glygen.org"
    api_url = f"{base_url}/glycan/detail/{quote(glytoucan_ac)}/"
    
    if payload is None:
        payload = {"glytoucan_ac": glytoucan_ac}
    
    headers = {"Content-Type": "application/json"}
    
    assert glytoucan_ac is not None, 'Missing required parameter: glytoucan_ac'
    
    response = requests.post(url=api_url, json=payload, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = glycan_detail(glytoucan_ac='G17689DH')
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