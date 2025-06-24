## Reject user

DETAILS:
**Tier:** Free, Premium, Ultimate
**Offering:** Self-managed, GitLab Dedicated

> - [Introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/339925) in GitLab 14.3.

Rejects specified user that is [pending approval](../administration/moderate_users.md#users-pending-approval). Available only for administrators.

```plaintext
POST /users/:id/reject
```

Parameters:

- `id` (required) - ID of specified user

```shell
curl --request POST --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/users/42/reject"
```

Returns:

- `200 OK` on success.
- `403 Forbidden` if not authenticated as an administrator.
- `404 User Not Found` if user cannot be found.
- `409 Conflict` if user is not pending approval.

Example Responses:

```json
{ "message": "Success" }
```

```json
{ "message": "404 User Not Found" }
```

```json
{ "message": "User does not have a pending request" }
```

