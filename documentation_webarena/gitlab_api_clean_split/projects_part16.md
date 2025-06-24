## Edit project

> - `operations_access_level` [removed](https://gitlab.com/gitlab-org/gitlab/-/issues/385798) in GitLab 16.0.
> - `model_registry_access_level` [introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/412734) in GitLab 16.7.

Updates an existing project.

If your HTTP repository isn't publicly accessible, add authentication information
to the URL `https://username:password@gitlab.company.com/group/project.git`,
where `password` is a public access key with the `api` scope enabled.

```plaintext
PUT /projects/:id
```

For example, to toggle the setting for
[shared runners on a GitLab.com project](../ci/runners/index.md):

```shell
curl --request PUT --header "PRIVATE-TOKEN: <your-token>" \
     --url "https://gitlab.com/api/v4/projects/<your-project-ID>" \
     --data "shared_runners_enabled=true" # to turn off: "shared_runners_enabled=false"
```

Supported attributes:

| Attribute                                                         | Type              | Required | Description |
|-------------------------------------------------------------------|-------------------|----------|-------------|
| `id`                                                              | integer or string | Yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding). |
| `allow_merge_on_skipped_pipeline`                                 | boolean           | No       | Set whether or not merge requests can be merged with skipped jobs. |
| `allow_pipeline_trigger_approve_deployment`                       | boolean           | No       | Set whether or not a pipeline triggerer is allowed to approve deployments. Premium and Ultimate only. |
| `only_allow_merge_if_all_status_checks_passed`                    | boolean           | No       | Indicates that merges of merge requests should be blocked unless all status checks have passed. Defaults to false.<br/><br/>[Introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/369859) in GitLab 15.5 with feature flag `only_allow_merge_if_all_status_checks_passed` disabled by default. The feature flag was enabled by default in GitLab 15.9. Ultimate only. |
| `analytics_access_level`                                          | string            | No       | One of `disabled`, `private` or `enabled` |
| `approvals_before_merge`                                          | integer           | No       | How many approvers should approve merge requests by default. [Deprecated](https://gitlab.com/gitlab-org/gitlab/-/issues/353097) in GitLab 16.0. To configure approval rules, see [Merge request approvals API](merge_request_approvals.md). Premium and Ultimate only. |
| `auto_cancel_pending_pipelines`                                   | string            | No       | Auto-cancel pending pipelines. This action toggles between an enabled state and a disabled state; it is not a boolean. |
| `auto_devops_deploy_strategy`                                     | string            | No       | Auto Deploy strategy (`continuous`, `manual`, or `timed_incremental`). |
| `auto_devops_enabled`                                             | boolean           | No       | Enable Auto DevOps for this project. |
| `autoclose_referenced_issues`                                     | boolean           | No       | Set whether auto-closing referenced issues on default branch. |
| `avatar`                                                          | mixed             | No       | Image file for avatar of the project. |
| `build_git_strategy`                                              | string            | No       | The Git strategy. Defaults to `fetch`. |
| `build_timeout`                                                   | integer           | No       | The maximum amount of time, in seconds, that a job can run. |
| `builds_access_level`                                             | string            | No       | One of `disabled`, `private`, or `enabled`. |
| `ci_config_path`                                                  | string            | No       | The path to CI configuration file. |
| `ci_default_git_depth`                                            | integer           | No       | Default number of revisions for [shallow cloning](../ci/pipelines/settings.md#limit-the-number-of-changes-fetched-during-clone). |
| `ci_forward_deployment_enabled`                                   | boolean           | No       | Enable or disable [prevent outdated deployment jobs](../ci/pipelines/settings.md#prevent-outdated-deployment-jobs). |
| `ci_forward_deployment_rollback_allowed`                          | boolean           | No       | Enable or disable [allow job retries for rollback deployments](../ci/pipelines/settings.md#prevent-outdated-deployment-jobs). |
| `ci_allow_fork_pipelines_to_run_in_parent_project`                | boolean           | No       | Enable or disable [running pipelines in the parent project for merge requests from forks](../ci/pipelines/merge_request_pipelines.md#run-pipelines-in-the-parent-project). _([Introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/325189) in GitLab 15.3.)_ |
| `ci_separated_caches`                                             | boolean           | No       | Set whether or not caches should be [separated](../ci/caching/index.md#cache-key-names) by branch protection status. |
| `ci_restrict_pipeline_cancellation_role`                          | string            | No       | Set the [role required to cancel a pipeline or job](../ci/pipelines/settings.md#restrict-roles-that-can-cancel-pipelines-or-jobs). One of `developer`, `maintainer`, or `no_one`. [Introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/429921) in GitLab 16.8. Premium and Ultimate only. |
| `container_expiration_policy_attributes`                          | hash              | No       | Update the image cleanup policy for this project. Accepts: `cadence` (string), `keep_n` (integer), `older_than` (string), `name_regex` (string), `name_regex_delete` (string), `name_regex_keep` (string), `enabled` (boolean). |
| `container_registry_access_level`                                 | string            | No       | Set visibility of container registry, for this project, to one of `disabled`, `private` or `enabled`. |
| `container_registry_enabled`                                      | boolean           | No       | _(Deprecated)_ Enable container registry for this project. Use `container_registry_access_level` instead. |
| `default_branch`                                                  | string            | No       | The [default branch](../user/project/repository/branches/default.md) name. |
| `description`                                                     | string            | No       | Short project description. |
| `emails_disabled`                                                 | boolean           | No       | _(Deprecated)_ Disable email notifications. Use `emails_enabled` instead |
| `emails_enabled`                                                  | boolean           | No       | Enable email notifications. |
| `enforce_auth_checks_on_uploads`                                  | boolean           | No       | Enforce [auth checks](../security/user_file_uploads.md#enable-authorization-checks-for-all-media-files) on uploads. |
| `external_authorization_classification_label`                     | string            | No       | The classification label for the project. Premium and Ultimate only. |
| `forking_access_level`                                            | string            | No       | One of `disabled`, `private`, or `enabled`. |
| `group_runners_enabled`                                           | boolean           | No       | Enable group runners for this project. |
| `import_url`                                                      | string            | No       | URL the repository was imported from. |
| `issues_access_level`                                             | string            | No       | One of `disabled`, `private`, or `enabled`. |
| `issues_enabled`                                                  | boolean           | No       | _(Deprecated)_ Enable issues for this project. Use `issues_access_level` instead. |
| `issues_template`                                                 | string            | No       | Default description for Issues. Description is parsed with GitLab Flavored Markdown. See [Templates for issues and merge requests](#templates-for-issues-and-merge-requests). Premium and Ultimate only. |
| `jobs_enabled`                                                    | boolean           | No       | _(Deprecated)_ Enable jobs for this project. Use `builds_access_level` instead. |
| `keep_latest_artifact`                                            | boolean           | No       | Disable or enable the ability to keep the latest artifact for this project. |
| `lfs_enabled`                                                     | boolean           | No       | Enable LFS. |
| `merge_commit_template`                                           | string            | No       | [Template](../user/project/merge_requests/commit_templates.md) used to create merge commit message in merge requests. |
| `merge_method`                                                    | string            | No       | Set the [merge method](#project-merge-method) used. |
| `merge_pipelines_enabled`                                         | boolean           | No       | Enable or disable merged results pipelines. |
| `merge_requests_access_level`                                     | string            | No       | One of `disabled`, `private`, or `enabled`. |
| `merge_requests_enabled`                                          | boolean           | No       | _(Deprecated)_ Enable merge requests for this project. Use `merge_requests_access_level` instead. |
| `merge_requests_template`                                         | string            | No       | Default description for merge requests. Description is parsed with GitLab Flavored Markdown. See [Templates for issues and merge requests](#templates-for-issues-and-merge-requests). Premium and Ultimate only. |
| `merge_trains_enabled`                                            | boolean           | No       | Enable or disable merge trains. |
| `mirror_overwrites_diverged_branches`                             | boolean           | No       | Pull mirror overwrites diverged branches. Premium and Ultimate only. |
| `mirror_trigger_builds`                                           | boolean           | No       | Pull mirroring triggers builds. Premium and Ultimate only. |
| `mirror_user_id`                                                  | integer           | No       | User responsible for all the activity surrounding a pull mirror event. _(administrators only)_ Premium and Ultimate only. |
| `mirror`                                                          | boolean           | No       | Enables pull mirroring in a project. Premium and Ultimate only. |
| `mr_default_target_self`                                          | boolean           | No       | For forked projects, target merge requests to this project. If `false`, the target is the upstream project. |
| `name`                                                            | string            | No       | The name of the project. |
| `only_allow_merge_if_all_discussions_are_resolved`                | boolean           | No       | Set whether merge requests can only be merged when all the discussions are resolved. |
| `only_allow_merge_if_pipeline_succeeds`                           | boolean           | No       | Set whether merge requests can only be merged with successful jobs. |
| `only_mirror_protected_branches`                                  | boolean           | No       | Only mirror protected branches. Premium and Ultimate only. |
| `packages_enabled`                                                | boolean           | No       | Enable or disable packages repository feature. |
| `pages_access_level`                                              | string            | No       | One of `disabled`, `private`, `enabled`, or `public`. |
| `path`                                                            | string            | No       | Custom repository name for the project. By default generated based on name. |
| `prevent_merge_without_jira_issue`                                | boolean           | No       | Set whether merge requests require an associated issue from Jira. Premium and Ultimate only. |
| `printing_merge_request_link_enabled`                             | boolean           | No       | Show link to create/view merge request when pushing from the command line. |
| `public_builds`                                                   | boolean           | No       | _(Deprecated)_ If `true`, jobs can be viewed by non-project members. Use `public_jobs` instead. |
| `public_jobs`                                                     | boolean           | No       | If `true`, jobs can be viewed by non-project members. |
| `releases_access_level`                                           | string            | No       | One of `disabled`, `private`, or `enabled`. |
| `environments_access_level`                                       | string            | No       | One of `disabled`, `private`, or `enabled`. |
| `feature_flags_access_level`                                      | string            | No       | One of `disabled`, `private`, or `enabled`. |
| `infrastructure_access_level`                                     | string            | No       | One of `disabled`, `private`, or `enabled`. |
| `monitor_access_level`                                            | string            | No       | One of `disabled`, `private`, or `enabled`. |
| `model_experiments_access_level`                                  | string            | No       | One of `disabled`, `private`, or `enabled`. |
| `model_registry_access_level`                                     | string            | No       | One of `disabled`, `private`, or `enabled`. |
| `remove_source_branch_after_merge`                                | boolean           | No       | Enable `Delete source branch` option by default for all new merge requests. |
| `repository_access_level`                                         | string            | No       | One of `disabled`, `private`, or `enabled`. |
| `repository_storage`                                              | string            | No       | Which storage shard the repository is on. _(administrators only)_ |
| `request_access_enabled`                                          | boolean           | No       | Allow users to request member access. |
| `requirements_access_level`                                       | string            | No       | One of `disabled`, `private`, `enabled` or `public` |
| `resolve_outdated_diff_discussions`                               | boolean           | No       | Automatically resolve merge request diffs discussions on lines changed with a push. |
| `restrict_user_defined_variables`                                 | boolean           | No       | Allow only users with the Maintainer role to pass user-defined variables when triggering a pipeline. For example when the pipeline is triggered in the UI, with the API, or by a trigger token. |
| `security_and_compliance_access_level`                            | string            | No       | Security and compliance access level. One of `disabled`, `private`, or `enabled`. |
| `service_desk_enabled`                                            | boolean           | No       | Enable or disable Service Desk feature. |
| `shared_runners_enabled`                                          | boolean           | No       | Enable shared runners for this project. |
| `show_default_award_emojis`                                       | boolean           | No       | Show default emoji reactions. |
| `snippets_access_level`                                           | string            | No       | One of `disabled`, `private`, or `enabled`. |
| `snippets_enabled`                                                | boolean           | No       | _(Deprecated)_ Enable snippets for this project. Use `snippets_access_level` instead. |
| `issue_branch_template`                                           | string            | No       | Template used to suggest names for [branches created from issues](../user/project/merge_requests/creating_merge_requests.md#from-an-issue). _([Introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/21243) in GitLab 15.6.)_ |
| `squash_commit_template`                                          | string            | No       | [Template](../user/project/merge_requests/commit_templates.md) used to create squash commit message in merge requests. |
| `squash_option`                                                   | string            | No       | One of `never`, `always`, `default_on`, or `default_off`. |
| `suggestion_commit_message`                                       | string            | No       | The commit message used to apply merge request suggestions. |
| `tag_list`                                                        | array             | No       | _([Deprecated](https://gitlab.com/gitlab-org/gitlab/-/issues/328226) in GitLab 14.0)_ The list of tags for a project; put array of tags, that should be finally assigned to a project. Use `topics` instead. |
| `topics`                                                          | array             | No       | The list of topics for the project. This replaces any existing topics that are already added to the project. |
| `visibility`                                                      | string            | No       | See [project visibility level](#project-visibility-level). |
| `warn_about_potentially_unwanted_characters`                      | boolean           | No       | Enable warnings about usage of potentially unwanted characters in this project. |
| `wiki_access_level`                                               | string            | No       | One of `disabled`, `private`, or `enabled`. |
| `wiki_enabled`                                                    | boolean           | No       | _(Deprecated)_ Enable wiki for this project. Use `wiki_access_level` instead. |

