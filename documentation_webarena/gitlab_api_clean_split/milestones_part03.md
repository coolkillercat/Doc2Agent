## Get single milestone

Gets a single project milestone.

```plaintext
GET /projects/:id/milestones/:milestone_id
```

Parameters:

| Attribute      | Type           | Required | Description                                                                                                     |
|----------------|----------------|----------|-----------------------------------------------------------------------------------------------------------------|
| `id`           | integer or string | yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user |
| `milestone_id` | integer        | yes      | The ID of the project's milestone                                                                               |

