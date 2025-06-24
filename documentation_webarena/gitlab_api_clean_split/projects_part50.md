## Get the path to repository storage

Get the path to repository storage for specified project if Gitaly Cluster is not being used. If Gitaly Cluster is being used, see
[Praefect-generated replica paths](../administration/gitaly/index.md#praefect-generated-replica-paths).

Available for administrators only.

```plaintext
GET /projects/:id/storage
```

| Attribute | Type              | Required | Description |
|-----------|-------------------|----------|-------------|
| `id`      | integer or string | Yes      | ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding). |

```json
[
  {
    "project_id": 1,
    "disk_path": "@hashed/6b/86/6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b",
    "created_at": "2012-10-12T17:04:47Z",
    "repository_storage": "default"
  }
]
```
