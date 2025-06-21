import requests
from urllib.parse import quote

def get_variation_for_accession_location(accession_locations=None):
    """
    Get natural variants by list of accession and its locations.
    
    Parameters:
    -----------
    accession_locations : str
        UniProt accession(s) with locations. Pipe | separated values accepted up to 100.
        Format: accession:location1,location2|accession:location3|...
        Example: P05067:5,7|P05067:12|A0A024QZ42:4
    
    Returns:
        Returns natural protein variants for specified UniProt accessions at specific amino acid positions.
    --------
    requests.Response
        The API response object containing variant information.
    
    Examples:
    ---------
    >>> response = get_variation_for_accession_location("P05067:5,7|P05067:12|A0A024QZ42:4")
    >>> response.status_code
    200
    """
    base_url = "https://www.ebi.ac.uk"
    
    assert accession_locations is not None, 'Missing required parameter: accession_locations'
    
    api_url = f"{base_url}/proteins/api/variation/accession_locations/{quote(accession_locations)}"
    headers = {'Content-Type': 'application/json'}
    
    response = requests.get(url=api_url, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = get_variation_for_accession_location(accession_locations='P05067:5,7|P05067:12|A0A024QZ42:4')
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