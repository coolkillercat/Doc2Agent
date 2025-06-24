## User follow

### Follow and unfollow users

Follow a user.

```plaintext
POST /users/:id/follow
```

Unfollow a user.

```plaintext
POST /users/:id/unfollow
```

| Attribute | Type    | Required | Description                  |
| --------- | ------- | -------- | ---------------------------- |
| `id`      | integer | yes      | ID of the user to follow |

```shell
curl --request POST --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/users/3/follow"
```

Example response:

```json
{
  "id": 1,
  "username": "john_smith",
  "name": "John Smith",
  "state": "active",
  "locked": false,
  "avatar_url": "http://localhost:3000/uploads/user/avatar/1/cd8.jpeg",
  "web_url": "http://localhost:3000/john_smith"
}
```

### Followers and following

Get the followers of a user.

```plaintext
GET /users/:id/followers
```

Get the list of users being followed.

```plaintext
GET /users/:id/following
```

| Attribute | Type    | Required | Description                  |
| --------- | ------- | -------- | ---------------------------- |
| `id`      | integer | yes      | ID of the user to follow |

```shell
curl --request GET --header "PRIVATE-TOKEN: <your_access_token>"  "https://gitlab.example.com/users/3/followers"
```

Example response:

```json
[
  {
    "id": 2,
    "name": "Lennie Donnelly",
    "username": "evette.kilback",
    "state": "active",
    "locked": false,
    "avatar_url": "https://www.gravatar.com/avatar/7955171a55ac4997ed81e5976287890a?s=80&d=identicon",
    "web_url": "http://127.0.0.1:3000/evette.kilback"
  },
  {
    "id": 4,
    "name": "Serena Bradtke",
    "username": "cammy",
    "state": "active",
    "locked": false,
    "avatar_url": "https://www.gravatar.com/avatar/a2daad869a7b60d3090b7b9bef4baf57?s=80&d=identicon",
    "web_url": "http://127.0.0.1:3000/cammy"
  }
]
```

