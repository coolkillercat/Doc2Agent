## Create new file in repository

Allows you to create a single file. For creating multiple files with a single request,
refer to the [commits API](commits.md#create-a-commit-with-multiple-files-and-actions).

```plaintext
POST /projects/:id/repository/files/:file_path
```

| Attribute        | Type           | Required | Description |
| ---------------- | -------------- | -------- | ----------- |
| `branch`         | string         | yes      | Name of the new branch to create. The commit is added to this branch. |
| `commit_message` | string         | yes      | The commit message. |
| `content`        | string         | yes      | The file's content. |
| `file_path`      | string         | yes      | URL-encoded full path to new file. For example: `lib%2Fclass%2Erb`. |
| `id`             | integer or string | yes   | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user. |
| `author_email`   | string         | no       | The commit author's email address. |
| `author_name`    | string         | no       | The commit author's name. |
| `encoding`       | string         | no       | Change encoding to `base64`. Default is `text`. |
| `execute_filemode` | boolean      | no       | Enables or disables the `execute` flag on the file. Can be `true` or `false`. |
| `start_branch`   | string         | no       | Name of the base branch to create the new branch from. |

```shell
curl --request POST --header 'PRIVATE-TOKEN: <your_access_token>' \
     --header "Content-Type: application/json" \
     --data '{"branch": "main", "author_email": "author@example.com", "author_name": "Firstname Lastname",
               "content": "some content", "commit_message": "create a new file"}' \
     "https://gitlab.example.com/api/v4/projects/13083/repository/files/app%2Fproject%2Erb"
```

Example response:

```json
{
  "file_path": "app/project.rb",
  "branch": "main"
}
```

