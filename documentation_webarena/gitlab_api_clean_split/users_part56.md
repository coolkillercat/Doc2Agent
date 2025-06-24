## Create a personal access token with limited scopes for the currently authenticated user

DETAILS:
**Tier:** Free, Premium, Ultimate
**Offering:** Self-managed, GitLab Dedicated

> - [Introduced](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/131923) in GitLab 16.5.

Use this API to create a new personal access token for the currently authenticated user.
For security purposes, the token:

- Is limited to the [`k8s_proxy` scope](../user/profile/personal_access_tokens.md#personal-access-token-scopes).
  This scope grants permission to perform Kubernetes API calls using the agent for Kubernetes.
- By default, expires at the end of the day it was created on.

Token values are returned once, so make sure you save the token as you cannot access
it again.

```plaintext
POST /user/personal_access_tokens
```

| Attribute    | Type   | Required | Description                                                                                                                                                                                                                                                                                           |
|--------------|--------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name`       | string | yes      | Name of the personal access token                                                                                                                                                                                                                                                                     |
| `scopes`     | array  | yes      | Array of scopes of the personal access token. Possible values are `k8s_proxy`                                                                                                                                                                                                                         |
| `expires_at` | array  | no       | Expiration date of the access token in ISO format (`YYYY-MM-DD`). If no date is set, the expiration is at the end of the current day. The expiration is subject to the [maximum allowable lifetime of an access token](../user/profile/personal_access_tokens.md#when-personal-access-tokens-expire). |

```shell
curl --request POST --header "PRIVATE-TOKEN: <your_access_token>" --data "name=mytoken" --data "scopes[]=k8s_proxy" "https://gitlab.example.com/api/v4/user/personal_access_tokens"
```

Example response:

```json
{
    "id": 3,
    "name": "mytoken",
    "revoked": false,
    "created_at": "2020-10-14T11:58:53.526Z",
    "scopes": [
        "k8s_proxy"
    ],
    "user_id": 42,
    "active": true,
    "expires_at": "2020-10-15",
    "token": "<your_new_access_token>"
}
```

