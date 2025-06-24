import requests
from urllib.parse import quote

def get_genome_coordinate_by_protein_sequence_position(taxonomy=None, chromosome=None, gstart=None, gend=None):
    """
    Get genome coordinate by protein sequence position.
    
    Args:
        taxonomy (str): Organism taxon ID (e.g., '9606' for human)
        chromosome (str): Chromosome name, i.e. 1, 2, X, etc.
        gstart (str): Genome location start
        gend (str): Genome location end
    
    Returns:
        Returns protein sequence information mapped to genomic coordinates for a specified organism, chromosome, and genomic location range.
    Example:
        >>> response = get_genome_coordinate_by_protein_sequence_position(
        ...     taxonomy='9606',
        ...     chromosome='1',
        ...     gstart='100000',
        ...     gend='200000'
        ... )
    """
    assert taxonomy is not None, 'Missing required parameter: taxonomy'
    assert chromosome is not None, 'Missing required parameter: chromosome'
    assert gstart is not None, 'Missing required parameter: gstart'
    assert gend is not None, 'Missing required parameter: gend'
    
    base_url = "https://www.ebi.ac.uk"
    api_url = f"{base_url}/proteins/api/coordinates/glocation/{quote(taxonomy, safe='')}/{quote(chromosome, safe='')}:{quote(str(gstart), safe='')}-{quote(str(gend), safe='')}"
    
    headers = {'Content-Type': 'application/json'}
    
    response = requests.get(url=api_url, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = get_genome_coordinate_by_protein_sequence_position(taxonomy='9606', chromosome='1', gstart='100000', gend='200000')
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