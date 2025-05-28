import json

import requests


def get_shopping_admin_admin_auth_token():
    response = requests.post(
        url='http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/integration/admin/token',
        headers={'content-type': 'application/json'},
        data=json.dumps({'username': 'admin', 'password': 'admin1234'}),
    )
    return response.json()


def search_tax_rates(
    searchCriteria_filterGroups__0__filters__0__field=None,
    searchCriteria_filterGroups__0__filters__0__value=None,
    searchCriteria_filterGroups__0__filters__0__conditionType=None,
    searchCriteria_sortOrders__0__field=None,
    searchCriteria_sortOrders__0__direction=None,
    searchCriteria_pageSize=None,
    searchCriteria_currentPage=None,
):
    """
    Search for tax rates based on specified criteria.

    Args:
        searchCriteria_filterGroups__0__filters__0__field: Field to filter by (e.g., 'rate')
        searchCriteria_filterGroups__0__filters__0__value: Value to filter by (e.g., '5%')
        searchCriteria_filterGroups__0__filters__0__conditionType: Condition type (e.g., 'gteq')
        searchCriteria_sortOrders__0__field: Field to sort by (e.g., 'rate')
        searchCriteria_sortOrders__0__direction: Sort direction (e.g., 'DESC')
        searchCriteria_pageSize: Number of items per page
        searchCriteria_currentPage: Current page number

    Returns:
        Response object from the API request
    """
    api_url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/taxRates/search'
    querystring = {}

    if searchCriteria_filterGroups__0__filters__0__field is not None:
        querystring['searchCriteria[filterGroups][0][filters][0][field]'] = (
            searchCriteria_filterGroups__0__filters__0__field
        )
    if searchCriteria_filterGroups__0__filters__0__value is not None:
        querystring['searchCriteria[filterGroups][0][filters][0][value]'] = (
            searchCriteria_filterGroups__0__filters__0__value
        )
    if searchCriteria_filterGroups__0__filters__0__conditionType is not None:
        querystring['searchCriteria[filterGroups][0][filters][0][conditionType]'] = (
            searchCriteria_filterGroups__0__filters__0__conditionType
        )
    if searchCriteria_sortOrders__0__field is not None:
        querystring['searchCriteria[sortOrders][0][field]'] = (
            searchCriteria_sortOrders__0__field
        )
    if searchCriteria_sortOrders__0__direction is not None:
        querystring['searchCriteria[sortOrders][0][direction]'] = (
            searchCriteria_sortOrders__0__direction
        )
    if searchCriteria_pageSize is not None:
        querystring['searchCriteria[pageSize]'] = searchCriteria_pageSize
    if searchCriteria_currentPage is not None:
        querystring['searchCriteria[currentPage]'] = searchCriteria_currentPage

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + get_shopping_admin_admin_auth_token(),
    }

    response = requests.get(
        url=api_url, headers=headers, params=querystring, timeout=50, verify=False
    )
    if response.status_code != 200:
        response2 = requests.get(url=api_url, headers=headers, timeout=50, verify=False)
        response = response2
    return response


if __name__ == '__main__':
    r = search_tax_rates(
        searchCriteria_filterGroups__0__filters__0__field='rate',
        searchCriteria_filterGroups__0__filters__0__value='5%',
        searchCriteria_filterGroups__0__filters__0__conditionType='gteq',
        searchCriteria_sortOrders__0__field='rate',
        searchCriteria_sortOrders__0__direction='DESC',
        searchCriteria_pageSize=20,
        searchCriteria_currentPage=2,
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
