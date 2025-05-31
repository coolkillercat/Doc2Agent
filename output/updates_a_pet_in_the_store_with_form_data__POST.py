import requests
from urllib.parse import quote
                
def updates_a_pet_in_the_store_with_form_data_(petId=None, name=None, status=None):
    api_url = f"/pet/{petId}"
    payload = {'petId': petId, 'name': name, 'status': status, }
    assert petId is not None, 'Missing required parameter: petId'
    
    response = requests.post(url=api_url, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = updates_a_pet_in_the_store_with_form_data_(petId=example, name='''example''', status='''example''')
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

