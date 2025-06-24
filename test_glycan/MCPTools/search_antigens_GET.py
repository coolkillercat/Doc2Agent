import requests
from urllib.parse import quote

def search_antigens(offset=0, size=100, accession=None, antigen_sequence=None, antigen_id=None, ensembl_ids=None, match_score=None):
    """
    Search antigens in UniProt using the EBI API.
    
    Parameters:
    -----------
    offset : int, optional
        Off set, page starting point, with default value 0
    size : int, optional
        Page size with default value 100. When page size is -1, it returns all records and offset will be ignored
    accession : str, optional
        UniProt accession(s). Comma separated values accepted up to 100.
        Example: 'Q9NXB0-3'
    antigen_sequence : str, optional
        Antigen sequence
        Example: 'MKTAYIAKQRQISFVKSHFSRQLEERLGLIEVQ'
    antigen_id : str, optional
        Human Protein Atlas (HPA) antigen ID. Comma separated values accepted up to 20.
        Example: 'HPA000123,HPA000456'
    ensembl_ids : str, optional
        Ensembl IDs. Comma separated values accepted up to 20.
        Example: 'ENSG00000139618,ENSG00000248378'
    match_score : int, optional
        Minimum alignment score for the antigen sequence and the target protein sequence
        Example: 50
        
    Returns:
        Returns antigen data from UniProt including accession numbers, sequences, and related identifiers based on search criteria.
    --------
    requests.Response
        The API response object
    """
    base_url = "https://www.ebi.ac.uk"
    api_url = f"{base_url}/proteins/api/antigen"
    
    # Build query parameters, filtering out None values
    querystring = {}
    if offset is not None:
        querystring['offset'] = offset
    if size is not None:
        querystring['size'] = size
    if accession is not None:
        querystring['accession'] = accession
    if antigen_sequence is not None:
        querystring['antigen_sequence'] = antigen_sequence
    if antigen_id is not None:
        querystring['antigen_id'] = antigen_id
    if ensembl_ids is not None:
        querystring['ensembl_ids'] = ensembl_ids
    if match_score is not None:
        querystring['match_score'] = match_score
    
    headers = {'Content-Type': 'application/json'}
    
    response = requests.get(url=api_url, params=querystring, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = search_antigens(accession='Q9NXB0-3')
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