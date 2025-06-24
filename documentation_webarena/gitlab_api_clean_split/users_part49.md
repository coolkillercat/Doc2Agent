## Get all impersonation tokens of a user

DETAILS:
**Tier:** Free, Premium, Ultimate
**Offering:** Self-managed, GitLab Dedicated

Requires administrator access.

It retrieves every impersonation token of the user. Use the pagination
parameters `page` and `per_page` to restrict the list of impersonation tokens.

```plaintext
GET /users/:user_id/impersonation_tokens
```

Parameters:

| Attribute | Type    | Required | Description                                                |
| --------- | ------- | -------- | ---------------------------------------------------------- |
| `user_id` | integer | yes      | ID of the user                                         |
| `state`   | string  | no       | Filter tokens based on state (`all`, `active`, `inactive`) |

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/users/42/impersonation_tokens"
```

Example response:

```json
[
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
      "expires_at" : "2017-04-04",
      "last_used_at": "2017-03-24T09:44:21.722Z"
   },
   {
      "active" : false,
      "user_id" : 2,
      "scopes" : [
         "read_user"
      ],
      "revoked" : true,
      "name" : "mytoken2",
      "created_at" : "2017-03-17T17:19:28.697Z",
      "id" : 3,
      "impersonation" : true,
      "expires_at" : "2017-04-14",
      "last_used_at": "2017-03-24T09:44:21.722Z"
   }
]
```

