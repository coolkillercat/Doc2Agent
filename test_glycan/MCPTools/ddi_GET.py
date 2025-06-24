import requests
from urllib.parse import quote

def ddi(dbentry=None, multiple_entries=None):
    """
    Find adverse drug-drug interactions from the KEGG database.
    
    This function queries the KEGG API to find drug-drug interactions designated as 
    contraindication (CI) and precaution (P) in Japanese drug labels.
    
    Args:
        dbentry (str): A single drug entry identifier (e.g., 'D00564').
        multiple_entries (list, optional): A list of drug identifiers to check for interactions
                                          between them (e.g., ['D00564', 'D00100']).
    
    Returns:
        Returns adverse drug-drug interactions designated as contraindication (CI) and precaution (P) in Japanese drug labels for specified drug entries.
    Examples:
        >>> response = ddi(dbentry='D00564')  # Get all interactions for a single drug
        >>> response = ddi(multiple_entries=['D00564', 'D00100', 'D00109'])  # Check interactions between drugs
    """
    if multiple_entries:
        # Join multiple entries with '+' for checking interactions between them
        query = '+'.join(multiple_entries)
    elif dbentry:
        query = dbentry
    else:
        raise ValueError('Missing required parameter: either dbentry or multiple_entries must be provided')
    
    api_url = f"https://rest.kegg.jp/ddi/{quote(query, safe='')}"
    
    response = requests.get(url=api_url, timeout=50)
    return response

if __name__ == '__main__':
    r = ddi(dbentry='D00564')
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