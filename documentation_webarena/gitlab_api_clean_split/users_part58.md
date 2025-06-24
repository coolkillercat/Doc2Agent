## User memberships

DETAILS:
**Tier:** Free, Premium, Ultimate
**Offering:** Self-managed, GitLab Dedicated

> - [Introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/20532) in GitLab 12.8.

Pre-requisite:

- You must be an administrator.

Lists all projects and groups a user is a member of.
It returns the `source_id`, `source_name`, `source_type`, and `access_level` of a membership.
Source can be of type `Namespace` (representing a group) or `Project`. The response represents only direct memberships. Inherited memberships, for example in subgroups, are not included.
Access levels are represented by an integer value. For more details, read about the meaning of [access level values](access_requests.md#valid-access-levels).

```plaintext
GET /users/:id/memberships
```

Parameters:

| Attribute | Type    | Required | Description                                                        |
| --------- | ------- | -------- | ------------------------------------------------------------------ |
| `id`      | integer | yes      | ID of a specified user                                         |
| `type`    | string  | no       | Filter memberships by type. Can be either `Project` or `Namespace` |

Returns:

- `200 OK` on success.
- `404 User Not Found` if user can't be found.
- `403 Forbidden` when not requested by an administrator.
- `400 Bad Request` when requested type is not supported.

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/users/:user_id/memberships"
```

Example response:

```json
[
  {
    "source_id": 1,
    "source_name": "Project one",
    "source_type": "Project",
    "access_level": "20"
  },
  {
    "source_id": 3,
    "source_name": "Group three",
    "source_type": "Namespace",
    "access_level": "20"
  }
]
```

