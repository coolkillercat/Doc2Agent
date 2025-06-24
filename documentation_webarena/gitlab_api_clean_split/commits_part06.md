## Get references a commit is pushed to

Get all references (from branches or tags) a commit is pushed to.
The pagination parameters `page` and `per_page` can be used to restrict the list of references.

```plaintext
GET /projects/:id/repository/commits/:sha/refs
```

Parameters:

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `id`      | integer/string | yes | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user |
| `sha` | string | yes | The commit hash  |
| `type` | string | no | The scope of commits. Possible values `branch`, `tag`, `all`. Default is `all`.  |

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" \
  --url "https://gitlab.example.com/api/v4/projects/5/repository/commits/5937ac0a7beb003549fc5fd26fc247adbce4a52e/refs?type=all"
```

Example response:

```json
[
  {"type": "branch", "name": "'test'"},
  {"type": "branch", "name": "add-balsamiq-file"},
  {"type": "branch", "name": "wip"},
  {"type": "tag", "name": "v1.1.0"}
 ]

```

