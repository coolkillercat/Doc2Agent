import requests, json
from urllib.parse import quote

def get_proteomics_peptides_by_accession(accession=None):
    """
    Get proteomics peptides mapped to UniProt by accession.
    
    Args:
        accession (str): UniProt accession (e.g., 'Q9NXB0-3')
        
    Returns:
        Returns proteomics peptide data mapped to a specific UniProt accession, including sequence information and peptide features.
    Examples:
        >>> response = get_proteomics_peptides_by_accession(accession='Q9NXB0-3')
    """
    base_url = "https://www.ebi.ac.uk"
    api_url = f"{base_url}/proteins/api/proteomics/{quote(accession)}"
    headers = {'Content-Type': 'application/json'}
    
    assert accession is not None, 'Missing required parameter: accession'
    
    response = requests.get(url=api_url, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = get_proteomics_peptides_by_accession(accession='Q9NXB0-3')
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