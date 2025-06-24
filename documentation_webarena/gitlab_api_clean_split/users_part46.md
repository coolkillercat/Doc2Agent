## Ban user

DETAILS:
**Tier:** Free, Premium, Ultimate
**Offering:** Self-managed, GitLab Dedicated

> - [Introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/327354) in GitLab 14.3.

Bans the specified user. Available only for administrator.

```plaintext
POST /users/:id/ban
```

Parameters:

- `id` (required) - ID of specified user

Returns:

- `201 OK` on success.
- `404 User Not Found` if user cannot be found.
- `403 Forbidden` when trying to ban a user that is not active.

