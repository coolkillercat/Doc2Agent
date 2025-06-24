import requests
from urllib.parse import quote

def get_uniprot_entry_by_accession(accession=None, format="json"):
    """
    Get UniProt entry by accession.
    
    Args:
        accession (str): UniProt accession ID (e.g., 'P12345', 'Q9NXB0-3')
        format (str, optional): Response format. Options: 'json', 'xml', 'fasta', 'flatfile'. Defaults to 'json'.
    
    Returns:
        Returns comprehensive UniProt protein entry data including accession, sequence, organism information, and annotations for a specified protein identifier.
    Examples:
        >>> response = get_uniprot_entry_by_accession(accession='P12345')
        >>> response = get_uniprot_entry_by_accession(accession='Q9NXB0-3', format='fasta')
    """
    assert accession is not None, 'Missing required parameter: accession'
    
    # Map format parameter to content type
    format_mapping = {
        'json': 'application/json',
        'xml': 'application/xml',
        'fasta': 'text/x-fasta',
        'flatfile': 'text/x-flatfile'
    }
    
    content_type = format_mapping.get(format.lower(), 'application/json')
    
    base_url = "https://www.ebi.ac.uk"
    api_url = f"{base_url}/proteins/api/proteins/{quote(accession)}"
    headers = {'Accept': content_type}
    
    response = requests.get(url=api_url, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = get_uniprot_entry_by_accession(accession='Q9NXB0-3')
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