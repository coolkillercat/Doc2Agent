## SAML Group Links

DETAILS:
**Tier:** Premium, Ultimate
**Offering:** GitLab.com, Self-managed, GitLab Dedicated

> - [Introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/290367) in GitLab 15.3.0.
> - `access_level` type [changed](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/95607) from `string` to `integer` in GitLab 15.3.3.
> - `member_role_id` type [Introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/417201) in GitLab 16.7 [with a flag](../administration/feature_flags.md) named `custom_roles_for_saml_group_links`. Disabled by default.
> - `member_role_id` type [Generally available](https://gitlab.com/gitlab-org/gitlab/-/issues/417201) in GitLab 16.8. Feature flag `custom_roles_for_saml_group_links` removed.

List, get, add, and delete SAML group links.

### List SAML group links

Lists SAML group links.

```plaintext
GET /groups/:id/saml_group_links
```

Supported attributes:

| Attribute | Type           | Required | Description                                                              |
|:----------|:---------------|:---------|:-------------------------------------------------------------------------|
| `id`      | integer/string | yes      | ID or [URL-encoded path of the group](rest/index.md#namespaced-path-encoding) |

If successful, returns [`200`](rest/index.md#status-codes) and the following response attributes:

| Attribute          | Type    | Description                                                                  |
|:-------------------|:--------|:-----------------------------------------------------------------------------|
| `[].name`          | string  | Name of the SAML group                                                       |
| `[].access_level`  | integer | [Role (`access_level`)](members.md#roles) for members of the SAML group. The attribute had a string type from GitLab 15.3.0 to GitLab 15.3.3 |
| `[].member_role_id` | integer | [Member Role ID (`member_role_id`)](member_roles.md) for members of the SAML group. |

Example request:

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/groups/1/saml_group_links"
```

Example response:

```json
[
  {
    "name": "saml-group-1",
    "access_level": 10,
    "member_role_id": 12
  },
  {
    "name": "saml-group-2",
    "access_level": 40,
    "member_role_id": 99
  }
]
```

### Get SAML group link

Get a SAML group link for the group.

```plaintext
GET /groups/:id/saml_group_links/:saml_group_name
```

Supported attributes:

| Attribute          | Type           | Required | Description                                                              |
|:-------------------|:---------------|:---------|:-------------------------------------------------------------------------|
| `id`               | integer/string | yes      | ID or [URL-encoded path of the group](rest/index.md#namespaced-path-encoding) |
| `saml_group_name`  | string         | yes      | Name of an SAML group                                                    |

If successful, returns [`200`](rest/index.md#status-codes) and the following response attributes:

| Attribute      | Type    | Description                                                                  |
|:---------------|:--------|:-----------------------------------------------------------------------------|
| `name`         | string  | Name of the SAML group                                                       |
| `access_level` | integer | [Role (`access_level`)](members.md#roles) for members of the SAML group. The attribute had a string type from GitLab 15.3.0 to GitLab 15.3.3 |
| `member_role_id` | integer | [Member Role ID (`member_role_id`)](member_roles.md) for members of the SAML group. |

Example request:

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/groups/1/saml_group_links/saml-group-1"
```

Example response:

```json
{
"name": "saml-group-1",
"access_level": 10,
"member_role_id": 12
}
```

### Add SAML group link

Adds a SAML group link for a group.

```plaintext
POST /groups/:id/saml_group_links
```

Supported attributes:

| Attribute          | Type           | Required | Description                                                                  |
|:-------------------|:---------------|:---------|:-----------------------------------------------------------------------------|
| `id`               | integer or string | yes      | ID or [URL-encoded path of the group](rest/index.md#namespaced-path-encoding)     |
| `saml_group_name`  | string         | yes      | Name of a SAML group                                                         |
| `access_level`     | integer        | yes      | [Role (`access_level`)](members.md#roles) for members of the SAML group |
| `member_role_id`   | integer        | no       | [Member Role ID (`member_role_id`)](member_roles.md) for members of the SAML group. |

If successful, returns [`201`](rest/index.md#status-codes) and the following response attributes:

| Attribute      | Type    | Description                                                                  |
|:---------------|:--------|:-----------------------------------------------------------------------------|
| `name`         | string  | Name of the SAML group                                                       |
| `access_level` | integer | [Role (`access_level`)](members.md#roles) for members of the for members of the SAML group. The attribute had a string type from GitLab 15.3.0 to GitLab 15.3.3 |
| `member_role_id` | integer | [Member Role ID (`member_role_id`)](member_roles.md) for members of the SAML group. |

Example request:

```shell
curl --request POST --header "PRIVATE-TOKEN: <your_access_token>" --header "Content-Type: application/json" --data '{ "saml_group_name": "<your_saml_group_name`>", "access_level": <chosen_access_level>, "member_role_id": <chosen_member_role_id> }' --url  "https://gitlab.example.com/api/v4/groups/1/saml_group_links"
```

Example response:

```json
{
"name": "saml-group-1",
"access_level": 10,
"member_role_id": 12
}
```

### Delete SAML group link

Deletes a SAML group link for the group.

```plaintext
DELETE /groups/:id/saml_group_links/:saml_group_name
```

Supported attributes:

| Attribute          | Type           | Required | Description                                                              |
|:-------------------|:---------------|:---------|:-------------------------------------------------------------------------|
| `id`               | integer/string | yes      | ID or [URL-encoded path of the group](rest/index.md#namespaced-path-encoding) |
| `saml_group_name`  | string         | yes      | Name of a SAML group                                                     |

If successful, returns [`204`](rest/index.md#status-codes) status code without any response body.

Example request:

```shell
curl --request DELETE --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/groups/1/saml_group_links/saml-group-1"
```

