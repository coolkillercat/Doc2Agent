import requests
from urllib.parse import quote

def get_uniparc_entry_by_uniprot_accession(accession, rfDdtype=None, rfDbid=None, rfActive=None, rfTaxId=None):
    """
    Get UniParc entry by UniProt accession.
    
    Args:
        accession (str): UniProt accession (required). Example: 'Q9NXB0-3'
        rfDdtype (str, optional): Response filter by Cross reference database type. 
                                 Comma separated values accepted. Example: 'EMBL,RefSeq'
        rfDbid (str, optional): Response filter by all UniParc cross reference accessions. 
                               Comma separated values accepted. Example: 'AAC02967,XP_006524055'
        rfActive (str, optional): Response filter by Active(true) or not Active(false) Cross reference.
                                 Example: 'true'
        rfTaxId (str, optional): Response filter by organism taxon ID. 
                                Comma separated values accepted. Example: '9606,10090'
    
    Returns:
        Returns UniParc (Universal Protein Archive) entry data for a specified UniProt accession, with optional filtering by database type, accession, active status, or taxonomy ID.
    Example:
        >>> response = get_uniparc_entry_by_uniprot_accession('Q9NXB0-3')
        >>> response = get_uniparc_entry_by_uniprot_accession('P12345', rfDdtype='EMBL,RefSeq')
    """
    base_url = "https://www.ebi.ac.uk"
    api_url = f"{base_url}/proteins/api/uniparc/accession/{quote(accession, safe='')}"
    
    # Build query parameters, excluding None values
    params = {}
    if rfDdtype is not None:
        params['rfDdtype'] = rfDdtype
    if rfDbid is not None:
        params['rfDbid'] = rfDbid
    if rfActive is not None:
        params['rfActive'] = rfActive
    if rfTaxId is not None:
        params['rfTaxId'] = rfTaxId
    
    headers = {'Content-Type': 'application/json'}
    
    response = requests.get(url=api_url, params=params, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = get_uniparc_entry_by_uniprot_accession(accession='Q9NXB0-3', rfDdtype='EMBL,RefSeq', rfDbid='AAC02967,XP_006524055', rfActive='true', rfTaxId='9606,10090')
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