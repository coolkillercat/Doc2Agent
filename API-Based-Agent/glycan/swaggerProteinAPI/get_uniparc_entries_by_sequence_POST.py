import requests
from urllib.parse import quote

def get_uniparc_entries_by_sequence(body, rfDdtype=None, rfDbid=None, rfActive=None, rfTaxId=None):
    """
    Get UniParc entries by sequence.
    
    Args:
        body (str): Protein sequence in plain text format. Required.
        rfDdtype (str, optional): Response filter by Cross reference database type, e.g EMBL, RefSeq, Ensembl, etc. Comma separated values accepted.
        rfDbid (str, optional): Response filter by all UniParc cross reference accessions, eg. AAC02967 (EMBL) or XP_006524055 (RefSeq). Comma separated values accepted.
        rfActive (str, optional): Response filter by Active(true) or not Active(false) Cross reference.
        rfTaxId (str, optional): Response filter by organism taxon ID. Comma separated values accepted.
    
    Returns:
        Returns UniParc protein sequence entries matching a provided sequence, with optional filtering by database type, accession, active status, or taxonomy ID.
    Example:
        >>> response = get_uniparc_entries_by_sequence(body="MLMPKRTKYR", rfDdtype="EMBL,RefSeq", rfActive="true")
        >>> print(response.status_code)
    """
    api_url = "https://www.ebi.ac.uk/proteins/api/uniparc/sequence"
    headers = {'Content-Type': 'text/plain'}
    
    assert body is not None, 'Missing required parameter: body'
    
    params = {}
    if rfDdtype:
        params['rfDdtype'] = rfDdtype
    if rfDbid:
        params['rfDbid'] = rfDbid
    if rfActive:
        params['rfActive'] = rfActive
    if rfTaxId:
        params['rfTaxId'] = rfTaxId
    
    response = requests.post(url=api_url, data=body, headers=headers, params=params, timeout=50)
    return response

if __name__ == '__main__':
    r = get_uniparc_entries_by_sequence(body='''MLMPKRTKYR''', rfDdtype='''EMBL,RefSeq''', rfDbid='''AAC02967,XP_006524055''', rfActive='''true''', rfTaxId='''9606,10090''')
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