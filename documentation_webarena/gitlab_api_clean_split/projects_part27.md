## Upload a file

> - [Generally available](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/112450) in GitLab 15.10. Feature flag `enforce_max_attachment_size_upload_api` removed.

Uploads a file to the specified project to be used in an issue or merge request
description, or a comment.

```plaintext
POST /projects/:id/uploads
```

| Attribute | Type              | Required | Description |
|-----------|-------------------|----------|-------------|
| `file`    | string            | Yes      | The file to be uploaded. |
| `id`      | integer or string | Yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding). |

To upload a file from your file system, use the `--form` argument. This causes
cURL to post data using the header `Content-Type: multipart/form-data`. The
`file=` parameter must point to a file on your file system and be preceded by
`@`. For example:

```shell
curl --request POST --header "PRIVATE-TOKEN: <your_access_token>" \
     --form "file=@dk.png" "https://gitlab.example.com/api/v4/projects/5/uploads"
```

Returned object:

```json
{
  "alt": "dk",
  "url": "/uploads/66dbcd21ec5d24ed6ea225176098d52b/dk.png",
  "full_path": "/namespace1/project1/uploads/66dbcd21ec5d24ed6ea225176098d52b/dk.png",
  "markdown": "![dk](/uploads/66dbcd21ec5d24ed6ea225176098d52b/dk.png)"
}
```

The returned `url` is relative to the project path. The returned `full_path` is
the absolute path to the file. In Markdown contexts, the link is expanded when
the format in `markdown` is used.

