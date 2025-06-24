import requests
from urllib.parse import quote

def search_proteomics_peptide_ptm(offset=None, size=100, accession=None, taxid=None, upid=None, datasource=None, peptide=None, unique=None, ptm=None, confidence_score=None):
    """
    Search proteomics peptide post-translational modification (PTM) data from UniProt.
    
    Args:
        offset (int, optional): Off set, page starting point. Default is 0.
        size (int, optional): Page size. Default is 100. When -1, returns all records.
        accession (str, optional): UniProt accession(s). Comma separated values up to 100.
        taxid (str, optional): Organism taxon ID. Comma separated values up to 20.
        upid (str, optional): UniProt proteome UPID(s). Comma separated values up to 100.
        datasource (str, optional): Proteomics data source(s): PRIDE, PTMExchange. Comma separated values.
        peptide (str, optional): Peptide sequence. Comma separated values up to 20.
        unique (str, optional): Peptide uniqueness. Values can be 'true' or 'false'.
        ptm (str, optional): Ptm name.
        confidence_score (list, optional): PTM Confidence score(s): Bronze, Silver, Gold.
    
    Returns:
        Returns proteomics peptide post-translational modification (PTM) data from UniProt based on specified search criteria.
    Example:
        >>> search_proteomics_peptide_ptm(accession="Q9NXB0-3")
        >>> search_proteomics_peptide_ptm(accession="P12345,Q67890", ptm="Phosphorylation")
    """
    api_url = "https://www.ebi.ac.uk/proteomics-ptm"
    
    # Build query parameters, filtering out None values
    querystring = {k: v for k, v in {
        'offset': offset, 
        'size': size, 
        'accession': accession, 
        'taxid': taxid, 
        'upid': upid, 
        'datasource': datasource, 
        'peptide': peptide, 
        'unique': unique, 
        'ptm': ptm
    }.items() if v is not None}
    
    # Handle confidence_score separately as it's a multi-value parameter
    if confidence_score:
        if isinstance(confidence_score, list):
            for score in confidence_score:
                if 'confidence_score' not in querystring:
                    querystring['confidence_score'] = []
                querystring['confidence_score'].append(score)
        else:
            querystring['confidence_score'] = confidence_score
    
    headers = {'Content-Type': 'application/json'}
    
    response = requests.get(url=api_url, params=querystring, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = search_proteomics_peptide_ptm(offset=0, size=100, accession='P12345,Q67890', taxid='9606,10090', upid='UP000005640,UP000002311', datasource='PRIDE,PTMExchange', peptide='PEPTIDE1,PEPTIDE2', unique='true', ptm='Phosphorylation', confidence_score=['Gold', 'Silver'])
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