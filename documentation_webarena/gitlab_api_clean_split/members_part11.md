## Remove a billable member from a group

Removes a billable member from a group and its subgroups and projects.

The user does not need to be a group member to qualify for removal.
For example, if the user was added directly to a project within the group, you can
still use this API to remove them.

```plaintext
DELETE /groups/:id/billable_members/:user_id
```

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `id`      | integer/string | yes | The ID or [URL-encoded path of the group](rest/index.md#namespaced-path-encoding) owned by the authenticated user |
| `user_id` | integer | yes   | The user ID of the member |

```shell
curl --request DELETE --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/groups/:id/billable_members/:user_id"
```

