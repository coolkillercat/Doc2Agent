import requests, json
from urllib.parse import quote



def mark_all_todos_as_done() -> None:
    """
    Marks all pending to-do items for the current user as done. This function helps users clear their entire to-do list in a single operation.
    
    Returns:
        Returns a response object indicating whether all pending to-do items for the current user were successfully marked as done."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED', }
    url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/todos/mark_as_done"
    
    response = requests.post(url, headers=headers)
    return response

if __name__ == '__main__':
    r = mark_all_todos_as_done()
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