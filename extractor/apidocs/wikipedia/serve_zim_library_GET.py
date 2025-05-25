import requests
from urllib.parse import quote
                
def serve_zim_library(LIBRARY_FILE_PATH=None, __library=None, _i____address='all', _p____port=80, _r____urlRootLocation=None, _d____daemon=None, _a____attachToProcess=None, _M____monitorLibrary=None, _m____nolibrarybutton=None, _n____nosearchbar=None, _b____blockexternal=None, _t____threads=None):
    api_url = "http://localhost:8080/serve_zim_library"  # Changed to local server address
    querystring = {'LIBRARY_FILE_PATH': LIBRARY_FILE_PATH, '__library': __library, '_i____address': _i____address, '_p____port': _p____port, '_r____urlRootLocation': _r____urlRootLocation, '_d____daemon': _d____daemon, '_a____attachToProcess': _a____attachToProcess, '_M____monitorLibrary': _M____monitorLibrary, '_m____nolibrarybutton': _m____nolibrarybutton, '_n____nosearchbar': _n____nosearchbar, '_b____blockexternal': _b____blockexternal, '_t____threads': _t____threads, }
    assert LIBRARY_FILE_PATH is not None, 'Missing required parameter: LIBRARY_FILE_PATH'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = serve_zim_library(LIBRARY_FILE_PATH='/path/to/library.xml', __library=True, _i____address='192.168.1.1', _p____port=8080, _r____urlRootLocation='/kiwix', _d____daemon=True, _a____attachToProcess=1234, _M____monitorLibrary=True, _m____nolibrarybutton=True, _n____nosearchbar=True, _b____blockexternal=True, _t____threads=4)
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