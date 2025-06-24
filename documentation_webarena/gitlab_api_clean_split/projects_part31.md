## Share project with group

Allow to share project with group.

```plaintext
POST /projects/:id/share
```

| Attribute      | Type              | Required | Description |
|----------------|-------------------|----------|-------------|
| `group_access` | integer           | Yes      | The [role (`access_level`)](members.md#roles) to grant the group. |
| `group_id`     | integer           | Yes      | The ID of the group to share with. |
| `id`           | integer or string | Yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding). |
| `expires_at`   | string            | No       | Share expiration date in ISO 8601 format. For example, `2016-09-26`. |

