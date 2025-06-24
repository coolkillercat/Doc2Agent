import requests, json
from urllib.parse import quote

def poll_project_status(pUUID=None):
    """
    Poll for the status of a default structure's project files.
    
    This function checks the status of a project by making a GET request to the GLYCAM API.
    The status can be "All complete", "minimizing", "submitted", etc.
    
    Args:
        pUUID (str): The project UUID obtained from a Build3DStructure response.
                     Example: "a997768f-6097-4aa6-9789-c756252358df"
    
    Returns:
        Returns the current status of a 3D structure project along with its default conformer ID and file path.
    Raises:
        AssertionError: If pUUID is None.
        requests.exceptions.RequestException: If the request fails.
    """
    assert pUUID is not None, 'Missing required parameter: pUUID'
    
    api_url = f"https://glycam.org/json/project_status/sequence/{pUUID}/"
    headers = {}
    
    response = requests.get(url=api_url, headers=headers, timeout=50)
    response.raise_for_status()
    return response.json()

if __name__ == '__main__':
    r = poll_project_status(pUUID='a997768f-6097-4aa6-9789-c756252358df')
    result_dict = dict()
    result_dict['status_code'] = 200
    result_dict['text'] = json.dumps(r)
    result_dict['json'] = r
    result_dict['content'] = json.dumps(r)
    print(json.dumps(result_dict, indent=4))