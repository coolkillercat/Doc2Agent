## List users

Get a list of users.

This function takes pagination parameters `page` and `per_page` to restrict the list of users.

### For non-administrator users

```plaintext
GET /users
```

| Attribute          | Type    | Required | Description                                                                                                            |
| ------------------ | ------- | -------- | ---------------------------------------------------------------------------------------------------------------------- |
| `username`         | string  | no       | Get a single user with a specific username.                                                                            |
| `search`           | string  | no       | Search for a username.                                                                                                |
| `active`           | boolean | no       | Filters only active users. Default is `false`.                                                                         |
| `external`         | boolean | no       | Filters only external users. Default is `false`.                                                                       |
| `exclude_external` | boolean | no       | Filters only non external users. Default is `false`.                                                                   |
| `blocked`          | boolean | no       | Filters only blocked users. Default is `false`.                                                                        |
| `created_after`    | DateTime| no       | Returns users created after specified time.                                                                            |
| `created_before`   | DateTime| no       | Returns users created before specified time.                                                                           |
| `exclude_internal` | boolean | no       | Filters only non internal users. Default is `false`.                                                                   |
| `without_project_bots`| boolean | no       | Filters user without project bots. Default is `false`.                                                             |

```json
[
  {
    "id": 1,
    "username": "john_smith",
    "name": "John Smith",
    "state": "active",
    "locked": false,
    "avatar_url": "http://localhost:3000/uploads/user/avatar/1/cd8.jpeg",
    "web_url": "http://localhost:3000/john_smith"
  },
  {
    "id": 2,
    "username": "jack_smith",
    "name": "Jack Smith",
    "state": "blocked",
    "locked": false,
    "avatar_url": "http://gravatar.com/../e32131cd8.jpeg",
    "web_url": "http://localhost:3000/jack_smith"
  }
]
```

