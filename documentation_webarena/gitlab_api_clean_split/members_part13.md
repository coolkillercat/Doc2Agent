## Add a member to a group or project

Adds a member to a group or project.

```plaintext
POST /groups/:id/members
POST /projects/:id/members
```

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `id`      | integer/string | yes | The ID or [URL-encoded path of the project or group](rest/index.md#namespaced-path-encoding) owned by the authenticated user |
| `user_id` | integer/string | yes | The user ID of the new member or multiple IDs separated by commas |
| `access_level` | integer | yes | [A valid access level](access_requests.md#valid-access-levels) |
| `expires_at` | string | no | A date string in the format `YEAR-MONTH-DAY` |
| `invite_source` | string | no | The source of the invitation that starts the member creation process. GitLab team members can view more information in this confidential issue: `https://gitlab.com/gitlab-org/gitlab/-/issues/327120>`. |
| `member_role_id` | integer | no | The ID of a member role. Ultimate only. |

```shell
curl --request POST --header "PRIVATE-TOKEN: <your_access_token>" \
     --data "user_id=1&access_level=30" "https://gitlab.example.com/api/v4/groups/:id/members"
curl --request POST --header "PRIVATE-TOKEN: <your_access_token>" \
     --data "user_id=1&access_level=30" "https://gitlab.example.com/api/v4/projects/:id/members"
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
  "created_at": "2012-10-22T14:13:35Z",
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
  "email": "john@example.com",
  "group_saml_identity": null
}
```

