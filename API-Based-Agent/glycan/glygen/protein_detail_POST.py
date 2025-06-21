import requests
import json
from urllib.parse import quote

def protein_detail(uniprot_canonical_ac='P14210', payload=None):
    """
    Retrieve detailed protein information from the GlyGen API.
    
    Args:
        uniprot_canonical_ac (str): UniProt canonical accession code for the protein.
            Example: 'P14210'
        payload (dict, optional): Additional parameters to send with the request.
            Default is an empty dictionary.
    
    Returns:
        requests.Response: Response object containing detailed protein information including 
        sequence, mass, function, glycosylation, disease associations, and structural data.
    
    Example:
        >>> response = protein_detail('P14210')
        >>> data = response.json()
    """
    api_url = f"https://api.glygen.org/protein/detail/{uniprot_canonical_ac}/"
    
    if payload is None:
        payload = {}
    
    headers = {'Content-Type': 'application/json'}
    
    assert uniprot_canonical_ac is not None, 'Missing required parameter: uniprot_canonical_ac'
    
    response = requests.post(url=api_url, json=payload, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = protein_detail(uniprot_canonical_ac='P14210', payload={})
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