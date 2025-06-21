import requests
from urllib.parse import quote

def get_uniparc_best_guess(upi=None, accession=None, dbid=None, gene=None, taxid=None, format=None):
    """
    Get UniParc longest sequence for entries.
    
    For a given user input (request parameters), Best Guess returns the UniParcEntry 
    with a cross-reference to the longest active UniProtKB sequence (preferably from 
    Swiss-Prot and if not then TrEMBL). It also returns the sequence and related information.
    
    Parameters:
    -----------
    upi : str, optional
        UniParc ID (UPI). Comma separated values accepted up to 100.
        Example: 'UPI0000000001'
    accession : str, optional
        UniProt accession(s). Comma separated values accepted up to 100.
        Example: 'P12345' or 'Q9NXB0-3'
    dbid : str, optional
        All UniParc cross reference accessions, eg. AAC02967 (EMBL) or XP_006524055 (RefSeq).
        Comma separated values accepted up to 100.
        Example: 'AAC02967'
    gene : str, optional
        UniProt gene name. Comma separated values accepted up to 20.
        Example: 'BRCA1'
    taxid : str, optional
        Organism taxon ID. Comma separated values accepted up to 20.
        Example: '9606'
    format : str, optional
        Response format. Options: 'json', 'xml', 'fasta'
        
    Returns:
        Returns the UniParc entry with a cross-reference to the longest active UniProtKB sequence, including sequence data and related information.
    --------
    requests.Response
        The API response object
    
    Example:
    --------
    >>> response = get_uniparc_best_guess(accession='Q9NXB0-3')
    >>> response.status_code
    200
    """
    base_url = "https://www.ebi.ac.uk"
    api_url = f"{base_url}/proteins/api/uniparc/bestguess"
    
    # Filter out None values
    params = {k: v for k, v in {
        'upi': upi,
        'accession': accession,
        'dbid': dbid,
        'gene': gene,
        'taxid': taxid
    }.items() if v is not None}
    
    headers = {'Content-Type': 'application/json'}
    
    # Add format to Accept header if specified
    if format:
        if format.lower() == 'json':
            headers['Accept'] = 'application/json'
        elif format.lower() == 'xml':
            headers['Accept'] = 'application/xml'
        elif format.lower() == 'fasta':
            headers['Accept'] = 'text/x-fasta'
    
    response = requests.get(url=api_url, params=params, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = get_uniparc_best_guess(accession='Q9NXB0-3')
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