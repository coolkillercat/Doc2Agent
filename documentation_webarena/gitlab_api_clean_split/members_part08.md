## List all billable members of a group

Gets a list of group members that count as billable. The list includes members in subgroups and projects.

This API endpoint works on top-level groups only. It does not work on subgroups.

This function takes [pagination](rest/index.md#pagination) parameters `page` and `per_page` to restrict the list of users.

Use the `search` parameter to search for billable group members by name and `sort` to sort the results.

```plaintext
GET /groups/:id/billable_members
```

| Attribute                     | Type            | Required  | Description                                                                                                   |
| ----------------------------- | --------------- | --------- |-------------------------------------------------------------------------------------------------------------- |
| `id`                          | integer/string  | yes       | The ID or [URL-encoded path of the group](rest/index.md#namespaced-path-encoding) owned by the authenticated user  |
| `search`                      | string          | no        | A query string to search for group members by name, username, or public email.                                |
| `sort`                        | string          | no        | A query string containing parameters that specify the sort attribute and order. See supported values below.   |

The supported values for the `sort` attribute are:

| Value                   | Description                  |
| ----------------------- | ---------------------------- |
| `access_level_asc`      | Access level, ascending      |
| `access_level_desc`     | Access level, descending     |
| `last_joined`           | Last joined                  |
| `name_asc`              | Name, ascending              |
| `name_desc`             | Name, descending             |
| `oldest_joined`         | Oldest joined                |
| `oldest_sign_in`        | Oldest sign in               |
| `recent_sign_in`        | Recent sign in               |
| `last_activity_on_asc`  | Last active date, ascending  |
| `last_activity_on_desc` | Last active date, descending |

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/groups/:id/billable_members"
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
    "last_activity_on": "2021-01-27",
    "membership_type": "group_member",
    "removable": true,
    "created_at": "2021-01-03T12:16:02.000Z",
    "last_login_at": "2022-10-09T01:33:06.000Z"
  },
  {
    "id": 2,
    "username": "john_doe",
    "name": "John Doe",
    "state": "active",
    "avatar_url": "https://www.gravatar.com/avatar/c2525a7f58ae3776070e44c106c48e15?s=80&d=identicon",
    "web_url": "http://192.168.1.8:3000/root",
    "email": "john@example.com",
    "last_activity_on": "2021-01-25",
    "membership_type": "group_member",
    "removable": true,
    "created_at": "2021-01-04T18:46:42.000Z",
    "last_login_at": "2022-09-29T22:18:46.000Z"
  },
  {
    "id": 3,
    "username": "foo_bar",
    "name": "Foo bar",
    "state": "active",
    "avatar_url": "https://www.gravatar.com/avatar/c2525a7f58ae3776070e44c106c48e15?s=80&d=identicon",
    "web_url": "http://192.168.1.8:3000/root",
    "last_activity_on": "2021-01-20",
    "membership_type": "group_invite",
    "removable": false,
    "created_at": "2021-01-09T07:12:31.000Z",
    "last_login_at": "2022-10-10T07:28:56.000Z"
  }
]
```

