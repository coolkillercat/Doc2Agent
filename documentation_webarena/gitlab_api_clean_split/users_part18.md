## List associations count for user

Get a list of a specified user's count of:

- Projects.
- Groups.
- Issues.
- Merge requests.

Administrators can query any user, but non-administrators can only query themselves.

```plaintext
GET /users/:id/associations_count
```

Parameters:

| Attribute | Type    | Required | Description      |
|-----------|---------|----------|------------------|
| `id`      | integer | yes      | ID of a user |

Example response:

```json
{
  "groups_count": 2,
  "projects_count": 3,
  "issues_count": 8,
  "merge_requests_count": 5
}
```

