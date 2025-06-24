## List a group's projects

Get a list of projects in this group. When accessed without authentication, only public projects are returned.

By default, this request returns 20 results at a time because the API results [are paginated](rest/index.md#pagination).

```plaintext
GET /groups/:id/projects
```

Parameters:

| Attribute                              | Type           | Required | Description |
| -------------------------------------- | -------------- | -------- | ----------- |
| `id`                                   | integer/string | yes      | The ID or [URL-encoded path of the group](rest/index.md#namespaced-path-encoding) owned by the authenticated user |
| `archived`                             | boolean        | no       | Limit by archived status |
| `visibility`                           | string         | no       | Limit by visibility `public`, `internal`, or `private` |
| `order_by`                             | string         | no       | Return projects ordered by `id`, `name`, `path`, `created_at`, `updated_at`, `similarity` <sup>1</sup>, `star_count` or `last_activity_at` fields. Default is `created_at` |
| `sort`                                 | string         | no       | Return projects sorted in `asc` or `desc` order. Default is `desc` |
| `search`                               | string         | no       | Return list of authorized projects matching the search criteria |
| `simple`                               | boolean        | no       | Return only limited fields for each project. This is a no-op without authentication where only simple fields are returned. |
| `owned`                                | boolean        | no       | Limit by projects owned by the current user |
| `starred`                              | boolean        | no       | Limit by projects starred by the current user |
| `topic`                                | string         | no       | Return projects matching the topic |
| `with_issues_enabled`                  | boolean        | no       | Limit by projects with issues feature enabled. Default is `false` |
| `with_merge_requests_enabled`          | boolean        | no       | Limit by projects with merge requests feature enabled. Default is `false` |
| `with_shared`                          | boolean        | no       | Include projects shared to this group. Default is `true` |
| `include_subgroups`                    | boolean        | no       | Include projects in subgroups of this group. Default is `false` |
| `min_access_level`                     | integer        | no       | Limit to projects where current user has at least this [role (`access_level`)](members.md#roles) |
| `with_custom_attributes`               | boolean        | no       | Include [custom attributes](custom_attributes.md) in response (administrators only) |
| `with_security_reports`                | boolean    | no       | Return only projects that have security reports artifacts present in any of their builds. This means "projects with security reports enabled". Default is `false`. Ultimate only. |

**Footnotes:**

1. Orders the results by a similarity score calculated from the `search` URL parameter.
   When you use `order_by=similarity`, the `sort` parameter is ignored.
   When the `search` parameter is not provided, the API returns the projects ordered by `name`.

Example response:

```json
[
  {
    "id": 9,
    "description": "foo",
    "default_branch": "main",
    "tag_list": [], //deprecated, use `topics` instead
    "topics": [],
    "archived": false,
    "visibility": "internal",
    "ssh_url_to_repo": "git@gitlab.example.com/html5-boilerplate.git",
    "http_url_to_repo": "http://gitlab.example.com/h5bp/html5-boilerplate.git",
    "web_url": "http://gitlab.example.com/h5bp/html5-boilerplate",
    "name": "Html5 Boilerplate",
    "name_with_namespace": "Experimental / Html5 Boilerplate",
    "path": "html5-boilerplate",
    "path_with_namespace": "h5bp/html5-boilerplate",
    "issues_enabled": true,
    "merge_requests_enabled": true,
    "wiki_enabled": true,
    "jobs_enabled": true,
    "snippets_enabled": true,
    "created_at": "2016-04-05T21:40:50.169Z",
    "last_activity_at": "2016-04-06T16:52:08.432Z",
    "shared_runners_enabled": true,
    "creator_id": 1,
    "namespace": {
      "id": 5,
      "name": "Experimental",
      "path": "h5bp",
      "kind": "group"
    },
    "avatar_url": null,
    "star_count": 1,
    "forks_count": 0,
    "open_issues_count": 3,
    "public_jobs": true,
    "shared_with_groups": [],
    "request_access_enabled": false
  }
]
```

NOTE:
To distinguish between a project in the group and a project shared to the group, the `namespace` attribute can be used. When a project has been shared to the group, its `namespace` differs from the group the request is being made for.

