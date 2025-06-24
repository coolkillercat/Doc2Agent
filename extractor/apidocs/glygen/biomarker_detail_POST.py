import requests, json
from urllib.parse import quote

def biomarker_detail(biomarker_id='AA4686-1', payload=None):
    """
    Retrieve detailed information about a specific biomarker.
    
    Args:
        biomarker_id (str): The ID of the biomarker to retrieve details for. Default is 'AA4686-1'.
        payload (dict, optional): Additional parameters to include in the request. 
                                If None, a default payload with the biomarker_id will be created.
    
    Returns:
        requests.Response: The response from the API.
    
    Example:
        >>> response = biomarker_detail('AA4686-1')
        >>> response = biomarker_detail(biomarker_id='AN6385-1', payload={'biomarker_id': 'AN6385-1'})
    """
    api_url = f"https://api.glygen.org/biomarker/detail/{quote(biomarker_id)}/"
    
    if payload is None:
        payload = {"biomarker_id": biomarker_id}
    
    headers = {"Content-Type": "application/json"}
    
    assert biomarker_id is not None, 'Missing required parameter: biomarker_id'
    
    response = requests.post(url=api_url, json=payload, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = biomarker_detail(biomarker_id='AA4686-1')
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