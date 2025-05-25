import requests
from urllib.parse import quote
                
def create_diagram__get_(diagram_type=None, output_format=None, encoded_diagram=None):
    api_url = f"https://kroki.io/{quote(diagram_type, safe='')}/{quote(output_format, safe='')}/{quote(encoded_diagram, safe='')}"
    querystring = {'diagram_type': diagram_type, 'output_format': output_format, 'encoded_diagram': encoded_diagram, }
    assert diagram_type is not None, 'Missing required parameter: diagram_type'
    assert output_format is not None, 'Missing required parameter: output_format'
    assert encoded_diagram is not None, 'Missing required parameter: encoded_diagram'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = create_diagram__get_(diagram_type='''graphviz''', output_format='''svg''', encoded_diagram='''eNpLyUwvSizIUHBXqPZIzcnJ17ULzy_KSanlAgB1EAjQ''')
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

