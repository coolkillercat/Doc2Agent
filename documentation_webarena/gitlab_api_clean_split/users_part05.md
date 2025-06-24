## User modification

DETAILS:
**Tier:** Free, Premium, Ultimate
**Offering:** Self-managed, GitLab Dedicated

> - The `namespace_id` field in the response was [introduced](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/82045) in GitLab 14.10.
> - Ability to modify an auditor user was [introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/366404) in GitLab 15.3.

Modifies an existing user. Only administrators can change attributes of a user.

The `email` field is the user's primary email address. You can only change this field to an already-added secondary email address for that user. To add more email addresses to the same user, use the [add email function](#add-email).

```plaintext
PUT /users/:id
```

Parameters:

| Attribute                            | Required | Description                                                                                                                                             |
| :----------------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `admin`                              | No       |User is an administrator. Valid values are `true` or `false`. Defaults to false. |
| `auditor`                            | No       |  User is an auditor. Valid values are `true` or `false`. Defaults to false. [Introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/366404) in GitLab 15.3.(default) Premium and Ultimate only.                                                                                                          |
| `avatar`                             | No       | Image file for user's avatar                                                                                                                            |
| `bio`                                | No       | User's biography                                                                                                                                        |
| `can_create_group`                   | No       | User can create groups - true or false                                                                                                                  |
| `color_scheme_id`                    | No       | User's color scheme for the file viewer (for more information, see the [user preference documentation](../user/profile/preferences.md#change-the-syntax-highlighting-theme) for more information) |
| `commit_email`                       | No       | User's commit email. Set to `_private` to use the private commit email. [Introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/375148) in GitLab 15.5. |
| `email`                              | No       | Email                                                                                                                                                   |
| `extern_uid`                         | No       | External UID                                                                                                                                            |
| `external`                           | No       | Flags the user as external - true or false (default)                                                                                                    |
| `extra_shared_runners_minutes_limit` | No       | Can be set by administrators only. Additional compute minutes for this user. Premium and Ultimate only.                                                                                                 |
| `group_id_for_saml`                  | No       | ID of group where SAML has been configured                                                                                                              |
| `id`                                 | Yes      | ID of the user                                                                                                                                      |
| `linkedin`                           | No       | LinkedIn                                                                                                                                                |
| `location`                           | No       | User's location                                                                                                                                         |
| `name`                               | No       | Name                                                                                                                                                    |
| `note`                               | No       | Administration notes for this user                                                                                                                               |
| `organization`                       | No       | Organization name                                                                                                                                       |
| `password`                           | No       | Password                                                                                                                                                |
| `private_profile`                    | No       | User's profile is private - true or false.                                                                 |
| `projects_limit`                     | No       | Limit projects each user can create                                                                                                                     |
| `pronouns`                           | No       | Pronouns                                                                                                                                                |
| `provider`                           | No       | External provider name                                                                                                                                  |
| `public_email`                       | No       | Public email of the user (must be already verified)                                                                                                                            |
| `shared_runners_minutes_limit`       | No       | Can be set by administrators only. Maximum number of monthly compute minutes for this user. Can be `nil` (default; inherit system default), `0` (unlimited) or `> 0`. Premium and Ultimate only.                                                                                                     |
| `skip_reconfirmation`                | No       | Skip reconfirmation - true or false (default)                                                                                                           |
| `skype`                              | No       | Skype ID                                                                                                                                                |
| `theme_id`                           | No       | GitLab theme for the user (for more information, see the [user preference documentation](../user/profile/preferences.md#change-the-color-theme) for more information)                    |
| `twitter`                            | No       | X (formerly Twitter) account                                                                                                                                         |
| `discord`                            | No       | Discord account                                                                                                                                         |
| `username`                           | No       | Username                                                                                                                                                |
| `view_diffs_file_by_file`            | No       | Flag indicating the user sees only one file diff per page                                                                                               |
| `website_url`                        | No       | Website URL                                                                                                                                             |

On password update, the user is forced to change it upon next login.
Note, at the moment this method does only return a `404` error,
even in cases where a `409` (Conflict) would be more appropriate.
For example, when renaming the email address to some existing one.

