import requests


def search(
    pattern=None,
    books_name=None,
    books_filter_lang=None,
    books_filter_category=None,
    start=1,
    pageLength=25,
    format='html',
):
    api_url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8888/search'
    querystring = {
        'pattern': pattern,
        'books_name': books_name,
        'books_filter_lang': books_filter_lang,
        'books_filter_category': books_filter_category,
        'start': start,
        'pageLength': pageLength,
        'format': format,
    }
    assert pattern is not None, 'Missing required parameter: pattern'

    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(
            url=api_url, timeout=50
        )  # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())


if __name__ == '__main__':
    r = search(
        pattern="""android""",
        books_name="""scifi-library""",
        books_filter_lang="""ita""",
        books_filter_category="""wikipedia""",
        start=51,
        pageLength=10,
        format="""xml""",
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
