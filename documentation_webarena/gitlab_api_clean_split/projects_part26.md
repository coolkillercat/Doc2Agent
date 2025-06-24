## Restore project marked for deletion

DETAILS:
**Tier:** Premium, Ultimate
**Offering:** GitLab.com, Self-managed, GitLab Dedicated

Restores project marked for deletion.

```plaintext
POST /projects/:id/restore
```

| Attribute | Type              | Required | Description |
|-----------|-------------------|----------|-------------|
| `id`      | integer or string | Yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding). |

