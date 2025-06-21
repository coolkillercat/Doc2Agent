import requests
from urllib.parse import quote
import os
from pathlib import Path

def upload_incident_metric_image(project_id: str, issue_iid: int, file_path: str, url: str = None, url_text: str = None):
    """
    Uploads a screenshot of metric charts to an incident's Metrics tab, allowing teams to visualize and share monitoring data during incident management.
    
    Args:
        project_id (str): The ID or URL-encoded path of the project
        issue_iid (int): The internal ID of the project's issue
        file_path (str): Path to the image file to be uploaded
        url (str, optional): The URL to view more metric information
        url_text (str, optional): A description of the image or URL
        
    Returns:
        Response: The API response containing the uploaded metric image details
        
    Example:
        >>> upload_incident_metric_image(
        ...     project_id="183", 
        ...     issue_iid=1, 
        ...     file_path="path/to/your/image.png", 
        ...     url="http://example.com", 
        ...     url_text="Example metric data"
        ... )
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    endpoint = f"{base_url}/projects/{quote(str(project_id))}/issues/{issue_iid}/metric_images"
    
    headers = {'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    
    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist. Please provide a valid file path.")
    
    # Prepare the multipart form data
    with open(file_path, 'rb') as file_obj:
        files = {'file': file_obj}
        data = {}
        
        if url:
            data['url'] = url
        if url_text:
            data['url_text'] = url_text
        
        # Make the POST request
        response = requests.post(endpoint, headers=headers, files=files, data=data)
    
    return response

if __name__ == '__main__':
    # Create a test image file if it doesn't exist
    test_image_path = "./test_image.png"
    if not os.path.exists(test_image_path):
        from PIL import Image
        img = Image.new('RGB', (100, 100), color = (73, 109, 137))
        img.save(test_image_path)
    
    r = upload_incident_metric_image(
        project_id="183", 
        issue_iid=1, 
        file_path=test_image_path, 
        url="http://example.com", 
        url_text="Example metric data"
    )
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