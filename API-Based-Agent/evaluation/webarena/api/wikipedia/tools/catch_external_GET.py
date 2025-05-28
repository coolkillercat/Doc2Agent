import requests


def catch_external(source=None):
    api_url = (
        'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8888/catch/external'
    )
    querystring = {
        'source': source,
    }
    assert source is not None, 'Missing required parameter: source'

    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(
            url=api_url, timeout=50
        )  # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())


if __name__ == '__main__':
    r = catch_external(source="""https%3A%2F%2Fexample.com%3Fquery%3Dabcd""")
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
