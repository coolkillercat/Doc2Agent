## Get a blob from repository

Allows you to receive information, such as size and content, about blobs in a repository.
Blob content is Base64 encoded. This endpoint can be accessed without authentication,
if the repository is publicly accessible.

```plaintext
GET /projects/:id/repository/blobs/:sha
```

Supported attributes:

| Attribute | Type           | Required | Description |
| :-------- | :------------- | :------- | :---------- |
| `id`      | integer or string | yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user. |
| `sha`     | string         | yes      | The blob SHA. |

