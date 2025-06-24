## Deactivate user

DETAILS:
**Tier:** Free, Premium, Ultimate
**Offering:** Self-managed, GitLab Dedicated

> - [Introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/22257) in GitLab 12.4.

Deactivates the specified user. Available only for administrator.

```plaintext
POST /users/:id/deactivate
```

Parameters:

| Attribute  | Type    | Required | Description          |
|------------|---------|----------|----------------------|
| `id`       | integer | yes      | ID of specified user |

Returns:

- `201 OK` on success.
- `404 User Not Found` if user cannot be found.
- `403 Forbidden` when trying to deactivate a user that is:
  - Blocked by administrator or by LDAP synchronization.
  - Not [dormant](../administration/moderate_users.md#automatically-deactivate-dormant-users).
  - Internal.

