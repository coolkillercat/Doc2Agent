## List a group's subgroups

Get a list of visible direct subgroups in this group.

By default, this request returns 20 results at a time because the API results [are paginated](rest/index.md#pagination).

If you request this list as:

- An unauthenticated user, the response returns only public groups.
- An authenticated user, the response returns only the groups you're
  a member of and does not include public groups.

Parameters:

| Attribute                | Type              | Required | Description |
| ------------------------ | ----------------- | -------- | ----------- |
| `id`                     | integer/string    | yes      | The ID or [URL-encoded path of the group](rest/index.md#namespaced-path-encoding) of the immediate parent group |
| `skip_groups`            | array of integers | no       | Skip the group IDs passed |
| `all_available`          | boolean           | no       | Show all the groups you have access to (defaults to `false` for authenticated users, `true` for administrators); Attributes `owned` and `min_access_level` have precedence |
| `search`                 | string            | no       | Return the list of authorized groups matching the search criteria. Only subgroup short paths are searched (not full paths) |
| `order_by`               | string            | no       | Order groups by `name`, `path` or `id`. Default is `name` |
| `sort`                   | string            | no       | Order groups in `asc` or `desc` order. Default is `asc` |
| `statistics`             | boolean           | no       | Include group statistics (administrators only) |
| `with_custom_attributes` | boolean           | no       | Include [custom attributes](custom_attributes.md) in response (administrators only) |
| `owned`                  | boolean           | no       | Limit to groups explicitly owned by the current user |
| `min_access_level`       | integer           | no       | Limit to groups where current user has at least this [role (`access_level`)](members.md#roles) |

```plaintext
GET /groups/:id/subgroups
```

```json
[
  {
    "id": 1,
    "name": "Foobar Group",
    "path": "foo-bar",
    "description": "An interesting group",
    "visibility": "public",
    "share_with_group_lock": false,
    "require_two_factor_authentication": false,
    "two_factor_grace_period": 48,
    "project_creation_level": "developer",
    "auto_devops_enabled": null,
    "subgroup_creation_level": "owner",
    "emails_disabled": null,
    "emails_enabled": null,
    "mentions_disabled": null,
    "lfs_enabled": true,
    "default_branch": null,
    "default_branch_protection": 2,
    "default_branch_protection_defaults": {
      "allowed_to_push": [
          {
              "access_level": 40
          }
      ],
      "allow_force_push": false,
      "allowed_to_merge": [
          {
              "access_level": 40
          }
      ]
    },
    "avatar_url": "http://gitlab.example.com/uploads/group/avatar/1/foo.jpg",
    "web_url": "http://gitlab.example.com/groups/foo-bar",
    "request_access_enabled": false,
    "repository_storage": "default",
    "full_name": "Foobar Group",
    "full_path": "foo-bar",
    "file_template_project_id": 1,
    "parent_id": 123,
    "created_at": "2020-01-15T12:36:29.590Z"
  }
]
```

Users of [GitLab Premium or Ultimate](https://about.gitlab.com/pricing/) also see the `wiki_access_level`,
`duo_features_enabled`, and `lock_duo_features_enabled` attributes.

