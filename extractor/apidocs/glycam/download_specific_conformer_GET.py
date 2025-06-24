import requests
from urllib.parse import quote

def download_specific_conformer(pUUID, conformerID):
    """
    Download a specific conformer PDB file from the GLYCAM-Web API.
    
    This function makes a GET request to the GLYCAM-Web API to download a PDB file
    for a specific conformer of a molecular structure.
    
    Parameters:
    -----------
    pUUID : str
        The project UUID that identifies the build project.
    conformerID : str
        The ID of the specific conformer to download.
    
    Returns:
    --------
    requests.Response
        The response object containing the PDB file if successful.
    
    Examples:
    ---------
    >>> response = download_specific_conformer("3c368bf2-ad73-43f3-a18d-d7d2dc11cf28", "1ogg")
    >>> with open("molecule.pdb", "wb") as f:
    ...     f.write(response.content)
    """
    assert pUUID is not None, 'Missing required parameter: pUUID'
    assert conformerID is not None, 'Missing required parameter: conformerID'
    
    api_url = f"https://glycam.org/json/download/sequence/cb/{quote(pUUID, safe='')}/{quote(conformerID, safe='')}/"
    
    response = requests.get(url=api_url, timeout=50)
    return response

if __name__ == '__main__':
    r = download_specific_conformer(pUUID='3c368bf2-ad73-43f3-a18d-d7d2dc11cf28', conformerID='1ogg')
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