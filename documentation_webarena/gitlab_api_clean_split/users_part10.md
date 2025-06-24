## Get the status of a user

Get the status of a user. This endpoint can be accessed without authentication.

```plaintext
GET /users/:id_or_username/status
```

| Attribute        | Type   | Required | Description                                       |
| ---------------- | ------ | -------- | ------------------------------------------------- |
| `id_or_username` | string | yes      | ID or username of the user to get a status of |

```shell
curl "https://gitlab.example.com/users/janedoe/status"
```

Example response:

```json
{
  "emoji":"coffee",
  "availability":"busy",
  "message":"I crave coffee :coffee:",
  "message_html": "I crave coffee <gl-emoji title=\"hot beverage\" data-name=\"coffee\" data-unicode-version=\"4.0\">☕</gl-emoji>",
  "clear_status_at": null
}
```

