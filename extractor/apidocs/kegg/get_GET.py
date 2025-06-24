import requests

def get(dbentries=None, option=None):
    """
    Retrieve given database entries from the KEGG API.
    
    This function retrieves detailed information about specified KEGG database entries
    in a flat file format or in other formats with options.
    
    Args:
        dbentries (str): KEGG database entries (e.g., 'C01290', 'hsa:10458', 'map00600').
                         Multiple entries can be specified by using '+' as a separator (e.g., 'C01290+G00092').
                         Limited to 10 entries maximum.
        option (str, optional): Retrieval option to get specific data format:
                               - 'aaseq': amino acid sequences (for gene entries)
                               - 'ntseq': nucleotide sequences (for gene entries)
                               - 'mol': chemical structure data (for compound/glycan/drug entries)
                               - 'kcf': chemical structure data in KCF format
                               - 'image': image file (gif for compound/glycan/drug, png for pathway)
                               - 'conf': conf file (for pathway entries)
                               - 'kgml': KGML file (for pathway entries)
                               - 'json': JSON file (for brite hierarchies)
    
    Returns:
        Returns detailed information about specified KEGG database entries in flat file format or alternative formats based on the provided option.
    Examples:
        >>> response = get(dbentries='C01290+G00092')
        >>> response = get(dbentries='hsa:10458', option='aaseq')
        >>> response = get(dbentries='map00600', option='kgml')
    """
    assert dbentries is not None, 'Missing required parameter: dbentries'
    
    base_url = "https://rest.kegg.jp/get"
    
    # Construct the URL
    if option:
        api_url = f"{base_url}/{dbentries}/{option}"
    else:
        api_url = f"{base_url}/{dbentries}"
    
    # Make the request
    response = requests.get(url=api_url, timeout=50)
    return response

if __name__ == '__main__':
    r = get(dbentries='C01290+G00092')
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