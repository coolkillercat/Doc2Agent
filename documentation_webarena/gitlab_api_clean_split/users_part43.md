## Unblock user

DETAILS:
**Tier:** Free, Premium, Ultimate
**Offering:** Self-managed, GitLab Dedicated

Unblocks the specified user. Available only for administrator.

```plaintext
POST /users/:id/unblock
```

Parameters:

| Attribute  | Type    | Required | Description          |
|------------|---------|----------|----------------------|
| `id`       | integer | yes      | ID of specified user |

Returns `201 OK` on success, `404 User Not Found` is user cannot be found or
`403 Forbidden` when trying to unblock a user blocked by LDAP synchronization.

