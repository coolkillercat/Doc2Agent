import json

import requests


def get_shopping_admin_admin_auth_token():
    response = requests.post(
        url='http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/integration/admin/token',
        headers={'content-type': 'application/json'},
        data=json.dumps({'username': 'admin', 'password': 'admin1234'}),
    )
    return response.json()


def list_orders(
    searchCriteria_filterGroups__0__filters__0__field_=None,
    searchCriteria_filterGroups__0__filters__0__value_=None,
    searchCriteria_filterGroups__0__filters__0__conditionType_=None,
    searchCriteria_sortOrders__0__field_=None,
    searchCriteria_sortOrders__0__direction_=None,
    searchCriteria_pageSize_=None,
    searchCriteria_currentPage_=None,
):
    """
    List orders from the Magento API with search criteria.

    Args:
        searchCriteria_filterGroups__0__filters__0__field_: Field to filter by (e.g., 'status')
        searchCriteria_filterGroups__0__filters__0__value_: Value to filter by (e.g., 'pending')
        searchCriteria_filterGroups__0__filters__0__conditionType_: Condition type (e.g., 'eq')
        searchCriteria_sortOrders__0__field_: Field to sort by (e.g., 'created_at')
        searchCriteria_sortOrders__0__direction_: Sort direction (e.g., 'ASC')
        searchCriteria_pageSize_: Number of results per page
        searchCriteria_currentPage_: Current page number

    Returns:
        Response object from the API request
    """
    api_url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/orders'

    # Fix parameter names by removing trailing underscores
    querystring = {
        'searchCriteria[filterGroups][0][filters][0][field]': searchCriteria_filterGroups__0__filters__0__field_,
        'searchCriteria[filterGroups][0][filters][0][value]': searchCriteria_filterGroups__0__filters__0__value_,
        'searchCriteria[filterGroups][0][filters][0][conditionType]': searchCriteria_filterGroups__0__filters__0__conditionType_,
        'searchCriteria[sortOrders][0][field]': searchCriteria_sortOrders__0__field_,
        'searchCriteria[sortOrders][0][direction]': searchCriteria_sortOrders__0__direction_,
        'searchCriteria[pageSize]': searchCriteria_pageSize_,
        'searchCriteria[currentPage]': searchCriteria_currentPage_,
    }

    # Remove None values
    querystring = {k: v for k, v in querystring.items() if v is not None}

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + get_shopping_admin_admin_auth_token(),
    }

    response = requests.get(
        url=api_url, headers=headers, params=querystring, timeout=50, verify=False
    )
    return response


if __name__ == '__main__':
    r = list_orders(
        searchCriteria_filterGroups__0__filters__0__field_="""status""",
        searchCriteria_filterGroups__0__filters__0__value_="""pending""",
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
