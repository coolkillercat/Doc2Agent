## Transfer a project to a new namespace

See the [Project documentation](../user/project/settings/migrate_projects.md#transfer-a-project-to-another-namespace)
for prerequisites to transfer a project.

```plaintext
PUT /projects/:id/transfer
```

| Attribute   | Type              | Required | Description |
|-------------|-------------------|----------|-------------|
| `id`        | integer or string | Yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding). |
| `namespace` | integer or string | Yes      | The ID or path of the namespace to transfer to project to. |

Example request:

```shell
curl --request PUT --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/projects/5/transfer?namespace=14"
```

Example response:

```json
  {
  "id": 7,
  "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
  "description_html": "<p data-sourcepos=\"1:1-1:56\" dir=\"auto\">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>",
  "name": "hello-world",
  "name_with_namespace": "cute-cats / hello-world",
  "path": "hello-world",
  "path_with_namespace": "cute-cats/hello-world",
  "created_at": "2020-10-15T16:25:22.415Z",
  "updated_at": "2020-10-15T16:25:22.415Z",
  "default_branch": "main",
  "tag_list": [], //deprecated, use `topics` instead
  "topics": [],
  "ssh_url_to_repo": "git@gitlab.example.com:cute-cats/hello-world.git",
  "http_url_to_repo": "https://gitlab.example.com/cute-cats/hello-world.git",
  "web_url": "https://gitlab.example.com/cute-cats/hello-world",
  "readme_url": "https://gitlab.example.com/cute-cats/hello-world/-/blob/main/README.md",
  "avatar_url": null,
  "forks_count": 0,
  "star_count": 0,
  "last_activity_at": "2020-10-15T16:25:22.415Z",
  "namespace": {
    "id": 18,
    "name": "cute-cats",
    "path": "cute-cats",
    "kind": "group",
    "full_path": "cute-cats",
    "parent_id": null,
    "avatar_url": null,
    "web_url": "https://gitlab.example.com/groups/cute-cats"
  },
  "container_registry_image_prefix": "registry.example.com/cute-cats/hello-world",
  "_links": {
    "self": "https://gitlab.example.com/api/v4/projects/7",
    "issues": "https://gitlab.example.com/api/v4/projects/7/issues",
    "merge_requests": "https://gitlab.example.com/api/v4/projects/7/merge_requests",
    "repo_branches": "https://gitlab.example.com/api/v4/projects/7/repository/branches",
    "labels": "https://gitlab.example.com/api/v4/projects/7/labels",
    "events": "https://gitlab.example.com/api/v4/projects/7/events",
    "members": "https://gitlab.example.com/api/v4/projects/7/members"
  },
  "packages_enabled": true,
  "empty_repo": false,
  "archived": false,
  "visibility": "private",
  "resolve_outdated_diff_discussions": false,
  "container_registry_enabled": true, // deprecated, use container_registry_access_level instead
  "container_registry_access_level": "enabled",
  "container_expiration_policy": {
    "cadence": "7d",
    "enabled": false,
    "keep_n": null,
    "older_than": null,
    "name_regex": null,
    "name_regex_keep": null,
    "next_run_at": "2020-10-22T16:25:22.746Z"
  },
  "issues_enabled": true,
  "merge_requests_enabled": true,
  "wiki_enabled": true,
  "jobs_enabled": true,
  "snippets_enabled": true,
  "service_desk_enabled": false,
  "service_desk_address": null,
  "can_create_merge_request_in": true,
  "issues_access_level": "enabled",
  "repository_access_level": "enabled",
  "merge_requests_access_level": "enabled",
  "forking_access_level": "enabled",
  "analytics_access_level": "enabled",
  "wiki_access_level": "enabled",
  "builds_access_level": "enabled",
  "snippets_access_level": "enabled",
  "pages_access_level": "enabled",
  "security_and_compliance_access_level": "enabled",
  "emails_disabled": null,
  "emails_enabled": null,
  "shared_runners_enabled": true,
  "group_runners_enabled": true,
  "lfs_enabled": true,
  "creator_id": 2,
  "import_status": "none",
  "open_issues_count": 0,
  "ci_default_git_depth": 50,
  "public_jobs": true,
  "build_timeout": 3600,
  "auto_cancel_pending_pipelines": "enabled",
  "ci_config_path": null,
  "shared_with_groups": [],
  "only_allow_merge_if_pipeline_succeeds": false,
  "allow_merge_on_skipped_pipeline": null,
  "restrict_user_defined_variables": false,
  "request_access_enabled": true,
  "only_allow_merge_if_all_discussions_are_resolved": false,
  "remove_source_branch_after_merge": true,
  "printing_merge_request_link_enabled": true,
  "merge_method": "merge",
  "squash_option": "default_on",
  "suggestion_commit_message": null,
  "merge_commit_template": null,
  "auto_devops_enabled": true,
  "auto_devops_deploy_strategy": "continuous",
  "autoclose_referenced_issues": true,
  "approvals_before_merge": 0, // Deprecated. Use merge request approvals API instead.
  "mirror": false,
  "compliance_frameworks": [],
  "warn_about_potentially_unwanted_characters": true
}
```

