import requests
import json

def get_proteins(query_protein=None):
    """
    Retrieve detailed protein information from the O-GlcNAc Database.
    
    This function queries the O-GlcNAc Database API to retrieve comprehensive 
    information about a specified protein, including post-translational 
    modifications (PTMs), gene names, sequence data, and O-GlcNAcylation sites.
    
    Args:
        query_protein (str): UniProtKB ID of the protein to query (e.g., 'P08047')
    
    Returns:
        requests.Response: The API response containing protein information
        
    Example:
        >>> response = get_proteins(query_protein='P08047')
        >>> protein_data = response.json()
    """
    api_url = "https://oglcnac.mcw.edu/api/v1/proteins/"
    
    assert query_protein is not None, 'Missing required parameter: query_protein'
    
    querystring = {'query_protein': query_protein}
    headers = {}
    
    response = requests.get(url=api_url, params=querystring, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = get_proteins(query_protein='P08047')
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