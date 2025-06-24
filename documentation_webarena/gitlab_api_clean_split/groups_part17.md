## List provisioned users

DETAILS:
**Tier:** Premium, Ultimate
**Offering:** GitLab.com, Self-managed, GitLab Dedicated

Get a list of users provisioned by a given group. Does not include subgroups.

Requires at least the Maintainer role on the group.

```plaintext
GET /groups/:id/provisioned_users
```

Parameters:

| Attribute        | Type           | Required | Description                                                              |
|:-----------------|:---------------|:---------|:-------------------------------------------------------------------------|
| `id`             | integer/string | yes      | ID or [URL-encoded path of the group](rest/index.md#namespaced-path-encoding) |
| `username`       | string         | no       | Return single user with a specific username                              |
| `search`         | string         | no       | Search users by name, email, username                                    |
| `active`         | boolean        | no       | Return only active users                                                 |
| `blocked`        | boolean        | no       | Return only blocked users                                                |
| `created_after`  | datetime       | no       | Return users created after the specified time                            |
| `created_before` | datetime       | no       | Return users created before the specified time                           |

Example response:

```json
[
  {
    "id": 66,
    "username": "user22",
    "name": "John Doe22",
    "state": "active",
    "avatar_url": "https://www.gravatar.com/avatar/xxx?s=80&d=identicon",
    "web_url": "http://my.gitlab.com/user22",
    "created_at": "2021-09-10T12:48:22.381Z",
    "bio": "",
    "location": null,
    "public_email": "",
    "skype": "",
    "linkedin": "",
    "twitter": "",
    "website_url": "",
    "organization": null,
    "job_title": "",
    "pronouns": null,
    "bot": false,
    "work_information": null,
    "followers": 0,
    "following": 0,
    "local_time": null,
    "last_sign_in_at": null,
    "confirmed_at": "2021-09-10T12:48:22.330Z",
    "last_activity_on": null,
    "email": "user22@example.org",
    "theme_id": 1,
    "color_scheme_id": 1,
    "projects_limit": 100000,
    "current_sign_in_at": null,
    "identities": [ ],
    "can_create_group": true,
    "can_create_project": true,
    "two_factor_enabled": false,
    "external": false,
    "private_profile": false,
    "commit_email": "user22@example.org",
    "shared_runners_minutes_limit": null,
    "extra_shared_runners_minutes_limit": null
  },
  ...
]
```

