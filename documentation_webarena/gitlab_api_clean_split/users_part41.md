## Delete email for given user

DETAILS:
**Tier:** Free, Premium, Ultimate
**Offering:** Self-managed, GitLab Dedicated

Prerequisites:

- You must be an administrator of a self-managed GitLab instance.

Deletes an email address owned by a specified user. This cannot delete a primary email address.

```plaintext
DELETE /users/:id/emails/:email_id
```

Parameters:

| Attribute  | Type    | Required | Description          |
|------------|---------|----------|----------------------|
| `id`       | integer | yes      | ID of specified user |
| `email_id` | integer | yes      | Email ID             |

