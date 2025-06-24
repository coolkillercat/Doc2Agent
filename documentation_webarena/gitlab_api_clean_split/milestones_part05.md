## Edit milestone

Updates an existing project milestone.

```plaintext
PUT /projects/:id/milestones/:milestone_id
```

Parameters:

| Attribute      | Type           | Required | Description                                                                                                     |
|----------------|----------------|----------|-----------------------------------------------------------------------------------------------------------------|
| `id`           | integer or string | yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user |
| `milestone_id` | integer        | yes      | The ID of the project's milestone                                                                               |
| `title`        | string         | no       | The title of a milestone                                                                                        |
| `description`  | string         | no       | The description of the milestone                                                                                |
| `due_date`     | string         | no       | The due date of the milestone (`YYYY-MM-DD`)                                                                    |
| `start_date`   | string         | no       | The start date of the milestone (`YYYY-MM-DD`)                                                                  |
| `state_event`  | string         | no       | The state event of the milestone (close or activate)                                                            |

