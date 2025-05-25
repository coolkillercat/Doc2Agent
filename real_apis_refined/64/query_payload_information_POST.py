import requests
from urllib.parse import quote
                
def query_payload_information(md5_hash=None, sha256_hash=None):
    api_url = f"https://urlhaus-api.abuse.ch/v1/payload/"
    payload = {'md5_hash': md5_hash, 'sha256_hash': sha256_hash, }
    assert md5_hash is not None, 'Missing required parameter: md5_hash'
    assert sha256_hash is not None, 'Missing required parameter: sha256_hash'
    
    response = requests.post(url=api_url, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = query_payload_information(md5_hash='''12c8aec5766ac3e6f26f2505e2f4a8f2''', sha256_hash='''35e304d10d53834e3e41035d12122773c9a4d183a24e03f980ad3e6b2ecde7fa''')
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

