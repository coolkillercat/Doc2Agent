import requests
from urllib.parse import quote

def get_uniprot_entries_by_cross_reference(dbtype=None, dbid=None, offset=0, size=100, reviewed=None, isoform=None, format="json"):
    """
    Get UniProt entries by UniProt cross reference and its ID.
    
    Args:
        dbtype (str): Cross reference database type, e.g, Ensembl, PDBe, etc.
        dbid (str): Cross-reference ID, e.g. ENSP00000351276 for Ensembl
        offset (int, optional): Off set, page starting point. Defaults to 0.
        size (int, optional): Page size. When page size is -1, it returns all records. Defaults to 100.
        reviewed (str, optional): Reviewed(true) or not Reviewed (false). Defaults to None.
        isoform (int, optional): 0 for exclude isoform only and 1 for isoform only. Defaults to None.
        format (str, optional): Response format (json, xml, fasta, flatfile). Defaults to "json".
    
    Returns:
        requests.Response: Response object from the API request
    
    Examples:
        >>> get_uniprot_entries_by_cross_reference(dbtype='Ensembl', dbid='ENSP00000351276')
        >>> get_uniprot_entries_by_cross_reference(dbtype='Ensembl', dbid='ENSP00000351276', reviewed='true', isoform=0)
        >>> get_uniprot_entries_by_cross_reference(dbtype='UniProtKB', dbid='Q9NXB0-3', format='fasta')
    """
    assert dbtype is not None, 'Missing required parameter: dbtype'
    assert dbid is not None, 'Missing required parameter: dbid'
    
    base_url = "https://www.ebi.ac.uk"
    api_url = f"{base_url}/proteins/api/proteins/{quote(dbtype)}:{quote(dbid)}"
    
    querystring = {}
    if offset is not None:
        querystring['offset'] = offset
    if size is not None:
        querystring['size'] = size
    if reviewed is not None:
        querystring['reviewed'] = reviewed
    if isoform is not None:
        querystring['isoform'] = isoform
    
    headers = {'Content-Type': 'application/json'}
    
    # Set the Accept header based on the requested format
    if format == "json":
        headers['Accept'] = 'application/json'
    elif format == "xml":
        headers['Accept'] = 'application/xml'
    elif format == "fasta":
        headers['Accept'] = 'text/x-fasta'
    elif format == "flatfile":
        headers['Accept'] = 'text/x-flatfile'
    
    response = requests.get(url=api_url, params=querystring, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = get_uniprot_entries_by_cross_reference(dbtype='UniProtKB', dbid='Q9NXB0-3', offset=0, size=100, reviewed='true', isoform=0)
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