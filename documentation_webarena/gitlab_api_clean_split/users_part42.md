## Block user

DETAILS:
**Tier:** Free, Premium, Ultimate
**Offering:** Self-managed, GitLab Dedicated

Blocks the specified user. Available only for administrator.

```plaintext
POST /users/:id/block
```

Parameters:

| Attribute  | Type    | Required | Description          |
|------------|---------|----------|----------------------|
| `id`       | integer | yes      | ID of specified user |

Returns:

- `201 OK` on success.
- `404 User Not Found` if user cannot be found.
- `403 Forbidden` when trying to block:
  - A user that is blocked through LDAP.
  - An internal user.

