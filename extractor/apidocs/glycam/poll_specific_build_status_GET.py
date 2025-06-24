import requests
import json
from urllib.parse import quote

def get_conformer_build_status(pUUID, conformerID, test=False):
    """
    Poll for the status of a specific build using pUUID and conformerID.
    
    This function checks the status of a specific molecular structure build
    by querying the GLYCAM API with the provided project UUID and conformer ID.
    
    Parameters:
    -----------
    pUUID : str
        The project UUID that identifies the build project.
    conformerID : str
        The ID of the specific conformer to check.
    test : bool, optional
        Flag to indicate if this is a test request. Default is False.
    
    Returns:
    --------
    requests.Response
        The response object from the API request containing build status information.
        The JSON response typically includes fields like:
        - minExists: Whether minimization is complete
        - tip3pExists: Whether TIP3P solvation is complete
        - tip5pExists: Whether TIP5P solvation is complete
        - conformerID: The ID of the conformer
        - status: Overall status (e.g., "All complete", "2 of 3 complete")
    
    Example:
    --------
    >>> response = get_conformer_build_status("3c368bf2-ad73-43f3-a18d-d7d2dc11cf28", "1ogg")
    >>> print(response.json())
    {
        "minExists": true,
        "tip3pExists": true,
        "tip5pExists": true,
        "conformerID": "1ogg",
        "status": "All complete"
    }
    """
    assert pUUID is not None, 'Missing required parameter: pUUID'
    assert conformerID is not None, 'Missing required parameter: conformerID'
    
    api_url = f"https://glycam.org/json/build_status/{pUUID}/{conformerID}/"
    
    if test:
        api_url += "?test=true"
    
    headers = {}
    
    response = requests.get(url=api_url, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = get_conformer_build_status(pUUID='3c368bf2-ad73-43f3-a18d-d7d2dc11cf28', conformerID='1ogg')
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