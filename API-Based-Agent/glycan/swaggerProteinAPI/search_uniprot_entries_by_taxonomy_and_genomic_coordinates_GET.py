import requests
from urllib.parse import quote

def search_uniprot_entries_by_taxonomy_and_genomic_coordinates(taxonomy, locations, offset=0, size=100, in_range=None, format="json"):
    """
    Search UniProt entries by taxonomy and genomic coordinates.
    
    Args:
        taxonomy (str): Organism taxon ID (required)
        locations (str): Genomic locations such as x:58205437-58219305,12452535-12452536,2:32452
                        Before colon is the chromosome such as x:58205437-58219305, or without 
                        chromosome such as 12452535-12452536, means any chromosome (required)
        offset (int, optional): Off set, page starting point. Defaults to 0.
        size (int, optional): Page size. When page size is -1, it returns all records and offset 
                             will be ignored. Defaults to 100.
        in_range (bool, optional): When set to true for location search, only those entries that 
                                  are in the range will be retrieved. Defaults to None.
        format (str, optional): Response format. Options: "json", "xml", "gff". Defaults to "json".
    
    Returns:
        Returns UniProt protein entries that match specified taxonomic identifiers and genomic coordinate locations.
    Example:
        >>> response = search_uniprot_entries_by_taxonomy_and_genomic_coordinates(
        ...     taxonomy='9606', 
        ...     locations='x:58205437-58219305'
        ... )
    """
    assert taxonomy is not None, 'Missing required parameter: taxonomy'
    assert locations is not None, 'Missing required parameter: locations'
    
    base_url = "https://www.ebi.ac.uk"
    api_url = f"{base_url}/proteins/api/coordinates/{taxonomy}/{quote(locations)}"
    
    params = {}
    if offset is not None:
        params['offset'] = offset
    if size is not None:
        params['size'] = size
    if in_range is not None:
        params['in_range'] = in_range
    
    headers = {'Content-Type': 'application/json'}
    
    # Set Accept header based on format
    if format == "json":
        headers['Accept'] = 'application/json'
    elif format == "xml":
        headers['Accept'] = 'application/xml'
    elif format == "gff":
        headers['Accept'] = 'text/x-gff'
    
    response = requests.get(url=api_url, params=params, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = search_uniprot_entries_by_taxonomy_and_genomic_coordinates(taxonomy='9606', locations='x:58205437-58219305', offset=0, size=100, in_range=False)
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