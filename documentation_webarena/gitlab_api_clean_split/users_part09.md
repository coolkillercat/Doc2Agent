## User status

Get the status of the authenticated user.

```plaintext
GET /user/status
```

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/user/status"
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

