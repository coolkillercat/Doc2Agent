## User preference modification

Update the current user's preferences.

```plaintext
PUT /user/preferences
```

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

| Attribute                        | Required | Description                                                                  |
| :------------------------------- | :------- | :--------------------------------------------------------------------------- |
| `view_diffs_file_by_file`        | Yes      | Flag indicating the user sees only one file diff per page.                   |
| `show_whitespace_in_diffs`       | Yes      | Flag indicating the user sees whitespace changes in diffs.                   |
| `pass_user_identities_to_ci_jwt` | Yes      | Flag indicating the user passes their external identities as CI information. This attribute does not contain enough information to identify or authorize the user in an external system. The attribute is internal to GitLab, and must not be passed to third-party services. For more information and examples, see [Token Payload](../ci/secrets/id_token_authentication.md#token-payload). |

