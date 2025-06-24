## Raw blob content

Get the raw file contents for a blob, by blob SHA. This endpoint can be accessed
without authentication if the repository is publicly accessible.

```plaintext
GET /projects/:id/repository/blobs/:sha/raw
```

Supported attributes:

| Attribute | Type     | Required | Description |
| :-------- | :------- | :------- | :---------- |
| `id`      | integer or string | yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user. |
| `sha`     | string | yes      | The blob SHA. |

