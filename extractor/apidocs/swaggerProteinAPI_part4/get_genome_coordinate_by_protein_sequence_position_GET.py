import requests
from urllib.parse import quote

def get_genome_coordinate_by_protein_sequence_position(taxonomy=None, chromosome=None, gPosition=None, format="json"):
    """
    Get genome coordinate by protein sequence position.
    
    Args:
        taxonomy (str): Organism taxon ID (e.g., '9606' for human)
        chromosome (str): Chromosome name, i.e. 1, 2, X, etc.
        gPosition (str): Genome location position
        format (str, optional): Response format, either "json" or "xml". Defaults to "json".
        
    Returns:
        Returns protein sequence information corresponding to a specific genomic location identified by taxonomy, chromosome, and position.
    Example:
        >>> response = get_genome_coordinate_by_protein_sequence_position(taxonomy='9606', chromosome='1', gPosition='81699010')
    """
    assert taxonomy is not None, 'Missing required parameter: taxonomy'
    assert chromosome is not None, 'Missing required parameter: chromosome'
    assert gPosition is not None, 'Missing required parameter: gPosition'
    
    base_url = "https://www.ebi.ac.uk"
    api_path = f"/proteins/api/coordinates/glocation/{taxonomy}/{chromosome}:{gPosition}"
    api_url = base_url + api_path
    
    headers = {'Content-Type': 'application/json'}
    params = {'format': format}
    
    response = requests.get(url=api_url, headers=headers, params=params, timeout=50)
    return response

if __name__ == '__main__':
    r = get_genome_coordinate_by_protein_sequence_position(taxonomy='9606', chromosome='1', gPosition='81699010')
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