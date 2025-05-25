import requests, json
from urllib.parse import quote


def multi_fetch(_nodes_ways_relations_=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:3000/api/0.6/[nodes|ways|relations]"
    querystring = {'_nodes_ways_relations_': _nodes_ways_relations_, }
    assert _nodes_ways_relations_ is not None, 'Missing required parameter: _nodes_ways_relations_'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = multi_fetch(_nodes_ways_relations_='''nodes=123,456,789''')
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

