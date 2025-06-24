## List indirect memberships for a billable member of a group

DETAILS:
**Status:** Experiment

> - [Introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/386583) in GitLab 16.11.

Gets a list of indirect memberships for a billable member of a group.

Lists all projects and groups that a user is a member of, that have been invited to the requested root group.
For instance, if the requested group is `Root Group`, and the requested user is a direct member of `Other Group / Sub Group Two`, which was invited to `Root Group`, then only `Other Group / Sub Group Two` is returned.

The response lists only indirect memberships. Direct memberships are not included.

This API endpoint works on top-level groups only. It does not work on subgroups.

This API endpoint requires permission to administer memberships for the group.

This API endpoint takes [pagination](rest/index.md#pagination) parameters `page` and `per_page` to restrict the list of memberships.

```plaintext
GET /groups/:id/billable_members/:user_id/indirect
```

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `id`      | integer/string | yes | The ID or [URL-encoded path of the group](rest/index.md#namespaced-path-encoding) owned by the authenticated user |
| `user_id` | integer        | yes | The user ID of the billable member |

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/groups/:id/billable_members/:user_id/indirect"
```

Example response:

```json
[
  {
    "id": 168,
    "source_id": 132,
    "source_full_name": "Invited Group / Sub Group One",
    "source_members_url": "https://gitlab.example.com/groups/invited-group/sub-group-one/-/group_members",
    "created_at": "2021-03-31T17:28:44.812Z",
    "expires_at": "2022-03-21",
    "access_level": {
      "string_value": "Developer",
      "integer_value": 30
    }
  }
]
```

