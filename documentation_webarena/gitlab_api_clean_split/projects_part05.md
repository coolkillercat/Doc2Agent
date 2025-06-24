## List all projects

> - The `_links.cluster_agents` attribute in the response was [introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/347047) in GitLab 15.0.

Get a list of all visible projects across GitLab for the authenticated user.
When accessed without authentication, only public projects with _simple_ fields
are returned.

```plaintext
GET /projects
```

| Attribute                                      | Type     | Required | Description |
|------------------------------------------------|----------|----------|-------------|
| `archived`                                     | boolean  | No       | Limit by archived status. |
| `id_after`                                     | integer  | No       | Limit results to projects with IDs greater than the specified ID. |
| `id_before`                                    | integer  | No       | Limit results to projects with IDs less than the specified ID. |
| `imported`                                     | boolean  | No       | Limit results to projects which were imported from external systems by current user. |
| `include_hidden`                               | boolean  | No       | Include hidden projects. _(administrators only)_ Premium and Ultimate only. |
| `include_pending_delete`                       | boolean  | No       | Include projects pending deletion. _(administrators only)_ |
| `last_activity_after`                          | datetime | No       | Limit results to projects with last activity after specified time. Format: ISO 8601 (`YYYY-MM-DDTHH:MM:SSZ`) |
| `last_activity_before`                         | datetime | No       | Limit results to projects with last activity before specified time. Format: ISO 8601 (`YYYY-MM-DDTHH:MM:SSZ`) |
| `membership`                                   | boolean  | No       | Limit by projects that the current user is a member of. |
| `min_access_level`                             | integer  | No       | Limit by current user minimal [role (`access_level`)](members.md#roles). |
| `order_by`                                     | string   | No       | Return projects ordered by `id`, `name`, `path`, `created_at`, `updated_at`, `last_activity_at`, or `similarity` fields. `repository_size`, `storage_size`, `packages_size` or `wiki_size` fields are only allowed for administrators. `similarity` is only available when searching and is limited to projects that the current user is a member of. Default is `created_at`. |
| `owned`                                        | boolean  | No       | Limit by projects explicitly owned by the current user. |
| `repository_checksum_failed`                   | boolean  | No       | Limit projects where the repository checksum calculation has failed. Premium and Ultimate only. |
| `repository_storage`                           | string   | No       | Limit results to projects stored on `repository_storage`. _(administrators only)_ |
| `search_namespaces`                            | boolean  | No       | Include ancestor namespaces when matching search criteria. Default is `false`. |
| `search`                                       | string   | No       | Return list of projects matching the search criteria. |
| `simple`                                       | boolean  | No       | Return only limited fields for each project. This operation is a no-op without authentication where only simple fields are returned. |
| `sort`                                         | string   | No       | Return projects sorted in `asc` or `desc` order. Default is `desc`. |
| `starred`                                      | boolean  | No       | Limit by projects starred by the current user. |
| `statistics`                                   | boolean  | No       | Include project statistics. Available only to users with at least the Reporter role. |
| `topic_id`                                     | integer  | No       | Limit results to projects with the assigned topic given by the topic ID. |
| `topic`                                        | string   | No       | Comma-separated topic names. Limit results to projects that match all of given topics. See `topics` attribute. |
| `updated_after`                                | datetime | No       | Limit results to projects last updated after the specified time. Format: ISO 8601 (`YYYY-MM-DDTHH:MM:SSZ`). [Introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/393979) in GitLab 15.10. For this filter to work, you must also provide `updated_at` as the `order_by` attribute. |
| `updated_before`                               | datetime | No       | Limit results to projects last updated before the specified time. Format: ISO 8601 (`YYYY-MM-DDTHH:MM:SSZ`). [Introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/393979) in GitLab 15.10. For this filter to work, you must also provide `updated_at` as the `order_by` attribute. |
| `visibility`                                   | string   | No       | Limit by visibility `public`, `internal`, or `private`. |
| `wiki_checksum_failed`                         | boolean  | No       | Limit projects where the wiki checksum calculation has failed. Premium and Ultimate only. |
| `with_custom_attributes`                       | boolean  | No       | Include [custom attributes](custom_attributes.md) in response. _(administrator only)_ |
| `with_issues_enabled`                          | boolean  | No       | Limit by enabled issues feature. |
| `with_merge_requests_enabled`                  | boolean  | No       | Limit by enabled merge requests feature. |
| `with_programming_language`                    | string   | No       | Limit by projects which use the given programming language. |

This endpoint supports [keyset pagination](rest/index.md#keyset-based-pagination)
for selected `order_by` options.

When `simple=true` or the user is unauthenticated this returns something like:

Example request:

```shell
curl --request GET "https://gitlab.example.com/api/v4/projects"
```

Example response:

```json
[
  {
    "id": 4,
    "description": null,
    "name": "Diaspora Client",
    "name_with_namespace": "Diaspora / Diaspora Client",
    "path": "diaspora-client",
    "path_with_namespace": "diaspora/diaspora-client",
    "created_at": "2013-09-30T13:46:02Z",
    "default_branch": "main",
    "tag_list": [
      "example",
      "disapora client"
    ],
    "topics": [
      "example",
      "disapora client"
    ],
    "ssh_url_to_repo": "git@gitlab.example.com:diaspora/diaspora-client.git",
    "http_url_to_repo": "https://gitlab.example.com/diaspora/diaspora-client.git",
    "web_url": "https://gitlab.example.com/diaspora/diaspora-client",
    "avatar_url": "https://gitlab.example.com/uploads/project/avatar/4/uploads/avatar.png",
    "star_count": 0,
    "last_activity_at": "2013-09-30T13:46:02Z",
    "namespace": {
      "id": 2,
      "name": "Diaspora",
      "path": "diaspora",
      "kind": "group",
      "full_path": "diaspora",
      "parent_id": null,
      "avatar_url": null,
      "web_url": "https://gitlab.example.com/diaspora"
    }
  },
  {
    ...
  }
```

When the user is authenticated and `simple` is not set this returns something like:

```json
[
  {
    "id": 4,
    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    "description_html": "<p data-sourcepos=\"1:1-1:56\" dir=\"auto\">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>",
    "name": "Diaspora Client",
    "name_with_namespace": "Diaspora / Diaspora Client",
    "path": "diaspora-client",
    "path_with_namespace": "diaspora/diaspora-client",
    "created_at": "2013-09-30T13:46:02Z",
    "updated_at": "2013-09-30T13:46:02Z",
    "default_branch": "main",
    "tag_list": [ //deprecated, use `topics` instead
      "example",
      "disapora client"
    ],
    "topics": [
      "example",
      "disapora client"
    ],
    "ssh_url_to_repo": "git@gitlab.example.com:diaspora/diaspora-client.git",
    "http_url_to_repo": "https://gitlab.example.com/diaspora/diaspora-client.git",
    "web_url": "https://gitlab.example.com/diaspora/diaspora-client",
    "readme_url": "https://gitlab.example.com/diaspora/diaspora-client/blob/main/README.md",
    "avatar_url": "https://gitlab.example.com/uploads/project/avatar/4/uploads/avatar.png",
    "forks_count": 0,
    "star_count": 0,
    "last_activity_at": "2022-06-24T17:11:26.841Z",
    "namespace": {
      "id": 3,
      "name": "Diaspora",
      "path": "diaspora",
      "kind": "group",
      "full_path": "diaspora",
      "parent_id": null,
      "avatar_url": "https://gitlab.example.com/uploads/project/avatar/6/uploads/avatar.png",
      "web_url": "https://gitlab.example.com/diaspora"
    },
    "container_registry_image_prefix": "registry.gitlab.example.com/diaspora/diaspora-client",
    "_links": {
      "self": "https://gitlab.example.com/api/v4/projects/4",
      "issues": "https://gitlab.example.com/api/v4/projects/4/issues",
      "merge_requests": "https://gitlab.example.com/api/v4/projects/4/merge_requests",
      "repo_branches": "https://gitlab.example.com/api/v4/projects/4/repository/branches",
      "labels": "https://gitlab.example.com/api/v4/projects/4/labels",
      "events": "https://gitlab.example.com/api/v4/projects/4/events",
      "members": "https://gitlab.example.com/api/v4/projects/4/members",
      "cluster_agents": "https://gitlab.example.com/api/v4/projects/4/cluster_agents"
    },
    "packages_enabled": true,
    "empty_repo": false,
    "archived": false,
    "visibility": "public",
    "resolve_outdated_diff_discussions": false,
    "container_expiration_policy": {
      "cadence": "1month",
      "enabled": true,
      "keep_n": 1,
      "older_than": "14d",
      "name_regex": "",
      "name_regex_keep": ".*-main",
      "next_run_at": "2022-06-25T17:11:26.865Z"
    },
    "issues_enabled": true,
    "merge_requests_enabled": true,
    "wiki_enabled": true,
    "jobs_enabled": true,
    "snippets_enabled": true,
    "container_registry_enabled": true,
    "service_desk_enabled": true,
    "can_create_merge_request_in": true,
    "issues_access_level": "enabled",
    "repository_access_level": "enabled",
    "merge_requests_access_level": "enabled",
    "forking_access_level": "enabled",
    "wiki_access_level": "enabled",
    "builds_access_level": "enabled",
    "snippets_access_level": "enabled",
    "pages_access_level": "enabled",
    "analytics_access_level": "enabled",
    "container_registry_access_level": "enabled",
    "security_and_compliance_access_level": "private",
    "emails_disabled": null,
    "emails_enabled": null,
    "shared_runners_enabled": true,
    "group_runners_enabled": true,
    "lfs_enabled": true,
    "creator_id": 1,
    "import_url": null,
    "import_type": null,
    "import_status": "none",
    "import_error": null,
    "open_issues_count": 0,
    "ci_default_git_depth": 20,
    "ci_forward_deployment_enabled": true,
    "ci_forward_deployment_rollback_allowed": true,
    "ci_allow_fork_pipelines_to_run_in_parent_project": true,
    "ci_job_token_scope_enabled": false,
    "ci_separated_caches": true,
    "ci_restrict_pipeline_cancellation_role": "developer",
    "public_jobs": true,
    "build_timeout": 3600,
    "auto_cancel_pending_pipelines": "enabled",
    "ci_config_path": "",
    "shared_with_groups": [],
    "only_allow_merge_if_pipeline_succeeds": false,
    "allow_merge_on_skipped_pipeline": null,
    "restrict_user_defined_variables": false,
    "request_access_enabled": true,
    "only_allow_merge_if_all_discussions_are_resolved": false,
    "remove_source_branch_after_merge": true,
    "printing_merge_request_link_enabled": true,
    "merge_method": "merge",
    "squash_option": "default_off",
    "enforce_auth_checks_on_uploads": true,
    "suggestion_commit_message": null,
    "merge_commit_template": null,
    "squash_commit_template": null,
    "issue_branch_template": "gitlab/%{id}-%{title}",
    "auto_devops_enabled": false,
    "auto_devops_deploy_strategy": "continuous",
    "autoclose_referenced_issues": true,
    "keep_latest_artifact": true,
    "runner_token_expiration_interval": null,
    "external_authorization_classification_label": "",
    "requirements_enabled": false,
    "requirements_access_level": "enabled",
    "security_and_compliance_enabled": false,
    "compliance_frameworks": [],
    "warn_about_potentially_unwanted_characters": true,
    "permissions": {
      "project_access": null,
      "group_access": null
    }
  },
  {
    ...
  }
]
```

NOTE:
`last_activity_at` is updated based on [project activity](../user/project/working_with_projects.md#view-project-activity) and [project events](events.md). `updated_at` is updated whenever the project record is changed in the database.

You can filter by [custom attributes](custom_attributes.md) with:

```plaintext
GET /projects?custom_attributes[key]=value&custom_attributes[other_key]=other_value
```

Example request:

```shell
curl --globoff --request GET "https://gitlab.example.com/api/v4/projects?custom_attributes[location]=Antarctica&custom_attributes[role]=Developer"
```

### Pagination limits

[Offset-based pagination](rest/index.md#offset-based-pagination)
is [limited to 50,000 records](https://gitlab.com/gitlab-org/gitlab/-/issues/34565).
[Keyset pagination](rest/index.md#keyset-based-pagination) is required to retrieve
projects beyond this limit.

Keyset pagination supports only `order_by=id`. Other sorting options aren't available.

