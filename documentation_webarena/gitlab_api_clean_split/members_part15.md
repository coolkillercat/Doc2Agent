## Remove a member from a group or project

Removes a user from a group or project where the user has been explicitly assigned a role.

The user needs to be a group member to qualify for removal.
For example, if the user was added directly to a project within the group but not this
group explicitly, you cannot use this API to remove them. See
[Remove a billable member from a group](#remove-a-billable-member-from-a-group) for an alternative approach.

```plaintext
DELETE /groups/:id/members/:user_id
DELETE /projects/:id/members/:user_id
```

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `id`      | integer/string | yes | The ID or [URL-encoded path of the project or group](rest/index.md#namespaced-path-encoding) owned by the authenticated user |
| `user_id` | integer | yes   | The user ID of the member |
| `skip_subresources` | boolean | false   | Whether the deletion of direct memberships of the removed member in subgroups and projects should be skipped. Default is `false`. |
| `unassign_issuables` | boolean | false   | Whether the removed member should be unassigned from any issues or merge requests inside a given group or project. Default is `false`. |

Example request:

```shell
curl --request DELETE --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/groups/:id/members/:user_id"
curl --request DELETE --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/projects/:id/members/:user_id"
```

