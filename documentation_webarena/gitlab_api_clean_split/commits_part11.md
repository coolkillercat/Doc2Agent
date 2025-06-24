## Get the comments of a commit

Get the comments of a commit in a project.

```plaintext
GET /projects/:id/repository/commits/:sha/comments
```

Parameters:

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `id`      | integer/string | yes | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user |
| `sha` | string | yes | The commit hash or name of a repository branch or tag |

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" \
  --url "https://gitlab.example.com/api/v4/projects/5/repository/commits/main/comments"
```

Example response:

```json
[
  {
    "note": "this code is really nice",
    "author": {
      "id": 11,
      "username": "admin",
      "email": "admin@local.host",
      "name": "Administrator",
      "state": "active",
      "created_at": "2014-03-06T08:17:35.000Z"
    }
  }
]
```

