## Add a member to a group or project

Adds a new member. You can specify a user ID or invite a user by email.

```plaintext
POST /groups/:id/invitations
POST /projects/:id/invitations
```

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `id`      | integer/string | yes | The ID or [URL-encoded path of the project or group](rest/index.md#namespaced-path-encoding) owned by the authenticated user |
| `email` | string | yes (if `user_id` isn't provided) | The email of the new member or multiple emails separated by commas. |
| `user_id`   | integer/string | yes (if `email` isn't provided) | The ID of the new member or multiple IDs separated by commas. |
| `access_level` | integer | yes | A valid access level |
| `expires_at` | string | no | A date string in the format YEAR-MONTH-DAY |
| `invite_source` | string | no | The source of the invitation that starts the member creation process. See [this issue](https://gitlab.com/gitlab-org/gitlab/-/issues/327120). |
| `member_role_id` | integer | no | Assigns the new member to the provided custom role. ([Introduced](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/134100)) in GitLab 16.6. Ultimate only. |

```shell
curl --request POST --header "PRIVATE-TOKEN: <your_access_token>" \
     --data "email=test@example.com&user_id=1&access_level=30" "https://gitlab.example.com/api/v4/groups/:id/invitations"
curl --request POST --header "PRIVATE-TOKEN: <your_access_token>" \
     --data "email=test@example.com&user_id=1&access_level=30" "https://gitlab.example.com/api/v4/projects/:id/invitations"
```

Example responses:

When all emails were successfully sent:

```json
{  "status":  "success"  }
```

When there was any error sending the email:

```json
{
  "status": "error",
  "message": {
               "test@example.com": "Invite email has already been taken",
               "test2@example.com": "User already exists in source",
               "test_username": "Access level is not included in the list"
             }
}
```

