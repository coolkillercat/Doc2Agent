import json

import requests


def get_shopping_admin_admin_auth_token():
    response = requests.post(
        url='http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/integration/admin/token',
        headers={'content-type': 'application/json'},
        data=json.dumps({'username': 'admin', 'password': 'admin1234'}),
    )
    return response.json()


def retrieve_all_attributes_for_entity_type(
    searchCriteria_filterGroups__0__filters__0__field_=None,
    searchCriteria_filterGroups__0__filters__0__value_=None,
    searchCriteria_filterGroups__0__filters__0__conditionType_=None,
    searchCriteria_sortOrders__0__field_=None,
    searchCriteria_sortOrders__0__direction_=None,
    searchCriteria_pageSize_=None,
    searchCriteria_currentPage_=None,
):
    api_url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/products/attributes'
    querystring = {
        'searchCriteria_filterGroups__0__filters__0__field_': searchCriteria_filterGroups__0__filters__0__field_,
        'searchCriteria_filterGroups__0__filters__0__value_': searchCriteria_filterGroups__0__filters__0__value_,
        'searchCriteria_filterGroups__0__filters__0__conditionType_': searchCriteria_filterGroups__0__filters__0__conditionType_,
        'searchCriteria_sortOrders__0__field_': searchCriteria_sortOrders__0__field_,
        'searchCriteria_sortOrders__0__direction_': searchCriteria_sortOrders__0__direction_,
        'searchCriteria_pageSize_': searchCriteria_pageSize_,
        'searchCriteria_currentPage_': searchCriteria_currentPage_,
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + get_shopping_admin_admin_auth_token(),
    }

    response = requests.get(
        url=api_url, headers=headers, params=querystring, timeout=50, verify=False
    )
    if response.status_code != 200:
        response2 = requests.get(
            url=api_url, timeout=50
        )  # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())


if __name__ == '__main__':
    r = retrieve_all_attributes_for_entity_type(
        searchCriteria_filterGroups__0__filters__0__field_="""name""",
        searchCriteria_filterGroups__0__filters__0__value_="""size""",
        searchCriteria_filterGroups__0__filters__0__conditionType_="""eq""",
        searchCriteria_sortOrders__0__field_="""created_at""",
        searchCriteria_sortOrders__0__direction_="""ASC""",
        searchCriteria_pageSize_=20,
        searchCriteria_currentPage_=1,
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
    result_dict['content'] = r.content.decode('utf-8')
    print(json.dumps(result_dict, indent=4))
