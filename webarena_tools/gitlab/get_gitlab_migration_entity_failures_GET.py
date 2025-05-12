import requests
from urllib.parse import quote
                
def get_gitlab_migration_entity_failures(import_id=None, entity_id=None):
    api_url = f"/api/v4/bulk_imports/{quote(import_id, safe='')}/entities/{quote(entity_id, safe='')}/failures"
    querystring = {'import_id': import_id, 'entity_id': entity_id, }
    assert import_id is not None, 'Missing required parameter: import_id'
    assert entity_id is not None, 'Missing required parameter: entity_id'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_gitlab_migration_entity_failures(import_id='''import123''', entity_id='''entity456''')
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

