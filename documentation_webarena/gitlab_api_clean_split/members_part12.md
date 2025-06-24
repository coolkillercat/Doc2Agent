## Change membership state of a user in a group

> - [Introduced](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/86705) in GitLab 15.0.

Changes the membership state of a user in a group. The state is applied to
all subgroups and projects.

```plaintext
PUT /groups/:id/members/:user_id/state
```

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `id`      | integer/string | yes | The ID or [URL-encoded path of the group](rest/index.md#namespaced-path-encoding) owned by the authenticated user. |
| `user_id` | integer | yes   | The user ID of the member. |
| `state`   | string | yes   | The new state for the user. State is either `awaiting` or `active`. |

```shell
curl --request PUT --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/groups/:id/members/:user_id/state?state=active"
```

Example response:

```json
{
  "success":true
}
```

