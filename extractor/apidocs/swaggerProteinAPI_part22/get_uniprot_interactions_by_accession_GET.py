import requests, json
from urllib.parse import quote

def get_uniprot_interactions_by_accession(accession=None):
    """
    Get UniProt interactions by accession.
    
    This function retrieves interaction data for a specified UniProt accession.
    
    Args:
        accession (str): UniProt accession ID. Required.
                         Example: 'P12345', 'Q9NXB0-3'
    
    Returns:
        requests.Response: The API response object containing interaction data.
        
    Raises:
        AssertionError: If accession parameter is not provided.
    """
    assert accession is not None, 'Missing required parameter: accession'
    
    base_url = "https://www.ebi.ac.uk"
    api_url = f"{base_url}/proteins/api/proteins/interaction/{quote(accession)}"
    headers = {'Content-Type': 'application/json'}
    
    response = requests.get(url=api_url, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = get_uniprot_interactions_by_accession(accession='Q9NXB0-3')
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