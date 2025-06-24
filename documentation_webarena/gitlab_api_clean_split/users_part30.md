## Delete a GPG key

Delete a GPG key owned by the authenticated user.

```plaintext
DELETE /user/gpg_keys/:key_id
```

Parameters:

| Attribute | Type    | Required | Description           |
| --------- | ------- | -------- | --------------------- |
| `key_id`  | integer | yes      | ID of the GPG key |

```shell
curl --request DELETE --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/user/gpg_keys/1"
```

Returns `204 No Content` on success or `404 Not Found` if the key cannot be found.

