## Get single merge request reviewers

Get a list of merge request reviewers.

```plaintext
GET /projects/:id/merge_requests/:merge_request_iid/reviewers
```

Supported attributes:

| Attribute           | Type              | Required | Description |
|---------------------|-------------------|----------|-------------|
| `id`                | integer or string | Yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user. |
| `merge_request_iid` | integer           | Yes      | The internal ID of the merge request. |

Example response:

```json
[
  {
    "user": {
      "id": 1,
      "name": "John Doe1",
      "username": "user1",
      "state": "active",
      "avatar_url": "http://www.gravatar.com/avatar/c922747a93b40d1ea88262bf1aebee62?s=80&d=identicon",
      "web_url": "http://localhost/user1"
    },
    "state": "unreviewed",
    "created_at": "2022-07-27T17:03:27.684Z"
  },
  {
    "user": {
      "id": 2,
      "name": "John Doe2",
      "username": "user2",
      "state": "active",
      "avatar_url": "http://www.gravatar.com/avatar/10fc7f102be8de7657fb4d80898bbfe3?s=80&d=identicon",
      "web_url": "http://localhost/user2"
    },
    "state": "reviewed",
    "created_at": "2022-07-27T17:03:27.684Z"
  }
]
```

