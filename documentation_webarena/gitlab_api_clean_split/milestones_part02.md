## List project milestones

Returns a list of project milestones.

```plaintext
GET /projects/:id/milestones
GET /projects/:id/milestones?iids[]=42
GET /projects/:id/milestones?iids[]=42&iids[]=43
GET /projects/:id/milestones?state=active
GET /projects/:id/milestones?state=closed
GET /projects/:id/milestones?title=1.0
GET /projects/:id/milestones?search=version
GET /projects/:id/milestones?updated_before=2013-10-02T09%3A24%3A18Z
GET /projects/:id/milestones?updated_after=2013-10-02T09%3A24%3A18Z
```

Parameters:

| Attribute                         | Type   | Required | Description |
| ----------------------------      | ------ | -------- | ----------- |
| `id`                              | integer or string | yes | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user |
| `iids[]`                          | integer array | no | Return only the milestones having the given `iid`. Ignored if `include_ancestors` is `true`.  |
| `state`                           | string | no | Return only `active` or `closed` milestones |
| `title`                           | string | no | Return only the milestones having the given `title` |
| `search`                          | string | no | Return only milestones with a title or description matching the provided string |
| `include_parent_milestones`       | boolean | no | [Deprecated](https://gitlab.com/gitlab-org/gitlab/-/issues/433298) in GitLab 16.7. Use `include_ancestors` instead. |
| `include_ancestors`               | boolean | no | Include milestones from all parent groups. |
| `updated_before`                  | datetime | no | Return only milestones updated before the given datetime. Expected in ISO 8601 format (`2019-03-15T08:00:00Z`). Introduced in GitLab 15.10 |
| `updated_after`                   | datetime | no | Return only milestones updated after the given datetime. Expected in ISO 8601 format (`2019-03-15T08:00:00Z`). Introduced in GitLab 15.10 |

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/projects/5/milestones"
```

Example Response:

```json
[
  {
    "id": 12,
    "iid": 3,
    "project_id": 16,
    "title": "10.0",
    "description": "Version",
    "due_date": "2013-11-29",
    "start_date": "2013-11-10",
    "state": "active",
    "updated_at": "2013-10-02T09:24:18Z",
    "created_at": "2013-10-02T09:24:18Z",
    "expired": false
  }
]
```

