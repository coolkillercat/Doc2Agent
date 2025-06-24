## Get a member of a group or project, including inherited and invited members

> - [Introduced](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/17744) in GitLab 12.4.
> - [Changed](https://gitlab.com/gitlab-org/gitlab/-/issues/219230) to return members of the invited private group if the current user is a member of the shared group or project in GitLab 16.10 [with a flag](../administration/feature_flags.md) named `webui_members_inherited_users`. Disabled by default.
> - [Enabled on GitLab.com and self-managed](https://gitlab.com/gitlab-org/gitlab/-/issues/219230) in GitLab 17.0.

FLAG:
On self-managed GitLab, by default this feature is available. To hide the feature per user, an administrator can [disable the feature flag](../administration/feature_flags.md) named `webui_members_inherited_users`.
On GitLab.com and GitLab Dedicated, this feature is available.

Gets a member of a group or project, including members inherited or invited through ancestor groups. See the corresponding [endpoint to list all inherited members](#list-all-members-of-a-group-or-project-including-inherited-and-invited-members) for details.

NOTE:
The invited group members have shared membership in the shared group or project.
This means that if the requester is a member of a shared group or project, but not a member of an invited private group,
then using this endpoint the requester can get all the shared group or project members, including the invited private group members.

```plaintext
GET /groups/:id/members/all/:user_id
GET /projects/:id/members/all/:user_id
```

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `id`      | integer/string | yes | The ID or [URL-encoded path of the project or group](rest/index.md#namespaced-path-encoding) owned by the authenticated user |
| `user_id` | integer | yes   | The user ID of the member |

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/groups/:id/members/all/:user_id"
curl --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/projects/:id/members/all/:user_id"
```

Example response:

```json
{
  "id": 1,
  "username": "raymond_smith",
  "name": "Raymond Smith",
  "state": "active",
  "avatar_url": "https://www.gravatar.com/avatar/c2525a7f58ae3776070e44c106c48e15?s=80&d=identicon",
  "web_url": "http://192.168.1.8:3000/root",
  "access_level": 30,
  "created_at": "2012-10-22T14:13:35Z",
  "created_by": {
    "id": 2,
    "username": "john_doe",
    "name": "John Doe",
    "state": "active",
    "avatar_url": "https://www.gravatar.com/avatar/c2525a7f58ae3776070e44c106c48e15?s=80&d=identicon",
    "web_url": "http://192.168.1.8:3000/root"
  },
  "email": "john@example.com",
  "expires_at": null,
  "group_saml_identity": null
}
```

