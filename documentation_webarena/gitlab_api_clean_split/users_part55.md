## Create a personal access token

DETAILS:
**Tier:** Free, Premium, Ultimate
**Offering:** Self-managed, GitLab Dedicated

> - The `expires_at` attribute default was [introduced](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/120213) in GitLab 16.0.

Use this API to create a new personal access token. Token values are returned once so,
make sure you save it as you can't access it again. This API can only be used by
GitLab administrators.

```plaintext
POST /users/:user_id/personal_access_tokens
```

| Attribute    | Type    | Required | Description                                                                                                              |
| ------------ | ------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| `user_id`    | integer | yes      | ID of the user                                                                                                       |
| `name`       | string  | yes      | Name of the personal access token                                                                                    |
| `expires_at` | date    | no       | Expiration date of the access token in ISO format (`YYYY-MM-DD`). If no date is set, the expiration is set to the [maximum allowable lifetime of an access token](../user/profile/personal_access_tokens.md#when-personal-access-tokens-expire). |
| `scopes`     | array   | yes      | Array of scopes of the personal access token. See [personal access token scopes](../user/profile/personal_access_tokens.md#personal-access-token-scopes) for possible values. |

```shell
curl --request POST --header "PRIVATE-TOKEN: <your_access_token>" --data "name=mytoken" --data "expires_at=2017-04-04" \
     --data "scopes[]=api" "https://gitlab.example.com/api/v4/users/42/personal_access_tokens"
```

Example response:

```json
{
    "id": 3,
    "name": "mytoken",
    "revoked": false,
    "created_at": "2020-10-14T11:58:53.526Z",
    "scopes": [
        "api"
    ],
    "user_id": 42,
    "active": true,
    "expires_at": "2020-12-31",
    "token": "ggbfKkC4n-Lujy8jwCR2"
}
```

