## Update an invitation to a group or project

Updates a pending invitation's access level or access expiry date.

```plaintext
PUT /groups/:id/invitations/:email
PUT /projects/:id/invitations/:email
```

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `id`      | integer/string | yes | The ID or [URL-encoded path of the project or group](rest/index.md#namespaced-path-encoding) owned by the authenticated user. |
| `email`   | string | yes    | The email address the invitation was previously sent to. |
| `access_level` | integer | no | A valid access level (defaults: `30`, the Developer role). |
| `expires_at` | string | no | A date string in ISO 8601 format (`YYYY-MM-DDTHH:MM:SSZ`). |

```shell
curl --request PUT --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/groups/55/invitations/email@example.org?access_level=40"
curl --request PUT --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/projects/55/invitations/email@example.org?access_level=40"
```

Example response:

```json
{
  "expires_at": "2012-10-22T14:13:35Z",
  "access_level": 40,
}
```

