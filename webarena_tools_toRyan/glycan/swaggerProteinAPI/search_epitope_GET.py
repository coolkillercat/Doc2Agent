import requests
from urllib.parse import quote

def search_epitope(offset=0, size=100, accession=None, epitope_sequence=None, iedb_id=None, match_score=None):
    """
    Search for epitopes in UniProt.
    
    Parameters:
    -----------
    offset : int, optional
        Off set, page starting point. Default is 0.
    size : int, optional
        Page size. Default is 100. When page size is -1, it returns all records and offset will be ignored.
    accession : str, optional
        UniProt accession(s). Comma separated values accepted up to 100.
        Example: 'P12345,Q67890' or 'Q9NXB0-3'
    epitope_sequence : str, optional
        Epitope sequence.
        Example: 'AGCT'
    iedb_id : str, optional
        Epitope or antigenic determinant ID. Comma separated values accepted up to 20.
        Example: '123,456'
    match_score : int, optional
        Minimum alignment score for the antigen sequence and the target protein sequence.
        Example: 50
        
    Returns:
        Returns epitope information from UniProt based on search criteria such as accession numbers, sequences, or IEDB IDs.
    --------
    requests.Response
        The API response object.
    
    Example:
    --------
    >>> response = search_epitope(accession='Q9NXB0-3')
    >>> response = search_epitope(offset=0, size=100, accession='P12345,Q67890', epitope_sequence='AGCT', iedb_id='123,456', match_score=50)
    """
    api_url = "https://www.ebi.ac.uk/proteins/api/epitope"
    
    # Build query parameters, excluding None values
    querystring = {}
    if offset is not None:
        querystring['offset'] = offset
    if size is not None:
        querystring['size'] = size
    if accession is not None:
        querystring['accession'] = accession
    if epitope_sequence is not None:
        querystring['epitope_sequence'] = epitope_sequence
    if iedb_id is not None:
        querystring['iedb_id'] = iedb_id
    if match_score is not None:
        querystring['match_score'] = match_score
    
    headers = {'Content-Type': 'application/json'}
    
    response = requests.get(url=api_url, params=querystring, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = search_epitope(offset=0, size=100, accession='Q9NXB0-3')
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