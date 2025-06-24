## List all members of a group or project including inherited and invited members

> - [Changed](https://gitlab.com/gitlab-org/gitlab/-/issues/219230) to return members of the invited private group if the current user is a member of the shared group or project in GitLab 16.10 [with a flag](../administration/feature_flags.md) named `webui_members_inherited_users`. Disabled by default.
> - Feature flag `webui_members_inherited_users` was [enabled on GitLab.com and self-managed](https://gitlab.com/gitlab-org/gitlab/-/issues/219230) in GitLab 17.0.

FLAG:
On self-managed GitLab, by default this feature is available. To hide the feature per user, an administrator can [disable the feature flag](../administration/feature_flags.md) named `webui_members_inherited_users`.
On GitLab.com and GitLab Dedicated, this feature is available.

Gets a list of group or project members viewable by the authenticated user, including inherited members, invited users, and permissions through ancestor groups.

If a user is a member of this group or project and also of one or more ancestor groups,
only its membership with the highest `access_level` is returned.
This represents the effective permission of the user.

Members from an invited group are returned if either:

- The invited group is public.
- The requester is also a member of the invited group.
- The requester is a member of the shared group or project.

NOTE:
The invited group members have shared membership in the shared group or project.
This means that if the requester is a member of a shared group or project, but not a member of an invited private group,
then using this endpoint the requester can get all the shared group or project members, including the invited private group members.

This function takes pagination parameters `page` and `per_page` to restrict the list of users.

```plaintext
GET /groups/:id/members/all
GET /projects/:id/members/all
```

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `id`      | integer/string | yes | The ID or [URL-encoded path of the project or group](rest/index.md#namespaced-path-encoding) owned by the authenticated user. |
| `query`   | string | no     | A query string to search for members. |
| `user_ids`   | array of integers | no     | Filter the results on the given user IDs. |
| `show_seat_info`   | boolean | no     | Show seat information for users. |
| `state`   | string | no | Filter results by member state, one of `awaiting` or `active`. Premium and Ultimate only. |

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/groups/:id/members/all"
curl --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/projects/:id/members/all"
```

Example response:

```json
[
  {
    "id": 1,
    "username": "raymond_smith",
    "name": "Raymond Smith",
    "state": "active",
    "avatar_url": "https://www.gravatar.com/avatar/c2525a7f58ae3776070e44c106c48e15?s=80&d=identicon",
    "web_url": "http://192.168.1.8:3000/root",
    "created_at": "2012-09-22T14:13:35Z",
    "created_by": {
      "id": 2,
      "username": "john_doe",
      "name": "John Doe",
      "state": "active",
      "avatar_url": "https://www.gravatar.com/avatar/c2525a7f58ae3776070e44c106c48e15?s=80&d=identicon",
      "web_url": "http://192.168.1.8:3000/root"
    },
    "expires_at": "2012-10-22T14:13:35Z",
    "access_level": 30,
    "group_saml_identity": null
  },
  {
    "id": 2,
    "username": "john_doe",
    "name": "John Doe",
    "state": "active",
    "avatar_url": "https://www.gravatar.com/avatar/c2525a7f58ae3776070e44c106c48e15?s=80&d=identicon",
    "web_url": "http://192.168.1.8:3000/root",
    "created_at": "2012-09-22T14:13:35Z",
    "created_by": {
      "id": 1,
      "username": "raymond_smith",
      "name": "Raymond Smith",
      "state": "active",
      "avatar_url": "https://www.gravatar.com/avatar/c2525a7f58ae3776070e44c106c48e15?s=80&d=identicon",
      "web_url": "http://192.168.1.8:3000/root"
    },
    "expires_at": "2012-10-22T14:13:35Z",
    "access_level": 30,
    "email": "john@example.com",
    "group_saml_identity": {
      "extern_uid":"ABC-1234567890",
      "provider": "group_saml",
      "saml_provider_id": 10
    }
  },
  {
    "id": 3,
    "username": "foo_bar",
    "name": "Foo bar",
    "state": "active",
    "avatar_url": "https://www.gravatar.com/avatar/c2525a7f58ae3776070e44c106c48e15?s=80&d=identicon",
    "web_url": "http://192.168.1.8:3000/root",
    "created_at": "2012-10-22T14:13:35Z",
    "created_by": {
      "id": 2,
      "username": "john_doe",
      "name": "John Doe",
      "state": "active",
      "avatar_url": "https://www.gravatar.com/avatar/c2525a7f58ae3776070e44c106c48e15?s=80&d=identicon",
      "web_url": "http://192.168.1.8:3000/root"
    },
    "expires_at": "2012-11-22T14:13:35Z",
    "access_level": 30,
    "group_saml_identity": null
  }
]
```

