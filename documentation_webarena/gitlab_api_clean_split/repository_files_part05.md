## Get raw file from repository

```plaintext
GET /projects/:id/repository/files/:file_path/raw
```

| Attribute   | Type           | Required | Description |
|-------------|----------------|----------|------------|
| `id`        | integer or string | yes   | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user. |
| `file_path` | string         | yes      | URL-encoded full path to new file, such as `lib%2Fclass%2Erb`. |
| `ref`       | string         | no       | The name of branch, tag or commit. Default is the `HEAD` of the project. |
| `lfs`       | boolean        | no       | Determines if the response should be Git LFS file contents, rather than the pointer. If the file is not tracked by Git LFS, ignored. Defaults to `false`. |

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/projects/13083/repository/files/app%2Fmodels%2Fkey%2Erb/raw?ref=main"
```

NOTE:
Like [Get file from repository](repository_files.md#get-file-from-repository), you can use `HEAD` to get just file metadata.

