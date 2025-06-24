## Service Accounts

DETAILS:
**Tier:** Premium, Ultimate
**Offering:** GitLab.com, Self-managed, GitLab Dedicated

### Create Service Account User

> - [Introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/407775) in GitLab 16.1.
> - Ability to specify a username or name was [introduced](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/144841) in GitLab 16.10.

Creates a service account user. You can specify username and name. If you do not specify these attributes, the default name is `Service account user` and the username is automatically generated.

This API endpoint works on top-level groups only. It does not work on subgroups.

```plaintext
POST /groups/:id/service_accounts
```

```shell
curl --request POST --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/groups/345/service_accounts"
```

Supported attributes:

| Attribute                  | Type           | Required                  | Description                                                                    |
|:---------------------------|:---------------|:--------------------------|:-------------------------------------------------------------------------------|
| `name`       | string | no | Name of the user |
| `username`   | string | no | Username of the user |

Example response:

```json
{
  "id": 57,
  "username": "service_account_group_345_6018816a18e515214e0c34c2b33523fc",
  "name": "Service account user"
}
```

### Create Personal Access Token for Service Account User

> - [Introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/406781) in GitLab 16.1.

```plaintext
POST /groups/:id/service_accounts/:user_id/personal_access_tokens
```

This API endpoint works on top-level groups only. It does not work on subgroups.

```shell
curl --request POST --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/groups/35/service_accounts/71/personal_access_tokens" --data "scopes[]=api,read_user,read_repository" --data "name=service_accounts_token"
```

Example response:

```json
{
  "id":6,
  "name":"service_accounts_token",
  "revoked":false,
  "created_at":"2023-06-13T07:47:13.900Z",
  "scopes":["api"],
  "user_id":71,
  "last_used_at":null,
  "active":true,
  "expires_at":"2024-06-12",
  "token":"<token_value>"
}
```

| Attribute | Type            | Required | Description |
| --------- | --------------- | -------- | ----------- |
| `name`    | string          | yes      | Name of the personal access token |
| `scopes`     | array   | yes      | Array of scopes of the personal access token. See [personal access token scopes](../user/profile/personal_access_tokens.md#personal-access-token-scopes) for possible values. |
| `expires_at`      | date | no      | Personal access token expiry date. When left blank, the token follows the [standard rule of expiry for personal access tokens](../user/profile/personal_access_tokens.md#when-personal-access-tokens-expire). |

### Rotate a Personal Access Token for Service Account User

> - [Introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/406781) in GitLab 16.1.

```plaintext
POST /groups/:id/service_accounts/:user_id/personal_access_tokens/:token_id/rotate
```

This API endpoint works on top-level groups only. It does not work on subgroups.

```shell
curl --request POST --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/groups/35/service_accounts/71/personal_access_tokens/6/rotate"
```

Example response:

```json
{
  "id":7,
  "name":"service_accounts_token",
  "revoked":false,
  "created_at":"2023-06-13T07:54:49.962Z",
  "scopes":["api"],
  "user_id":71,
  "last_used_at":null,
  "active":true,
  "expires_at":"2023-06-20",
  "token":"<token_value>"
}
```

