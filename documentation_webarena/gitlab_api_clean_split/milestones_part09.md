## Promote project milestone to a group milestone

> - [Changed](https://gitlab.com/gitlab-org/gitlab/-/issues/343889) the minimum user role from Developer to Reporter in GitLab 15.0.

Only for users with at least the Reporter role in the group.

```plaintext
POST /projects/:id/milestones/:milestone_id/promote
```

Parameters:

| Attribute      | Type           | Required | Description                                                                                                     |
|----------------|----------------|----------|-----------------------------------------------------------------------------------------------------------------|
| `id`           | integer or string | yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user |
| `milestone_id` | integer        | yes      | The ID of the project's milestone                                                                               |

