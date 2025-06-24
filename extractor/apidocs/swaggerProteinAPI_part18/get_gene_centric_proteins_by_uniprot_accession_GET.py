import requests
from urllib.parse import quote

def get_gene_centric_proteins_by_uniprot_accession(accession=None):
    """
    Get gene centric proteins by Uniprot accession.
    
    Args:
        accession (str): UniProt accession (e.g., 'Q9NXB0-3', 'P12345')
    
    Returns:
        Returns gene-centric protein information associated with a specified UniProt accession, including gene name, type, and length.
    Examples:
        >>> response = get_gene_centric_proteins_by_uniprot_accession(accession='Q9NXB0-3')
        >>> response = get_gene_centric_proteins_by_uniprot_accession(accession='P12345')
    """
    base_url = "https://www.ebi.ac.uk"
    api_url = f"{base_url}/proteins/api/genecentric/{quote(accession)}"
    headers = {'Content-Type': 'application/json'}
    
    assert accession is not None, 'Missing required parameter: accession'
    
    response = requests.get(url=api_url, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = get_gene_centric_proteins_by_uniprot_accession(accession='P12345')
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