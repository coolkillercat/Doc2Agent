## Fork relationship

Allows modification of the forked relationship between existing projects.
Available only for project owners and administrators.

### Create a forked from/to relation between existing projects

```plaintext
POST /projects/:id/fork/:forked_from_id
```

| Attribute        | Type              | Required | Description |
|------------------|-------------------|----------|-------------|
| `forked_from_id` | ID                | Yes      | The ID of the project that was forked from. |
| `id`             | integer or string | Yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding). |

### Delete an existing forked from relationship

```plaintext
DELETE /projects/:id/fork
```

| Attribute | Type              | Required | Description |
|-----------|-------------------|----------|-------------|
| `id`      | integer or string | Yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding). |

