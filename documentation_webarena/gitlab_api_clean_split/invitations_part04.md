## List all invitations pending for a group or project

Gets a list of invited group or project members viewable by the authenticated user.
Returns invitations to direct members only, and not through inherited ancestors' groups.

This function takes pagination parameters `page` and `per_page` to restrict the list of members.

```plaintext
GET /groups/:id/invitations
GET /projects/:id/invitations
```

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `id`      | integer/string | yes | The ID or [URL-encoded path of the project or group](rest/index.md#namespaced-path-encoding) owned by the authenticated user |
| `page`    | integer | no   | Page to retrieve                      |
| `per_page`| integer | no   | Number of member invitations to return per page |
| `query`   | string  | no   | A query string to search for invited members by invite email. Query text must match email address exactly. When empty, returns all invitations. |

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/groups/:id/invitations?query=member@example.org"
curl --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/projects/:id/invitations?query=member@example.org"
```

Example response:

```json
 [
   {
     "id": 1,
     "invite_email": "member@example.org",
     "created_at": "2020-10-22T14:13:35Z",
     "access_level": 30,
     "expires_at": "2020-11-22T14:13:35Z",
     "user_name": "Raymond Smith",
     "created_by_name": "Administrator"
   },
]
```

