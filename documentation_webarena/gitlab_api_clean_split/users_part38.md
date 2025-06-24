## Add email

Creates a new email owned by the authenticated user.

```plaintext
POST /user/emails
```

Parameters:

| Attribute | Type   | Required | Description |
|-----------|--------|----------|-------------|
| `email`   | string | yes      | Email address |

```json
{
  "id": 4,
  "email": "email@example.com",
  "confirmed_at" : "2021-03-26T19:07:56.248Z"
}
```

Returns a created email with status `201 Created` on success. If an
error occurs a `400 Bad Request` is returned with a message explaining the error:

```json
{
  "message": {
    "email": [
      "has already been taken"
    ]
  }
}
```

