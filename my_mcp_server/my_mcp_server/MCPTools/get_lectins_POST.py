import requests
import json

def get_lectins(getcolumns="pdb,uniprot", wherecolumn="pdb", isvalue="%%", limit=1000):
    """
    Retrieve lectin data from UniLectin3D database based on specified column filters and criteria.
    
    Parameters:
        getcolumns (str): Comma-separated list of columns to retrieve (e.g., "pdb,uniprot")
        wherecolumn (str): Column to filter on (e.g., "pdb", "species", "uniprot")
        isvalue (str): Value to match in the wherecolumn (supports wildcards like "%%" for all)
        limit (int): Maximum number of results to return (default: 1000, use -1 for all)
    
    Returns:
        Returns lectin data from UniLectin3D database including specified columns like PDB IDs, UniProt IDs, fold, class, and other properties based on filtering criteria.
    Examples:
        # Get all PDB IDs and their UniProt IDs
        get_lectins(getcolumns="pdb,uniprot", wherecolumn="pdb", isvalue="%%")
        
        # Get lectins from a specific species
        get_lectins(getcolumns="pdb,uniprot", wherecolumn="species", isvalue="Rattus norvegicus")
        
        # Get lectins with a specific UniProt ID
        get_lectins(getcolumns="pdb,fold,class", wherecolumn="uniprot", isvalue="P19999")
    """
    api_url = "https://unilectin.unige.ch/api/getlectins"
    
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
    r = get_lectins(getcolumns="pdb,uniprot", wherecolumn="pdb", isvalue="%%", limit=1000)
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