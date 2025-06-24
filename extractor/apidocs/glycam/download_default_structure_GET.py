import requests
from urllib.parse import quote

def download_default_structure(pUUID=None, conformer_id=None):
    """
    Download a structure from GLYCAM-Web.
    
    This function downloads a structure file from GLYCAM-Web using the provided project UUID.
    If a conformer_id is provided, it will download that specific conformer.
    Otherwise, it will download the default structure.
    
    Args:
        pUUID (str): The project UUID obtained from a Build3DStructure response.
        conformer_id (str, optional): The specific conformer ID to download. Defaults to None.
        
    Returns:
        requests.Response: The response object containing the downloaded structure.
        
    Examples:
        >>> response = download_default_structure(pUUID="3c368bf2-ad73-43f3-a18d-d7d2dc11cf28")
        >>> response = download_default_structure(pUUID="3c368bf2-ad73-43f3-a18d-d7d2dc11cf28", conformer_id="1ogg")
    """
    assert pUUID is not None, 'Missing required parameter: pUUID'
    
    if conformer_id:
        api_url = f"https://glycam.org/json/download/sequence/cb/{quote(pUUID, safe='')}/{quote(conformer_id, safe='')}"
    else:
        api_url = f"https://glycam.org/json/download/sequence/cb/{quote(pUUID, safe='')}"
    
    headers = {}
    response = requests.get(url=api_url, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = download_default_structure(pUUID='3c368bf2-ad73-43f3-a18d-d7d2dc11cf28')
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