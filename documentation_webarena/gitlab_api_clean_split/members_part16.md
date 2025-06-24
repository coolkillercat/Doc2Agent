## Approve a member for a group

Approves a pending user for a group and its subgroups and projects.

```plaintext
PUT /groups/:id/members/:member_id/approve
```

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `id`      | integer/string | yes | The ID or [URL-encoded path of the root group](rest/index.md#namespaced-path-encoding) owned by the authenticated user |
| `member_id` | integer | yes   | The ID of the member |

Example request:

```shell
curl --request PUT --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/groups/:id/members/:member_id/approve"
```

