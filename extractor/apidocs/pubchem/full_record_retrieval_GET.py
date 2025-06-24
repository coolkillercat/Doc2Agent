import requests
from urllib.parse import quote

def full_record_retrieval(source_id=None, cid=None, record_type='2d', image_size='large'):
    """
    Retrieves a full record from PubChem using the PUG REST API.
    
    Parameters:
    -----------
    source_id : str
        The source ID of the substance to retrieve. Format should be 'source_name/id'.
        Example: 'DTP.NCI/747285'
    cid : str or int, optional
        The PubChem Compound ID. If provided, source_id will be ignored.
    record_type : str, optional
        Type of conformer for compounds. Options: '2d' (default) or '3d'.
    image_size : str, optional
        Image size for PNG output. Options: 'large' (300x300, default), 'small' (100x100), 
        or custom dimensions in the format 'widthxheight' (e.g., '320x240').
    
    Returns:
        Returns a full PubChem record including compound or substance data in ASNT format based on either a PubChem Compound ID (CID) or source identifier.
    --------
    requests.Response
        The response object from the API request.
    
    Examples:
    ---------
    >>> response = full_record_retrieval(source_id='DTP.NCI/747285')
    >>> response = full_record_retrieval(cid=2244, record_type='3d', image_size='small')
    >>> response = full_record_retrieval(source_id='ChemIDplus/57-27-2')
    """
    # Build the API URL
    if cid is not None:
        api_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/ASNT"
    elif source_id is not None:
        # Check if source_id contains a slash
        if '/' in source_id:
            source_name, source_id_value = source_id.split('/', 1)
            # Replace '/' with '.' in source names as per API documentation
            source_name = source_name.replace('/', '.')
            api_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/sourceid/{quote(source_name, safe='')}/{quote(source_id_value, safe='')}/ASNT"
        else:
            raise ValueError("source_id must be in the format 'source_name/id'")
    else:
        raise ValueError("Either source_id or cid must be provided")
    
    # Build query parameters
    querystring = {}
    if record_type and record_type != '2d':
        querystring['record_type'] = record_type
    if image_size and image_size != 'large':
        querystring['image_size'] = image_size
    
    # Make the request
    response = requests.get(url=api_url, params=querystring, timeout=50)
    return response

if __name__ == '__main__':
    r = full_record_retrieval(source_id='DTP.NCI/747285')
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