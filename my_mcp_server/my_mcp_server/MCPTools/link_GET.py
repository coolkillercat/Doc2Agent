import requests
from urllib.parse import quote

def link(target_db=None, source_db=None, dbentries=None, option=None):
    """
    Find related entries by using database cross-references in the KEGG database.
    
    This function allows retrieval of cross-references within all KEGG databases, 
    as well as between KEGG databases and outside databases.
    
    Args:
        target_db (str): Target database name (e.g., 'pathway', 'ko', 'hsa', etc.)
        source_db (str): Source database name (e.g., 'pathway', 'ko', 'hsa', etc.)
        dbentries (str): Specific database entries (e.g., 'hsa:10458+ece:Z5100')
        option (str, optional): Output format option (e.g., 'turtle', 'n-triple')
    
    Returns:
        Returns cross-references between KEGG database entries, showing relationships between biological entities like genes, pathways, and compounds.
    Examples:
        >>> link(target_db='pathway', source_db='hsa')  # KEGG pathways linked from each human gene
        >>> link(target_db='hsa', source_db='pathway')  # Human genes linked from each KEGG pathway
        >>> link(target_db='pathway', dbentries='hsa:10458+ece:Z5100')  # Pathways linked from specific genes
        >>> link(target_db='ko', dbentries='map00010')  # List of KO entries in pathway map00010
    """
    assert target_db is not None, 'Missing required parameter: target_db'
    
    # Construct the API URL based on the provided parameters
    if dbentries is not None:
        api_url = f"https://rest.kegg.jp/link/{quote(target_db, safe='')}/{quote(dbentries, safe='')}"
    else:
        assert source_db is not None, 'Missing required parameter: source_db'
        api_url = f"https://rest.kegg.jp/link/{quote(target_db, safe='')}/{quote(source_db, safe='')}"
    
    # Add option if provided
    if option is not None:
        api_url = f"{api_url}/{option}"
    
    # Make the API request
    response = requests.get(url=api_url, timeout=50)
    return response

if __name__ == '__main__':
    r = link(target_db='pathway', source_db='hsa')
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