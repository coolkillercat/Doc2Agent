## Delete a GPG key for a given user

DETAILS:
**Tier:** Free, Premium, Ultimate
**Offering:** Self-managed, GitLab Dedicated

Delete a GPG key owned by a specified user. Available only for administrator.

```plaintext
DELETE /users/:id/gpg_keys/:key_id
```

Parameters:

| Attribute | Type    | Required | Description           |
| --------- | ------- | -------- | --------------------- |
| `id`      | integer | yes      | ID of the user    |
| `key_id`  | integer | yes      | ID of the GPG key |

```shell
curl --request DELETE --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/users/2/gpg_keys/1"
```

