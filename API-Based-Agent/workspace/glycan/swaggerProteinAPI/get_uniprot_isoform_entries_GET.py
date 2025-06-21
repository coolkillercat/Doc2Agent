import requests
from urllib.parse import quote

def get_uniprot_isoform_entries(accession=None, format="json"):
    """
    Get UniProt isoform entries from parent entry accession.
    
    Args:
        accession (str): UniProt accession (required). Example: 'P08047'
        format (str, optional): Response format. Options: 'json', 'xml', 'fasta', 'flatfile'. Default: 'json'
    
    Returns:
        Returns a list of protein isoform entries with their sequences, annotations, and metadata for a given UniProt accession.
    Example:
        >>> response = get_uniprot_isoform_entries(accession='P08047')
        >>> isoforms = response.json()
    """
    assert accession is not None, 'Missing required parameter: accession'
    
    # Map format parameter to content type
    format_mapping = {
        'json': 'application/json',
        'xml': 'application/xml',
        'fasta': 'text/x-fasta',
        'flatfile': 'text/x-flatfile'
    }
    
    content_type = format_mapping.get(format, 'application/json')
    
    base_url = "https://www.ebi.ac.uk"
    api_url = f"{base_url}/proteins/api/proteins/{quote(accession)}/isoforms"
    
    headers = {'Accept': content_type}
    
    response = requests.get(url=api_url, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = get_uniprot_isoform_entries(accession='Q9NXB0')
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