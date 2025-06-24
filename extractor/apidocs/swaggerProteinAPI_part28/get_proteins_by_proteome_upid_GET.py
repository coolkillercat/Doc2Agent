import requests
from urllib.parse import quote

def get_proteins_by_proteome_upid(upid=None, reviewed=None):
    """
    Get proteins by proteome UPID from the EBI API.
    
    Args:
        upid (str): UniProt Proteome UPID. Required. Format should match UP[0-9]{9}.
        reviewed (str, optional): Filter for reviewed proteins. 
                                 Set to 'true' for reviewed proteins only, 
                                 'false' for unreviewed proteins only.
    
    Returns:
        Returns protein information for a specified proteome identified by its UniProt Proteome ID (UPID), with optional filtering for reviewed or unreviewed proteins.
    Examples:
        >>> response = get_proteins_by_proteome_upid(upid='UP000005640', reviewed='true')
        >>> response = get_proteins_by_proteome_upid(upid='UP000005640')
    """
    base_url = "https://www.ebi.ac.uk"
    api_url = f"{base_url}/proteins/api/proteomes/proteins/{upid}"
    
    assert upid is not None, 'Missing required parameter: upid'
    
    querystring = {}
    if reviewed is not None:
        querystring['reviewed'] = reviewed
    
    headers = {'Content-Type': 'application/json'}
    
    response = requests.get(url=api_url, params=querystring, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = get_proteins_by_proteome_upid(upid='UP000005640', reviewed='true')
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