import requests
from urllib.parse import quote

def get_gene_centric_proteins_by_proteome_upid__deprecated_(upid=None):
    """
    Get gene centric proteins by proteome UPID (deprecated).
    
    This function is deprecated. Please use the new /genecentric?upid= endpoint.
    
    Args:
        upid (str): UniProt Proteome UPID. Format should match UP[0-9]{9}.
                    Example: 'UP000005640' (Human proteome)
    
    Returns:
        Returns proteome information including genes, taxonomy, annotation scores, and genome assembly details for a specified UniProt Proteome ID.
    Raises:
        AssertionError: If the required parameter 'upid' is not provided.
    
    Example:
        >>> response = get_gene_centric_proteins_by_proteome_upid__deprecated_(upid='UP000005640')
        >>> print(response.status_code)
        200
    """
    base_url = "https://www.ebi.ac.uk"
    assert upid is not None, 'Missing required parameter: upid'
    
    # Ensure upid follows the correct format (UP followed by 9 digits)
    if not upid.startswith('UP') or not len(upid) == 11 or not upid[2:].isdigit():
        raise ValueError("Invalid upid format. Must be UP followed by 9 digits (e.g., UP000005640)")
    
    api_url = f"{base_url}/proteins/api/proteomes/genecentric/{upid}"
    headers = {'Content-Type': 'application/json'}
    
    response = requests.get(url=api_url, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    # Using a valid proteome ID (Human proteome)
    r = get_gene_centric_proteins_by_proteome_upid__deprecated_(upid='UP000005640')
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