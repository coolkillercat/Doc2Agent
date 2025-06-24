## Update group

> - `unique_project_download_limit`, `unique_project_download_limit_interval_in_seconds`, and `unique_project_download_limit_allowlist` [introduced](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/92970) in GitLab 15.3 [with a flag](../administration/feature_flags.md) named `limit_unique_project_downloads_per_namespace_user`. Disabled by default.

FLAG:
On self-managed GitLab, by default `unique_project_download_limit`, `unique_project_download_limit_interval_in_seconds`, `unique_project_download_limit_allowlist` and `auto_ban_user_on_excessive_projects_download` are not available.
To make them available, an administrator can [enable the feature flag](../administration/feature_flags.md)
named `limit_unique_project_downloads_per_namespace_user`.

Updates the project group. Only available to group owners and administrators.

```plaintext
PUT /groups/:id
```

| Attribute                                               | Type    | Required | Description |
| ------------------------------------------------------- | ------- | -------- | ----------- |
| `id`                                                    | integer | yes      | The ID of the group. |
| `name`                                                  | string  | no       | The name of the group. |
| `path`                                                  | string  | no       | The path of the group. |
| `auto_devops_enabled`                                   | boolean | no       | Default to Auto DevOps pipeline for all projects within this group. |
| `avatar`                                                | mixed   | no       | Image file for avatar of the group. |
| `default_branch`                                        | string  | no       | The [default branch](../user/project/repository/branches/default.md) name for group's projects. [Introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/442298) in GitLab 16.11. |
| `default_branch_protection`                             | integer | no       | [Deprecated](https://gitlab.com/gitlab-org/gitlab/-/issues/408314) in GitLab 17.0. Use `default_branch_protection_defaults` instead. |
| `default_branch_protection_defaults`                    | hash    | no       | See [Options for `default_branch_protection_defaults`](#options-for-default_branch_protection_defaults). |
| `description`                                           | string  | no       | The description of the group. |
| `enabled_git_access_protocol`                           | string  | no       | Enabled protocols for Git access. Allowed values are: `ssh`, `http`, and `all` to allow both protocols. [Introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/436618) in GitLab 16.9. |
| `emails_disabled`                                       | boolean | no       | _([Deprecated](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/127899) in GitLab 16.5.)_ Disable email notifications. Use `emails_enabled` instead. |
| `emails_enabled`                                        | boolean | no       | Enable email notifications. |
| `lfs_enabled`                                           | boolean | no       | Enable/disable Large File Storage (LFS) for the projects in this group. |
| `mentions_disabled`                                     | boolean | no       | Disable the capability of a group from getting mentioned. |
| `prevent_sharing_groups_outside_hierarchy`              | boolean | no       | See [Prevent group sharing outside the group hierarchy](../user/group/access_and_permissions.md#prevent-group-sharing-outside-the-group-hierarchy). This attribute is only available on top-level groups. |
| `project_creation_level`                                | string  | no       | Determine if developers can create projects in the group. Can be `noone` (No one), `maintainer` (users with the Maintainer role), or `developer` (users with the Developer or Maintainer role). |
| `request_access_enabled`                                | boolean | no       | Allow users to request member access. |
| `require_two_factor_authentication`                     | boolean | no       | Require all users in this group to set up two-factor authentication. |
| `shared_runners_setting`                                | string  | no       | See [Options for `shared_runners_setting`](#options-for-shared_runners_setting). Enable or disable shared runners for a group's subgroups and projects. |
| `share_with_group_lock`                                 | boolean | no       | Prevent sharing a project with another group within this group. |
| `subgroup_creation_level`                               | string  | no       | Allowed to [create subgroups](../user/group/subgroups/index.md#create-a-subgroup). Can be `owner` (Owners), or `maintainer` (users with the Maintainer role). |
| `two_factor_grace_period`                               | integer | no       | Time before Two-factor authentication is enforced (in hours). |
| `visibility`                                            | string  | no       | The visibility level of the group. Can be `private`, `internal`, or `public`. |
| `extra_shared_runners_minutes_limit`                    | integer | no       | Can be set by administrators only. Additional compute minutes for this group. Self-managed, Premium and Ultimate only. |
| `file_template_project_id`                              | integer | no       | The ID of a project to load custom file templates from. Premium and Ultimate only. |
| `membership_lock`                                       | boolean | no       | Users cannot be added to projects in this group. Premium and Ultimate only. |
| `prevent_forking_outside_group`                         | boolean | no       | When enabled, users can **not** fork projects from this group to external namespaces. Premium and Ultimate only. |
| `shared_runners_minutes_limit`                          | integer | no       | Can be set by administrators only. Maximum number of monthly compute minutes for this group. Can be `nil` (default; inherit system default), `0` (unlimited), or `> 0`. Self-managed, Premium and Ultimate only. |
| `unique_project_download_limit`                         | integer | no       | Maximum number of unique projects a user can download in the specified time period before they are banned. Available only on top-level groups. Default: 0, Maximum: 10,000. Ultimate only. |
| `unique_project_download_limit_interval_in_seconds`     | integer | no       | Time period during which a user can download a maximum amount of projects before they are banned. Available only on top-level groups. Default: 0, Maximum: 864,000 seconds (10 days). Ultimate only. |
| `unique_project_download_limit_allowlist`               | array of strings | no | List of usernames excluded from the unique project download limit. Available only on top-level groups. Default: `[]`, Maximum: 100 usernames. Ultimate only.|
| `unique_project_download_limit_alertlist`               | array of integers | no | List of user IDs that are emailed when the unique project download limit is exceeded. Available only on top-level groups. Default: `[]`, Maximum: 100 user IDs. [Introduced](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/110201) in GitLab 15.9. Ultimate only.|
| `auto_ban_user_on_excessive_projects_download`          | boolean | no       | When enabled, users are automatically banned from the group when they download more than the maximum number of unique projects specified by `unique_project_download_limit` and `unique_project_download_limit_interval_in_seconds`. [Introduced](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/94159) in GitLab 15.4. Ultimate only.|
| `ip_restriction_ranges`                                 | string  | no       | Comma-separated list of IP addresses or subnet masks to restrict group access. [Introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/351493) in GitLab 15.4. Premium and Ultimate only.|
| `wiki_access_level`                                     | string  | no       | The wiki access level. Can be `disabled`, `private`, or `enabled`. Premium and Ultimate only.|
| `math_rendering_limits_enabled`                         | boolean | no       | Indicates if math rendering limits are used for this group.|
| `lock_math_rendering_limits_enabled`                    | boolean | no       | Indicates if math rendering limits are locked for all descendent groups.|
| `duo_features_enabled`                                  | boolean | no       | Indicates whether GitLab Duo features are enabled for this group. [Introduced](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/144931) in GitLab 16.10. Self-managed, Premium and Ultimate only. |
| `lock_duo_features_enabled`                             | boolean | no       | Indicates whether the GitLab Duo features enabled setting is enforced for all subgroups. [Introduced](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/144931) in GitLab 16.10. Self-managed, Premium and Ultimate only. |

NOTE:
The `projects` and `shared_projects` attributes in the response are deprecated and [scheduled for removal in API v5](https://gitlab.com/gitlab-org/gitlab/-/issues/213797).
To get the details of all projects within a group, use either the [list a group's projects](#list-a-groups-projects) or the [list a group's shared projects](#list-a-groups-shared-projects) endpoint.

```shell
curl --request PUT --header "PRIVATE-TOKEN: <your_access_token>" \
     "https://gitlab.example.com/api/v4/groups/5?name=Experimental"
```

This endpoint returns a maximum of 100 projects and shared projects. To get the details of all projects within a group, use the
  [list a group's projects endpoint](#list-a-groups-projects) instead.

Example response:

```json
{
  "id": 5,
  "name": "Experimental",
  "path": "h5bp",
  "description": "foo",
  "visibility": "internal",
  "avatar_url": null,
  "web_url": "http://gitlab.example.com/groups/h5bp",
  "request_access_enabled": false,
  "repository_storage": "default",
  "full_name": "Foobar Group",
  "full_path": "h5bp",
  "file_template_project_id": 1,
  "parent_id": null,
  "enabled_git_access_protocol": "all",
  "created_at": "2020-01-15T12:36:29.590Z",
  "prevent_sharing_groups_outside_hierarchy": false,
  "projects": [ // Deprecated and will be removed in API v5
    {
      "id": 9,
      "description": "foo",
      "default_branch": "main",
      "tag_list": [], //deprecated, use `topics` instead
      "topics": [],
      "public": false,
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
  ],
  "ip_restriction_ranges": null,
  "math_rendering_limits_enabled": true,
  "lock_math_rendering_limits_enabled": false
}
```

The `prevent_sharing_groups_outside_hierarchy` attribute is present in the response only for top-level groups.

Users of [GitLab Premium or Ultimate](https://about.gitlab.com/pricing/) also see the `wiki_access_level`,
`duo_features_enabled`, and`lock_duo_features_enabled` attributes.

### Options for `shared_runners_setting`

The `shared_runners_setting` attribute determines whether shared runners are enabled for a group's subgroups and projects.

| Value | Description |
|-------|-------------------------------------------------------------------------------------------------------------|
| `enabled`                      | Enables shared runners for all projects and subgroups in this group. |
| `disabled_and_overridable`     | Disables shared runners for all projects and subgroups in this group, but allows subgroups to override this setting. |
| `disabled_and_unoverridable`   | Disables shared runners for all projects and subgroups in this group, and prevents subgroups from overriding this setting. |
| `disabled_with_override`       | (Deprecated. Use `disabled_and_overridable`) Disables shared runners for all projects and subgroups in this group, but allows subgroups to override this setting. |

### Upload a group avatar

To upload an avatar file from your file system, use the `--form` argument. This causes
curl to post data using the header `Content-Type: multipart/form-data`. The
`file=` parameter must point to a file on your file system and be preceded by
`@`. For example:

```shell
curl --request PUT --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/groups/22" \
     --form "avatar=@/tmp/example.png"
```

### Remove a group avatar

> - [Introduced](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/96421) in GitLab 15.4.

To remove a group avatar, use a blank value for the `avatar` attribute.

Example request:

```shell
curl --request PUT --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/groups/22" \
     --data "avatar="
```

