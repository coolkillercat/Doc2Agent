## Delete an invitation to a group or project

Deletes a pending invitation by email address.

```plaintext
DELETE /groups/:id/invitations/:email
DELETE /projects/:id/invitations/:email
```

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `id`      | integer/string | yes | The ID or [URL-encoded path of the project or group](rest/index.md#namespaced-path-encoding) owned by the authenticated user |
| `email`   | string | yes    | The email address to which the invitation was previously sent |

```shell
curl --request DELETE --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/groups/55/invitations/email@example.org"
curl --request DELETE --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/projects/55/invitations/email@example.org"
```

- Returns `204` and no content on success.
- Returns `403` forbidden if unauthorized to delete the invitation.
- Returns `404` not found if authorized and no invitation is found for that email address.
- Returns `409` if the request was valid but the invitation could not be deleted.
