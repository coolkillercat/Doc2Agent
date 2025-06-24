import requests
from urllib.parse import quote

def get_uniparc_entries_by_proteome_upid(upid=None, offset=0, size=100, rfDdtype=None, rfDbid=None, rfActive=None, rfTaxId=None, format="text/x-fasta"):
    """
    Get UniParc entries by Proteome UPID.
    
    Args:
        upid (str): UniProt Proteome UPID. Required.
        offset (int, optional): Off set, page starting point. Default is 0.
        size (int, optional): Page size. Default is 100. When page size is -1, it returns all records and offset will be ignored.
        rfDdtype (str, optional): Response filter by Cross reference database type, e.g EMBL, RefSeq, Ensembl, etc. Comma separated values accepted.
        rfDbid (str, optional): Response filter by all UniParc cross reference accessions, eg. AAC02967 (EMBL) or XP_006524055 (RefSeq). Comma separated values accepted.
        rfActive (str, optional): Response filter by Active(true) or not Active(false) Cross reference.
        rfTaxId (str, optional): Response filter by organism taxon ID. Comma separated values accepted.
        format (str, optional): Response format. Default is "text/x-fasta". Other options include "application/json" and "application/xml".
    
    Returns:
        Returns UniParc entries associated with a specific proteome identified by its UPID, with optional filtering by database type, accession, active status, or taxonomy ID.
    Example:
        >>> get_uniparc_entries_by_proteome_upid(upid='UP000005640', rfDdtype='EMBL,RefSeq', rfTaxId='9606')
    """
    assert upid is not None, 'Missing required parameter: upid'
    
    base_url = "https://www.ebi.ac.uk"
    api_url = f"{base_url}/proteins/api/uniparc/proteome/{quote(str(upid))}"
    
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
    
    headers = {'Content-Type': 'application/json', 'Accept': format}
    
    response = requests.get(url=api_url, params=querystring, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = get_uniparc_entries_by_proteome_upid(upid='UP000005640', offset=0, size=100, rfDdtype='EMBL,RefSeq', rfDbid='AAC02967,XP_006524055', rfActive='true', rfTaxId='9606')
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