## User creation

DETAILS:
**Tier:** Free, Premium, Ultimate
**Offering:** Self-managed, GitLab Dedicated

> - The `namespace_id` field in the response was [introduced](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/82045) in GitLab 14.10.
> - Ability to create an auditor user was [introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/366404) in GitLab 15.3.

Creates a new user. Note only administrators can create new
users. Either `password`, `reset_password`, or `force_random_password`
must be specified. If `reset_password` and `force_random_password` are
both `false`, then `password` is required.

`force_random_password` and `reset_password` take priority
over `password`. In addition, `reset_password` and
`force_random_password` can be used together.

NOTE:
`private_profile` defaults to the value of the
[Set profiles of new users to private by default](../administration/settings/account_and_limit_settings.md#set-profiles-of-new-users-to-private-by-default) setting.
`bio` defaults to `""` instead of `null`.

```plaintext
POST /users
```

Parameters:

| Attribute                            | Required | Description                                                                                                                                             |
| :----------------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `admin`                              | No       | User is an administrator. Valid values are `true` or `false`. Defaults to false. |
| `auditor`                            | No       | User is an auditor. Valid values are `true` or `false`. Defaults to false. [Introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/366404) in GitLab 15.3. Premium and Ultimate only.                                                                                       |
| `avatar`                             | No       | Image file for user's avatar                                                                                                                            |
| `bio`                                | No       | User's biography                                                                                                                                        |
| `can_create_group`                   | No       | User can create top-level groups - true or false                                                                                                                  |
| `color_scheme_id`                    | No       | User's color scheme for the file viewer (for more information, see the [user preference documentation](../user/profile/preferences.md#change-the-syntax-highlighting-theme)) |
| `commit_email`                       | No       | User's commit email address                                                                                                                        |
| `email`                              | Yes      | Email                                                                                                                                                   |
| `extern_uid`                         | No       | External UID                                                                                                                                            |
| `external`                           | No       | Flags the user as external - true or false (default)                                                                                                    |
| `extra_shared_runners_minutes_limit` | No       | Can be set by administrators only. Additional compute minutes for this user. Premium and Ultimate only.                                                                        |
| `force_random_password`              | No       | Set user password to a random value - true or false (default)                                                                                           |
| `group_id_for_saml`                  | No       | ID of group where SAML has been configured                                                                                                              |
| `linkedin`                           | No       | LinkedIn                                                                                                                                                |
| `location`                           | No       | User's location                                                                                                                                         |
| `name`                               | Yes      | Name                                                                                                                                                    |
| `note`                               | No       | Administrator notes for this user                                                                                                                               |
| `organization`                       | No       | Organization name                                                                                                                                       |
| `password`                           | No       | Password                                                                                                                                                |
| `private_profile`                    | No       | User's profile is private - true or false. The default value is determined by [this](../administration/settings/account_and_limit_settings.md#set-profiles-of-new-users-to-private-by-default) setting. |
| `projects_limit`                     | No       | Number of projects user can create                                                                                                                      |
| `pronouns`                           | No       | User's pronouns                                                                                                                                    |
| `provider`                           | No       | External provider name                                                                                                                                  |
| `public_email`                       | No       | User's public email address                                                                                                                        |
| `reset_password`                     | No       | Send user password reset link - true or false(default)                                                                                                  |
| `shared_runners_minutes_limit`       | No       | Can be set by administrators only. Maximum number of monthly compute minutes for this user. Can be `nil` (default; inherit system default), `0` (unlimited), or `> 0`. Premium and Ultimate only.                                                                                          |
| `skip_confirmation`                  | No       | Skip confirmation - true or false (default)                                                                                                             |
| `skype`                              | No       | Skype ID                                                                                                                                                |
| `theme_id`                           | No       | GitLab theme for the user (for more information, see the [user preference documentation](../user/profile/preferences.md#change-the-color-theme) for more information)                    |
| `twitter`                            | No       | X (formerly Twitter) account                                                                                                                                         |
| `discord`                            | No       | Discord account                                                                                                                                         |
| `username`                           | Yes      | Username                                                                                                                                                |
| `view_diffs_file_by_file`            | No       | Flag indicating the user sees only one file diff per page                                                                                               |
| `website_url`                        | No       | Website URL                                                                                                                                             |

