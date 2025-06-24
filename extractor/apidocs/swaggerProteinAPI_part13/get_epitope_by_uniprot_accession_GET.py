import requests
from urllib.parse import quote

def get_epitope_by_uniprot_accession(accession=None):
    """
    Get epitope information by UniProt accession.
    
    This function retrieves epitope data for a protein identified by its UniProt accession number.
    
    Args:
        accession (str): UniProt accession number (e.g., 'P12345', 'Q9NXB0-3')
    
    Returns:
        requests.Response: The response object from the API request
    
    Examples:
        >>> response = get_epitope_by_uniprot_accession(accession='P12345')
        >>> response = get_epitope_by_uniprot_accession(accession='Q9NXB0-3')
    """
    assert accession is not None, 'Missing required parameter: accession'
    
    base_url = "https://www.ebi.ac.uk"
    api_url = f"{base_url}/proteins/api/epitope/{quote(accession, safe='')}"
    headers = {'Content-Type': 'application/json'}
    
    response = requests.get(url=api_url, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = get_epitope_by_uniprot_accession(accession='Q9NXB0-3')
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