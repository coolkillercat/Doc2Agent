## Reorder an issue

Reorders an issue. You can see the results when [sorting issues manually](../user/project/issues/sorting_issue_lists.md#manual-sorting).

```plaintext
PUT /projects/:id/issues/:issue_iid/reorder
```

Supported attributes:

| Attribute   | Type    | Required | Description                          |
|-------------|---------|----------|--------------------------------------|
| `id`        | integer/string | Yes      | The global ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user.  |
| `issue_iid` | integer | Yes      | The internal ID of the project's issue. |
| `move_after_id` | integer | No | The global ID of a project's issue that should be placed after this issue. |
| `move_before_id` | integer | No | The global ID of a project's issue that should be placed before this issue. |

Example request:

```shell
curl --request PUT \
  --header "PRIVATE-TOKEN: <your_access_token>" \
  --url "https://gitlab.example.com/api/v4/projects/4/issues/85/reorder?move_after_id=51&move_before_id=92"
```

