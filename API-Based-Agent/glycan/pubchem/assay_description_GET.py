import requests
from urllib.parse import quote

def assay_description(aid=None, output_format="XML", version=None):
    """
    Retrieve assay description from PubChem using PUG REST API.
    
    Parameters:
    -----------
    aid : str or int
        Assay ID (AID) to retrieve description for. Required.
    output_format : str, optional
        Output format. Options: XML, JSON, JSONP, ASNT, ASNB. Default is XML.
    version : str or float, optional
        Version of the assay to retrieve. If not specified, the latest version is returned.
        
    Returns:
        Returns assay description data from PubChem for a specified assay ID (AID).
    --------
    requests.Response
        Response object containing the assay description.
        
    Examples:
    ---------
    >>> response = assay_description(450)
    >>> response = assay_description(450, output_format="JSON")
    >>> response = assay_description(450, version="1.1")
    """
    assert aid is not None, 'Missing required parameter: aid'
    
    # Validate output format
    valid_formats = ["XML", "JSON", "JSONP", "ASNT", "ASNB"]
    if output_format not in valid_formats:
        raise ValueError(f"Invalid output format. Must be one of: {', '.join(valid_formats)}")
    
    # Construct the API URL
    api_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/{quote(str(aid), safe='')}/description/{output_format}"
    
    # Add version parameter if specified
    params = {}
    if version:
        params["version"] = version
    
    # Make the request
    response = requests.get(url=api_url, params=params, timeout=50)
    return response

if __name__ == '__main__':
    r = assay_description(aid=450)
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