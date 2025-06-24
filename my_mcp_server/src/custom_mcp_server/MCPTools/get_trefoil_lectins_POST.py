import requests
import json
from urllib.parse import quote

def get_trefoil_lectins(getcolumns=None, wherecolumn=None, isvalue=None, limit=1000):
    """
    Retrieve information about trefoil lectins from the UniLectin database based on specified column filters.
    
    Parameters:
        getcolumns (str): Comma-separated list of columns to retrieve (e.g., "domain,uniprot,superkingdom")
        wherecolumn (str): Column to filter on (e.g., "superkingdom")
        isvalue (str): Value to match in the wherecolumn (wildcards are accepted, e.g., "Bacteria%")
        limit (int): Maximum number of results to return (default: 1000, use -1 for all results)
    
    Returns:
        Returns information about trefoil lectins from the UniLectin database based on specified column filters such as domain, uniprot, and superkingdom.
    Example:
        >>> response = get_trefoil_lectins(
        ...     getcolumns="domain,uniprot,superkingdom",
        ...     wherecolumn="superkingdom",
        ...     isvalue="Bacteria%",
        ...     limit=2000
        ... )
    """
    api_url = "https://unilectin.unige.ch/api/gettreflec"
    
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
    
    response = requests.post(url=api_url, json=payload, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = get_trefoil_lectins(getcolumns="domain,uniprot,superkingdom", wherecolumn="superkingdom", isvalue="Bacteria%", limit=2000)
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