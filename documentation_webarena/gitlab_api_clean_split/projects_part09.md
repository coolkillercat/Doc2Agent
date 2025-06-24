## Get single project

Get a specific project. This endpoint can be accessed without authentication if
the project is publicly accessible.

```plaintext
GET /projects/:id
```

| Attribute                | Type              | Required | Description |
|--------------------------|-------------------|----------|-------------|
| `id`                     | integer or string | Yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding). |
| `license`                | boolean           | No       | Include project license data. |
| `statistics`             | boolean           | No       | Include project statistics. Available only to users with at least the Reporter role. |
| `with_custom_attributes` | boolean           | No       | Include [custom attributes](custom_attributes.md) in response. _(administrators only)_ |

```json
{
  "id": 3,
  "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
  "description_html": "<p data-sourcepos=\"1:1-1:56\" dir=\"auto\">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>",
  "default_branch": "main",
  "visibility": "private",
  "ssh_url_to_repo": "git@example.com:diaspora/diaspora-project-site.git",
  "http_url_to_repo": "http://example.com/diaspora/diaspora-project-site.git",
  "web_url": "http://example.com/diaspora/diaspora-project-site",
  "readme_url": "http://example.com/diaspora/diaspora-project-site/blob/main/README.md",
  "tag_list": [ //deprecated, use `topics` instead
    "example",
    "disapora project"
  ],
  "topics": [
    "example",
    "disapora project"
  ],
  "owner": {
    "id": 3,
    "name": "Diaspora",
    "created_at": "2013-09-30T13:46:02Z"
  },
  "name": "Diaspora Project Site",
  "name_with_namespace": "Diaspora / Diaspora Project Site",
  "path": "diaspora-project-site",
  "path_with_namespace": "diaspora/diaspora-project-site",
  "issues_enabled": true,
  "open_issues_count": 1,
  "merge_requests_enabled": true,
  "jobs_enabled": true,
  "wiki_enabled": true,
  "snippets_enabled": false,
  "can_create_merge_request_in": true,
  "resolve_outdated_diff_discussions": false,
  "container_registry_enabled": false, // deprecated, use container_registry_access_level instead
  "container_registry_access_level": "disabled",
  "security_and_compliance_access_level": "disabled",
  "container_expiration_policy": {
    "cadence": "7d",
    "enabled": false,
    "keep_n": null,
    "older_than": null,
    "name_regex": null, // to be deprecated in GitLab 13.0 in favor of `name_regex_delete`
    "name_regex_delete": null,
    "name_regex_keep": null,
    "next_run_at": "2020-01-07T21:42:58.658Z"
  },
  "created_at": "2013-09-30T13:46:02Z",
  "updated_at": "2013-09-30T13:46:02Z",
  "last_activity_at": "2013-09-30T13:46:02Z",
  "creator_id": 3,
  "namespace": {
    "id": 3,
    "name": "Diaspora",
    "path": "diaspora",
    "kind": "group",
    "full_path": "diaspora",
    "avatar_url": "http://localhost:3000/uploads/group/avatar/3/foo.jpg",
    "web_url": "http://localhost:3000/groups/diaspora"
  },
  "import_url": null,
  "import_type": null,
  "import_status": "none",
  "import_error": null,
  "permissions": {
    "project_access": {
      "access_level": 10,
      "notification_level": 3
    },
    "group_access": {
      "access_level": 50,
      "notification_level": 3
    }
  },
  "archived": false,
  "avatar_url": "http://example.com/uploads/project/avatar/3/uploads/avatar.png",
  "license_url": "http://example.com/diaspora/diaspora-client/blob/main/LICENSE",
  "license": {
    "key": "lgpl-3.0",
    "name": "GNU Lesser General Public License v3.0",
    "nickname": "GNU LGPLv3",
    "html_url": "http://choosealicense.com/licenses/lgpl-3.0/",
    "source_url": "http://www.gnu.org/licenses/lgpl-3.0.txt"
  },
  "shared_runners_enabled": true,
  "group_runners_enabled": true,
  "forks_count": 0,
  "star_count": 0,
  "runners_token": "b8bc4a7a29eb76ea83cf79e4908c2b",
  "ci_default_git_depth": 50,
  "ci_forward_deployment_enabled": true,
  "ci_forward_deployment_rollback_allowed": true,
  "ci_allow_fork_pipelines_to_run_in_parent_project": true,
  "ci_separated_caches": true,
  "ci_restrict_pipeline_cancellation_role": "developer",
  "public_jobs": true,
  "shared_with_groups": [
    {
      "group_id": 4,
      "group_name": "Twitter",
      "group_full_path": "twitter",
      "group_access_level": 30
    },
    {
      "group_id": 3,
      "group_name": "Gitlab Org",
      "group_full_path": "gitlab-org",
      "group_access_level": 10
    }
  ],
  "repository_storage": "default",
  "only_allow_merge_if_pipeline_succeeds": false,
  "allow_merge_on_skipped_pipeline": false,
  "restrict_user_defined_variables": false,
  "only_allow_merge_if_all_discussions_are_resolved": false,
  "remove_source_branch_after_merge": false,
  "printing_merge_requests_link_enabled": true,
  "request_access_enabled": false,
  "merge_method": "merge",
  "squash_option": "default_on",
  "auto_devops_enabled": true,
  "auto_devops_deploy_strategy": "continuous",
  "approvals_before_merge": 0, // Deprecated. Use merge request approvals API instead.
  "mirror": false,
  "mirror_user_id": 45,
  "mirror_trigger_builds": false,
  "only_mirror_protected_branches": false,
  "mirror_overwrites_diverged_branches": false,
  "external_authorization_classification_label": null,
  "packages_enabled": true,
  "service_desk_enabled": false,
  "service_desk_address": null,
  "autoclose_referenced_issues": true,
  "suggestion_commit_message": null,
  "enforce_auth_checks_on_uploads": true,
  "merge_commit_template": null,
  "squash_commit_template": null,
  "issue_branch_template": "gitlab/%{id}-%{title}",
  "marked_for_deletion_at": "2020-04-03", // Deprecated and will be removed in API v5 in favor of marked_for_deletion_on
  "marked_for_deletion_on": "2020-04-03",
  "compliance_frameworks": [ "sox" ],
  "warn_about_potentially_unwanted_characters": true,
  "statistics": {
    "commit_count": 37,
    "storage_size": 1038090,
    "repository_size": 1038090,
    "wiki_size" : 0,
    "lfs_objects_size": 0,
    "job_artifacts_size": 0,
    "pipeline_artifacts_size": 0,
    "packages_size": 0,
    "snippets_size": 0,
    "uploads_size": 0
  },
  "container_registry_image_prefix": "registry.example.com/diaspora/diaspora-client",
  "_links": {
    "self": "http://example.com/api/v4/projects",
    "issues": "http://example.com/api/v4/projects/1/issues",
    "merge_requests": "http://example.com/api/v4/projects/1/merge_requests",
    "repo_branches": "http://example.com/api/v4/projects/1/repository_branches",
    "labels": "http://example.com/api/v4/projects/1/labels",
    "events": "http://example.com/api/v4/projects/1/events",
    "members": "http://example.com/api/v4/projects/1/members",
    "cluster_agents": "http://example.com/api/v4/projects/1/cluster_agents"
  }
}
```

