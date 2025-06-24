import requests
from urllib.parse import quote

def get_uniprot_entries_by_genomic_database_cross_reference_ids(dbtype=None, dbid=None, offset=0, size=100):
    """
    Search UniProt entries by genomic database cross reference IDs: Ensembl, CCDS, HGNC or RefSeq.
    
    Parameters:
    -----------
    dbtype : str
        Cross-reference database type: Ensembl, CCDS, HGNC or RefSeq
    dbid : str
        Cross reference ID, such as ENSP00000351276 for Ensembl, NP_083392 for RefSeq, 
        CCDS52493 for CCDS, 26588 for HGNC (case insensitive)
    offset : int, optional
        Off set, page starting point, with default value 0
    size : int, optional
        Page size with default value 100. When page size is -1, it returns all records and offset will be ignored
    
    Returns:
        Returns UniProt protein entries that match specified genomic database cross-references from Ensembl, CCDS, HGNC, or RefSeq.
    --------
    requests.Response
        The API response object
    
    Examples:
    ---------
    >>> get_uniprot_entries_by_genomic_database_cross_reference_ids(dbtype='Ensembl', dbid='ENSP00000351276')
    >>> get_uniprot_entries_by_genomic_database_cross_reference_ids(dbtype='RefSeq', dbid='NP_083392', size=10)
    """
    assert dbtype is not None, 'Missing required parameter: dbtype'
    assert dbid is not None, 'Missing required parameter: dbid'
    
    base_url = "https://www.ebi.ac.uk"
    api_url = f"{base_url}/proteins/api/coordinates/{quote(dbtype, safe='')}:{quote(dbid, safe='')}"
    
    querystring = {}
    if offset is not None:
        querystring['offset'] = offset
    if size is not None:
        querystring['size'] = size
    
    headers = {'Content-Type': 'application/json'}
    
    response = requests.get(url=api_url, params=querystring, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = get_uniprot_entries_by_genomic_database_cross_reference_ids(dbtype='Ensembl', dbid='ENSP00000351276', offset=0, size=100)
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