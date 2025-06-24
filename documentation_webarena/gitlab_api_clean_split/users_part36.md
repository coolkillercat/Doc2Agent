## List emails for user

DETAILS:
**Tier:** Free, Premium, Ultimate
**Offering:** Self-managed, GitLab Dedicated

Get a list of a specified user's emails. Available only for administrator

NOTE:
This endpoint does not return the primary email address, but [issue 25077](https://gitlab.com/gitlab-org/gitlab/-/issues/25077) proposes to change this behavior.

```plaintext
GET /users/:id/emails
```

Parameters:

| Attribute | Type    | Required | Description          |
|-----------|---------|----------|----------------------|
| `id`      | integer | yes      | ID of specified user |

