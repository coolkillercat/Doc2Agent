import requests
from urllib.parse import quote

def search_protein_sequence_features(offset=0, size=100, accession=None, reviewed=None, gene=None, exact_gene=None, protein=None, organism=None, taxid=None, categories=None, types=None):
    """
    Search protein sequence features in UniProt.
    
    Parameters:
    -----------
    offset : int, optional
        Off set, page starting point, with default value 0
    size : int, optional
        Page size with default value 100. When page size is -1, it returns all records and offset will be ignored
    accession : str, optional
        UniProt accession(s). Comma separated values accepted up to 100.
        Example: 'P12345,Q67890' or 'Q9NXB0-3'
    reviewed : str, optional
        The reviewed parameter can only be true or false
        Example: 'true'
    gene : str, optional
        UniProt gene name. Comma separated values accepted up to 20.
        Example: 'BRCA1,TP53'
    exact_gene : str, optional
        UniProt exact gene name. Comma separated values accepted up to 20.
        Example: 'BRCA1,TP53'
    protein : str, optional
        UniProt protein name
        Example: 'Hemoglobin'
    organism : str, optional
        Organism name
        Example: 'Homo sapiens'
    taxid : str, optional
        Organism taxon ID. Comma separated values accepted up to 20.
        Example: '9606,10090'
    categories : str, optional
        Category type(s): MOLECULE_PROCESSING, TOPOLOGY, SEQUENCE_INFORMATION, STRUCTURAL, DOMAINS_AND_SITES, PTM, VARIANTS, MUTAGENESIS. Comma separated values accepted up to 20
        Example: 'MOLECULE_PROCESSING,TOPOLOGY'
    types : str, optional
        Feature type(s): INIT_MET, SIGNAL, PROPEP, TRANSIT, CHAIN, PEPTIDE, TOPO_DOM, TRANSMEM, DOMAIN, REPEAT, ZN_FING, DNA_BIND, REGION, COILED, MOTIF, COMPBIAS, ACT_SITE, BINDING, SITE, NON_STD, MOD_RES, LIPID, CARBOHYD, DISULFID, CROSSLNK, VAR_SEQ, VARIANT, MUTAGEN, UNSURE, CONFLICT, NON_CONS, NON_TER, HELIX, TURN, STRAND, INTRAMEM. Comma separated values accepted up to 20
        Example: 'INIT_MET,SIGNAL'
    
    Returns:
        Returns protein sequence features from UniProt based on search criteria such as accession numbers, genes, organisms, and feature types.
    --------
    response : requests.Response
        The API response object
    
    Example:
    --------
    >>> response = search_protein_sequence_features(accession='Q9NXB0-3')
    >>> response = search_protein_sequence_features(offset=0, size=100, accession='P12345,Q67890', reviewed='true', gene='BRCA1,TP53')
    """
    api_url = "https://www.ebi.ac.uk/proteins/api/features"
    
    # Remove None values from querystring
    querystring = {k: v for k, v in {
        'offset': offset, 
        'size': size, 
        'accession': accession, 
        'reviewed': reviewed, 
        'gene': gene, 
        'exact_gene': exact_gene, 
        'protein': protein, 
        'organism': organism, 
        'taxid': taxid, 
        'categories': categories, 
        'types': types
    }.items() if v is not None}
    
    headers = {'Content-Type': 'application/json'}
    
    response = requests.get(url=api_url, params=querystring, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = search_protein_sequence_features(offset=0, size=100, accession='P12345,Q67890', reviewed='true', gene='BRCA1,TP53', exact_gene='BRCA1,TP53', protein='Hemoglobin', organism='Homo sapiens', taxid='9606,10090', categories='MOLECULE_PROCESSING,TOPOLOGY', types='INIT_MET,SIGNAL')
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