## Revoke an impersonation token

DETAILS:
**Tier:** Free, Premium, Ultimate
**Offering:** Self-managed, GitLab Dedicated

Requires administrator access.

It revokes an impersonation token.

```plaintext
DELETE /users/:user_id/impersonation_tokens/:impersonation_token_id
```

Parameters:

| Attribute                | Type    | Required | Description                       |
| ------------------------ | ------- | -------- | --------------------------------- |
| `user_id`                | integer | yes      | ID of the user                |
| `impersonation_token_id` | integer | yes      | ID of the impersonation token |

```shell
curl --request DELETE --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/users/42/impersonation_tokens/1"
```

