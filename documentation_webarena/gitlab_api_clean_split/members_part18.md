## List pending members of a group and its subgroups and projects

For a group and its subgroups and projects, get a list of all members in an `awaiting` state and those who are invited but do not have a GitLab account.

This request returns all matching group and project members from all groups and projects in the root group's hierarchy.

When the member is an invited user that has not signed up for a GitLab account yet, the invited email address is returned.

This API endpoint works on top-level groups only. It does not work on subgroups.

This API endpoint requires permission to administer members for the group.

This API endpoint takes [pagination](rest/index.md#pagination) parameters `page` and `per_page` to restrict the list of members.

```plaintext
GET /groups/:id/pending_members
```

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `id`      | integer/string | yes | The ID or [URL-encoded path of the group](rest/index.md#namespaced-path-encoding) owned by the authenticated user |

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/groups/:id/pending_members"
```

Example response:

```json
[
  {
    "id": 168,
    "name": "Alex Garcia",
    "username": "alex_garcia",
    "email": "alex@example.com",
    "avatar_url": "http://example.com/uploads/user/avatar/1/cd8.jpeg",
    "web_url": "http://example.com/alex_garcia",
    "approved": false,
    "invited": false
  },
  {
    "id": 169,
    "email": "sidney@example.com",
    "avatar_url": "http://gravatar.com/../e346561cd8.jpeg",
    "approved": false,
    "invited": true
  },
  {
    "id": 170,
    "email": "zhang@example.com",
    "avatar_url": "http://gravatar.com/../e32131cd8.jpeg",
    "approved": true,
    "invited": true
  }
]
```

