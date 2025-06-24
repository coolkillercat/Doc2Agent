## Approve all pending members for a group

Approves all pending users for a group and its subgroups and projects.

```plaintext
POST /groups/:id/members/approve_all
```

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `id`      | integer/string | yes | The ID or [URL-encoded path of the root group](rest/index.md#namespaced-path-encoding) owned by the authenticated user |

Example request:

```shell
curl --request POST --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/groups/:id/members/approve_all"
```

