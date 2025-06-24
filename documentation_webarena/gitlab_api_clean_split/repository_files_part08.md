## Delete existing file in repository

This allows you to delete a single file. For deleting multiple files with a single request,
refer to the [commits API](commits.md#create-a-commit-with-multiple-files-and-actions).

```plaintext
DELETE /projects/:id/repository/files/:file_path
```

| Attribute        | Type           | Required | Description |
| ---------------- | -------------- | -------- | ----------- |
| `branch`         | string         | yes      | Name of the new branch to create. The commit is added to this branch. |
| `commit_message` | string         | yes      | The commit message. |
| `file_path`      | string         | yes      | URL-encoded full path to new file. For example: `lib%2Fclass%2Erb`. |
| `id`             | integer or string | yes   | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user. |
| `author_email`   | string         | no       | The commit author's email address. |
| `author_name`    | string         | no       | The commit author's name. |
| `last_commit_id` | string         | no       | Last known file commit ID. |
| `start_branch`   | string         | no       | Name of the base branch to create the new branch from. |

```shell
curl --request DELETE --header 'PRIVATE-TOKEN: <your_access_token>' \
     --header "Content-Type: application/json" \
     --data '{"branch": "main", "author_email": "author@example.com", "author_name": "Firstname Lastname",
       "commit_message": "delete file"}' \
     "https://gitlab.example.com/api/v4/projects/13083/repository/files/app%2Fproject%2Erb"
```
