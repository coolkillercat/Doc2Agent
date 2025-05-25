import requests, json
from urllib.parse import quote


def import_a_file_from_aws_s3(access_key_id=None, bucket_name=None, file_key=None, path=None, region=None, secret_access_key=None, name=None, namespace=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/projects/remote-import-s3"
    payload = {'access_key_id': access_key_id, 'bucket_name': bucket_name, 'file_key': file_key, 'path': path, 'region': region, 'secret_access_key': secret_access_key, 'name': name, 'namespace': namespace, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert access_key_id is not None, 'Missing required parameter: access_key_id'
    assert bucket_name is not None, 'Missing required parameter: bucket_name'
    assert file_key is not None, 'Missing required parameter: file_key'
    assert path is not None, 'Missing required parameter: path'
    assert region is not None, 'Missing required parameter: region'
    assert secret_access_key is not None, 'Missing required parameter: secret_access_key'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = import_a_file_from_aws_s3(access_key_id='''<Your AWS access key id>''', bucket_name='''<Your S3 bucket name>''', file_key='''<Your S3 file key>''', path='''sample-project''', region='''<Your S3 region name>''', secret_access_key='''<Your AWS secret access key>''', name='''Sample Project''', namespace=example-group)
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

