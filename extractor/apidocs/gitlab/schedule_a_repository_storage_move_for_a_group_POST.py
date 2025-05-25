import requests, json
from urllib.parse import quote


def schedule_a_repository_storage_move_for_a_group(group_id=None, destination_storage_name=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/groups/:group_id/repository_storage_moves"
    payload = {'group_id': group_id, 'destination_storage_name': destination_storage_name, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    assert group_id is not None, 'Missing required parameter: group_id'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = schedule_a_repository_storage_move_for_a_group(group_id=1, destination_storage_name='''storage2''')
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

