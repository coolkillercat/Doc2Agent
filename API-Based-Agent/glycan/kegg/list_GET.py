import requests
from urllib.parse import quote

def list_kegg(database=None):
    """
    Retrieve a list of entries from a specified KEGG database with their identifiers and descriptions.
    
    This function calls the KEGG API's list operation to obtain a list of all entries in the specified database.
    
    Args:
        database (str): The KEGG database name to query. Valid options include:
            - pathway: Reference pathways
            - brite: BRITE functional hierarchies
            - module: KEGG modules
            - ko: KEGG Orthology
            - organism codes (e.g., 'hsa' for human)
            - genome: KEGG organisms
            - compound: Small molecules
            - drug: Drugs
            - and others as specified in the KEGG API documentation
    
    Returns:
        Returns a list of entries from a specified KEGG database with their identifiers and descriptions.
    Examples:
        >>> response = list_kegg('pathway')  # List all reference pathways
        >>> response = list_kegg('hsa')      # List all human genes
        >>> response = list_kegg('compound') # List all compounds
    """
    assert database is not None, 'Missing required parameter: database'
    
    api_url = f"https://rest.kegg.jp/list/{quote(database, safe='')}"
    
    response = requests.get(url=api_url, timeout=50)
    return response

if __name__ == '__main__':
    r = list_kegg(database='pathway')
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