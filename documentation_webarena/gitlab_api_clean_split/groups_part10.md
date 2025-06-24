## Transfer project to group

Transfer a project to the Group namespace. Available only to instance administrators, although an [alternative API endpoint](projects.md#transfer-a-project-to-a-new-namespace)
is available which does not require administrator access on the instance. Transferring projects may fail when tagged packages exist in the project's repository.

```plaintext
POST  /groups/:id/projects/:project_id
```

Parameters:

| Attribute    | Type           | Required | Description |
| ------------ | -------------- | -------- | ----------- |
| `id`         | integer/string | yes      | The ID or [URL-encoded path of the target group](rest/index.md#namespaced-path-encoding) |
| `project_id` | integer/string | yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) |

```shell
curl --request POST --header "PRIVATE-TOKEN: <your_access_token>" \
     "https://gitlab.example.com/api/v4/groups/4/projects/56"
```

