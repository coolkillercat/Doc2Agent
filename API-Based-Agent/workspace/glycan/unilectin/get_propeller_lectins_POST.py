import requests
import json

def get_propeller_lectins(getcolumns="domain,uniprot,superkingdom", wherecolumn="superkingdom", isvalue="Bacteria%", limit=2000):
    """
    Retrieve information about propeller lectins from the UniLectin database based on specified column filters.
    
    Parameters:
        getcolumns (str): Comma-separated list of columns to retrieve (e.g., "domain,uniprot,superkingdom")
        wherecolumn (str): Column to filter on (e.g., "superkingdom")
        isvalue (str): Value to match in the wherecolumn (supports wildcards, e.g., "Bacteria%")
        limit (int): Maximum number of results to return (default: 2000)
    
    Returns:
        Returns information about propeller lectins from the UniLectin database based on specified column filters such as domain, uniprot, and superkingdom.
    Example:
        >>> response = get_propeller_lectins(
        ...     getcolumns="domain,uniprot,superkingdom",
        ...     wherecolumn="superkingdom",
        ...     isvalue="Bacteria%",
        ...     limit=2000
        ... )
        >>> data = response.text
    """
    api_url = "https://unilectin.unige.ch/api/getproplec"
    
    # Validate required parameters
    assert getcolumns is not None, 'Missing required parameter: getcolumns'
    assert wherecolumn is not None, 'Missing required parameter: wherecolumn'
    assert isvalue is not None, 'Missing required parameter: isvalue'
    
    payload = {
        'getcolumns': getcolumns,
        'wherecolumn': wherecolumn,
        'isvalue': isvalue,
        'limit': limit
    }
    
    headers = {
        'Content-Type': 'application/json',
        'accept': 'text/plain'
    }
    
    response = requests.post(
        url=api_url,
        json=payload,
        headers=headers,
        timeout=50
    )
    
    return response

if __name__ == '__main__':
    r = get_propeller_lectins(
        getcolumns="domain,uniprot,superkingdom",
        wherecolumn="superkingdom",
        isvalue="Bacteria%",
        limit=2000
    )
    
    r_json = None
    try:
        r_json = r.json()
    except:
        pass
    
    result_dict = dict()
    result_dict['status_code'] = r.status_code
    result_dict['text'] = r.text
    result_dict['json'] = r_json
    result_dict['content'] = r.content.decode("utf-8")
    print(json.dumps(result_dict, indent=4))