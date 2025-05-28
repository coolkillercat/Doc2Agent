import json

import requests


def get_shopping_admin_admin_auth_token():
    response = requests.post(
        url='http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/integration/admin/token',
        headers={'content-type': 'application/json'},
        data=json.dumps({'username': 'admin', 'password': 'admin1234'}),
    )
    return response.json()


def get_product_list(
    searchCriteria_filterGroups__0__filters__0__field=None,
    searchCriteria_filterGroups__0__filters__0__value=None,
    searchCriteria_filterGroups__0__filters__0__conditionType=None,
    searchCriteria_sortOrders__0__field=None,
    searchCriteria_sortOrders__0__direction=None,
    searchCriteria_pageSize=None,
    searchCriteria_currentPage=None,
):
    """
    Get a list of products based on search criteria.

    Args:
        searchCriteria_filterGroups__0__filters__0__field: Field to filter by
        searchCriteria_filterGroups__0__filters__0__value: Value to filter with
        searchCriteria_filterGroups__0__filters__0__conditionType: Condition type for filtering
        searchCriteria_sortOrders__0__field: Field to sort by
        searchCriteria_sortOrders__0__direction: Sort direction (asc/desc)
        searchCriteria_pageSize: Number of items per page
        searchCriteria_currentPage: Current page number

    Returns:
        Response object from the API request
    """
    api_url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/products'
    querystring = {
        'searchCriteria[filterGroups][0][filters][0][field]': searchCriteria_filterGroups__0__filters__0__field,
        'searchCriteria[filterGroups][0][filters][0][value]': searchCriteria_filterGroups__0__filters__0__value,
        'searchCriteria[filterGroups][0][filters][0][conditionType]': searchCriteria_filterGroups__0__filters__0__conditionType,
        'searchCriteria[sortOrders][0][field]': searchCriteria_sortOrders__0__field,
        'searchCriteria[sortOrders][0][direction]': searchCriteria_sortOrders__0__direction,
        'searchCriteria[pageSize]': searchCriteria_pageSize,
        'searchCriteria[currentPage]': searchCriteria_currentPage,
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
    if response.status_code != 200:
        response2 = requests.get(
            url=api_url, headers=headers, timeout=50, verify=False
        )  # in case API can't handle redundant params
        response = response2
    return response


if __name__ == '__main__':
    r = get_product_list(
        searchCriteria_filterGroups__0__filters__0__field='name',
        searchCriteria_filterGroups__0__filters__0__value='laptop',
        searchCriteria_filterGroups__0__filters__0__conditionType='eq',
        searchCriteria_sortOrders__0__field='price',
        searchCriteria_sortOrders__0__direction='asc',
        searchCriteria_pageSize=10,
        searchCriteria_currentPage=1,
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
