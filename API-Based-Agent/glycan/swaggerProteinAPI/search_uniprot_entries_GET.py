import requests
from urllib.parse import quote

def search_uniprot_entries(offset=0, size=100, accession=None, reviewed=None, isoform=None, goterms=None, 
                          keywords=None, ec=None, gene=None, exact_gene=None, protein=None, organism=None, 
                          taxid=None, pubmed=None, seqLength=None, md5=None):
    """
    Search UniProt entries using the EBI API.
    
    Parameters:
    -----------
    offset : int, optional
        Off set, page starting point, with default value 0
    size : int, optional
        Page size with default value 100. When page size is -1, it returns all records and offset will be ignored
    accession : str, optional
        UniProt accession(s). Comma separated values accepted up to 100.
        Example: 'P12345,Q67890'
    reviewed : str, optional
        Reviewed(true) or not Reviewed (false)
        Example: 'true'
    isoform : int, optional
        0 for excluding isoform, 1 for isoform only and 2 for both canonical and isoform
        Example: 2
    goterms : str, optional
        GO ontology terms
        Example: 'GO:0008150'
    keywords : str, optional
        UniProt keywords
        Example: 'kinase'
    ec : str, optional
        UniProt EC number. Comma separated values accepted up to 20.
        Example: '1.1.1.1'
    gene : str, optional
        UniProt gene name. Comma separated values accepted up to 20.
        Example: 'BRCA1'
    exact_gene : str, optional
        UniProt exact gene name. Comma separated values accepted up to 20.
        Example: 'BRCA1'
    protein : str, optional
        UniProt protein name
        Example: 'Hemoglobin'
    organism : str, optional
        Organism name
        Example: 'Homo sapiens'
    taxid : str, optional
        Organism taxon ID. Comma separated values accepted up to 20.
        Example: '9606'
    pubmed : str, optional
        UniProt reference PubMed ID. Comma separated values accepted up to 20.
        Example: '12345678'
    seqLength : str, optional
        Sequence length. Sequence length can be a single length value such as 123 or range 123-234
        Example: '100-200'
    md5 : str, optional
        Sequence md5 value.
        Example: 'd41d8cd98f00b204e9800998ecf8427e'
    
    Returns:
        Returns UniProt protein entries matching specified search criteria such as accession numbers, gene names, organisms, and other biological parameters.
    --------
    response : requests.Response
        The API response object
    
    Example:
    --------
    >>> response = search_uniprot_entries(accession='Q9NXB0-3')
    >>> response = search_uniprot_entries(offset=0, size=100, accession='P12345,Q67890', reviewed='true')
    """
    api_url = "https://www.ebi.ac.uk/proteins/api/proteins"
    
    # Create a dictionary of parameters, filtering out None values
    querystring = {k: v for k, v in {
        'offset': offset, 
        'size': size, 
        'accession': accession, 
        'reviewed': reviewed, 
        'isoform': isoform, 
        'goterms': goterms, 
        'keywords': keywords, 
        'ec': ec, 
        'gene': gene, 
        'exact_gene': exact_gene, 
        'protein': protein, 
        'organism': organism, 
        'taxid': taxid, 
        'pubmed': pubmed, 
        'seqLength': seqLength, 
        'md5': md5
    }.items() if v is not None}
    
    headers = {'Content-Type': 'application/json'}
    
    response = requests.get(url=api_url, params=querystring, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = search_uniprot_entries(offset=0, size=100, accession='P12345,Q67890', reviewed='true', isoform=2, 
                              goterms='GO:0008150', keywords='kinase', ec='1.1.1.1', gene='BRCA1', 
                              exact_gene='BRCA1', protein='Hemoglobin', organism='Homo sapiens', 
                              taxid='9606', pubmed='12345678', seqLength='100-200', 
                              md5='d41d8cd98f00b204e9800998ecf8427e')
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