import requests
from urllib.parse import quote

def search_gene_centric_proteins(offset=0, size=100, upid=None, accession=None, gene=None):
    """
    Search gene centric proteins using the EBI API.
    
    Parameters:
    -----------
    offset : int, optional
        Off set, page starting point. Default is 0.
    size : int, optional
        Page size. Default is 100. When set to -1, returns all records and offset is ignored.
    upid : str, optional
        UniProt proteome UPID(s). Comma separated values accepted up to 100.
        Example: 'UP000005640'
    accession : str, optional
        UniProt accession(s). Comma separated values accepted up to 100.
        Example: 'P12345', 'Q9NXB0-3'
    gene : str, optional
        Unique gene identifier found in MOD, Ensembl, Ensembl Genomes, OLN, ORF or UniProt Gene Name database.
        Comma separated values accepted up to 20.
        Example: 'BRCA1', 'SP1'
    
    Returns:
        Returns gene-centric protein information from the EBI Proteins API based on proteome ID, UniProt accession, or gene identifier.
    --------
    requests.Response
        The API response object.
    
    Examples:
    ---------
    >>> response = search_gene_centric_proteins(accession='Q9NXB0-3')
    >>> response = search_gene_centric_proteins(gene='BRCA1')
    >>> response = search_gene_centric_proteins(upid='UP000005640', size=10)
    """
    api_url = "https://www.ebi.ac.uk/proteins/api/genecentric"
    
    # Remove None values from querystring
    querystring = {}
    if offset is not None:
        querystring['offset'] = offset
    if size is not None:
        querystring['size'] = size
    if upid is not None:
        querystring['upid'] = upid
    if accession is not None:
        querystring['accession'] = accession
    if gene is not None:
        querystring['gene'] = gene
    
    headers = {'Content-Type': 'application/json'}
    
    response = requests.get(url=api_url, params=querystring, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = search_gene_centric_proteins(offset=0, size=100, upid='UP000005640', accession='P12345', gene='BRCA1')
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