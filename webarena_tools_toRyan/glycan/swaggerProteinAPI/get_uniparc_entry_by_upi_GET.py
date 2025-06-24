import requests
from urllib.parse import quote

def get_uniparc_entry_by_upi(upi, rfDdtype=None, rfDbid=None, rfActive=None, rfTaxId=None):
    """
    Get UniParc entry by UniParc UPI.
    
    Args:
        upi (str): UniParc ID (UPI), required. Example: 'UPI0000000001'
        rfDdtype (str, optional): Response filter by Cross reference database type, e.g EMBL, RefSeq, Ensembl, etc. 
                                 Comma separated values accepted. Example: 'EMBL,RefSeq'
        rfDbid (str, optional): Response filter by all UniParc cross reference accessions, eg. AAC02967 (EMBL) or 
                               XP_006524055 (RefSeq). Comma separated values accepted. Example: 'AAC02967,XP_006524055'
        rfActive (str, optional): Response filter by Active(true) or not Active(false) Cross reference. Example: 'true'
        rfTaxId (str, optional): Response filter by organism taxon ID. Comma separated values accepted. Example: '9606,10090'
    
    Returns:
        Returns a UniParc protein sequence entry with its cross-references and metadata based on the provided UniParc UPI identifier.
    Example:
        >>> response = get_uniparc_entry_by_upi(upi='UPI0000000001')
        >>> response = get_uniparc_entry_by_upi(upi='UPI0000000001', rfDdtype='EMBL,RefSeq', rfTaxId='9606')
    """
    base_url = "https://www.ebi.ac.uk"
    api_url = f"{base_url}/proteins/api/uniparc/upi/{quote(upi, safe='')}"
    
    # Remove upi from querystring as it's already in the path
    querystring = {}
    if rfDdtype is not None:
        querystring['rfDdtype'] = rfDdtype
    if rfDbid is not None:
        querystring['rfDbid'] = rfDbid
    if rfActive is not None:
        querystring['rfActive'] = rfActive
    if rfTaxId is not None:
        querystring['rfTaxId'] = rfTaxId
    
    headers = {'Content-Type': 'application/json'}
    
    assert upi is not None, 'Missing required parameter: upi'
    
    response = requests.get(url=api_url, params=querystring, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = get_uniparc_entry_by_upi(upi='UPI0000000001', rfDdtype='EMBL,RefSeq', rfDbid='AAC02967,XP_006524055', rfActive='true', rfTaxId='9606,10090')
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