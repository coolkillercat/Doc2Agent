import json

import requests


def get_shopping_admin_admin_auth_token():
    response = requests.post(
        url='http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/integration/admin/token',
        headers={'content-type': 'application/json'},
        data=json.dumps({'username': 'admin', 'password': 'admin1234'}),
    )
    return response.json()


def get_category_list(
    searchCriteria_filterGroups__0__filters__0__field_=None,
    searchCriteria_filterGroups__0__filters__0__value_=None,
    searchCriteria_filterGroups__0__filters__0__conditionType_=None,
    searchCriteria_sortOrders__0__field_=None,
    searchCriteria_sortOrders__0__direction_=None,
    searchCriteria_pageSize_=None,
    searchCriteria_currentPage_=None,
):
    """
    Get a list of categories based on search criteria.

    Args:
        searchCriteria_filterGroups__0__filters__0__field_: Field to filter by
        searchCriteria_filterGroups__0__filters__0__value_: Value to filter by
        searchCriteria_filterGroups__0__filters__0__conditionType_: Condition type for filtering
        searchCriteria_sortOrders__0__field_: Field to sort by
        searchCriteria_sortOrders__0__direction_: Sort direction (ASC or DESC)
        searchCriteria_pageSize_: Number of items per page
        searchCriteria_currentPage_: Current page number

    Returns:
        Response object from the API request
    """
    api_url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/categories/list'

    # Remove None values from querystring
    querystring = {}
    if searchCriteria_filterGroups__0__filters__0__field_:
        querystring['searchCriteria[filterGroups][0][filters][0][field]'] = (
            searchCriteria_filterGroups__0__filters__0__field_
        )
    if searchCriteria_filterGroups__0__filters__0__value_:
        querystring['searchCriteria[filterGroups][0][filters][0][value]'] = (
            searchCriteria_filterGroups__0__filters__0__value_
        )
    if searchCriteria_filterGroups__0__filters__0__conditionType_:
        querystring['searchCriteria[filterGroups][0][filters][0][conditionType]'] = (
            searchCriteria_filterGroups__0__filters__0__conditionType_
        )
    if searchCriteria_sortOrders__0__field_:
        querystring['searchCriteria[sortOrders][0][field]'] = (
            searchCriteria_sortOrders__0__field_
        )
    if searchCriteria_sortOrders__0__direction_:
        querystring['searchCriteria[sortOrders][0][direction]'] = (
            searchCriteria_sortOrders__0__direction_
        )
    if searchCriteria_pageSize_:
        querystring['searchCriteria[pageSize]'] = searchCriteria_pageSize_
    if searchCriteria_currentPage_:
        querystring['searchCriteria[currentPage]'] = searchCriteria_currentPage_

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + get_shopping_admin_admin_auth_token(),
    }

    response = requests.get(
        url=api_url, headers=headers, params=querystring, timeout=50, verify=False
    )
    return response


if __name__ == '__main__':
    r = get_category_list(
        searchCriteria_filterGroups__0__filters__0__field_="""name""",
        searchCriteria_filterGroups__0__filters__0__value_="""furniture""",
        searchCriteria_filterGroups__0__filters__0__conditionType_="""like""",
        searchCriteria_sortOrders__0__field_="""name""",
        searchCriteria_sortOrders__0__direction_="""DESC""",
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
