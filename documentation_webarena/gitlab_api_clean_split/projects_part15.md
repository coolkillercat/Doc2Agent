## Create project for user

> - `operations_access_level` [removed](https://gitlab.com/gitlab-org/gitlab/-/issues/385798) in GitLab 16.0.
> - `model_registry_access_level` [introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/412734) in GitLab 16.7.

Creates a new project owned by the specified user. Available only for administrators.

If your HTTP repository isn't publicly accessible, add authentication information
to the URL `https://username:password@gitlab.company.com/group/project.git`,
where `password` is a public access key with the `api` scope enabled.

```plaintext
POST /projects/user/:user_id
```

| Attribute                                                         | Type    | Required | Description |
|-------------------------------------------------------------------|---------|----------|-------------|
| `name`                                                            | string  | Yes      | The name of the new project. |
| `user_id`                                                         | integer | Yes      | The user ID of the project owner. |
| `allow_merge_on_skipped_pipeline`                                 | boolean | No       | Set whether or not merge requests can be merged with skipped jobs. |
| `analytics_access_level`                                          | string  | No       | One of `disabled`, `private` or `enabled` |
| `approvals_before_merge`                                          | integer | No       | How many approvers should approve merge requests by default. [Deprecated](https://gitlab.com/gitlab-org/gitlab/-/issues/353097) in GitLab 16.0. To configure approval rules, see [Merge request approvals API](merge_request_approvals.md). Premium and Ultimate only. |
| `auto_cancel_pending_pipelines`                                   | string  | No       | Auto-cancel pending pipelines. This action toggles between an enabled state and a disabled state; it is not a boolean. |
| `auto_devops_deploy_strategy`                                     | string  | No       | Auto Deploy strategy (`continuous`, `manual` or `timed_incremental`). |
| `auto_devops_enabled`                                             | boolean | No       | Enable Auto DevOps for this project. |
| `autoclose_referenced_issues`                                     | boolean | No       | Set whether auto-closing referenced issues on default branch. |
| `avatar`                                                          | mixed   | No       | Image file for avatar of the project. |
| `build_git_strategy`                                              | string  | No       | The Git strategy. Defaults to `fetch`. |
| `build_timeout`                                                   | integer | No       | The maximum amount of time, in seconds, that a job can run. |
| `builds_access_level`                                             | string  | No       | One of `disabled`, `private`, or `enabled`. |
| `ci_config_path`                                                  | string  | No       | The path to CI configuration file. |
| `container_registry_access_level`                                 | string  | No       | Set visibility of container registry, for this project, to one of `disabled`, `private` or `enabled`. |
| `container_registry_enabled`                                      | boolean | No       | _(Deprecated)_ Enable container registry for this project. Use `container_registry_access_level` instead. |
| `default_branch`                                                  | string  | No       | The [default branch](../user/project/repository/branches/default.md) name. Requires `initialize_with_readme` to be `true`. |
| `description`                                                     | string  | No       | Short project description. |
| `emails_disabled`                                                 | boolean | No       | _(Deprecated)_ Disable email notifications. Use `emails_enabled` instead |
| `emails_enabled`                                                  | boolean | No       | Enable email notifications. |
| `enforce_auth_checks_on_uploads`                                  | boolean | No       | Enforce [auth checks](../security/user_file_uploads.md#enable-authorization-checks-for-all-media-files) on uploads. |
| `environments_access_level`                                       | string  | No       | One of `disabled`, `private`, or `enabled`. |
| `external_authorization_classification_label`                     | string  | No       | The classification label for the project. Premium and Ultimate only. |
| `feature_flags_access_level`                                      | string  | No       | One of `disabled`, `private`, or `enabled`. |
| `forking_access_level`                                            | string  | No       | One of `disabled`, `private`, or `enabled`. |
| `group_runners_enabled`                                           | boolean | No       | Enable group runners for this project. |
| `group_with_project_templates_id`                                 | integer | No       | For group-level custom templates, specifies ID of group from which all the custom project templates are sourced. Leave empty for instance-level templates. Requires `use_custom_template` to be true. Premium and Ultimate only. |
| `import_url`                                                      | string  | No       | URL to import repository from. |
| `infrastructure_access_level`                                     | string  | No       | One of `disabled`, `private`, or `enabled`. |
| `initialize_with_readme`                                          | boolean | No       | `false` by default. |
| `issue_branch_template`                                           | string  | No       | Template used to suggest names for [branches created from issues](../user/project/merge_requests/creating_merge_requests.md#from-an-issue). _([Introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/21243) in GitLab 15.6.)_ |
| `issues_access_level`                                             | string  | No       | One of `disabled`, `private`, or `enabled`. |
| `issues_enabled`                                                  | boolean | No       | _(Deprecated)_ Enable issues for this project. Use `issues_access_level` instead. |
| `jobs_enabled`                                                    | boolean | No       | _(Deprecated)_ Enable jobs for this project. Use `builds_access_level` instead. |
| `lfs_enabled`                                                     | boolean | No       | Enable LFS. |
| `merge_commit_template`                                           | string  | No       | [Template](../user/project/merge_requests/commit_templates.md) used to create merge commit message in merge requests. |
| `merge_method`                                                    | string  | No       | Set the [merge method](#project-merge-method) used. |
| `merge_requests_access_level`                                     | string  | No       | One of `disabled`, `private`, or `enabled`. |
| `merge_requests_enabled`                                          | boolean | No       | _(Deprecated)_ Enable merge requests for this project. Use `merge_requests_access_level` instead. |
| `mirror_trigger_builds`                                           | boolean | No       | Pull mirroring triggers builds. Premium and Ultimate only. |
| `mirror`                                                          | boolean | No       | Enables pull mirroring in a project. Premium and Ultimate only. |
| `model_experiments_access_level`                                  | string  | No       | One of `disabled`, `private`, or `enabled`. |
| `model_registry_access_level`                                     | string  | No       | One of `disabled`, `private`, or `enabled`. |
| `monitor_access_level`                                            | string  | No       | One of `disabled`, `private`, or `enabled`. |
| `namespace_id`                                                    | integer | No       | Namespace for the new project (defaults to the current user's namespace). |
| `only_allow_merge_if_all_discussions_are_resolved`                | boolean | No       | Set whether merge requests can only be merged when all the discussions are resolved. |
| `only_allow_merge_if_all_status_checks_passed`                    | boolean | No       | Indicates that merges of merge requests should be blocked unless all status checks have passed. Defaults to false. [Introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/369859) in GitLab 15.5 with feature flag `only_allow_merge_if_all_status_checks_passed` disabled by default. Ultimate only. |
| `only_allow_merge_if_pipeline_succeeds`                           | boolean | No       | Set whether merge requests can only be merged with successful jobs. |
| `packages_enabled`                                                | boolean | No       | Enable or disable packages repository feature. |
| `pages_access_level`                                              | string  | No       | One of `disabled`, `private`, `enabled`, or `public`. |
| `path`                                                            | string  | No       | Custom repository name for new project. By default generated based on name. |
| `printing_merge_request_link_enabled`                             | boolean | No       | Show link to create/view merge request when pushing from the command line. |
| `public_builds`                                                   | boolean | No       | _(Deprecated)_ If `true`, jobs can be viewed by non-project members. Use `public_jobs` instead. |
| `public_jobs`                                                     | boolean | No       | If `true`, jobs can be viewed by non-project members. |
| `releases_access_level`                                           | string  | No       | One of `disabled`, `private`, or `enabled`. |
| `repository_object_format`                                        | string  | No       | Repository object format. Defaults to `sha1`. [Introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/419887) in GitLab 16.9. |
| `remove_source_branch_after_merge`                                | boolean | No       | Enable `Delete source branch` option by default for all new merge requests. |
| `repository_access_level`                                         | string  | No       | One of `disabled`, `private`, or `enabled`. |
| `repository_storage`                                              | string  | No       | Which storage shard the repository is on. _(administrators only)_ |
| `request_access_enabled`                                          | boolean | No       | Allow users to request member access. |
| `requirements_access_level`                                       | string  | No       | One of `disabled`, `private`, `enabled` or `public` |
| `resolve_outdated_diff_discussions`                               | boolean | No       | Automatically resolve merge request diffs discussions on lines changed with a push. |
| `security_and_compliance_access_level`                            | string  | No       | Security and compliance access level. One of `disabled`, `private`, or `enabled`. |
| `shared_runners_enabled`                                          | boolean | No       | Enable shared runners for this project. |
| `show_default_award_emojis`                                       | boolean | No       | Show default emoji reactions. |
| `snippets_access_level`                                           | string  | No       | One of `disabled`, `private`, or `enabled`. |
| `snippets_enabled`                                                | boolean | No       | _(Deprecated)_ Enable snippets for this project. Use `snippets_access_level` instead. |
| `squash_commit_template`                                          | string  | No       | [Template](../user/project/merge_requests/commit_templates.md) used to create squash commit message in merge requests. |
| `squash_option`                                                   | string  | No       | One of `never`, `always`, `default_on`, or `default_off`. |
| `suggestion_commit_message`                                       | string  | No       | The commit message used to apply merge request [suggestions](../user/project/merge_requests/reviews/suggestions.md). |
| `tag_list`                                                        | array   | No       | _([Deprecated](https://gitlab.com/gitlab-org/gitlab/-/issues/328226) in GitLab 14.0)_ The list of tags for a project; put array of tags, that should be finally assigned to a project. Use `topics` instead. |
| `template_name`                                                   | string  | No       | When used without `use_custom_template`, name of a [built-in project template](../user/project/index.md#create-a-project-from-a-built-in-template). When used with `use_custom_template`, name of a custom project template. |
| `topics`                                                          | array   | No       | The list of topics for the project. |
| `use_custom_template`                                             | boolean | No       | Use either custom [instance](../administration/custom_project_templates.md) or [group](../user/group/custom_project_templates.md) (with `group_with_project_templates_id`) project template. Premium and Ultimate only. |
| `visibility`                                                      | string  | No       | See [project visibility level](#project-visibility-level). |
| `warn_about_potentially_unwanted_characters`                      | boolean | No       | Enable warnings about usage of potentially unwanted characters in this project. |
| `wiki_access_level`                                               | string  | No       | One of `disabled`, `private`, or `enabled`. |
| `wiki_enabled`                                                    | boolean | No       | _(Deprecated)_ Enable wiki for this project. Use `wiki_access_level` instead. |

