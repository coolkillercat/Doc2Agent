import json

import requests


def get_shopping_admin_admin_auth_token():
    response = requests.post(
        url='http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/integration/admin/token',
        headers={'content-type': 'application/json'},
        data=json.dumps({'username': 'admin', 'password': 'admin1234'}),
    )
    return response.json()


def get_product_render_info(
    storeId=None,
    currencyCode=None,
    searchCriteria_filterGroups__0__filters__0__field_=None,
    searchCriteria_filterGroups__0__filters__0__value_=None,
    searchCriteria_filterGroups__0__filters__0__conditionType_=None,
    searchCriteria_sortOrders__0__field_=None,
    searchCriteria_sortOrders__0__direction_=None,
    searchCriteria_pageSize_=None,
    searchCriteria_currentPage_=None,
):
    """
    Get product render information based on search criteria.

    Args:
        storeId (int): The store ID (required)
        currencyCode (str): The currency code (required)
        searchCriteria_filterGroups__0__filters__0__field_ (str): Filter field
        searchCriteria_filterGroups__0__filters__0__value_ (str): Filter value
        searchCriteria_filterGroups__0__filters__0__conditionType_ (str): Filter condition type
        searchCriteria_sortOrders__0__field_ (str): Sort field
        searchCriteria_sortOrders__0__direction_ (str): Sort direction
        searchCriteria_pageSize_ (int): Page size
        searchCriteria_currentPage_ (int): Current page

    Returns:
        Response object from the API call
    """
    api_url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/products-render-info'

    assert storeId is not None, 'Missing required parameter: storeId'
    assert currencyCode is not None, 'Missing required parameter: currencyCode'

    querystring = {
        'storeId': storeId,
        'currencyCode': currencyCode,
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
    if response.status_code != 200:
        response2 = requests.get(
            url=api_url, timeout=50
        )  # in case API can't handle redundant params
        response = response2
    return response


if __name__ == '__main__':
    r = get_product_render_info(
        storeId=1,
        currencyCode='USD',
        searchCriteria_filterGroups__0__filters__0__field_='name',
        searchCriteria_filterGroups__0__filters__0__value_='laptop',
        searchCriteria_filterGroups__0__filters__0__conditionType_='eq',
        searchCriteria_sortOrders__0__field_='price',
        searchCriteria_sortOrders__0__direction_='asc',
        searchCriteria_pageSize_=10,
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
