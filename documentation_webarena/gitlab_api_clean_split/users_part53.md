## Create an impersonation token

DETAILS:
**Tier:** Free, Premium, Ultimate
**Offering:** Self-managed, GitLab Dedicated

Requires administrator access. Token values are returned once. Make sure you save it because you can't access
it again.

It creates a new impersonation token. Only administrators can do this.
You are only able to create impersonation tokens to impersonate the user and perform
both API calls and Git reads and writes. The user can't see these tokens in their profile
settings page.

```plaintext
POST /users/:user_id/impersonation_tokens
```

| Attribute    | Type    | Required | Description                                                                 |
| ------------ | ------- | -------- | --------------------------------------------------------------------------- |
| `user_id`    | integer | yes      | ID of the user                                                          |
| `name`       | string  | yes      | Name of the impersonation token                                         |
| `expires_at` | date    | yes      | Expiration date of the impersonation token in ISO format (`YYYY-MM-DD`) |
| `scopes`     | array   | yes      | Array of scopes of the impersonation token (`api`, `read_user`)         |

```shell
curl --request POST --header "PRIVATE-TOKEN: <your_access_token>" --data "name=mytoken" --data "expires_at=2017-04-04" \
     --data "scopes[]=api" "https://gitlab.example.com/api/v4/users/42/impersonation_tokens"
```

Example response:

```json
{
   "id" : 2,
   "revoked" : false,
   "user_id" : 2,
   "scopes" : [
      "api"
   ],
   "token" : "EsMo-vhKfXGwX9RKrwiy",
   "active" : true,
   "impersonation" : true,
   "name" : "mytoken",
   "created_at" : "2017-03-17T17:18:09.283Z",
   "expires_at" : "2017-04-04"
}
```

