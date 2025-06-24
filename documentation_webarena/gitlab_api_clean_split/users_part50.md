## Approve user

DETAILS:
**Tier:** Free, Premium, Ultimate
**Offering:** Self-managed, GitLab Dedicated

Approves the specified user. Available only for administrators.

```plaintext
POST /users/:id/approve
```

Parameters:

| Attribute  | Type    | Required | Description          |
|------------|---------|----------|----------------------|
| `id`       | integer | yes      | ID of specified user |

```shell
curl --request POST --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/users/42/approve"
```

Returns:

- `201 Created` on success.
- `404 User Not Found` if user cannot be found.
- `403 Forbidden` if the user cannot be approved because they are blocked by an administrator or by LDAP synchronization.
- `409 Conflict` if the user has been deactivated.

Example Responses:

```json
{ "message": "Success" }
```

```json
{ "message": "404 User Not Found" }
```

```json
{ "message": "The user you are trying to approve is not pending approval" }
```

