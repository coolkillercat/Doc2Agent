import requests
from typing import List, Optional, Union


def search_protein_sequence_features_by_type(
    type: str, 
    terms: Union[str, List[str]], 
    offset: Optional[int] = 0, 
    size: int = 100, 
    categories: Optional[Union[str, List[str]]] = None, 
    types: Optional[Union[str, List[str]]] = None
):
    """
    Search protein sequence features of a given type in UniProt.
    
    Args:
        type (str): Feature type (e.g., DOMAIN, CHAIN, VARIANT)
        terms (Union[str, List[str]]): Search terms that appear in feature description
        offset (int, optional): Page starting point. Defaults to 0.
        size (int, optional): Page size. Defaults to 100. When -1, returns all records.
        categories (Union[str, List[str]], optional): Category types (e.g., MOLECULE_PROCESSING, TOPOLOGY)
        types (Union[str, List[str]], optional): Additional feature types
    
    Returns:
        Returns protein sequence features of a specified type from UniProt, including protein accession, entry name, sequence data, and associated features matching the search terms.
    Example:
        >>> response = search_protein_sequence_features_by_type(
        ...     type="DOMAIN", 
        ...     terms=["Kinase"], 
        ...     offset=0, 
        ...     size=100, 
        ...     categories=["MOLECULE_PROCESSING"], 
        ...     types=["DOMAIN", "CHAIN"]
        ... )
    """
    base_url = "https://www.ebi.ac.uk"
    api_url = f"{base_url}/proteins/api/features/type/{type}"
    
    # Prepare parameters
    params = {'offset': offset, 'size': size}
    
    # Handle list parameters
    if isinstance(terms, list):
        params['terms'] = ','.join(terms)
    else:
        params['terms'] = terms
        
    if categories:
        if isinstance(categories, list):
            params['categories'] = ','.join(categories)
        else:
            params['categories'] = categories
            
    if types:
        if isinstance(types, list):
            params['types'] = ','.join(types)
        else:
            params['types'] = types
    
    headers = {'Content-Type': 'application/json'}
    
    response = requests.get(url=api_url, params=params, headers=headers, timeout=50)
    return response


if __name__ == '__main__':
    r = search_protein_sequence_features_by_type(type='DOMAIN', terms=['Kinase'], offset=0, size=100, categories=['MOLECULE_PROCESSING'], types=['DOMAIN', 'CHAIN'])
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