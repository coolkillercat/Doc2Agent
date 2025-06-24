## Get user preferences

Get a list of the authenticated user's preferences.

```plaintext
GET /user/preferences
```

Example response:

```json
{
  "id": 1,
  "user_id": 1,
  "view_diffs_file_by_file": true,
  "show_whitespace_in_diffs": false,
  "pass_user_identities_to_ci_jwt": false
}
```

Parameters:

- **none**

