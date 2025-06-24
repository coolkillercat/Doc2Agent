## Delete a shared project link within a group

Unshare the project from the group. Returns `204` and no content on success.

```plaintext
DELETE /projects/:id/share/:group_id
```

| Attribute  | Type              | Required | Description |
|------------|-------------------|----------|-------------|
| `group_id` | integer           | Yes      | The ID of the group. |
| `id`       | integer or string | Yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding). |

```shell
curl --request DELETE --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/projects/5/share/17"
```

