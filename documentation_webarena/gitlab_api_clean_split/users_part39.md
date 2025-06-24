## Add email for user

DETAILS:
**Tier:** Free, Premium, Ultimate
**Offering:** Self-managed, GitLab Dedicated

Create new email owned by specified user. Available only for administrator

```plaintext
POST /users/:id/emails
```

Parameters:

| Attribute           | Type    | Required | Description                                                               |
|---------------------|---------|----------|---------------------------------------------------------------------------|
| `id`                | string  | yes      | ID of specified user                                                      |
| `email`             | string  | yes      | Email address                                                             |
| `skip_confirmation` | boolean | no       | Skip confirmation and assume email is verified - true or false (default) |

