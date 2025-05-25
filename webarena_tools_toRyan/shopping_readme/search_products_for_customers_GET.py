import requests
from urllib.parse import quote
                
def search_products_for_customers(searchCriteria_requestName_=None, searchCriteria_filterGroups__0__filters__0__field_=None, searchCriteria_filterGroups__0__filters__0__value_=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/search"
    querystring = {
        'searchCriteria[requestName]': searchCriteria_requestName_,
        'searchCriteria[filterGroups][0][filters][0][field]': searchCriteria_filterGroups__0__filters__0__field_,
        'searchCriteria[filterGroups][0][filters][0][value]': searchCriteria_filterGroups__0__filters__0__value_,
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer eyJraWQiOiIxIiwiYWxnIjoiSFMyNTYifQ.eyJ1aWQiOjI3LCJ1dHlwaWQiOjMsImlhdCI6MTc0NzQ0MzM1NCwiZXhwIjoxNzQ3NDQ2OTU0fQ.I5TPXdqzfz5Bt3iPa5lruhK-cr8zuDJZxJlvIDOhUP8",
    }
    assert searchCriteria_requestName_ is not None, 'Missing required parameter: searchCriteria_requestName_'
    assert searchCriteria_filterGroups__0__filters__0__field_ is not None, 'Missing required parameter: searchCriteria_filterGroups__0__filters__0__field_'
    assert searchCriteria_filterGroups__0__filters__0__value_ is not None, 'Missing required parameter: searchCriteria_filterGroups__0__filters__0__value_'
    
    response = requests.get(url=api_url, headers=headers, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = search_products_for_customers(searchCriteria_requestName_='''quick_search_container''', searchCriteria_filterGroups__0__filters__0__field_='''search_term''', searchCriteria_filterGroups__0__filters__0__value_='''digital watch''')
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