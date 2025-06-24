## Single email

Get a single email.

```plaintext
GET /user/emails/:email_id
```

Parameters:

| Attribute  | Type    | Required | Description |
|------------|---------|----------|-------------|
| `email_id` | integer | yes      | Email ID    |

```json
{
  "id": 1,
  "email": "email@example.com",
  "confirmed_at" : "2021-03-26T19:07:56.248Z"
}
```

