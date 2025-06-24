import requests
from urllib.parse import quote

def get_mutagenesis_by_accession(accession, location=None):
    """
    Get mutagenesis mapped to UniProt by accession.
    
    Args:
        accession (str): UniProt accession (required). Example: 'Q9NXB0-3'
        location (str, optional): Filter by the amino acid range position in the sequence(s).
                                 Any valid amino acid range position within the length of the 
                                 protein sequence such as 10-60 (start position to end position).
                                 Example: '10-60'
    
    Returns:
        requests.Response: The API response object
    
    Example:
        >>> response = get_mutagenesis_by_accession('Q9NXB0-3')
        >>> response = get_mutagenesis_by_accession('Q9NXB0-3', location='10-60')
    """
    base_url = "https://www.ebi.ac.uk"
    api_url = f"{base_url}/proteins/api/mutagenesis/{quote(accession)}"
    
    headers = {'Content-Type': 'application/json'}
    
    params = {}
    if location:
        params['location'] = location
    
    response = requests.get(url=api_url, params=params, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = get_mutagenesis_by_accession(accession='Q9NXB0-3', location='10-60')
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