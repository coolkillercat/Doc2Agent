import requests
from urllib.parse import quote

def get_genomic_coordinates(accession=None, format="json"):
    """
    Get genomic coordinates for a UniProt accession.
    
    Args:
        accession (str): UniProt accession (e.g., 'Q9NXB0-3', 'P05067')
        format (str, optional): Response format - "json", "xml", or "gff". Defaults to "json".
    
    Returns:
        requests.Response: Response object containing genomic coordinates data
        
    Example:
        >>> response = get_genomic_coordinates(accession='Q9NXB0-3')
        >>> print(response.status_code)
        >>> print(response.json())
        
        >>> response = get_genomic_coordinates(accession='P05067', format='xml')
        >>> print(response.status_code)
        >>> print(response.text)
    """
    assert accession is not None, 'Missing required parameter: accession'
    
    # Validate format
    valid_formats = {"json": "application/json", "xml": "application/xml", "gff": "text/x-gff"}
    if format not in valid_formats:
        raise ValueError(f"Invalid format. Must be one of: {', '.join(valid_formats.keys())}")
    
    base_url = "https://www.ebi.ac.uk"
    api_url = f"{base_url}/proteins/api/coordinates/{quote(accession)}"
    headers = {'Content-Type': 'application/json', 'Accept': valid_formats[format]}
    
    response = requests.get(url=api_url, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = get_genomic_coordinates(accession='P12345')
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