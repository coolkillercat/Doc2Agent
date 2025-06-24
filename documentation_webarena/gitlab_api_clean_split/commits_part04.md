## Create a commit with multiple files and actions

Create a commit by posting a JSON payload

```plaintext
POST /projects/:id/repository/commits
```

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `id` | integer/string | yes | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) |
| `branch` | string | yes | Name of the branch to commit into. To create a new branch, also provide either `start_branch` or `start_sha`, and optionally `start_project`. |
| `commit_message` | string | yes | Commit message |
| `start_branch` | string | no | Name of the branch to start the new branch from |
| `start_sha` | string | no | SHA of the commit to start the new branch from |
| `start_project` | integer/string | no | The project ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) to start the new branch from. Defaults to the value of `id`. |
| `actions[]` | array | yes | An array of action hashes to commit as a batch. See the next table for what attributes it can take. |
| `author_email` | string | no | Specify the commit author's email address |
| `author_name` | string | no | Specify the commit author's name |
| `stats` | boolean | no | Include commit stats. Default is true |
| `force` | boolean | no | When `true` overwrites the target branch with a new commit based on the `start_branch` or `start_sha` |

| `actions[]` Attribute | Type    | Required | Description |
|-----------------------|---------|----------|-------------|
| `action`              | string  | yes      | The action to perform: `create`, `delete`, `move`, `update`, or `chmod`. |
| `file_path`           | string  | yes      | Full path to the file. For example: `lib/class.rb`. |
| `previous_path`       | string  | no       | Original full path to the file being moved. For example `lib/class1.rb`. Only considered for `move` action. |
| `content`             | string  | no       | File content, required for all except `delete`, `chmod`, and `move`. Move actions that do not specify `content` preserve the existing file content, and any other value of `content` overwrites the file content. |
| `encoding`            | string  | no       | `text` or `base64`. `text` is default. |
| `last_commit_id`      | string  | no       | Last known file commit ID. Only considered in update, move, and delete actions. |
| `execute_filemode`    | boolean | no       | When `true/false` enables/disables the execute flag on the file. Only considered for `chmod` action. |

```shell
PAYLOAD=$(cat << 'JSON'
{
  "branch": "main",
  "commit_message": "some commit message",
  "actions": [
    {
      "action": "create",
      "file_path": "foo/bar",
      "content": "some content"
    },
    {
      "action": "delete",
      "file_path": "foo/bar2"
    },
    {
      "action": "move",
      "file_path": "foo/bar3",
      "previous_path": "foo/bar4",
      "content": "some content"
    },
    {
      "action": "update",
      "file_path": "foo/bar5",
      "content": "new content"
    },
    {
      "action": "chmod",
      "file_path": "foo/bar5",
      "execute_filemode": true
    }
  ]
}
JSON
)
curl --request POST \
  --header "PRIVATE-TOKEN: <your_access_token>" \
  --header "Content-Type: application/json" \
  --data "$PAYLOAD" \
  --url "https://gitlab.example.com/api/v4/projects/1/repository/commits"
```

Example response:

```json
{
  "id": "ed899a2f4b50b4370feeea94676502b42383c746",
  "short_id": "ed899a2f4b5",
  "title": "some commit message",
  "author_name": "Example User",
  "author_email": "user@example.com",
  "committer_name": "Example User",
  "committer_email": "user@example.com",
  "created_at": "2016-09-20T09:26:24.000-07:00",
  "message": "some commit message",
  "parent_ids": [
    "ae1d9fb46aa2b07ee9836d49862ec4e2c46fbbba"
  ],
  "committed_date": "2016-09-20T09:26:24.000-07:00",
  "authored_date": "2016-09-20T09:26:24.000-07:00",
  "stats": {
    "additions": 2,
    "deletions": 2,
    "total": 4
  },
  "status": null,
  "web_url": "https://gitlab.example.com/janedoe/gitlab-foss/-/commit/ed899a2f4b50b4370feeea94676502b42383c746"
}
```

GitLab supports [form encoding](rest/index.md#encoding-api-parameters-of-array-and-hash-types). The following is an example using Commit API with form encoding:

```shell
curl --request POST \
     --form "branch=main" \
     --form "commit_message=some commit message" \
     --form "start_branch=main" \
     --form "actions[][action]=create" \
     --form "actions[][file_path]=foo/bar" \
     --form "actions[][content]=</path/to/local.file" \
     --form "actions[][action]=delete" \
     --form "actions[][file_path]=foo/bar2" \
     --form "actions[][action]=move" \
     --form "actions[][file_path]=foo/bar3" \
     --form "actions[][previous_path]=foo/bar4" \
     --form "actions[][content]=</path/to/local1.file" \
     --form "actions[][action]=update" \
     --form "actions[][file_path]=foo/bar5" \
     --form "actions[][content]=</path/to/local2.file" \
     --form "actions[][action]=chmod" \
     --form "actions[][file_path]=foo/bar5" \
     --form "actions[][execute_filemode]=true" \
     --header "PRIVATE-TOKEN: <your_access_token>" \
     "https://gitlab.example.com/api/v4/projects/1/repository/commits"
```

