## Edit a member of a group or project

Updates a member of a group or project.

```plaintext
PUT /groups/:id/members/:user_id
PUT /projects/:id/members/:user_id
```

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `id`      | integer/string | yes | The ID or [URL-encoded path of the project or group](rest/index.md#namespaced-path-encoding) owned by the authenticated user |
| `user_id` | integer | yes   | The user ID of the member |
| `access_level` | integer | yes | A [valid access level](access_requests.md#valid-access-levels) |
| `expires_at` | string | no | A date string in the format `YEAR-MONTH-DAY` |
| `member_role_id` | integer | no | The ID of a member role. Ultimate only. |

```shell
curl --request PUT --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/groups/:id/members/:user_id?access_level=40"
curl --request PUT --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/projects/:id/members/:user_id?access_level=40"
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
  "access_level": 40,
  "email": "john@example.com",
  "group_saml_identity": null
}
```

### Set override flag for a member of a group

By default, the access level of LDAP group members is set to the value specified
by LDAP through Group Sync. You can allow access level overrides by calling this endpoint.

```plaintext
POST /groups/:id/members/:user_id/override
```

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `id`      | integer/string | yes | The ID or [URL-encoded path of the group](rest/index.md#namespaced-path-encoding) owned by the authenticated user |
| `user_id` | integer | yes   | The user ID of the member |

```shell
curl --request POST --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/groups/:id/members/:user_id/override"
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
  "access_level": 40,
  "email": "john@example.com",
  "override": true
}
```

### Remove override for a member of a group

Sets the override flag to false and allows LDAP Group Sync to reset the access
level to the LDAP-prescribed value.

```plaintext
DELETE /groups/:id/members/:user_id/override
```

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `id`      | integer/string | yes | The ID or [URL-encoded path of the group](rest/index.md#namespaced-path-encoding) owned by the authenticated user |
| `user_id` | integer | yes   | The user ID of the member |

```shell
curl --request PUT --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/groups/:id/members/:user_id/override"
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
  "expires_at": "2012-10-22",
  "access_level": 40,
  "email": "john@example.com",
  "override": false
}
```

