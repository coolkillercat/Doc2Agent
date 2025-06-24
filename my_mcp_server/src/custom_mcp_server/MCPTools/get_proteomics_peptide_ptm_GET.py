import requests
from urllib.parse import quote

def get_proteomics_peptide_ptm(accession, confidence_score=None):
    """
    Get proteomics peptide PTM mapped to UniProt by accession.
    
    Args:
        accession (str): UniProt accession (required). Example: 'Q9NXB0-3'
        confidence_score (list, optional): PTM Confidence score(s): Bronze, Silver, Gold. 
                                          Example: ['Gold', 'Silver']
    
    Returns:
        Returns proteomics peptide post-translational modifications (PTMs) for a specified UniProt protein accession with optional confidence score filtering.
    Example:
        >>> response = get_proteomics_peptide_ptm('Q9NXB0-3', ['Gold', 'Silver'])
        >>> print(response.status_code)
    """
    base_url = "https://www.ebi.ac.uk"
    api_url = f"{base_url}/proteins/api/proteomics-ptm/{quote(accession)}"
    
    headers = {'Content-Type': 'application/json'}
    
    params = {}
    if confidence_score:
        params['confidence_score'] = confidence_score
    
    response = requests.get(url=api_url, params=params, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = get_proteomics_peptide_ptm(accession='Q9NXB0-3', confidence_score=['Gold', 'Silver'])
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