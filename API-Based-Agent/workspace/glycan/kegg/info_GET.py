import requests

def info(database="kegg"):
    """
    Retrieve information about a KEGG database.
    
    This function queries the KEGG API to get information about a specified database,
    including its entry count and release details.
    
    Args:
        database (str): The KEGG database name to query. Default is "kegg".
            Valid options include: kegg, pathway, brite, module, ko, genes, 
            organism codes (e.g., hsa, eco), vg, vp, ag, network, variant, 
            disease, drug, dgroup.
    
    Returns:
        Returns information about a specified KEGG database, including its entry count and release details.
    Examples:
        >>> response = info("kegg")  # Get information about the entire KEGG database
        >>> response = info("pathway")  # Get information about the pathway database
        >>> response = info("hsa")  # Get information about human genes database
    """
    assert database is not None, 'Missing required parameter: database'
    
    api_url = f"https://rest.kegg.jp/info/{quote(database, safe='')}"
    
    response = requests.get(url=api_url, timeout=50)
    return response

if __name__ == '__main__':
    from urllib.parse import quote
    import json
    
    r = info(database='kegg')
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