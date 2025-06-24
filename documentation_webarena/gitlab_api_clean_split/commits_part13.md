## Get the discussions of a commit

Get the discussions of a commit in a project.

```plaintext
GET /projects/:id/repository/commits/:sha/discussions
```

Parameters:

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `id`      | integer/string | yes | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user |
| `sha`     | string | yes | The commit hash or name of a repository branch or tag |

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" \
  --url "https://gitlab.example.com/api/v4/projects/5/repository/commits/4604744a1c64de00ff62e1e8a6766919923d2b41/discussions"
```

Example response:

```json
[
  {
    "id": "4604744a1c64de00ff62e1e8a6766919923d2b41",
    "individual_note": true,
    "notes": [
      {
        "id": 334686748,
        "type": null,
        "body": "Nice piece of code!",
        "attachment": null,
        "author" : {
          "id" : 28,
          "name" : "Jane Doe",
          "username" : "janedoe",
          "web_url" : "https://gitlab.example.com/janedoe",
          "state" : "active",
          "avatar_url" : "https://gitlab.example.com/uploads/user/avatar/28/jane-doe-400-400.png"
        },
        "created_at": "2020-04-30T18:48:11.432Z",
        "updated_at": "2020-04-30T18:48:11.432Z",
        "system": false,
        "noteable_id": null,
        "noteable_type": "Commit",
        "resolvable": false,
        "confidential": null,
        "noteable_iid": null,
        "commands_changes": {}
      }
    ]
  }
]

```

