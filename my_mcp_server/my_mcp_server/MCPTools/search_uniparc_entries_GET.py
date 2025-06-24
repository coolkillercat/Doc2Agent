import requests
from urllib.parse import quote

def search_uniparc_entries(offset=0, size=100, upi=None, dbtype=None, accession=None, dbid=None, gene=None, protein=None, taxid=None, organism=None, sequencechecksum=None, ipr=None, signaturetype=None, signatureid=None, upid=None, seqLength=None, rfDdtype=None, rfDbid=None, rfActive=None, rfTaxId=None):
    """
    Search UniParc entries using the EBI UniParc API.
    
    Parameters:
    -----------
    offset : int, optional
        Off set, page starting point, with default value 0
    size : int, optional
        Page size with default value 100. When page size is -1, it returns all records and offset will be ignored
    upi : str, optional
        UniParc ID (UPI). Comma separated values accepted up to 100
    dbtype : str, optional
        Search by Cross reference database type, e.g EMBL, RefSeq, Ensembl, etc.
    accession : str, optional
        UniProt accession(s). Comma separated values accepted up to 100. Example: 'Q9NXB0-3'
    dbid : str, optional
        All UniParc cross reference accessions, eg. AAC02967 (EMBL) or XP_006524055 (RefSeq). Comma separated values accepted up to 100.
    gene : str, optional
        UniProt gene name. Comma separated values accepted up to 20.
    protein : str, optional
        UniProt protein name
    taxid : str, optional
        Organism taxon ID. Comma separated values accepted up to 20.
    organism : str, optional
        Organism name
    sequencechecksum : str, optional
        Sequence CRC64 checksum. eg 4104A3A57D1B08E3
    ipr : str, optional
        Search by InterPro identifier(s). Comma separated values accepted up to 20.
    signaturetype : str, optional
        Search by signature database type, e.g. SMART, SUPFAM, Pfam, PIRSF, PROSITE, etc. Comma separated values accepted up to 20.
    signatureid : str, optional
        Search by signature database id, e.g. SM00044, SSF55073, PF00211, PIRSF039050, PS00452, etc. Comma separated values accepted up to 20.
    upid : str, optional
        UniProt proteome UPID(s). Comma separated values accepted up to 100.
    seqLength : str, optional
        Sequence length. Sequence length can be a single length value such as 123 or range 123-234
    rfDdtype : str, optional
        Response filter by Cross reference database type, e.g EMBL, RefSeq, Ensembl, etc. Comma separated values accepted.
    rfDbid : str, optional
        Response filter by all UniParc cross reference accessions, eg. AAC02967 (EMBL) or XP_006524055 (RefSeq). Comma separated values accepted.
    rfActive : str, optional
        Response filter by Active(true) or not Active(false) Cross reference.
    rfTaxId : str, optional
        Response filter by organism taxon ID. Comma separated values accepted.
    
    Returns:
        Returns UniParc entries containing protein sequence data, cross-references, signature sequence matches, and dataset information.
    --------
    requests.Response
        The API response object
    
    Example:
    --------
    >>> response = search_uniparc_entries(accession='Q9NXB0-3')
    >>> response = search_uniparc_entries(upi='UPI0000000001', dbtype='EMBL')
    """
    api_url = "https://www.ebi.ac.uk/proteins/api/uniparc"
    
    # Build query parameters, filtering out None values
    querystring = {k: v for k, v in {
        'offset': offset, 
        'size': size, 
        'upi': upi, 
        'dbtype': dbtype, 
        'accession': accession, 
        'dbid': dbid, 
        'gene': gene, 
        'protein': protein, 
        'taxid': taxid, 
        'organism': organism, 
        'sequencechecksum': sequencechecksum, 
        'ipr': ipr, 
        'signaturetype': signaturetype, 
        'signatureid': signatureid, 
        'upid': upid, 
        'seqLength': seqLength, 
        'rfDdtype': rfDdtype, 
        'rfDbid': rfDbid, 
        'rfActive': rfActive, 
        'rfTaxId': rfTaxId
    }.items() if v is not None}
    
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    
    response = requests.get(url=api_url, params=querystring, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = search_uniparc_entries(accession='Q9NXB0-3')
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