## Start the Housekeeping task for a project

```plaintext
POST /projects/:id/housekeeping
```

| Attribute | Type              | Required | Description |
|-----------|-------------------|----------|-------------|
| `id`      | integer or string | Yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding). |
| `task`    | string            | No       | `prune` to trigger manual prune of unreachable objects or `eager` to trigger eager housekeeping. |

