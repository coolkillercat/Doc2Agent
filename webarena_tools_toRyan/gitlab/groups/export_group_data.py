import requests, json
from urllib.parse import quote

def export_group_data(group_id: str, include_relations: bool = False, output_format: str = 'json'):
    """
    Exports data from a specified group, with options to include relationship data and choose output format.
    
    Args:
        group_id (str): The ID or URL-encoded path of the group to export.
        include_relations (bool, optional): Include relationship data in the export. Defaults to False.
        output_format (str, optional): The export format. Can be 'json' or 'ndjson'. Defaults to 'json'.
    
    Returns:
        requests.Response: The API response containing the exported group data.
    
    Examples:
        >>> export_group_data(group_id='2597')
        >>> export_group_data(group_id='183', include_relations=True, output_format='json')
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    encoded_group_id = quote(str(group_id), safe='')
    
    url = f"{base_url}/groups/{encoded_group_id}/export"
    
    params = {
        'include_relations': include_relations,
        'format': output_format
    }
    
    response = requests.get(url, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = export_group_data(group_id='183', include_relations=True, output_format='json')
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