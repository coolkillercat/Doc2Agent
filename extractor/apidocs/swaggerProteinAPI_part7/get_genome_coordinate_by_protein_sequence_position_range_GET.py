import requests
import json
from urllib.parse import quote

def get_genome_coordinate_by_protein_sequence_position_range(accession=None, pStart=None, pEnd=None, format='json'):
    """
    Get genome coordinate by protein sequence position range.
    
    Args:
        accession (str): UniProt accession. Required.
        pStart (int): Start position in protein sequence. Required.
        pEnd (int): End position in protein sequence. Required.
        format (str): Response format, either 'json' or 'xml'. Default is 'json'.
    
    Returns:
        requests.Response: Response object from the API request.
    
    Examples:
        >>> get_genome_coordinate_by_protein_sequence_position_range(accession='Q9NXB0-3', pStart=1, pEnd=100)
        >>> get_genome_coordinate_by_protein_sequence_position_range(accession='P05067', pStart=294, pEnd=296)
    """
    assert accession is not None, 'Missing required parameter: accession'
    assert pStart is not None, 'Missing required parameter: pStart'
    assert pEnd is not None, 'Missing required parameter: pEnd'
    
    base_url = "https://www.ebi.ac.uk"
    api_url = f"{base_url}/proteins/api/coordinates/location/{quote(accession)}:{pStart}-{pEnd}"
    headers = {'Content-Type': 'application/json'}
    
    response = requests.get(url=api_url, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = get_genome_coordinate_by_protein_sequence_position_range(accession='P12345', pStart=1, pEnd=100)
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