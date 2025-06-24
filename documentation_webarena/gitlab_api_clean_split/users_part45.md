## Activate user

DETAILS:
**Tier:** Free, Premium, Ultimate
**Offering:** Self-managed, GitLab Dedicated

> - [Introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/22257) in GitLab 12.4.

Activates the specified user. Available only for administrator.

```plaintext
POST /users/:id/activate
```

Parameters:

| Attribute  | Type    | Required | Description          |
|------------|---------|----------|----------------------|
| `id`       | integer | yes      | ID of specified user |

Returns:

- `201 OK` on success.
- `404 User Not Found` if the user cannot be found.
- `403 Forbidden` if the user cannot be activated because they are blocked by an administrator or by LDAP synchronization.

