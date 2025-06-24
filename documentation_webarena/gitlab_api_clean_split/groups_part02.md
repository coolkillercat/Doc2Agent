## List groups

Get a list of visible groups for the authenticated user. When accessed without
authentication, only public groups are returned.

By default, this request returns 20 results at a time because the API results [are paginated](rest/index.md#pagination).

When accessed without authentication, this endpoint also supports [keyset pagination](rest/index.md#keyset-based-pagination):

- When requesting consecutive pages of results, you should use keyset pagination.
- Beyond a specific offset limit (specified by [max offset allowed by the REST API for offset-based pagination](../administration/instance_limits.md#max-offset-allowed-by-the-rest-api-for-offset-based-pagination)), offset pagination is unavailable.

Parameters:

| Attribute                             | Type              | Required | Description |
| ------------------------------------- | ----------------- | -------- | ---------- |
| `skip_groups`                         | array of integers | no       | Skip the group IDs passed |
| `all_available`                       | boolean           | no       | Show all the groups you have access to (defaults to `false` for authenticated users, `true` for administrators); Attributes `owned` and `min_access_level` have precedence |
| `search`                              | string            | no       | Return the list of authorized groups matching the search criteria |
| `order_by`                            | string            | no       | Order groups by `name`, `path`, `id`, or `similarity`. Default is `name` |
| `sort`                                | string            | no       | Order groups in `asc` or `desc` order. Default is `asc` |
| `statistics`                          | boolean           | no       | Include group statistics (administrators only).<br>*Note:* The REST API response does not provide the full `RootStorageStatistics` data that is shown in the UI. To match the data in the UI, use GraphQL instead of REST. For more information, see the [Group GraphQL API resources](../api/graphql/reference/index.md#group).|
| `visibility`                          | string            | no       | Limit to groups with `public`, `internal`, or `private` visibility. |
| `with_custom_attributes`              | boolean           | no       | Include [custom attributes](custom_attributes.md) in response (administrators only) |
| `owned`                               | boolean           | no       | Limit to groups explicitly owned by the current user |
| `min_access_level`                    | integer           | no       | Limit to groups where current user has at least this [role (`access_level`)](members.md#roles) |
| `top_level_only`                      | boolean           | no       | Limit to top level groups, excluding all subgroups |
| `repository_storage`                  | string            | no       | Filter by repository storage used by the group _(administrators only)_. [Introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/419643) in GitLab 16.3. Premium and Ultimate only. |

```plaintext
GET /groups
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
    "avatar_url": "http://localhost:3000/uploads/group/avatar/1/foo.jpg",
    "web_url": "http://localhost:3000/groups/foo-bar",
    "request_access_enabled": false,
    "repository_storage": "default",
    "full_name": "Foobar Group",
    "full_path": "foo-bar",
    "file_template_project_id": 1,
    "parent_id": null,
    "created_at": "2020-01-15T12:36:29.590Z",
    "ip_restriction_ranges": null
  }
]
```

When adding the parameter `statistics=true` and the authenticated user is an administrator, additional group statistics are returned.

```plaintext
GET /groups?statistics=true
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
    "avatar_url": "http://localhost:3000/uploads/group/avatar/1/foo.jpg",
    "web_url": "http://localhost:3000/groups/foo-bar",
    "request_access_enabled": false,
    "repository_storage": "default",
    "full_name": "Foobar Group",
    "full_path": "foo-bar",
    "file_template_project_id": 1,
    "parent_id": null,
    "created_at": "2020-01-15T12:36:29.590Z",
    "statistics": {
      "storage_size": 363,
      "repository_size": 33,
      "wiki_size": 100,
      "lfs_objects_size": 123,
      "job_artifacts_size": 57,
      "pipeline_artifacts_size": 0,
      "packages_size": 0,
      "snippets_size": 50,
      "uploads_size": 0
    },
    "wiki_access_level": "private",
    "duo_features_enabled": true,
    "lock_duo_features_enabled": false,
  }
]
```

Users of [GitLab Premium or Ultimate](https://about.gitlab.com/pricing/) also see the `wiki_access_level`,
`duo_features_enabled`, and `lock_duo_features_enabled` attributes.

You can search for groups by name or path, see below.

You can filter by [custom attributes](custom_attributes.md) with:

```plaintext
GET /groups?custom_attributes[key]=value&custom_attributes[other_key]=other_value
```

