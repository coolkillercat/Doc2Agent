import requests, json
from urllib.parse import quote


def create_a_draft_note(id=None, merge_request_iid=None, note=None, position_base_sha_=None, position_head_sha_=None, position_start_sha_=None, position_position_type_=None, commit_id=None, in_reply_to_discussion_id=None, resolve_discussion=None, position_new_path_=None, position_old_path_=None, position_new_line_=None, position_old_line_=None, position_line_range_=None, position_width_=None, position_height_=None, position_x_=None, position_y_=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/projects/:id/merge_requests/:merge_request_iid/draft_notes"
    payload = {'id': id, 'merge_request_iid': merge_request_iid, 'note': note, 'position_base_sha_': position_base_sha_, 'position_head_sha_': position_head_sha_, 'position_start_sha_': position_start_sha_, 'position_position_type_': position_position_type_, 'commit_id': commit_id, 'in_reply_to_discussion_id': in_reply_to_discussion_id, 'resolve_discussion': resolve_discussion, 'position_new_path_': position_new_path_, 'position_old_path_': position_old_path_, 'position_new_line_': position_new_line_, 'position_old_line_': position_old_line_, 'position_line_range_': position_line_range_, 'position_width_': position_width_, 'position_height_': position_height_, 'position_x_': position_x_, 'position_y_': position_y_, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    assert id is not None, 'Missing required parameter: id'
    assert merge_request_iid is not None, 'Missing required parameter: merge_request_iid'
    assert note is not None, 'Missing required parameter: note'
    assert position_base_sha_ is not None, 'Missing required parameter: position_base_sha_'
    assert position_head_sha_ is not None, 'Missing required parameter: position_head_sha_'
    assert position_start_sha_ is not None, 'Missing required parameter: position_start_sha_'
    assert position_position_type_ is not None, 'Missing required parameter: position_position_type_'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = create_a_draft_note(id=14, merge_request_iid=11, note='''This is a draft note.''', position_base_sha_='''abc123''', position_head_sha_='''def456''', position_start_sha_='''ghi789''', position_position_type_='''text''', commit_id='''jkl012''', in_reply_to_discussion_id='''123''', resolve_discussion=False, position_new_path_='''new_file_path.txt''', position_old_path_='''old_file_path.txt''', position_new_line_=10, position_old_line_=8, position_line_range_={}, position_width_=100, position_height_=200, position_x_=10.5, position_y_=20.5)
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

