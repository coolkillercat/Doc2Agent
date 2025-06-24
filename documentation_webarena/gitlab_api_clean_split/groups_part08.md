## New group

NOTE:
On GitLab SaaS, you must use the GitLab UI to create groups without a parent group. You cannot
use the API to do this.

Creates a new project group. Available only for users who can create groups.

```plaintext
POST /groups
```

Parameters:

| Attribute                                               | Type    | Required | Description                                                                                                                                                                                     |
| ------------------------------------------------------- | ------- | -------- |-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name`                                                  | string  | yes      | The name of the group.                                                                                                                                                                          |
| `path`                                                  | string  | yes      | The path of the group.                                                                                                                                                                          |
| `auto_devops_enabled`                                   | boolean | no       | Default to Auto DevOps pipeline for all projects within this group.                                                                                                                             |
| `avatar`                                                | mixed   | no       | Image file for avatar of the group.                                                                                                                                                             |
| `default_branch`                                        | string  | no       | The [default branch](../user/project/repository/branches/default.md) name for group's projects. [Introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/442298) in GitLab 16.11.             |
| `default_branch_protection`                             | integer | no       | [Deprecated](https://gitlab.com/gitlab-org/gitlab/-/issues/408314) in GitLab 17.0. Use `default_branch_protection_defaults` instead.             |
| `default_branch_protection_defaults`                    | hash    | no       | See [Options for `default_branch_protection_defaults`](#options-for-default_branch_protection_defaults).                                                                                        |
| `description`                                           | string  | no       | The group's description.                                                                                                                                                                        |
| `enabled_git_access_protocol`                           | string  | no       | Enabled protocols for Git access. Allowed values are: `ssh`, `http`, and `all` to allow both protocols. [Introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/436618) in GitLab 16.9. |
| `emails_disabled`                                       | boolean | no       | _([Deprecated](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/127899) in GitLab 16.5.)_ Disable email notifications. Use `emails_enabled` instead.                                       |
| `emails_enabled`                                        | boolean | no       | Enable email notifications.                                                                                                                                                                     |
| `lfs_enabled`                                           | boolean | no       | Enable/disable Large File Storage (LFS) for the projects in this group.                                                                                                                         |
| `mentions_disabled`                                     | boolean | no       | Disable the capability of a group from getting mentioned.                                                                                                                                       |
| `organization_id`                                       | integer | no       | The organization ID for the group.                                                                                                                                                              |
| `parent_id`                                             | integer | no       | The parent group ID for creating nested group.                                                                                                                                                  |
| `project_creation_level`                                | string  | no       | Determine if developers can create projects in the group. Can be `noone` (No one), `maintainer` (users with the Maintainer role), or `developer` (users with the Developer or Maintainer role). |
| `request_access_enabled`                                | boolean | no       | Allow users to request member access.                                                                                                                                                           |
| `require_two_factor_authentication`                     | boolean | no       | Require all users in this group to set up two-factor authentication.                                                                                                                            |
| `share_with_group_lock`                                 | boolean | no       | Prevent sharing a project with another group within this group.                                                                                                                                 |
| `subgroup_creation_level`                               | string  | no       | Allowed to [create subgroups](../user/group/subgroups/index.md#create-a-subgroup). Can be `owner` (Owners), or `maintainer` (users with the Maintainer role).                                   |
| `two_factor_grace_period`                               | integer | no       | Time before Two-factor authentication is enforced (in hours).                                                                                                                                   |
| `visibility`                                            | string  | no       | The group's visibility. Can be `private`, `internal`, or `public`.                                                                                                                              |
| `membership_lock`                                       | boolean | no       | Users cannot be added to projects in this group. Premium and Ultimate only.                                                                                              |
| `extra_shared_runners_minutes_limit`                    | integer | no       | Can be set by administrators only. Additional compute minutes for this group. Self-managed, Premium and Ultimate only.                                                                  |
| `shared_runners_minutes_limit`                          | integer | no       | Can be set by administrators only. Maximum number of monthly compute minutes for this group. Can be `nil` (default; inherit system default), `0` (unlimited), or `> 0`. Self-managed, Premium and Ultimate only.            |
| `wiki_access_level`                                     | string  | no       | The wiki access level. Can be `disabled`, `private`, or `enabled`. Premium and Ultimate only.                                                                       |

### Options for `default_branch_protection`

The `default_branch_protection` attribute determines whether users with the Developer or Maintainer role can push to the applicable [default branch](../user/project/repository/branches/default.md), as described in the following table:

| Value | Description |
|-------|-------------------------------------------------------------------------------------------------------------|
| `0`   | No protection. Users with the Developer or Maintainer role can:  <br>- Push new commits<br>- Force push changes<br>- Delete the branch |
| `1`   | Partial protection. Users with the Developer or Maintainer role can:  <br>- Push new commits |
| `2`   | Full protection. Only users with the Maintainer role can:  <br>- Push new commits |
| `3`   | Protected against pushes. Users with the Maintainer role can: <br>- Push new commits<br>- Force push changes<br>- Accept merge requests<br>Users with the Developer role can:<br>- Accept merge requests|
| `4`   | Full protection after initial push. User with the Developer role can: <br>- Push commit to empty repository.<br> Users with the Maintainer role can: <br>- Push new commits<br>- Accept merge requests|

### Options for `default_branch_protection_defaults`

The `default_branch_protection_defaults` attribute describes the default branch
protection defaults. All parameters are optional.

| Key                          | Type    | Description                                                                             |
|------------------------------|---------|-----------------------------------------------------------------------------------------|
| `allowed_to_push`            | array   | An array of access levels allowed to push. Supports Developer (30) or Maintainer (40).  |
| `allow_force_push`           | boolean | Allow force push for all users with push access.                                        |
| `allowed_to_merge`           | array   | An array of access levels allowed to merge. Supports Developer (30) or Maintainer (40). |
| `developer_can_initial_push` | boolean | Allow developers to initial push.                                                       |

