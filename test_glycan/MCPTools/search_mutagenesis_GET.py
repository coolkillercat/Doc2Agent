import requests
from urllib.parse import quote

def search_mutagenesis(offset=0, size=100, accession=None, taxid=None, dbid=None):
    """
    Search mutagenesis information in UniProt.
    
    Parameters:
    -----------
    offset : int, optional
        Page starting point, default is 0.
    size : int, optional
        Page size, default is 100. When set to -1, returns all records.
    accession : str, optional
        UniProt accession(s). Comma separated values accepted up to 100.
        Example: 'P12345,Q67890' or 'Q9NXB0-3'
    taxid : str, optional
        Organism taxon ID. Comma separated values accepted up to 20.
        Example: '9606,10090'
    dbid : str, optional
        Cross-reference database ID. Comma separated values accepted up to 20.
        Example: 'rs121918508,COSM29836'
    
    Returns:
        Returns mutagenesis information from UniProt based on specified protein accessions, taxonomy IDs, and database cross-references.
    --------
    requests.Response
        The API response object.
    
    Example:
    --------
    >>> response = search_mutagenesis(accession='Q9NXB0-3')
    >>> response = search_mutagenesis(offset=0, size=100, accession='P12345,Q67890', taxid='9606,10090', dbid='rs121918508,COSM29836')
    """
    api_url = "https://www.ebi.ac.uk/proteins/api/mutagenesis"
    
    # Remove None values from parameters
    params = {k: v for k, v in {
        'offset': offset,
        'size': size,
        'accession': accession,
        'taxid': taxid,
        'dbid': dbid
    }.items() if v is not None}
    
    headers = {'Content-Type': 'application/json'}
    
    response = requests.get(url=api_url, params=params, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = search_mutagenesis(offset=0, size=100, accession='P12345,Q67890', taxid='9606,10090', dbid='rs121918508,COSM29836')
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