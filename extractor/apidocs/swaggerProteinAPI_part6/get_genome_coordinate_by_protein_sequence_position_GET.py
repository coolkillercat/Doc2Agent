import requests
from urllib.parse import quote

def get_genome_coordinate_by_protein_sequence_position(accession=None, pPosition=None):
    """
    Get genome coordinate by protein sequence position.
    
    Args:
        accession (str): UniProt accession. Required.
        pPosition (int): Protein position. Required.
    
    Returns:
        requests.Response: The API response object.
    
    Examples:
        >>> get_genome_coordinate_by_protein_sequence_position(accession='Q9NXB0-3', pPosition=42)
        >>> get_genome_coordinate_by_protein_sequence_position(accession='P12345', pPosition=42)
    """
    assert accession is not None, 'Missing required parameter: accession'
    assert pPosition is not None, 'Missing required parameter: pPosition'
    
    base_url = "https://www.ebi.ac.uk"
    api_endpoint = f"/pdbe/graph-api/coordinates/location/{quote(str(accession))}:{pPosition}"
    api_url = f"{base_url}{api_endpoint}"
    
    headers = {'Content-Type': 'application/json'}
    
    response = requests.get(url=api_url, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = get_genome_coordinate_by_protein_sequence_position(accession='Q9NXB0-3', pPosition=42)
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