Users of [GitLab Ultimate](https://about.gitlab.com/pricing/)
can also see the `only_allow_merge_if_all_status_checks_passed`
parameters using GitLab 15.5 and later:

```json
{
  "id": 1,
  "project_id": 3,
  "only_allow_merge_if_all_status_checks_passed": false,
  ...
}
```

If the project is a fork, the `forked_from_project` field appears in the response.
For this field, if the upstream project is private, a valid token for authentication must be provided.
The field `mr_default_target_self` appears as well. If this value is `false`, then all merge requests
target the upstream project by default.

```json
{
   "id":3,

   ...

   "mr_default_target_self": false,
   "forked_from_project":{
      "id":13083,
      "description":"GitLab Community Edition",
      "name":"GitLab Community Edition",
      "name_with_namespace":"GitLab.org / GitLab Community Edition",
      "path":"gitlab-foss",
      "path_with_namespace":"gitlab-org/gitlab-foss",
      "created_at":"2013-09-26T06:02:36.000Z",
      "default_branch":"main",
      "tag_list":[], //deprecated, use `topics` instead
      "topics":[],
      "ssh_url_to_repo":"git@gitlab.com:gitlab-org/gitlab-foss.git",
      "http_url_to_repo":"https://gitlab.com/gitlab-org/gitlab-foss.git",
      "web_url":"https://gitlab.com/gitlab-org/gitlab-foss",
      "avatar_url":"https://gitlab.com/uploads/-/system/project/avatar/13083/logo-extra-whitespace.png",
      "license_url": "https://gitlab.com/gitlab-org/gitlab/-/blob/main/LICENSE",
      "license": {
        "key": "mit",
        "name": "MIT License",
        "nickname": null,
        "html_url": "http://choosealicense.com/licenses/mit/",
        "source_url": "https://opensource.org/licenses/MIT"
      },
      "star_count":3812,
      "forks_count":3561,
      "last_activity_at":"2018-01-02T11:40:26.570Z",
      "namespace": {
            "id": 72,
            "name": "GitLab.org",
            "path": "gitlab-org",
            "kind": "group",
            "full_path": "gitlab-org",
            "parent_id": null
      },
      "repository_storage": "default"
   }

   ...

}
```

### Templates for issues and merge requests

DETAILS:
**Tier:** Premium, Ultimate
**Offering:** GitLab.com, Self-managed, GitLab Dedicated

Users of [GitLab Premium or Ultimate](https://about.gitlab.com/pricing/)
can also see the `issues_template` and `merge_requests_template` parameters for managing
[issue and merge request description templates](../user/project/description_templates.md).

```json
{
  "id": 3,
  "issues_template": null,
  "merge_requests_template": null,
  ...
}
```

