import requests
from urllib.parse import quote

def get_antigen_by_uniprot_accession(accession=None):
    """
    Get antigen information by UniProt accession.
    
    This function retrieves antigen information from the EBI API using a UniProt accession number.
    
    Args:
        accession (str): UniProt accession number (e.g., 'Q9NXB0-3')
        
    Returns:
        requests.Response: The API response object containing antigen information
        
    Examples:
        >>> response = get_antigen_by_uniprot_accession(accession='Q9NXB0-3')
    """
    base_url = "https://www.ebi.ac.uk"
    assert accession is not None, 'Missing required parameter: accession'
    
    # Construct the API URL with the accession in the path
    api_url = f"{base_url}/proteins/api/antigen/{quote(accession)}"
    
    headers = {'Content-Type': 'application/json'}
    
    response = requests.get(url=api_url, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = get_antigen_by_uniprot_accession(accession='Q9NXB0-3')
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