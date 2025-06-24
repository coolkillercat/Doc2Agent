import requests
import json

def get_fungal_lectins(getcolumns="fold,domain,species", wherecolumn="species", isvalue="Sclerotinia sclerotiorum", limit=2000):
    """
    Retrieve information about fungal lectins from the UniLectin database.
    
    This function queries the UniLectin API to get information about fungal lectins
    based on specified column filters.
    
    Args:
        getcolumns (str): Comma-separated list of columns to retrieve. Default is "fold,domain,species".
        wherecolumn (str): The column to filter on. Default is "species".
        isvalue (str): The value to match in the wherecolumn. Default is "Sclerotinia sclerotiorum".
        limit (int): Maximum number of results to return. Default is 2000.
    
    Returns:
        Returns information about fungal lectins from the UniLectin database based on specified column filters such as fold, domain, and species.
    Example:
        >>> response = get_fungal_lectins(
        ...     getcolumns="fold,domain,species",
        ...     wherecolumn="species",
        ...     isvalue="Sclerotinia sclerotiorum",
        ...     limit=2000
        ... )
        >>> data = response.json()
    """
    api_url = "https://unilectin.unige.ch/api/getmycolec"
    payload = {
        'getcolumns': getcolumns,
        'wherecolumn': wherecolumn,
        'isvalue': isvalue,
        'limit': limit
    }
    headers = {'Content-Type': 'application/json'}
    
    assert getcolumns is not None, 'Missing required parameter: getcolumns'
    assert wherecolumn is not None, 'Missing required parameter: wherecolumn'
    assert isvalue is not None, 'Missing required parameter: isvalue'
    
    response = requests.post(url=api_url, json=payload, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = get_fungal_lectins(getcolumns="fold,domain,species", wherecolumn="species", isvalue="Sclerotinia sclerotiorum", limit=2000)
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