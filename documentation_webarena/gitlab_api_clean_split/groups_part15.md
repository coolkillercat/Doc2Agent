## Restore group marked for deletion

DETAILS:
**Tier:** Premium, Ultimate
**Offering:** GitLab.com, Self-managed, GitLab Dedicated

Restores a group marked for deletion.

```plaintext
POST /groups/:id/restore
```

Parameters:

| Attribute       | Type           | Required | Description |
| --------------- | -------------- | -------- | ----------- |
| `id`            | integer/string | yes      | The ID or [URL-encoded path of the group](rest/index.md#namespaced-path-encoding) |

