## List participants in an issue

Lists users that are participants in the issue.

If the project is private or the issue is confidential, you need to provide credentials to authorize.
The preferred way to do this, is by using [personal access tokens](../user/profile/personal_access_tokens.md).

```plaintext
GET /projects/:id/issues/:issue_iid/participants
```

Supported attributes:

| Attribute   | Type    | Required | Description                          |
|-------------|---------|----------|--------------------------------------|
| `id`        | integer/string | Yes      | The global ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user.  |
| `issue_iid` | integer | Yes      | The internal ID of a project's issue. |

Example request:

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" \
  -url "https://gitlab.example.com/api/v4/projects/5/issues/93/participants"
```

Example response:

```json
[
  {
    "id": 1,
    "name": "John Doe1",
    "username": "user1",
    "state": "active",
    "avatar_url": "http://www.gravatar.com/avatar/c922747a93b40d1ea88262bf1aebee62?s=80&d=identicon",
    "web_url": "http://gitlab.example.com/user1"
  },
  {
    "id": 5,
    "name": "John Doe5",
    "username": "user5",
    "state": "active",
    "avatar_url": "http://www.gravatar.com/avatar/4aea8cf834ed91844a2da4ff7ae6b491?s=80&d=identicon",
    "web_url": "http://gitlab.example.com/user5"
  }
]
```

