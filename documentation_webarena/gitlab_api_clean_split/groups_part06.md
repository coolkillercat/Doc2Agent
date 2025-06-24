## List a group's shared projects

Get a list of projects shared to this group. When accessed without authentication, only public shared projects are returned.

By default, this request returns 20 results at a time because the API results [are paginated](rest/index.md#pagination).

```plaintext
GET /groups/:id/projects/shared
```

Parameters:

| Attribute                     | Type           | Required | Description |
| ----------------------------- | -------------- | -------- | ----------- |
| `id`                          | integer/string | yes      | The ID or [URL-encoded path of the group](rest/index.md#namespaced-path-encoding) owned by the authenticated user |
| `archived`                    | boolean        | no       | Limit by archived status |
| `visibility`                  | string         | no       | Limit by visibility `public`, `internal`, or `private` |
| `order_by`                    | string         | no       | Return projects ordered by `id`, `name`, `path`, `created_at`, `updated_at`, `star_count` or `last_activity_at` fields. Default is `created_at` |
| `sort`                        | string         | no       | Return projects sorted in `asc` or `desc` order. Default is `desc` |
| `search`                      | string         | no       | Return list of authorized projects matching the search criteria |
| `simple`                      | boolean        | no       | Return only limited fields for each project. This is a no-op without authentication where only simple fields are returned. |
| `starred`                     | boolean        | no       | Limit by projects starred by the current user |
| `with_issues_enabled`         | boolean        | no       | Limit by projects with issues feature enabled. Default is `false` |
| `with_merge_requests_enabled` | boolean        | no       | Limit by projects with merge requests feature enabled. Default is `false` |
| `min_access_level`            | integer        | no       | Limit to projects where current user has at least this [role (`access_level`)](members.md#roles) |
| `with_custom_attributes`      | boolean        | no       | Include [custom attributes](custom_attributes.md) in response (administrators only) |

Example response:

```json
[
   {
      "id":8,
      "description":"Shared project for Html5 Boilerplate",
      "name":"Html5 Boilerplate",
      "name_with_namespace":"H5bp / Html5 Boilerplate",
      "path":"html5-boilerplate",
      "path_with_namespace":"h5bp/html5-boilerplate",
      "created_at":"2020-04-27T06:13:22.642Z",
      "default_branch":"main",
      "tag_list":[], //deprecated, use `topics` instead
      "topics":[],
      "ssh_url_to_repo":"ssh://git@gitlab.com/h5bp/html5-boilerplate.git",
      "http_url_to_repo":"https://gitlab.com/h5bp/html5-boilerplate.git",
      "web_url":"https://gitlab.com/h5bp/html5-boilerplate",
      "readme_url":"https://gitlab.com/h5bp/html5-boilerplate/-/blob/main/README.md",
      "avatar_url":null,
      "star_count":0,
      "forks_count":4,
      "last_activity_at":"2020-04-27T06:13:22.642Z",
      "namespace":{
         "id":28,
         "name":"H5bp",
         "path":"h5bp",
         "kind":"group",
         "full_path":"h5bp",
         "parent_id":null,
         "avatar_url":null,
         "web_url":"https://gitlab.com/groups/h5bp"
      },
      "_links":{
         "self":"https://gitlab.com/api/v4/projects/8",
         "issues":"https://gitlab.com/api/v4/projects/8/issues",
         "merge_requests":"https://gitlab.com/api/v4/projects/8/merge_requests",
         "repo_branches":"https://gitlab.com/api/v4/projects/8/repository/branches",
         "labels":"https://gitlab.com/api/v4/projects/8/labels",
         "events":"https://gitlab.com/api/v4/projects/8/events",
         "members":"https://gitlab.com/api/v4/projects/8/members"
      },
      "empty_repo":false,
      "archived":false,
      "visibility":"public",
      "resolve_outdated_diff_discussions":false,
      "container_registry_enabled":true,
      "container_expiration_policy":{
         "cadence":"7d",
         "enabled":true,
         "keep_n":null,
         "older_than":null,
         "name_regex":null,
         "name_regex_keep":null,
         "next_run_at":"2020-05-04T06:13:22.654Z"
      },
      "issues_enabled":true,
      "merge_requests_enabled":true,
      "wiki_enabled":true,
      "jobs_enabled":true,
      "snippets_enabled":true,
      "can_create_merge_request_in":true,
      "issues_access_level":"enabled",
      "repository_access_level":"enabled",
      "merge_requests_access_level":"enabled",
      "forking_access_level":"enabled",
      "wiki_access_level":"enabled",
      "builds_access_level":"enabled",
      "snippets_access_level":"enabled",
      "pages_access_level":"enabled",
      "security_and_compliance_access_level":"enabled",
      "emails_disabled":null,
      "emails_enabled": null,
      "shared_runners_enabled":true,
      "lfs_enabled":true,
      "creator_id":1,
      "import_status":"failed",
      "open_issues_count":10,
      "ci_default_git_depth":50,
      "ci_forward_deployment_enabled":true,
      "ci_forward_deployment_rollback_allowed": true,
      "ci_allow_fork_pipelines_to_run_in_parent_project":true,
      "public_jobs":true,
      "build_timeout":3600,
      "auto_cancel_pending_pipelines":"enabled",
      "ci_config_path":null,
      "shared_with_groups":[
         {
            "group_id":24,
            "group_name":"Commit451",
            "group_full_path":"Commit451",
            "group_access_level":30,
            "expires_at":null
         }
      ],
      "only_allow_merge_if_pipeline_succeeds":false,
      "request_access_enabled":true,
      "only_allow_merge_if_all_discussions_are_resolved":false,
      "remove_source_branch_after_merge":true,
      "printing_merge_request_link_enabled":true,
      "merge_method":"merge",
      "suggestion_commit_message":null,
      "auto_devops_enabled":true,
      "auto_devops_deploy_strategy":"continuous",
      "autoclose_referenced_issues":true,
      "repository_storage":"default"
   }
]
```

