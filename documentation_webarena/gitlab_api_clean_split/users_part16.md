## Create Service Account User

DETAILS:
**Tier:** Premium, Ultimate
**Offering:** Self-managed, GitLab Dedicated

> - Ability to create a service account user was [introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/406782) in GitLab 16.1
> - Ability to specify a username or name was [introduced](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/144841) in GitLab 16.10.

Creates a service account user. You can specify the account username and name. If you do not specify these attributes, the default name is `Service account user` and the username is automatically generated. Available only for administrators.

```plaintext
POST /service_accounts
```

```shell
curl --request POST --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/service_accounts"
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
  "username": "service_account_6018816a18e515214e0c34c2b33523fc",
  "name": "Service account user"
}
```

