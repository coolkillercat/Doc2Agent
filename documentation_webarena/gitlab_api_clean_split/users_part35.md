## List emails

Get a list of the authenticated user's emails.

NOTE:
This endpoint does not return the primary email address, but [issue 25077](https://gitlab.com/gitlab-org/gitlab/-/issues/25077) proposes to change this behavior.

```plaintext
GET /user/emails
```

```json
[
  {
    "id": 1,
    "email": "email@example.com",
    "confirmed_at" : "2021-03-26T19:07:56.248Z"
  },
  {
    "id": 3,
    "email": "email2@example.com",
    "confirmed_at" : null
  }
]
```

Parameters:

- **none**

