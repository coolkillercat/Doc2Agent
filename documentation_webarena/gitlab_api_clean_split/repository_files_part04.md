## Get file blame from repository

Allows you to receive blame information. Each blame range contains lines and corresponding commit information.

```plaintext
GET /projects/:id/repository/files/:file_path/blame
```

| Attribute       | Type              | Required | Description |
|-----------------|-------------------|----------|-------------|
| `id`            | integer or string | yes   | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user. |
| `file_path`     | string            | yes   | URL-encoded full path to new file, such as`lib%2Fclass%2Erb`. |
| `ref`           | string            | yes   | The name of branch, tag or commit. |
| `range[end]`    | integer           | yes   | The last line of the range to blame. |
| `range[start]`  | integer           | yes   | The first line of the range to blame. |
| `range`         | hash              | no    | Blame range. |

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/projects/13083/repository/files/path%2Fto%2Ffile.rb/blame?ref=main"
```

Example response:

```json
[
  {
    "commit": {
      "id": "d42409d56517157c48bf3bd97d3f75974dde19fb",
      "message": "Add feature\n\nalso fix bug\n",
      "parent_ids": [
        "cc6e14f9328fa6d7b5a0d3c30dc2002a3f2a3822"
      ],
      "authored_date": "2015-12-18T08:12:22.000Z",
      "author_name": "John Doe",
      "author_email": "john.doe@example.com",
      "committed_date": "2015-12-18T08:12:22.000Z",
      "committer_name": "John Doe",
      "committer_email": "john.doe@example.com"
    },
    "lines": [
      "require 'fileutils'",
      "require 'open3'",
      ""
    ]
  },
  ...
]
```

NOTE:
`HEAD` method returns just file metadata, as in [Get file from repository](repository_files.md#get-file-from-repository).

```shell
curl --head --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/projects/13083/repository/files/path%2Fto%2Ffile.rb/blame?ref=main"
```

Example response:

```plaintext
HTTP/1.1 200 OK
...
X-Gitlab-Blob-Id: 79f7bbd25901e8334750839545a9bd021f0e4c83
X-Gitlab-Commit-Id: d5a3ff139356ce33e37e73add446f16869741b50
X-Gitlab-Content-Sha256: 4c294617b60715c1d218e61164a3abd4808a4284cbc30e6728a01ad9aada4481
X-Gitlab-Encoding: base64
X-Gitlab-File-Name: file.rb
X-Gitlab-File-Path: path/to/file.rb
X-Gitlab-Last-Commit-Id: 570e7b2abdd848b95f2f578043fc23bd6f6fd24d
X-Gitlab-Ref: main
X-Gitlab-Size: 1476
X-Gitlab-Execute-Filemode: false
...
```

### Examples

To request a blame range, specify `range[start]` and `range[end]` parameters with
the starting and ending line numbers of the file.

```shell
curl --head --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/projects/13083/repository/files/path%2Fto%2Ffile.rb/blame?ref=main&range[start]=1&range[end]=2"
```

Example response:

```json
[
  {
    "commit": {
      "id": "d42409d56517157c48bf3bd97d3f75974dde19fb",
      "message": "Add feature\n\nalso fix bug\n",
      "parent_ids": [
        "cc6e14f9328fa6d7b5a0d3c30dc2002a3f2a3822"
      ],
      "authored_date": "2015-12-18T08:12:22.000Z",
      "author_name": "John Doe",
      "author_email": "john.doe@example.com",
      "committed_date": "2015-12-18T08:12:22.000Z",
      "committer_name": "John Doe",
      "committer_email": "john.doe@example.com"
    },
    "lines": [
      "require 'fileutils'",
      "require 'open3'"
    ]
  },
  ...
]
```

