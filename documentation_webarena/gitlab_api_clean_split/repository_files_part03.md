## Get file from repository

Allows you to receive information about file in repository like name, size, and
content. File content is Base64 encoded. This endpoint can be accessed
without authentication if the repository is publicly accessible.

```plaintext
GET /projects/:id/repository/files/:file_path
```

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/projects/13083/repository/files/app%2Fmodels%2Fkey%2Erb?ref=main"
```

| Attribute   | Type           | Required | Description |
|-------------|----------------|----------|-------------|
| `id`        | integer or string | yes   | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user. |
| `file_path` | string         | yes      | URL encoded full path to new file, such as `lib%2Fclass%2Erb`. |
| `ref`       | string         | yes      | The name of branch, tag or commit. |

Example response:

```json
{
  "file_name": "key.rb",
  "file_path": "app/models/key.rb",
  "size": 1476,
  "encoding": "base64",
  "content": "IyA9PSBTY2hlbWEgSW5mb3...",
  "content_sha256": "4c294617b60715c1d218e61164a3abd4808a4284cbc30e6728a01ad9aada4481",
  "ref": "main",
  "blob_id": "79f7bbd25901e8334750839545a9bd021f0e4c83",
  "commit_id": "d5a3ff139356ce33e37e73add446f16869741b50",
  "last_commit_id": "570e7b2abdd848b95f2f578043fc23bd6f6fd24d",
  "execute_filemode": false
}
```

NOTE:
`blob_id` is the blob SHA. Refer to [Get a blob from repository](repositories.md#get-a-blob-from-repository)
in the Repositories API.

In addition to the `GET` method, you can also use `HEAD` to get just file metadata.

```plaintext
HEAD /projects/:id/repository/files/:file_path
```

```shell
curl --head --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/projects/13083/repository/files/app%2Fmodels%2Fkey%2Erb?ref=main"
```

Example response:

```plaintext
HTTP/1.1 200 OK
...
X-Gitlab-Blob-Id: 79f7bbd25901e8334750839545a9bd021f0e4c83
X-Gitlab-Commit-Id: d5a3ff139356ce33e37e73add446f16869741b50
X-Gitlab-Content-Sha256: 4c294617b60715c1d218e61164a3abd4808a4284cbc30e6728a01ad9aada4481
X-Gitlab-Encoding: base64
X-Gitlab-File-Name: key.rb
X-Gitlab-File-Path: app/models/key.rb
X-Gitlab-Last-Commit-Id: 570e7b2abdd848b95f2f578043fc23bd6f6fd24d
X-Gitlab-Ref: main
X-Gitlab-Size: 1476
X-Gitlab-Execute-Filemode: false
...
```

