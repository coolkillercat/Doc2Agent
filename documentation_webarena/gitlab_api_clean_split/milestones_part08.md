## Get all merge requests assigned to a single milestone

Gets all merge requests assigned to a single project milestone.

```plaintext
GET /projects/:id/milestones/:milestone_id/merge_requests
```

Parameters:

| Attribute      | Type           | Required | Description                                                                                                     |
|----------------|----------------|----------|-----------------------------------------------------------------------------------------------------------------|
| `id`           | integer or string | yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user |
| `milestone_id` | integer        | yes      | The ID of the project's milestone                                                                               |

