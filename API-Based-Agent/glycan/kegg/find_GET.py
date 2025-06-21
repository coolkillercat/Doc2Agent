import requests
from urllib.parse import quote

def find(database=None, query=None, option=None):
    """
    Find entries with matching query keyword or other query data in the KEGG database.
    
    Args:
        database (str): The database to search in. Options include pathway, brite, module, ko, genes, 
                       organism codes, vg, vp, ag, genome, variant, disease, drug, dgroup, compound, etc.
        query (str): The search query. Keywords to search for in the database.
        option (str, optional): Additional search options for compound/drug databases:
                               formula, exact_mass, mol_weight, or nop.
    
    Returns:
        Returns entries from the KEGG database that match the specified query keyword or search criteria.
    Examples:
        >>> find(database="genes", query="shiga toxin")
        >>> find(database="compound", query="C7H10O5", option="formula")
        >>> find(database="compound", query="174.05", option="exact_mass")
    """
    api_url = f"https://rest.kegg.jp/find/{quote(database, safe='')}/{quote(query, safe='')}"
    
    # Add option to URL if provided
    if option:
        api_url += f"/{option}"
    
    assert database is not None, 'Missing required parameter: database'
    assert query is not None, 'Missing required parameter: query'
    
    response = requests.get(url=api_url, timeout=50)
    return response

if __name__ == '__main__':
    r = find(database='genes', query='shiga toxin')
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