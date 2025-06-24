## Contributors

Get repository contributors list. This endpoint can be accessed without
authentication if the repository is publicly accessible.

```plaintext
GET /projects/:id/repository/contributors
```

Supported attributes:

| Attribute  | Type           | Required | Description |
| :--------- | :------------- | :------- | :---------- |
| `id`       | integer or string | yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user. |
| `order_by` | string         | no       | Return contributors ordered by `name`, `email`, or `commits` (orders by commit date) fields. Default is `commits`. |
| `sort`     | string         | no       | Return contributors sorted in `asc` or `desc` order. Default is `asc`. |

Example response:

```json
[{
  "name": "Example User",
  "email": "example@example.com",
  "commits": 117,
  "additions": 0,
  "deletions": 0
}, {
  "name": "Sample User",
  "email": "sample@example.com",
  "commits": 33,
  "additions": 0,
  "deletions": 0
}]
```

