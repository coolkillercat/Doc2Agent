import requests
from urllib.parse import quote

def get_uniparc_entries_by_cross_reference_accessions(dbid, offset=0, size=100, rfDdtype=None, rfDbid=None, rfActive=None, rfTaxId=None, format="fasta"):
    """
    Get UniParc entries by all UniParc cross reference accessions.
    
    Parameters:
    -----------
    dbid : str
        All UniParc cross reference accessions, eg. AAC02967 (EMBL) or XP_006524055 (RefSeq).
    offset : int, optional
        Off set, page starting point, with default value 0.
    size : int, optional
        Page size with default value 100. When page size is -1, it returns all records and offset will be ignored.
    rfDdtype : str, optional
        Response filter by Cross reference database type, e.g EMBL, RefSeq, Ensembl, etc. Comma separated values accepted.
    rfDbid : str, optional
        Response filter by all UniParc cross reference accessions. Comma separated values accepted.
    rfActive : str, optional
        Response filter by Active(true) or not Active(false) Cross reference.
    rfTaxId : str, optional
        Response filter by organism taxon ID. Comma separated values accepted.
    format : str, optional
        Response format. Options: "json", "xml", "fasta". Default is "fasta".
    
    Returns:
        Returns UniParc entries that match specified cross-reference accessions with optional filtering by database type, activity status, and taxonomy.
    --------
    requests.Response
        The API response object.
    
    Examples:
    ---------
    >>> get_uniparc_entries_by_cross_reference_accessions(dbid='AAC02967')
    >>> get_uniparc_entries_by_cross_reference_accessions(dbid='AAC02967', rfDdtype='EMBL,RefSeq', rfActive='true', rfTaxId='9606')
    >>> get_uniparc_entries_by_cross_reference_accessions(dbid='UPI0000000114', format='fasta')
    """
    base_url = "https://www.ebi.ac.uk"
    api_url = f"{base_url}/proteins/api/uniparc/dbreference/{quote(str(dbid))}"
    
    querystring = {}
    if offset is not None:
        querystring['offset'] = offset
    if size is not None:
        querystring['size'] = size
    if rfDdtype is not None:
        querystring['rfDdtype'] = rfDdtype
    if rfDbid is not None:
        querystring['rfDbid'] = rfDbid
    if rfActive is not None:
        querystring['rfActive'] = rfActive
    if rfTaxId is not None:
        querystring['rfTaxId'] = rfTaxId
    
    headers = {'Content-Type': 'application/json'}
    
    # Set the Accept header based on the format parameter
    if format.lower() == "json":
        headers['Accept'] = 'application/json'
    elif format.lower() == "xml":
        headers['Accept'] = 'application/xml'
    elif format.lower() == "fasta":
        headers['Accept'] = 'text/x-fasta'
    
    response = requests.get(url=api_url, params=querystring, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = get_uniparc_entries_by_cross_reference_accessions(dbid='UPI0000000114', format='fasta')
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