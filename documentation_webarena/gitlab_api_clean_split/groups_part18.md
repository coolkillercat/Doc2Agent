## List group users

DETAILS:
**Tier:** Premium, Ultimate
**Offering:** GitLab.com, Self-managed, GitLab Dedicated
**Status:** Experiment

> - [Introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/424505) in GitLab 16.6. This feature is an [Experiment](../policy/experiment-beta-support.md).

Get a list of users for a group. This endpoint returns users that are related to a top-level group regardless
of their current membership. For example, users that have a SAML identity connected to the group, or service accounts created
by the group or subgroups.

This endpoint is an [Experiment](../policy/experiment-beta-support.md) and might be changed or removed without notice.

Requires Owner role in the group.

```plaintext
GET /groups/:id/users
```

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/groups/345/users?include_saml_users=true&include_service_accounts=true"
```

Parameters:

| Attribute                  | Type           | Required                  | Description                                                                    |
|:---------------------------|:---------------|:--------------------------|:-------------------------------------------------------------------------------|
| `id`                       | integer/string | yes                       | ID or [URL-encoded path of the group](rest/index.md#namespaced-path-encoding). |
| `include_saml_users`       | boolean        | yes (see description)  | Include users with a SAML identity. Either this value or `include_service_accounts` must be `true`. |
| `include_service_accounts` | boolean        | yes (see description)  | Include service account users. Either this value or `include_saml_users` must be `true`. |
| `search`                   | string         | no                        | Search users by name, email, username.                                         |

If successful, returns [`200 OK`](../api/rest/index.md#status-codes) and the
following response attributes:

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

