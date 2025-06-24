import requests, json
from urllib.parse import quote

def get_proteome_by_upid(upid=None):
    """
    Get proteome information by UniProt Proteome UPID.
    
    Args:
        upid (str): UniProt Proteome UPID. Format should match UP[0-9]{9}.
                    Example: 'UP000005640' (Human proteome)
    
    Returns:
        Returns comprehensive proteome information including taxonomy, genome assembly details, annotation scores, and component data for a specified UniProt Proteome ID.
    Raises:
        AssertionError: If upid parameter is not provided.
        
    Example:
        >>> response = get_proteome_by_upid(upid='UP000005640')
        >>> proteome_data = response.json()
    """
    assert upid is not None, 'Missing required parameter: upid'
    
    base_url = "https://www.ebi.ac.uk"
    api_url = f"{base_url}/proteins/api/proteomes/{upid}"
    
    headers = {'Content-Type': 'application/json'}
    
    response = requests.get(url=api_url, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    # Using a valid proteome ID (Human proteome)
    r = get_proteome_by_upid(upid='UP000005640')
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