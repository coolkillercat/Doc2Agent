import requests
from urllib.parse import quote
                
def create_diagram__post_(diagram_type=None, output_format=None, diagram_source=None):
    api_url = f"https://kroki.io/{diagram_type}/{output_format}"
    payload = {'diagram_type': diagram_type, 'output_format': output_format, 'diagram_source': diagram_source, }
    assert diagram_type is not None, 'Missing required parameter: diagram_type'
    assert output_format is not None, 'Missing required parameter: output_format'
    assert diagram_source is not None, 'Missing required parameter: diagram_source'
    
    response = requests.post(url=api_url, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = create_diagram__post_(diagram_type='''graphviz''', output_format='''svg''', diagram_source='''digraph G {Hello->World}''')
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

