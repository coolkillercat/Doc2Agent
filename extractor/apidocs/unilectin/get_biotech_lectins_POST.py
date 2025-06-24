import requests
import json

def get_biotech_lectins(getcolumns=None, wherecolumn=None, isvalue=None, limit=1000, exactmatch=False):
    """
    Retrieve information about biotechnology-related lectins from the UniLectin database.
    
    Parameters:
        getcolumns (str): Comma-separated list of columns to retrieve (e.g., "Lectin,Preferred glycan,uniprot")
        wherecolumn (str): Column to filter on (e.g., "Origin", "Class", "Organism")
        isvalue (str): Value to match in the wherecolumn (supports wildcards with %)
        limit (int): Maximum number of results to return (default: 1000, use -1 for all)
        exactmatch (bool): Whether to perform exact matching on the isvalue (default: False)
    
    Returns:
        Returns information about biotechnology-related lectins from the UniLectin database based on specified filtering criteria.
    Example:
        # Get all plant lectins
        get_biotech_lectins(
            getcolumns="Lectin,Preferred glycan,uniprot,protein name,Length,PDB",
            wherecolumn="Origin",
            isvalue="Plant"
        )
        
        # Get all Jacalin-like lectins
        get_biotech_lectins(
            getcolumns="Lectin,Preferred glycan,uniprot,protein name,Length,PDB",
            wherecolumn="Class",
            isvalue="Jacalin",
            exactmatch=False
        )
    """
    api_url = "https://unilectin.unige.ch/api/getbiotechlectins"
    
    assert getcolumns is not None, 'Missing required parameter: getcolumns'
    assert wherecolumn is not None, 'Missing required parameter: wherecolumn'
    assert isvalue is not None, 'Missing required parameter: isvalue'
    
    payload = {
        'getcolumns': getcolumns,
        'wherecolumn': wherecolumn,
        'isvalue': isvalue,
        'limit': limit,
        'exactmatch': str(exactmatch)
    }
    
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'text/plain'
    }
    
    response = requests.post(url=api_url, json=payload, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = get_biotech_lectins(
        getcolumns="Lectin,Preferred glycan,uniprot,protein name,Length,PDB",
        wherecolumn="Origin",
        isvalue="Plant",
        limit=1000
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