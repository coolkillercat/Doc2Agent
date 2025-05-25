import requests, json
from urllib.parse import quote


def start_a_new_group_or_project_migration(configuration=None, entities=None, entities_destination_name_=None, entities_migrate_projects_=True):
    api_url = f"https://destination-gitlab-instance.example.com/api/v4/bulk_imports"
    payload = {'configuration': configuration, 'entities': entities, 'entities_destination_name_': entities_destination_name_, 'entities_migrate_projects_': entities_migrate_projects_, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    assert configuration is not None, 'Missing required parameter: configuration'
    assert entities is not None, 'Missing required parameter: entities'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = start_a_new_group_or_project_migration(configuration={'url': 'https://source-gitlab-instance.example.com', 'access_token': '<your_access_token_for_source_gitlab_instance>'}, entities=[{'source_full_path': 'source/full/path', 'source_type': 'group_entity', 'destination_slug': 'destination_slug', 'destination_namespace': 'destination/namespace/path'}], entities_destination_name_=destination_name, entities_migrate_projects_=True)
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

