## Get groups to which a user can transfer a project

> - [Introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/371006) in GitLab 15.4

Retrieve a list of groups to which the user can transfer a project.

```plaintext
GET /projects/:id/transfer_locations
```

| Attribute | Type              | Required | Description |
|-----------|-------------------|----------|-------------|
| `id`      | integer or string | Yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding). |
| `search`  | string            | No       | The group names to search for. |

Example request:

```shell
curl --request GET "https://gitlab.example.com/api/v4/projects/1/transfer_locations"
```

Example response:

```json
[
  {
    "id": 27,
    "web_url": "https://gitlab.example.com/groups/gitlab",
    "name": "GitLab",
    "avatar_url": null,
    "full_name": "GitLab",
    "full_path": "GitLab"
  },
  {
    "id": 31,
    "web_url": "https://gitlab.example.com/groups/foobar",
    "name": "FooBar",
    "avatar_url": null,
    "full_name": "FooBar",
    "full_path": "FooBar"
  }
]
```

