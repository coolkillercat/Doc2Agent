import requests
from urllib.parse import quote

def conv(target_db=None, source_db=None, dbentries=None):
    """
    Convert KEGG identifiers to/from outside identifiers.
    
    This function allows conversion between KEGG database identifiers and outside database identifiers.
    It supports two modes of operation:
    1. Database-to-database mapping (provide target_db and source_db)
    2. Conversion of specific entries (provide target_db and dbentries)
    
    Args:
        target_db (str): Target database for conversion. For gene identifiers: KEGG organism code or 
                         outside database (ncbi-geneid, ncbi-proteinid, uniprot).
                         For chemical substances: compound, glycan, drug, pubchem, or chebi.
        source_db (str): Source database for conversion. Same options as target_db.
        dbentries (str): Specific database entries to convert, separated by '+' if multiple.
                         
    Returns:
        Returns conversion results between KEGG database identifiers and outside database identifiers.
    Examples:
        # Convert from NCBI GeneID to KEGG ID for E. coli genes
        conv(target_db='eco', source_db='ncbi-geneid')
        
        # Convert specific KEGG IDs to NCBI ProteinID
        conv(target_db='ncbi-proteinid', dbentries='hsa:10458+ece:Z5100')
        
        # Convert from NCBI GeneID to KEGG ID when organism code is unknown
        conv(target_db='genes', dbentries='ncbi-geneid:948364')
    """
    assert (target_db is not None), 'Missing required parameter: target_db'
    assert (source_db is not None or dbentries is not None), 'Missing required parameter: either source_db or dbentries'
    
    if dbentries is not None:
        api_url = f"https://rest.kegg.jp/conv/{quote(target_db, safe='')}/{quote(dbentries, safe='')}"
    else:
        api_url = f"https://rest.kegg.jp/conv/{quote(target_db, safe='')}/{quote(source_db, safe='')}"
    
    response = requests.get(url=api_url, timeout=50)
    return response

if __name__ == '__main__':
    r = conv(target_db='eco', source_db='ncbi-geneid')
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