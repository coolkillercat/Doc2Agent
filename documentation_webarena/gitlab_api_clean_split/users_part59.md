## Disable two factor authentication

DETAILS:
**Tier:** Free, Premium, Ultimate
**Offering:** Self-managed, GitLab Dedicated

> - [Introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/295260) in GitLab 15.2.

Pre-requisite:

- You must be an administrator.

Disables two factor authentication (2FA) for the specified user.

Administrators cannot disable 2FA for their own user account or other administrators using the API. Instead, they can disable an
administrator's 2FA [using the Rails console](../security/two_factor_authentication.md#for-a-single-user).

```plaintext
PATCH /users/:id/disable_two_factor
```

Parameters:

| Attribute | Type    | Required | Description           |
| --------- | ------- | -------- | --------------------- |
| `id`      | integer | yes      | ID of the user    |

```shell
curl --request PATCH --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/users/1/disable_two_factor"
```

Returns:

- `204 No content` on success.
- `400 Bad request` if two factor authentication is not enabled for the specified user.
- `403 Forbidden` if not authenticated as an administrator.
- `404 User Not Found` if user cannot be found.

