## Create new milestone

Creates a new project milestone.

```plaintext
POST /projects/:id/milestones
```

Parameters:

| Attribute     | Type           | Required | Description                                                                                                     |
|---------------|----------------|----------|-----------------------------------------------------------------------------------------------------------------|
| `id`          | integer or string | yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user |
| `title`       | string         | yes      | The title of a milestone                                                                                        |
| `description` | string         | no       | The description of the milestone                                                                                |
| `due_date`    | string         | no       | The due date of the milestone (`YYYY-MM-DD`)                                                                    |
| `start_date`  | string         | no       | The start date of the milestone (`YYYY-MM-DD`)                                                                  |