This endpoint supports [keyset pagination](rest/index.md#keyset-based-pagination). Keyset pagination [introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/419556) in GitLab 16.5.

You can also use `?search=` to search for users by name, username, or public email. For example, `/users?search=John`. When you search for a:

- Public email, you must use the full email address to get an exact match. A search might return a partial match. For example, if you search for the email `on@example.com`, the search can return both `on@example.com` and `jon@example.com`.
- Name or username, you do not have to get an exact match because this is a fuzzy search.

In addition, you can lookup users by username:

```plaintext
GET /users?username=:username
```

For example:

```plaintext
GET /users?username=jack_smith
```

NOTE:
Username search is case insensitive.

In addition, you can filter users based on the states `blocked` and `active`.
It does not support `active=false` or `blocked=false`.

```plaintext
GET /users?active=true
```

```plaintext
GET /users?blocked=true
```

In addition, you can search for external users only with `external=true`.
It does not support `external=false`.

```plaintext
GET /users?external=true
```

GitLab supports bot users such as the [alert bot](../operations/incident_management/integrations.md)
or the [support bot](../user/project/service_desk/configure.md#support-bot-user).
You can exclude the following types of [internal users](../development/internal_users.md#internal-users)
from the users' list with the `exclude_internal=true` parameter:

- Alert bot
- Support bot

However, this action does not exclude [bot users for projects](../user/project/settings/project_access_tokens.md#bot-users-for-projects)
or [bot users for groups](../user/group/settings/group_access_tokens.md#bot-users-for-groups).

```plaintext
GET /users?exclude_internal=true
```

In addition, to exclude external users from the users' list, you can use the parameter `exclude_external=true`.

```plaintext
GET /users?exclude_external=true
```

To exclude [bot users for projects](../user/project/settings/project_access_tokens.md#bot-users-for-projects)
and [bot users for groups](../user/group/settings/group_access_tokens.md#bot-users-for-groups), you can use the
parameter `without_project_bots=true`.

```plaintext
GET /users?without_project_bots=true
```

### For administrators

DETAILS:
**Tier:** Free, Premium, Ultimate
**Offering:** Self-managed, GitLab Dedicated

> - The `created_by` field in the response was [introduced](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/93092) in GitLab 15.6.
> - The `scim_identities` field in the response [introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/324247) in GitLab 16.1.
> - The `auditors` field in the response [introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/418023) in GitLab 16.2.
> - The `email_reset_offered_at` field in the response [introduced](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/137610) in GitLab 16.7.

```plaintext
GET /users
```

You can use all [parameters available for everyone](#for-non-administrator-users) plus these additional parameters available only for administrators.

| Attribute          | Type    | Required | Description                                                                                                           |
| ------------------ | ------- | -------- | --------------------------------------------------------------------------------------------------------------------- |
| `extern_uid`       | string  | no       | Get a single user with a specific external authentication provider UID.                                                |
| `provider`         | string  | no       | The external provider.                                                                                                 |
| `order_by`         | string  | no       | Return users ordered by `id`, `name`, `username`, `created_at`, or `updated_at` fields. Default is `id`               |
| `sort`             | string  | no       | Return users sorted in `asc` or `desc` order. Default is `desc`                                                       |
| `two_factor`       | string  | no       | Filter users by Two-factor authentication. Filter values are `enabled` or `disabled`. By default it returns all users |
| `without_projects` | boolean | no       | Filter users without projects. Default is `false`, which means that all users are returned, with and without projects. |
| `admins`           | boolean | no       | Return only administrators. Default is `false`                                 |
| `auditors`         | boolean | no       | Return only auditor users. Default is `false`. If not included, it returns all users. Premium and Ultimate only. |
| `saml_provider_id` | number | no     | Return only users created by the specified SAML provider ID. If not included, it returns all users. Premium and Ultimate only. |
| `skip_ldap`        | boolean | no     | Skip LDAP users. Premium and Ultimate only. |

```json
[
  {
    "id": 1,
    "username": "john_smith",
    "email": "john@example.com",
    "name": "John Smith",
    "state": "active",
    "locked": false,
    "avatar_url": "http://localhost:3000/uploads/user/avatar/1/index.jpg",
    "web_url": "http://localhost:3000/john_smith",
    "created_at": "2012-05-23T08:00:58Z",
    "is_admin": false,
    "bio": "",
    "location": null,
    "skype": "",
    "linkedin": "",
    "twitter": "",
    "discord": "",
    "website_url": "",
    "organization": "",
    "job_title": "",
    "last_sign_in_at": "2012-06-01T11:41:01Z",
    "confirmed_at": "2012-05-23T09:05:22Z",
    "theme_id": 1,
    "last_activity_on": "2012-05-23",
    "color_scheme_id": 2,
    "projects_limit": 100,
    "current_sign_in_at": "2012-06-02T06:36:55Z",
    "note": "DMCA Request: 2018-11-05 | DMCA Violation | Abuse | https://gitlab.zendesk.com/agent/tickets/123",
    "identities": [
      {"provider": "github", "extern_uid": "2435223452345"},
      {"provider": "bitbucket", "extern_uid": "john.smith"},
      {"provider": "google_oauth2", "extern_uid": "8776128412476123468721346"}
    ],
    "can_create_group": true,
    "can_create_project": true,
    "two_factor_enabled": true,
    "external": false,
    "private_profile": false,
    "current_sign_in_ip": "196.165.1.102",
    "last_sign_in_ip": "172.127.2.22",
    "namespace_id": 1,
    "created_by": null,
    "email_reset_offered_at": null
  },
  {
    "id": 2,
    "username": "jack_smith",
    "email": "jack@example.com",
    "name": "Jack Smith",
    "state": "blocked",
    "locked": false,
    "avatar_url": "http://localhost:3000/uploads/user/avatar/2/index.jpg",
    "web_url": "http://localhost:3000/jack_smith",
    "created_at": "2012-05-23T08:01:01Z",
    "is_admin": false,
    "bio": "",
    "location": null,
    "skype": "",
    "linkedin": "",
    "twitter": "",
    "discord": "",
    "website_url": "",
    "organization": "",
    "job_title": "",
    "last_sign_in_at": null,
    "confirmed_at": "2012-05-30T16:53:06.148Z",
    "theme_id": 1,
    "last_activity_on": "2012-05-23",
    "color_scheme_id": 3,
    "projects_limit": 100,
    "current_sign_in_at": "2014-03-19T17:54:13Z",
    "identities": [],
    "can_create_group": true,
    "can_create_project": true,
    "two_factor_enabled": true,
    "external": false,
    "private_profile": false,
    "current_sign_in_ip": "10.165.1.102",
    "last_sign_in_ip": "172.127.2.22",
    "namespace_id": 2,
    "created_by": null,
    "email_reset_offered_at": null
  }
]
```

Users on [GitLab Premium or Ultimate](https://about.gitlab.com/pricing/) also see the `shared_runners_minutes_limit`, `extra_shared_runners_minutes_limit`, `is_auditor`, and `using_license_seat` parameters.

```json
[
  {
    "id": 1,
    ...
    "shared_runners_minutes_limit": 133,
    "extra_shared_runners_minutes_limit": 133,
    "is_auditor": false,
    "using_license_seat": true
    ...
  }
]
```

Users on [GitLab Premium or Ultimate](https://about.gitlab.com/pricing/) also see
the `group_saml` provider option and `provisioned_by_group_id` parameter:

```json
[
  {
    "id": 1,
    ...
    "identities": [
      {"provider": "github", "extern_uid": "2435223452345"},
      {"provider": "bitbucket", "extern_uid": "john.smith"},
      {"provider": "google_oauth2", "extern_uid": "8776128412476123468721346"},
      {"provider": "group_saml", "extern_uid": "123789", "saml_provider_id": 10}
    ],
    "provisioned_by_group_id": 123789
    ...
  }
]
```

You can also use `?search=` to search for users by name, username, or email. For example, `/users?search=John`. When you search for a:

- Email, you must use the full email address to get an exact match. As an administrator, you can search for both public and private email addresses.
- Name or username, you do not have to get an exact match because this is a fuzzy search.

You can lookup users by external UID and provider:

```plaintext
GET /users?extern_uid=:extern_uid&provider=:provider
```

For example:

```plaintext
GET /users?extern_uid=1234567&provider=github
```

Users on [GitLab Premium or Ultimate](https://about.gitlab.com/pricing/) have the `scim` provider available:

```plaintext
GET /users?extern_uid=1234567&provider=scim
```

You can search users by creation date time range with:

```plaintext
GET /users?created_before=2001-01-02T00:00:00.060Z&created_after=1999-01-02T00:00:00.060
```

You can search for users without projects with: `/users?without_projects=true`

You can filter by [custom attributes](custom_attributes.md) with:

```plaintext
GET /users?custom_attributes[key]=value&custom_attributes[other_key]=other_value
```

You can include the users' [custom attributes](custom_attributes.md) in the response with:

```plaintext
GET /users?with_custom_attributes=true
```

You can use the `created_by` parameter to see if a user account was created:

- [Manually by an administrator](../user/profile/account/create_accounts.md#create-users-in-admin-area).
- As a [project bot user](../user/project/settings/project_access_tokens.md#bot-users-for-projects).

If the returned value is `null`, the account was created by a user who registered an account themselves.

