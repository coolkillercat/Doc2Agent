import requests
from urllib.parse import quote

def get_feature_by_locations(taxonomy=None, locations=None, offset=0, size=100, in_range=None, format="json"):
    """
    Search UniProt entries by taxonomy and genomic coordinates.
    
    Args:
        taxonomy (str): Organism taxon ID. Required.
        locations (str): Genomic locations such as x:58205437-58219305,12452535-12452536,2:32452.
                        Before colon is the chromosome such as x:58205437-58219305, or without 
                        chromosome such as 12452535-12452536, means any chromosome. Required.
        offset (int, optional): Off set, page starting point. Defaults to 0.
        size (int, optional): Page size. When page size is -1, it returns all records and offset 
                             will be ignored. Defaults to 100.
        in_range (bool, optional): When set to true for location search, only those entries that 
                                  are in the range will be retrieved.
        format (str, optional): Response format. Options: "json", "xml", "gff". Defaults to "json".
    
    Returns:
        Returns UniProt entries matching specific genomic coordinates for a given taxonomy.
    Examples:
        >>> get_feature_by_locations(taxonomy='9606', locations='x:58205437-58219305')
        >>> get_feature_by_locations(taxonomy='9606', locations='x:58205437-58219305', in_range=True)
    """
    assert taxonomy is not None, 'Missing required parameter: taxonomy'
    assert locations is not None, 'Missing required parameter: locations'
    
    base_url = "https://www.ebi.ac.uk"
    api_url = f"{base_url}/proteins/api/coordinates/{taxonomy}/{locations}/feature"
    
    params = {
        'offset': offset,
        'size': size
    }
    
    if in_range is not None:
        params['in_range'] = in_range
    
    headers = {'Content-Type': 'application/json'}
    
    # Set Accept header based on format
    if format.lower() == "json":
        headers['Accept'] = 'application/json'
    elif format.lower() == "xml":
        headers['Accept'] = 'application/xml'
    elif format.lower() == "gff":
        headers['Accept'] = 'text/x-gff'
    
    response = requests.get(url=api_url, params=params, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = get_feature_by_locations(taxonomy='9606', locations='x:58205437-58219305', offset=0, size=100, in_range=False)
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