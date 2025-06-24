## Upload a project avatar

Uploads an avatar to the specified project.

```plaintext
PUT /projects/:id
```

| Attribute | Type              | Required | Description |
|-----------|-------------------|----------|-------------|
| `avatar`  | string            | Yes      | The file to be uploaded. |
| `id`      | integer or string | Yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding). |

To upload an avatar from your file system, use the `--form` argument. This causes
cURL to post data using the header `Content-Type: multipart/form-data`. The
`file=` parameter must point to an image file on your file system and be
preceded by `@`. For example:

Example request:

```shell
curl --request PUT --header "PRIVATE-TOKEN: <your_access_token>" \
     --form "avatar=@dk.png" "https://gitlab.example.com/api/v4/projects/5"
```

Returned object:

```json
{
  "avatar_url": "https://gitlab.example.com/uploads/-/system/project/avatar/2/dk.png"
}
```

