import requests
from urllib.parse import quote
                
def retry_builds_in_the_pipeline(id=None, pipeline_id=None):
    api_url = f"/api/v4/projects/{id}/pipelines/{pipeline_id}/retry"
    payload = {'id': id, 'pipeline_id': pipeline_id, }
    assert id is not None, 'Missing required parameter: id'
    assert pipeline_id is not None, 'Missing required parameter: pipeline_id'
    
    response = requests.post(url=api_url, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = retry_builds_in_the_pipeline(id=1, pipeline_id=100)
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

