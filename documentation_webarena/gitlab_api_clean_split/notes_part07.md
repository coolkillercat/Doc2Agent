## Merge requests

### List all merge request notes

Gets a list of all notes for a single merge request.

```plaintext
GET /projects/:id/merge_requests/:merge_request_iid/notes
GET /projects/:id/merge_requests/:merge_request_iid/notes?sort=asc&order_by=updated_at
```

| Attribute           | Type             | Required   | Description                                                                                                                                         |
| ------------------- | ---------------- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                | integer or string   | yes        | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) |
| `merge_request_iid` | integer          | yes        | The IID of a project merge request |
| `sort`              | string           | no         | Return merge request notes sorted in `asc` or `desc` order. Default is `desc` |
| `order_by`          | string           | no         | Return merge request notes ordered by `created_at` or `updated_at` fields. Default is `created_at` |

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/projects/5/merge_requests/11/notes"
```

### Get single merge request note

Returns a single note for a given merge request.

```plaintext
GET /projects/:id/merge_requests/:merge_request_iid/notes/:note_id
```

Parameters:

| Attribute           | Type           | Required | Description                                                                     |
|---------------------|----------------|----------|---------------------------------------------------------------------------------|
| `id`                | integer or string | yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) |
| `merge_request_iid` | integer        | yes      | The IID of a project merge request                                              |
| `note_id`           | integer        | yes      | The ID of a merge request note                                                        |

```json
{
  "id": 301,
  "body": "Comment for MR",
  "attachment": null,
  "author": {
    "id": 1,
    "username": "pipin",
    "email": "admin@example.com",
    "name": "Pip",
    "state": "active",
    "created_at": "2013-09-30T13:46:01Z"
  },
  "created_at": "2013-10-02T08:57:14Z",
  "updated_at": "2013-10-02T08:57:14Z",
  "system": false,
  "noteable_id": 2,
  "noteable_type": "MergeRequest",
  "project_id": 5,
  "noteable_iid": 2,
  "resolvable": false,
  "confidential": false,
  "internal": false
}
```

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/projects/5/merge_requests/11/notes/1"
```

### Create new merge request note

Creates a new note for a single merge request. Notes are not attached to specific
lines in a merge request. For other approaches with more granular control, see
[Post comment to commit](commits.md#post-comment-to-commit) in the Commits API,
and [Create a new thread in the merge request diff](discussions.md#create-a-new-thread-in-the-merge-request-diff)
in the Discussions API.

If you create a note where the body only contains an emoji reaction, GitLab returns this object.

```plaintext
POST /projects/:id/merge_requests/:merge_request_iid/notes
```

Parameters:

| Attribute           | Type           | Required | Description                                                                                                                  |
|---------------------|----------------|----------|------------------------------------------------------------------------------------------------------------------------------|
| `id`                    | integer or string | yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding)                                              |
| `merge_request_iid`     | integer        | yes      | The IID of a project merge request                                                                                           |
| `body`                  | string         | yes      | The content of a note. Limited to 1,000,000 characters.                                                                      |
| `created_at`            | string         | no       | Date time string, ISO 8601 formatted. Example: `2016-03-11T03:45:40Z` (requires administrator or project/group owner rights) |
| `merge_request_diff_head_sha`| string         | no       | Required for the `/merge` [quick action](../user/project/quick_actions.md). The SHA of the head commit, which ensures the merge request wasn't updated after the API request was sent. |

### Modify existing merge request note

Modify existing note of a merge request.

```plaintext
PUT /projects/:id/merge_requests/:merge_request_iid/notes/:note_id
```

Parameters:

| Attribute           | Type              | Required | Description                                                                                        |
|---------------------|-------------------|----------|----------------------------------------------------------------------------------------------------|
| `id`                | integer or string | yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding)                     |
| `merge_request_iid` | integer           | yes      | The IID of a project merge request                                                                 |
| `note_id`           | integer           | no       | The ID of a note                                                                                   |
| `body`              | string            | yes      | The content of a note. Limited to 1,000,000 characters.                                            |
| `confidential`      | boolean           | no       | **Deprecated:** Scheduled to be removed in GitLab 16.0. The confidential flag of a note. Default is false. |

```shell
curl --request PUT --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/projects/5/merge_requests/11/notes/1?body=note"
```

### Delete a merge request note

Deletes an existing note of a merge request.

```plaintext
DELETE /projects/:id/merge_requests/:merge_request_iid/notes/:note_id
```

Parameters:

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `id` | integer or string | yes | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) |
| `merge_request_iid` | integer | yes | The IID of a merge request |
| `note_id` | integer | yes | The ID of a note |

```shell
curl --request DELETE --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/projects/5/merge_requests/7/notes/1602"
```

