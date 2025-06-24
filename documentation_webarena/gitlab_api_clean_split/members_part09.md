## List memberships for a billable member of a group

Gets a list of memberships for a billable member of a group.

Lists all projects and groups a user is a member of. Only projects and groups within the group hierarchy are included.
For instance, if the requested group is `Root Group`, and the requested user is a direct member of both `Root Group / Sub Group One` and `Other Group / Sub Group Two`, then only `Root Group / Sub Group One` will be returned, because `Other Group / Sub Group Two` is not within the `Root Group` hierarchy.

The response represents only direct memberships. Inherited memberships are not included.

This API endpoint works on top-level groups only. It does not work on subgroups.

This API endpoint requires permission to administer memberships for the group.

This API endpoint takes [pagination](rest/index.md#pagination) parameters `page` and `per_page` to restrict the list of memberships.

```plaintext
GET /groups/:id/billable_members/:user_id/memberships
```

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `id`      | integer/string | yes | The ID or [URL-encoded path of the group](rest/index.md#namespaced-path-encoding) owned by the authenticated user |
| `user_id` | integer        | yes | The user ID of the billable member |

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/groups/:id/billable_members/:user_id/memberships"
```

Example response:

```json
[
  {
    "id": 168,
    "source_id": 131,
    "source_full_name": "Root Group / Sub Group One",
    "source_members_url": "https://gitlab.example.com/groups/root-group/sub-group-one/-/group_members",
    "created_at": "2021-03-31T17:28:44.812Z",
    "expires_at": "2022-03-21",
    "access_level": {
      "string_value": "Developer",
      "integer_value": 30
    }
  },
  {
    "id": 169,
    "source_id": 63,
    "source_full_name": "Root Group / Sub Group One / My Project",
    "source_members_url": "https://gitlab.example.com/root-group/sub-group-one/my-project/-/project_members",
    "created_at": "2021-03-31T17:29:14.934Z",
    "expires_at": null,
    "access_level": {
      "string_value": "Maintainer",
      "integer_value": 40
    }
  }
]
```

