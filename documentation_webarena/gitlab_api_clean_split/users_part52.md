## Get an impersonation token of a user

DETAILS:
**Tier:** Free, Premium, Ultimate
**Offering:** Self-managed, GitLab Dedicated

> Requires administrators permissions.

It shows a user's impersonation token.

```plaintext
GET /users/:user_id/impersonation_tokens/:impersonation_token_id
```

Parameters:

| Attribute                | Type    | Required | Description                       |
| ------------------------ | ------- | -------- | --------------------------------- |
| `user_id`                | integer | yes      | ID of the user                |
| `impersonation_token_id` | integer | yes      | ID of the impersonation token |

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/users/42/impersonation_tokens/2"
```

Example response:

```json
{
   "active" : true,
   "user_id" : 2,
   "scopes" : [
      "api"
   ],
   "revoked" : false,
   "name" : "mytoken",
   "id" : 2,
   "created_at" : "2017-03-17T17:18:09.283Z",
   "impersonation" : true,
   "expires_at" : "2017-04-04"
}
```

