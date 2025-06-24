import requests
import json
import pandas as pd

def get_predicted_lectins(getcolumns="fold,domain,uniprot,superkingdom", wherecolumn="superkingdom", isvalue="Bacteria%", limit=2000):
    """
    Retrieve predicted lectin data from UniLectin database based on specified column filters.
    
    This function queries the UniLectin API to get predicted lectin information based on the provided parameters.
    
    Parameters:
        getcolumns (str): Comma-separated list of columns to retrieve (e.g., "fold,domain,uniprot,superkingdom")
        wherecolumn (str): Column to filter on (e.g., "superkingdom")
        isvalue (str): Value to match in the wherecolumn. Supports wildcards with % (e.g., "Bacteria%")
        limit (int): Maximum number of results to return (default: 2000, use -1 for all results)
    
    Returns:
        Returns predicted lectin data from UniLectin database with specified columns like fold, domain, uniprot, and taxonomic information.
    Example:
        >>> response = get_predicted_lectins(
        ...     getcolumns="fold,domain,uniprot,superkingdom",
        ...     wherecolumn="superkingdom",
        ...     isvalue="Bacteria%",
        ...     limit=2000
        ... )
        >>> data = pd.DataFrame(json.loads(response.text))
    """
    api_url = "https://unilectin.unige.ch/api/getlectinspredicted"
    
    # Validate required parameters
    assert getcolumns is not None, 'Missing required parameter: getcolumns'
    assert wherecolumn is not None, 'Missing required parameter: wherecolumn'
    assert isvalue is not None, 'Missing required parameter: isvalue'
    
    # Prepare payload
    payload = {
        'getcolumns': getcolumns,
        'wherecolumn': wherecolumn,
        'isvalue': isvalue,
        'limit': limit
    }
    
    # Make the request
    response = requests.post(
        url=api_url,
        json=payload,
        headers={'Content-Type': 'application/json'},
        timeout=50
    )
    
    return response

if __name__ == '__main__':
    r = get_predicted_lectins(
        getcolumns="fold,domain,uniprot,superkingdom",
        wherecolumn="superkingdom",
        isvalue="Bacteria%",
        limit=2000
    )
    
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