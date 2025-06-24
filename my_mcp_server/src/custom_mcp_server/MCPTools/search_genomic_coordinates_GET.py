import requests

def search_genomic_coordinates(offset=0, size=100, accession=None, chromosome=None, ensembl=None, gene=None, protein=None, taxid=None, location=None, format="json"):
    """
    Search genomic coordinates for UniProt entries.
    
    Parameters:
    -----------
    offset : int, optional
        Offset, page starting point, with default value 0.
    size : int, optional
        Page size with default value 100. When page size is -1, it returns all records and offset will be ignored.
    accession : str, optional
        UniProt accession(s). Comma separated values accepted up to 100.
        Example: 'P12345,Q67890'
    chromosome : str, optional
        Chromosome name, i.e. 1, 2, X, etc. Comma separated values accepted up to 20.
        Example: '1,2,X'
    ensembl : str, optional
        Ensembl gene ID, transcript ID or translation ID. Comma separated values accepted up to 20.
        Example: 'ENSG00000139618,ENST00000380152'
    gene : str, optional
        UniProt gene name. Comma separated values accepted up to 20.
        Example: 'BRCA1,TP53'
    protein : str, optional
        UniProt protein name.
        Example: 'Hemoglobin'
    taxid : str, optional
        Organism taxon ID. Comma separated values accepted up to 20.
        Example: '9606,10090'
    location : str, optional
        Genome location range such as 58205437-58219305 (genome start to genome end).
        Example: '58205437-58219305'
    format : str, optional
        Response format: 'json', 'xml', or 'gff'. Default is 'json'.
    
    Returns:
        Returns genomic coordinate information for UniProt protein entries based on various search criteria such as accession, chromosome, gene name, or location.
    --------
    requests.Response
        The API response object.
    
    Example:
    --------
    >>> response = search_genomic_coordinates(accession='Q9NXB0-3')
    >>> response.status_code
    200
    """
    api_url = "https://www.ebi.ac.uk/proteins/api/coordinates"
    
    # Build query parameters, excluding None values
    querystring = {}
    if offset is not None:
        querystring['offset'] = offset
    if size is not None:
        querystring['size'] = size
    if accession is not None:
        querystring['accession'] = accession
    if chromosome is not None:
        querystring['chromosome'] = chromosome
    if ensembl is not None:
        querystring['ensembl'] = ensembl
    if gene is not None:
        querystring['gene'] = gene
    if protein is not None:
        querystring['protein'] = protein
    if taxid is not None:
        querystring['taxid'] = taxid
    if location is not None:
        querystring['location'] = location
    
    # Set appropriate headers based on requested format
    headers = {}
    if format.lower() == "json":
        headers['Accept'] = 'application/json'
    elif format.lower() == "xml":
        headers['Accept'] = 'application/xml'
    elif format.lower() == "gff":
        headers['Accept'] = 'text/x-gff'
    else:
        headers['Accept'] = 'application/json'
    
    response = requests.get(url=api_url, params=querystring, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = search_genomic_coordinates(offset=0, size=100, accession='Q9NXB0-3', format="xml")
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