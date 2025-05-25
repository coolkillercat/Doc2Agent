import requests
from urllib.parse import quote
                
def get_all_drupal_association_individual_members(field_da_ind_membership_value___=None):
    api_url = f"https://www.drupal.org/api-d7/user.json"
    querystring = {'field_da_ind_membership_value___': field_da_ind_membership_value___, }
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_all_drupal_association_individual_members(field_da_ind_membership_value___='''Current''')
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

