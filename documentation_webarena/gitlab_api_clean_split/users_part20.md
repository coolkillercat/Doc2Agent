## List SSH keys for user

Get a list of a specified user's SSH keys.

```plaintext
GET /users/:id_or_username/keys
```

| Attribute        | Type   | Required | Description                                             |
| ---------------- | ------ | -------- | ------------------------------------------------------- |
| `id_or_username` | string | yes      | ID or username of the user to get the SSH keys for. |

