## Single user

Get a single user.

### For user

Prerequisites:

- You must be signed in to use this endpoint.

```plaintext
GET /users/:id
```

Parameters:

| Attribute | Type    | Required | Description      |
|-----------|---------|----------|------------------|
| `id`      | integer | yes      | ID of a user |

```json
{
  "id": 1,
  "username": "john_smith",
  "name": "John Smith",
  "state": "active",
  "locked": false,
  "avatar_url": "http://localhost:3000/uploads/user/avatar/1/cd8.jpeg",
  "web_url": "http://localhost:3000/john_smith",
  "created_at": "2012-05-23T08:00:58Z",
  "bio": "",
  "bot": false,
  "location": null,
  "public_email": "john@example.com",
  "skype": "",
  "linkedin": "",
  "twitter": "",
  "discord": "",
  "website_url": "",
  "organization": "",
  "job_title": "Operations Specialist",
  "pronouns": "he/him",
  "work_information": null,
  "followers": 1,
  "following": 1,
  "local_time": "3:38 PM",
  "is_followed": false
}
```

### For administrators

DETAILS:
**Tier:** Free, Premium, Ultimate
**Offering:** Self-managed, GitLab Dedicated

> - The `namespace_id` field in the response was [introduced](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/82045) in GitLab 14.10.
> - The `created_by` field in the response was [introduced](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/93092) in GitLab 15.6.
> - The `email_reset_offered_at` field in the response [introduced](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/137610) in GitLab 16.7.

```plaintext
GET /users/:id
```

Parameters:

| Attribute | Type    | Required | Description      |
|-----------|---------|----------|------------------|
| `id`      | integer | yes      | ID of a user |

Example Responses:

```json
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
  "public_email": "john@example.com",
  "skype": "",
  "linkedin": "",
  "twitter": "",
  "discord": "",
  "website_url": "",
  "organization": "",
  "job_title": "Operations Specialist",
  "pronouns": "he/him",
  "work_information": null,
  "followers": 1,
  "following": 1,
  "local_time": "3:38 PM",
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
  "commit_email": "john-codes@example.com",
  "current_sign_in_ip": "196.165.1.102",
  "last_sign_in_ip": "172.127.2.22",
  "plan": "gold",
  "trial": true,
  "sign_in_count": 1337,
  "namespace_id": 1,
  "created_by": null,
  "email_reset_offered_at": null
}
```

NOTE:
The `plan` and `trial` parameters are only available on GitLab Enterprise Edition.

Users on [GitLab Premium or Ultimate](https://about.gitlab.com/pricing/) also see
the `shared_runners_minutes_limit`, `is_auditor`, and `extra_shared_runners_minutes_limit` parameters.

```json
{
  "id": 1,
  "username": "john_smith",
  "is_auditor": false,
  "shared_runners_minutes_limit": 133,
  "extra_shared_runners_minutes_limit": 133,
  ...
}
```

Users on [GitLab.com Premium or Ultimate](https://about.gitlab.com/pricing/) also
see the `group_saml` option and `provisioned_by_group_id` parameter:

```json
{
  "id": 1,
  "username": "john_smith",
  "shared_runners_minutes_limit": 133,
  "extra_shared_runners_minutes_limit": 133,
  "identities": [
    {"provider": "github", "extern_uid": "2435223452345"},
    {"provider": "bitbucket", "extern_uid": "john.smith"},
    {"provider": "google_oauth2", "extern_uid": "8776128412476123468721346"},
    {"provider": "group_saml", "extern_uid": "123789", "saml_provider_id": 10}
  ],
  "provisioned_by_group_id": 123789
  ...
}
```

Users on [GitLab.com Premium or Ultimate](https://about.gitlab.com/pricing/) also
see the `scim_identities` parameter:

```json
{
  ...
  "extra_shared_runners_minutes_limit": null,
  "scim_identities": [
      {"extern_uid": "2435223452345", "group_id": "3", "active": true},
      {"extern_uid": "john.smith", "group_id": "42", "active": false}
    ]
  ...
}
```

Administrators can use the `created_by` parameter to see if a user account was created:

- [Manually by an administrator](../user/profile/account/create_accounts.md#create-users-in-admin-area).
- As a [project bot user](../user/project/settings/project_access_tokens.md#bot-users-for-projects).

If the returned value is `null`, the account was created by a user who registered an account themselves.

You can include the user's [custom attributes](custom_attributes.md) in the response with:

```plaintext
GET /users/:id?with_custom_attributes=true
```

