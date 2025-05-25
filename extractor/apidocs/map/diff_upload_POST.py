import requests, json
from urllib.parse import quote


def diff_upload(id=None, POST_data=None):
    """
    Upload a diff in OsmChange format to a changeset.
    
    This API call uploads files in the OsmChange format to the server. 
    This is guaranteed to be running in a transaction, so either all 
    changes are applied or none.
    
    Parameters:
    -----------
    id : str
        The ID of the changeset this diff belongs to.
    POST_data : str or file-like object
        The OsmChange file data to upload.
        
    Returns:
    --------
    response : requests.Response
        The response from the API call.
        
    Example:
    --------
    >>> with open('changes.osc', 'r') as f:
    ...     response = diff_upload(id='12345', POST_data=f.read())
    """
    assert id is not None, 'Missing required parameter: id'
    assert POST_data is not None, 'Missing required parameter: POST_data'
    
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:3000/api/0.6/changeset/{id}/upload"
    
    # Send the POST_data directly in the request body
    response = requests.post(url=api_url, data=POST_data, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    # Example usage - you need to define osmchange_data with actual OsmChange content
    osmchange_data = """<osmChange version="0.6" generator="JOSM">
    <!-- Your OsmChange content here -->
    </osmChange>"""
    
    r = diff_upload(id='12345', POST_data=osmchange_data)
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